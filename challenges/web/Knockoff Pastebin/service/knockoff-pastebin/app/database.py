import sqlite3 as sql
import threading
import time
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


  def add_user(self, username, password):
    try:
      cursor = self.conn.cursor()
      cursor.execute(
        "INSERT INTO users (username, password) VALUES (?, ?)",
        (username, password)
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
    

  def restart(self):
    self.init_database()


database = Database()