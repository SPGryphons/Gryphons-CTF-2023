import requests
from checks import check_is_authenticated
from database import database
from flask import Blueprint, redirect, request
from jwt_utils import createJWT

api = Blueprint("api", __name__)


@api.route("/login", methods=["POST"])
def api_login():
  data = request.json
  username = data.get("username")
  password = data.get("password")
  otp = data.get("otp")

  if not otp:
    return {"error": "Missing TOTP."}, 400
  
  if username and password:
    user_id = database.login(username, password)
  else:
    user_id = database.get_user_id(username)
  
  if not user_id:
    return {"error": "Invalid username or password."}, 401
  else:
    # Get TOTP secret
    secret = database.get_totp_secret(user_id)

    try:
      resp = requests.post(
        f"{request.root_url}otp/verify",
        json={"secret": secret, "otp": otp}
      )
      resp = resp.json()
    except Exception as e:
      print(e)
      return {"error": "Error verifying TOTP."}, 500
    
    if not resp["success"]:
      return {"error": "Invalid TOTP."}, 401
    
    admin = database.is_admin(user_id)
    token = createJWT(username, admin)
    return {"token": token}, 200


@api.route("/delete/<path:paste>", methods=["GET"])
@check_is_authenticated
def api_delete(paste):
  # We are under maintenance, so we don't want to allow deleting pastes.
  # So we will just redirect the user to the /profile endpoint, with a
  # message saying that deleting pastes is disabled.
  return redirect("/profile?msg=Deleting%20pastes%20is%20disabled%20while%20we%20are%20under%20maintenance.")
