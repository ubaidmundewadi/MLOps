from flask import Flask,jsonify,request

items = [
    { 'id': 1, 'name': 'Apple', 'description': 'Apple a day'},
    { 'id': 2, 'name': 'Mango', 'description': 'Mango is a king'}
]

app = Flask(__name__)

@app.route('/')
def welcome():
    return "Welcome to the homepage"

@app.route('/items',methods=['GET'])
def get_items():
    return jsonify(items)

@app.route('/items/<int:item_id>',methods=["GET"])
def get_item(item_id):
    item = next((item for item in items if item['id'] == item_id), None)
    if item is None:
        return jsonify({'error': 'Item not found'})
    return jsonify(item)

@app.route('/items',methods=['POST'])
def add_item():
    new_item = {
        'id': items[-1]['id']+1 if items else 1,
        'name': request.json['name'],
        'description': request.json['description']
    }
    items.append(new_item)
    return jsonify(new_item)

@app.route('/items/<int:item_id>',methods=['PUT'])
def update_item(item_id):
    item = next((item for item in items if item['id'] == item_id), None)
    if item is None:
        return jsonify({"response": "Error"})
    item['name'] = request.json.get('name',item['name'])
    item['description'] = request.json.get('description',item['description'])
    return jsonify(item)


@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    global items
    items = [item for item in items if item['id'] != item_id]
    return jsonify({"response": "Item deleted"})

if __name__ == "__main__":
    app.run(debug=True)

