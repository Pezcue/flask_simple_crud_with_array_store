from flask import Flask, request, jsonify
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


users = ["foo", "bar", "baz", "qux"]


@app.route("/")
def index():
    return "bienvenidos al sistema"


@app.route("/users")
def all_users():
    return jsonify(users)


@app.route("/q")
def query_user():
    n = request.args["n"]
    idx = users.index(n)
    return jsonify(users[idx])


@app.route("/add", methods=["POST"])
def add_user():
    if request.method == "POST":
        nombre = request.args["nombre"]
        users.append(nombre)
        return jsonify("usuario agregado...")


@app.route("/del", methods=["DELETE"])
def del_user():
    if request.method == "DELETE":
        nombre = request.args["nombre"]
        idx = users.index(nombre)
        users.pop(idx)
        return jsonify("usuario:{} eliminado".format(nombre))


@app.route("/up", methods=["PUT"])
def up_user():
    if request.method == "PUT":
        n = request.args["nombre"]
        f = request.args["valor"]
        idx = users.index(n)
        users[idx] = f
        return jsonify("usuario:{} actualizado...".format(n))


app.run(host="127.0.0.1", port=5000, debug=True)
