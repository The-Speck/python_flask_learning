from flask import Flask, request, jsonify
from flask_restful import Resource, Api, reqparse
from flask_jwt_extended import JWTManager, jwt_required, create_access_token
import uuid as _

from security import authenticate, identity

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = str(_.uuid4())
api = Api(app)
jwt = JWTManager(app)

items = [
  {
    "id": 1,
    "name": "odorizer",
    "price": 123.12
  }
]

def message(msg):
  return {'message': msg}

class Item(Resource):
  parser = reqparse.RequestParser()
  parser.add_argument(
      'price',
      type=float,
      required=True,
      help='Price cannot be blank!'
  )
  parser.add_argument(
      'name',
      type=str,
      required=True,
      help='name cannot be blank!'
  )

  @jwt_required
  def get(self, id):
    item = next(filter(lambda item: item['id'] == id, items), None)
    if item is not None:
      return item
    else:
      return 404
  
  def put(self, id):
    print('Updating item')
    updateItem = Item.parser.parse_args()
    
    item = next(filter(lambda item: item['id'] == id, items), None)
    if item:
        item.update(updateItem)
    else:
      items.append(updateItem)
    return updateItem, 201
  
  def delete(self, id):
    global items
    items = list(filter(lambda item: item['id'] != id, items))
    return None, 204

class ItemList(Resource):
  def get(self):
    print('Getting all items')
    return items
  
  def post(self):
    print('Creating item')
    item = Item.parser.parse_args()

    id = max([item['id'] for item in items]) + 1
    item['id'] = id
    items.append(item)
    return item, 201


class Auth(Resource):
  def post(self):
    username = request.json.get('username', None)
    password = request.json.get('password', None)
    if not username:
      return message("Missing username parameter"), 400
    if not password:
      return message("Missing password parameter"), 400
    
    user = authenticate(username, password)

    if user:
      accessToken = create_access_token(identity=username)
      return {'access_token': accessToken}, 200
    else:
      return message('Invalid Username or Password'), 401


api.add_resource(Item, '/item/<int:id>')
api.add_resource(ItemList, '/items')
api.add_resource(Auth, '/login')

print('Random test text3')
print('__name__ = ' + __name__)
if __name__ == '__main__':
  app.run()
