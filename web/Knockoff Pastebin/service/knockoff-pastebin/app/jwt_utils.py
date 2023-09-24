import os
import jwt
from secrets import token_hex
from uuid import uuid4

from datetime import datetime, timedelta
  

class JWTClient:
  def __init__(self):
    if not os.path.exists("keys"):
      os.mkdir("keys")
    elif os.listdir("keys"):
      for file in os.listdir("keys"):
        os.remove(f"keys/{file}")

    self.generate_key()

  def generate_key(self):
    key = token_hex(16)
    kid = str(uuid4())
    with open(f"keys/{kid}", 'w') as key_file:
      key_file.write(key)

    self.kid = kid

  
  def get_key(self, kid):
    with open(f"keys/{kid}", 'r') as key_file:
      return key_file.read()
    

  def createJWT(self, username, admin):
    key = self.get_key(self.kid)

    expires = datetime.utcnow() + timedelta(hours=1)

    return jwt.encode({
      'username': username,
      'admin': admin,
      'exp': expires
    }, key, algorithm='HS256', headers={'kid': self.kid})
  

  def decodeJWT(self, token):
    try:
      return jwt.decode(token, options={"verify_signature": False})
    except jwt.exceptions.DecodeError:
      return None
    

  def verifyJWT(self, token):
    # This is fine because we delete the old key IDs when we rotate keys :)
    kid = jwt.get_unverified_header(token)['kid']
    
    try:
      key = self.get_key(kid)
    except Exception:
      return False
    
    try:
      return jwt.decode(token, key, algorithms=['HS256'])
    except Exception:
      return False
    

  def rotate_keys(self):
    os.remove(f"keys/{self.kid}")
    self.generate_key()


jwt_client = JWTClient()
createJWT = jwt_client.createJWT
decodeJWT = jwt_client.decodeJWT
verifyJWT = jwt_client.verifyJWT