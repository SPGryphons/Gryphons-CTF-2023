from functools import wraps

from database import database
from flask import redirect, request
from jwt_utils import decodeJWT, verifyJWT


def check_is_authenticated(f):
  @wraps(f)
  def decorator(*args, **kwargs):
    token = request.cookies.get('token')

    if token is None:
      return redirect('/login')

    data = verifyJWT(token)
    if data:
      if database.get_user_id(data['username']):
        return f(*args, **kwargs)
      
    response = redirect('/login')
    response.set_cookie('token', '', expires=0)
    return response
  
  return decorator


def check_is_not_authenticated(f):
  @wraps(f)
  def decorator(*args, **kwargs):
    token = request.cookies.get('token')

    if token is not None and verifyJWT(token):
      return redirect('/profile')
    
    return f(*args, **kwargs)
  
  return decorator


def is_admin():
  token = request.cookies.get('token')

  decoded = decodeJWT(token)

  if decoded is None or not decoded['admin']:
    return False
  
  return True


def check_is_admin(f):
  @wraps(f)
  def decorator(*args, **kwargs):
    token = request.cookies.get('token')

    if token is None or not verifyJWT(token):
      return redirect('/login')
    
    if not is_admin():
      return redirect('/login')
    
    return f(*args, **kwargs)
  
  return decorator