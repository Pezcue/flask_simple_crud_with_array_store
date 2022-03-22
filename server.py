from crypt import methods
from flask import Flask, request, jsonify
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

productos = [
    {
        'nombre': 'Microondas',
        'detalle': '14 pulgadas',
        'stock': 12,

    },
    {
        'nombre': 'televisor',
        'detalle': '42 pulgadas',
        'stock': 22,

    },
    {
        'nombre': 'licuadora',
        'detalle': 'grande',
        'stock': 14,

    },
    {
        'nombre': 'aire acondicionado',
        'detalle': '12000 btu',
        'stock': 40,

    },
]

# Endpoint 1 ~(ver los productos)
@app.route("/all" , methods=["GET"])
def get_productos():
    return jsonify(productos)

# Endpoint 2 ~(Agregar productos)
@app.route("/add", methods=["POST"])
def add_productos():
    if request.method == "POST":
        producto = request.args["producto"]
        productos.append(producto)
        return jsonify("Se ha agregado {}".format(producto))

# Endpoint 3 ~(Buscar productos)
@app.route("/src", methods=["GET"])
def display_productos():
    producto = request.args["nombre"]
    idx = productos.index(producto)
    return jsonify(productos[idx])

# Endpoint 4 ~(Borrar productos)
@app.route("/del", methods=["DELETE"])
def remove_productos():
    producto = request.args["nombre"]
    idx = productos.index(producto)
    productos.pop(idx)
    return jsonify("Se ha borrado {}".format(productos))

app.run(host="127.0.0.1", port=5000, debug=True)
