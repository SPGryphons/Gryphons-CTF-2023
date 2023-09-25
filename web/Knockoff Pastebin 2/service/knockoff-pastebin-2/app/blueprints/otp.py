from flask import Blueprint, request
from pyotp import TOTP

otp = Blueprint("otp", __name__)


@otp.route("/verify", methods=["POST"])
def verify():
  secret = request.json.get("secret")
  otp = request.json.get("otp")

  if not secret or not otp:
    return {"error": "Missing secret or OTP"}, 400
  
  if not TOTP(secret).verify(otp, valid_window=1):
    return {"success": False}, 200
  
  return {"success": True}, 200