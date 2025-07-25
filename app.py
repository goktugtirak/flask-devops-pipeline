from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "API is running!"

@app.route("/hello", methods=["GET"])
def hello():
    return jsonify({"message": "Hello, DevOps!"})

@app.route("/greet", methods=(["POST"]))
def greet():
    data = request.get_json()
    name = data.get("name", "stranger")
    return jsonify({"message": f"Hello, {name}!"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)