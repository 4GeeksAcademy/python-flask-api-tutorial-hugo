from flask import Flask,jsonify, request

app = Flask(__name__)

todos=[{
   "label":"My first task",
   "done": False
}]



@app.route('/todos', methods=['GET'])
def hello_world():
    return jsonify(todos)

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.get_json()
    if not request_body.get("label") or not request_body.get("done") or not request_body["label"] or not request_body["done"]:
        return jsonify({"message":"The fields can´t be empty"}) , 400
    print("Incoming request with the following body", request_body)
    todos.append(request_body)
    return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    if len(todos)==position or len(todos)<position: 
        return jsonify({"message":"the product isn`t exit"}), 400
    del todos[position]
    print("This is the position to delete:", position, len(todos))
    return jsonify(todos)






if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)