from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


usuarios = ["ade", "rdx", "foo", "mek"]


@app.route("/usuarios", methods=["GET"])
def get_usuarios():
    return jsonify(usuarios)


@app.route("/agregar", methods=["POST"])
def add_usuarios():
    if request.method == "POST":
        usuario = request.args["usuario"]  
        usuarios.append(usuario)  
    
        return jsonify("usuario agregado:{}".format(usuario))


@app.route("/borrar", methods=["DELETE"])
def delete_usuario():
    if request.method == "DELETE":
       usuario = request.args["nombre"]
       idx = usuarios.index(usuario)
       usuarios.pop(idx)
       
       return jsonify("usuario eliminado:{}".format(usuario))
    

@app.route("/editar", methods=["PUT"])
def update_usuario():
    if request.method == "PUT":
       usuario = request.args["nombre"] 
       nuevo_usuario = request.args.get("editado")

       idx = usuarios.index(usuario)
       usuarios[idx] = nuevo_usuario
               
       return jsonify("usuario editado:{}".format(usuario))
       
       
@app.route("/mostrar", methods=["GET"])
def find_usuario():
    usuario = request.args["nombre"] 
    idx = usuarios.index(usuario)
    
    return jsonify(usuarios[idx])
    
    
    
app.run(host="127.0.0.1",port=3000, debug=True)