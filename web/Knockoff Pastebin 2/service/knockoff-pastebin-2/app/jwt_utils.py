from datetime import datetime, timedelta
from secrets import token_hex

import jwt


class JWTClient:
  def __init__(self):
    self.generate_new_key()


  def generate_new_key(self):
    self.key = token_hex(32)


  def createJWT(self, username, admin):
    expires = datetime.utcnow() + timedelta(hours=1)

    return jwt.encode({
      "username": username,
      "admin": admin,
      "exp": expires
    }, self.key, algorithm="HS256")
  

  def decodeJWT(self, token):
    try:
      return jwt.decode(token, options={"verify_signature": False})
    except jwt.exceptions.DecodeError:
      return None
    

  def verifyJWT(self, token):
    try:
      return jwt.decode(token, self.key, algorithms=["HS256"])
    except Exception:
      return False
    

jwt_client = JWTClient()
createJWT = jwt_client.createJWT
decodeJWT = jwt_client.decodeJWT
verifyJWT = jwt_client.verifyJWT