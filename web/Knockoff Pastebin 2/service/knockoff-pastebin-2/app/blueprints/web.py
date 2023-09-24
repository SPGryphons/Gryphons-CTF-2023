from checks import check_is_authenticated, check_is_not_authenticated
from database import database
from flask import (Blueprint, Response, redirect, render_template, request,
                   send_file)
from jwt_utils import decodeJWT, verifyJWT

web = Blueprint("web", __name__)


@web.route("/")
def index():
  token = request.cookies.get("token", None)
  logged_in = False
  if token:
    logged_in = verifyJWT(token)
    if not logged_in:
      response = redirect("/login")
      response.set_cookie("token", "", expires=0)
      return response
  return render_template("index.html", logged_in=logged_in)


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
  msg = request.args.get("msg")

  token = request.cookies.get("token")
  data = decodeJWT(token)
  username = data["username"]
  user_id = database.get_user_id(username)

  pastes = database.get_user_pastes(user_id)

  return render_template("profile.html", username=username, user_id=user_id, pastes=pastes, msg=msg)
  

@web.route("/create", methods=["GET"])
@check_is_authenticated
def create():
  token = request.cookies.get("token")
  data = decodeJWT(token)
  username = data["username"]
  return render_template("create.html", username=username)


@web.route("/view/<path:link>", methods=["GET"])
def view(link):
  if request.cookies.get("token") is None:
    username = None
  else:
    token = request.cookies.get("token")
    data = verifyJWT(token)
    if not data:
      response = redirect(f"/view/{link}")
      response.set_cookie("token", "", expires=0)
      return response
    username = data["username"]

  paste = database.get_paste_by_link(link)
  if not paste:
    return render_template("404.html")
  title = paste[0]
  content = paste[1]
  link = paste[2]

  return render_template("view.html", title=title, content=content, link=link, username=username)


@web.route("/raw/<path:paste>", methods=["GET"])
def raw(paste):
  paste = database.get_paste_by_link(paste)
  if not paste:
    return render_template("404.html")
  return Response(paste[1], mimetype="text/plain")


@web.route("/403", methods=["GET"])
def error():
  return send_file("./templates/403.html")


@web.route("/<path:path>", methods=["GET"])
def not_found(path):
  print(f"Attempted access to {path} but not found.")
  return send_file("./templates/404.html")