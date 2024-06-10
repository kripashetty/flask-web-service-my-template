from flask import Flask, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

items = []


class HelloWorld(Resource):
    def get(self):
        return {'message': 'This is a Flask API!'}


class Item(Resource):
    def get(self, name=None):
        if name:
            for item in items:
                if item['name'] == name:
                    return item
            return {'item': None}, 404
        return items  # List all items

    def post(self, name):
        data = request.get_json()
        item = {'name': name, 'price': data['price']}
        items.append(item)
        return item, 201

    def delete(self, name):
        global items
        items = [item for item in items if item['name'] != name]
        return {'message': 'Item deleted'}


class ItemList(Resource):
    def get(self):
        return items  # List all items


# Adding resource for single item
api.add_resource(Item, '/item/<string:name>')
# Adding resource for listing all items
api.add_resource(ItemList, '/items')
api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)