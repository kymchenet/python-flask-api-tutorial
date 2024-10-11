from flask import Flask
from flask import Flask, jsonify
from flask import request

app = Flask(__name__) 

todos = [
    {
        "label": "Programar",
        "done": False}
    ]

@app.route('/todos', methods=['GET'])
def get_todo():
    return jsonify(todos)

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    print("Incoming request with the following body", request_body)
    todos.append(request_body)
    return jsonify(todos), 200

@app.route('/todos/<int:index>', methods=['DELETE'])
def delete_todo(index):
    if index < 0 or index >= len(todos):
       return jsonify({"error": "index no existe"}), 400
 
    todos.pop(index)

    return jsonify(todos), 200










# Estas dos líneas siempre deben estar al final de tu archivo app.py

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)