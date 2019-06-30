from functools import wraps
import sqlite3

def handle_connection(func):
  @wraps(func)
  def wrapper(*args, **kwargs):
      connection = sqlite3.connect('python-flask.db')
      cursor = connection.cursor()
      result = func(*args, **kwargs, cursor=cursor, connection=connection)
      if result:
        connection.commit()
      connection.close()
      return result
  return wrapper
