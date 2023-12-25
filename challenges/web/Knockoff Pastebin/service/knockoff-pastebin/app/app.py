import logging
import time
import threading
import shutil
import os
import traceback

from blueprints.routes import api, web
from database import database
from flask import Flask, send_file
from jwt_utils import jwt_client


def reset_loop():
  while True:
    time.sleep(60 * 60)
    print("Resetting database")
    database.restart()
    print("Resetting uploads")
    shutil.rmtree("uploads")
    os.mkdir("uploads")
    print("Rotating JWT keys")
    jwt_client.rotate_keys()
    print("Reset complete")


def create_app():

  app = Flask(__name__)


  app.register_blueprint(web, url_prefix="/")
  app.register_blueprint(api, url_prefix="/api")


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
  
  reset_thread = threading.Thread(target=reset_loop, daemon=True)
  reset_thread.start()

  return app