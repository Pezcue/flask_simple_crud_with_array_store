const axios = require("axios");

let log = console.log;
let domainServer = "http://localhost:3000";

async function usuarios() {
    try {
        let r = await axios.get(domainServer + "/usuarios");
        log(r.data)
    } catch (err) {
        log(err)
    }
}

async function agregarUsuario(usuario) {
    try {
        let r = await axios.post(domainServer + "/agregar", null, {
            params: {
                usuario
            }
        });
        log(r.data)
    } catch (err) {
        log(err)
    }
}

async function borrarUsuario(nombre) {
    try {
        let r = await axios.delete(domainServer + "/borrar", {
            params: {
                nombre
            }
        });
        log(r.data)
    } catch (err) {
        log(err)
    }
}


async function editarUsuario(nombre, editado) {
    try {
        let r = await axios.put(domainServer + "/editar", null, {
            params: {
                nombre,
                editado
            }
        });
        log(r.data)
    } catch (err) {
        log(err)
    }
}

async function mostrarUsuario(nombre) {
    try {
        let r = await axios.get(domainServer + "/mostrar", {
            params: {
                nombre
            }
        });
        log(r.data)
    } catch (err) {
        log(err)
    }
}


//agregarUsuario("test")
//borrarUsuario("foo");
//editarUsuario("mek", "toto")
//usuarios();
//mostrarUsuario("toto")