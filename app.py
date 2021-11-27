from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/foo', methods=['GET']) 
def foo():
    a()
    # data = request.json
    # return jsonify(data)
    # return "Hello world"
    return jsonify({"F":"4"}), 200

def a():
    print("a")
    b()

def b():
    print("b")