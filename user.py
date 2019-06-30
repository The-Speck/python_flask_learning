import sqlite3
from flask_restful import Resource, reqparse
from db import handle_connection
from util import message

class User:
  def __init__(self, _id, username, password):
    self.id = _id
    self.username = username
    self.password = password

  @classmethod
  @handle_connection
  def find_by_username(cls, username, cursor=None, connection=None):
    query = 'SELECT * FROM users WHERE username=?'
    result = cursor.execute(query, (username,))
    row = result.fetchone()
    if row:
      user = cls(*row)
    else:
      user = None

    return user

  @classmethod
  @handle_connection
  def find_by_id(cls, _id, cursor=None, connection=None):
    query = 'SELECT * FROM users WHERE id=?'
    result = cursor.execute(query, (_id,))
    row = result.fetchone()
    if row:
      user = cls(*row)
    else:
      user = None

    return user

class UserRegister(Resource):
  parser = reqparse.RequestParser()
  parser.add_argument(
      'username',
      type=str,
      required=True,
      help='username cannot be blank!'
  )
  parser.add_argument(
      'password',
      type=str,
      required=True,
      help='password cannot be blank!'
  )

  @classmethod
  @handle_connection
  def post(cls, cursor, connection):
    data = UserRegister.parser.parse_args()

    if User.find_by_username(data['username']):
      return message('Username already exists'), 422

    query = "INSERT INTO users ('username', 'password') VALUES (?, ?)"
    cursor.execute(query, (data['username'], data['password']))
    connection.commit()
    id = cursor.lastrowid
    user = User.find_by_id(id)

    return user.__dict__, 201
