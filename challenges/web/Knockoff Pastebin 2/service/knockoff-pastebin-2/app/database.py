import sqlite3 as sql
import logging


class Database:
  def __init__(self):
    self.conn = sql.connect(":memory:", check_same_thread=False)
    self.init_database()

  
  def init_database(self):
    cursor = self.conn.cursor()
    with open("init.sql", "r") as f:
      cursor.executescript(f.read())

    self.conn.commit()
    cursor.close()


  def get_user_id(self, username):
    try:
      cursor = self.conn.cursor()
      cursor.execute(
        "SELECT id FROM users WHERE username = ?",
        (username,)
      )
      user = cursor.fetchone()
      cursor.close()
      if user:
        return user[0]
      else:
        return False
    except Exception as e:
      logging.error(e)
      return False


  def is_admin(self, user_id):
    try:
      cursor = self.conn.cursor()
      cursor.execute(
        "SELECT admin FROM users WHERE id = ?",
        (user_id,)
      )
      admin = cursor.fetchone()
      cursor.close()
      if admin and admin[0]:
        return True
      else:
        return False
    except Exception as e:
      logging.error(e)
      return False


  def add_user(self, username, password, totp_secret, admin=False):
    try:
      cursor = self.conn.cursor()
      cursor.execute(
        "INSERT INTO users (username, password, totp_secret, admin) VALUES (?, ?, ?, ?)",
        (username, password, totp_secret, int(admin))
      )
      self.conn.commit()
      cursor.close()
      return True
    except Exception as e:
      logging.error(e)
      return False
    

  def login(self, username, password):
    try:
      cursor = self.conn.cursor()
      cursor.execute(
        "SELECT id FROM users WHERE username = ? AND password = ?",
        (username, password)
      )
      user = cursor.fetchone()
      cursor.close()
      if user:
        return user[0]
      else:
        return False
    except Exception as e:
      logging.error(e)
      return False
    
  
  def get_totp_secret(self, user_id):
    try:
      cursor = self.conn.cursor()
      cursor.execute(
        "SELECT totp_secret FROM users WHERE id = ?",
        (user_id,)
      )
      secret = cursor.fetchone()
      cursor.close()
      if secret:
        return secret[0]
      else:
        return False
    except Exception as e:
      logging.error(e)
      return False
    

  def add_paste(self, user_id, title, content, link):
    try:
      cursor = self.conn.cursor()
      cursor.execute(
        "INSERT INTO pastes (user_id, title, content, link) VALUES (?, ?, ?, ?)",
        (user_id, title, content, link)
      )
      self.conn.commit()
      cursor.close()
      return True
    except Exception as e:
      logging.error(e)
      return False
    

  def get_user_pastes(self, user_id):
    try:
      cursor = self.conn.cursor()
      cursor.execute(
        "SELECT title, content, link FROM pastes WHERE user_id = ?",
        (user_id,)
      )
      pastes = cursor.fetchall()
      cursor.close()
      if pastes:
        return pastes
      else:
        return False
    except Exception as e:
      logging.error(e)
      return False


  def get_paste_by_link(self, link):
    try:
      cursor = self.conn.cursor()
      cursor.execute(
        "SELECT title, content, link FROM pastes WHERE link = ?",
        (link,)
      )
      paste = cursor.fetchone()
      cursor.close()
      if paste:
        return paste
      else:
        return False
    except Exception as e:
      logging.error(e)
      return False
    

  def delete_paste(self, id):
    try:
      cursor = self.conn.cursor()
      cursor.execute(
        "DELETE FROM pastes WHERE id = ?",
        (id,)
      )
      self.conn.commit()
      cursor.close()
      return True
    except Exception as e:
      logging.error(e)
      return False


database = Database()