from flask import Flask, request
from flask_restful import Resource, Api
import uuid as _

app = Flask(__name__)
app.secret_key = _.uuid4()
api = Api(app)

items = [
  {
    "id": 1,
    "name": "odorizer",
    "price": 123.12
  }
]

class Item(Resource):
  def get(self, id):
    item = next((item for item in items if item['id'] == id), None)
    if item is not None:
      return item
    else:
      return 404
  
  def put(self, id):
    print('Updating item')
    item = next((item for item in items if item['id'] == id), None)
    if item is not None:
        requestItem = request.get_json()
        item.update(requestItem)
        return item, 201
    return None, 404
  
  def delete(self, id):
    for idx, item in enumerate(items):
      if item['id'] == id:
        del items[idx]
        break
    return None, 204

class ItemList(Resource):
  def get(self):
    print('Getting all items')
    return items
  
  def post(self):
    print('Create item')
    item = request.get_json()
    id = max([item['id'] for item in items]) + 1
    item['id'] = id
    items.append(item)
    return item, 201

api.add_resource(Item, '/item/<int:id>')
api.add_resource(ItemList, '/items')

print('Random test text3')
print('__name__ = ' + __name__)
if __name__ == '__main__':
  app.run()
