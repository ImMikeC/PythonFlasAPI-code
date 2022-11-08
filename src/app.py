from flask import Flask, jsonify, request
app = Flask(__name__)

todos = [
    { "done": True, "label": "Sam67ple Todo 37434" },
    { "done": True, "label": "Sample Todo 1" },  
    { "done": True, "label": "Sample Todo 2" },
    { "done": True, "label": "Sample Todo 3" },
    { "done": True, "label": "Sample Todo 4" },
    { "done": True, "label": "Sample Todo 5" },
    { "done": True, "label": "Sample Todo 6" }
]

@app.route('/todos', methods=['GET'])
def hello_world():
    json_text = jsonify(todos)
    return json_text

@app.route('/todos', methods=['POST'])
def add_new_todo():
    json_text = jsonify(todos)
    print("Incoming request with the following body", json_text)
    return json_text

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print('This is the position to delete', position)
    return 'something'





if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)