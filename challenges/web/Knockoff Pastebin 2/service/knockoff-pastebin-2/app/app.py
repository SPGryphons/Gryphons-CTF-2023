import logging
import secrets
import threading
import time
import traceback
import uuid

from flask import Flask, send_file
from pyotp import random_base32

from blueprints.routes import api, otp, web
from database import database
from jwt_utils import jwt_client


def setup_database():
  database.init_database()

  password = secrets.token_hex(32)
  print(f"Admin password: {password}")
  totp_secret = random_base32()
  print(f"Admin OTP secret: {totp_secret}")

  database.add_user("admin", password, totp_secret, True)

  user_id = database.get_user_id("admin")

  with open("../flag.txt", "r") as f:
    flag = f.read().strip()

  # Create a paste
  database.add_paste(
    user_id,
    "Flag for GCTF",
    flag,
    str(uuid.uuid4())
  )



def reset_loop():
  while True:
    time.sleep(60 * 60)
    print("Resetting database")
    setup_database()
    print("Generating new JWT key")
    jwt_client.generate_new_key()
    print("Reset complete")


def create_app():

  app = Flask(__name__)


  app.register_blueprint(web, url_prefix="/")
  app.register_blueprint(api, url_prefix="/api")
  app.register_blueprint(otp, url_prefix="/otp")


  @app.errorhandler(Exception)
  def handle_exception(e):
    message = e.description if hasattr(e, "description") else [str(e) for a in e.args]
    response = {
      "error": {
        "type": e.__class__.__name__,
        "message": message
      }
    }

    logging.error(response)
    logging.error(traceback.format_exc())

    return response, e.code if hasattr(e, "code") else 500

  @app.errorhandler(404)
  def handle_404(e):
    return send_file("templates/404.html")
  
  setup_database()
  
  reset_thread = threading.Thread(target=reset_loop, daemon=True)
  reset_thread.start()

  return app