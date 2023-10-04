from pathlib import Path
from uuid import uuid4
from checks import check_is_authenticated
from database import database
from flask import Blueprint, redirect, request
from jwt_utils import createJWT, decodeJWT

api = Blueprint("api", __name__)


@api.route("/login", methods=["POST"])
def api_login():
  data = request.json
  username = data["username"]
  password = data["password"]
  user_id = database.login(username, password)
  if not user_id:
    return {"error": "Invalid username or password."}, 401
  else:
    admin = database.is_admin(user_id)
    token = createJWT(username, admin)
    return {"token": token}, 200
  

@api.route("/register", methods=["POST"])
def api_register():
  data = request.json
  username = data["username"]
  password = data["password"]
  if database.add_user(username, password):
    return "", 200
  else:
    return {"error": "User already exists."}, 400
  

@api.route("/create", methods=["POST"])
@check_is_authenticated
def api_create():
  data = decodeJWT(request.cookies.get("token"))

  username = data["username"]

  # Get number of pastes by user
  # It can be located in "uploads/<user_id>/"
  user_id = database.get_user_id(username)
  path = Path(f"uploads/{user_id}")
  if path.exists():
    pastes = len(list(path.iterdir()))
  else:
    pastes = 0

  if pastes >= 5:
    return {"error": "You have reached the maximum number of pastes."}, 403
  
  data = request.json
  content = data["content"]

  # Create a new paste
  paste_id = str(uuid4())
  if not path.exists():
    path.mkdir(parents=True)

  with open(f"uploads/{user_id}/{paste_id}", "w") as f:
    f.write(content)

  return {"link": f"{user_id}/{paste_id}"}, 200


@api.route("/delete/<path:paste>", methods=["GET"])
@check_is_authenticated
def api_delete(paste):
  token = request.cookies.get("token")
  data = decodeJWT(token)
  username = data["username"]
  user_id = database.get_user_id(username)
  path = Path(f"uploads/{user_id}/{paste}")
  if path.exists():
    path.unlink()
    return redirect("/profile")
  else:
    return {"error": "Paste does not exist."}, 404
