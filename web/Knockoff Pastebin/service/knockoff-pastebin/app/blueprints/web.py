import urllib.parse
from pathlib import Path

from flask import (Blueprint, Response, redirect, render_template, request,
                   send_file, send_from_directory)
from werkzeug.security import safe_join

from checks import check_is_authenticated, check_is_not_authenticated, is_admin
from database import database
from jwt_utils import verifyJWT

web = Blueprint("web", __name__)


@web.route("/")
def index():
  token = request.cookies.get("token", None)
  logged_in = False
  admin = False
  if token:
    logged_in = verifyJWT(token)
    if not logged_in:
      response = redirect("/login")
      response.set_cookie("token", "", expires=0)
      return response
    admin = logged_in["admin"]
  return render_template("index.html", logged_in=logged_in, admin=admin)


@web.route("/favicon.ico", methods=["GET"])
def favicon():
  return send_file("./static/img/icon.png")


@web.route("/login", methods=["GET"])
@check_is_not_authenticated
def login():
  return render_template("login.html")


@web.route("/register", methods=["GET"])
@check_is_not_authenticated
def register():
  return render_template("register.html")


@web.route("/logout", methods=["GET"])
@check_is_authenticated
def logout():
  response = redirect("/login")
  response.set_cookie("token", "", expires=0)
  return response


@web.route("/profile", methods=["GET"])
@check_is_authenticated
def profile():
  token = request.cookies.get("token")
  data = verifyJWT(token)
  username = data["username"]
  user_id = database.get_user_id(username)
  
  # Get number of pastes by user
  # It can be located in "uploads/<user_id>/"
  path = Path(f"uploads/{user_id}")
  if path.exists():
    pastes = [paste.name for paste in path.iterdir()]
  else:
    pastes = []

  return render_template("profile.html", username=username, user_id=user_id, pastes=pastes)
  

@web.route("/create", methods=["GET"])
@check_is_authenticated
def create():
  token = request.cookies.get("token")
  data = verifyJWT(token)
  username = data["username"]
  return render_template("create.html", username=username)


@web.route("/view/<path:user_id>/<path:paste_id>", methods=["GET"])
def view(user_id, paste_id):
  if request.cookies.get("token") is None:
    username = None
  else:
    token = request.cookies.get("token")
    data = verifyJWT(token)
    if not data:
      response = redirect(f"/view/{user_id}/{paste_id}")
      response.set_cookie("token", "", expires=0)
      return response
    username = data["username"]

  path = safe_join("uploads", user_id, paste_id)
  try:
    with open(path, 'r') as paste:
      content = paste.read()
  except Exception:
    return redirect("/")
  
  show_back = database.get_user_id(username) == user_id
  return render_template("view.html", username=username, content=content, show_back=show_back, link=f"{user_id}/{paste_id}")


@web.route("/raw/<path:paste>", methods=["GET"])
def raw(paste):
  if is_admin():
    if "../" in paste:
      return "Try harder :)"
    else:
      paste = urllib.parse.unquote(paste)
      try:
        with open("uploads/" + paste, 'r') as paste:
          content = paste.read()
      except Exception:
        return {"error": "File not found."}
      # No flags past this point! :p
      if "GCTF23" in content:
        return "It's never that easy... :)"
      return Response(content, mimetype="text/plain")
  else:
    return send_from_directory("uploads", paste, mimetype="text/plain")



@web.route("/403", methods=["GET"])
def error():
  return send_file("./templates/403.html")


@web.route("/<path:path>", methods=["GET"])
def not_found(path):
  print(f"Attempted access to {path} but not found.")
  return send_file("./templates/404.html")