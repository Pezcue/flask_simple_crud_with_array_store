var axios = require("axios");

let url = "http://localhost:5000"

async function getUsers() {
    try {
        let res = await axios.get(url + "/users");
        console.log(res.data)
    } catch (err) {
        console.log(err);
    }
}

async function addUser(nombre) {
    try {
        let r = await axios.post(url + "/add", null, {
            params: {
                nombre: nombre
            }
        });
        console.log(r.data)
    } catch (err) {
        console.log(err)
    }
}

async function delUser(nombre) {
    try {
        let r = await axios.delete(url + "/del", {
            params: {
                nombre
            }
        });
        console.log(r.data)
    } catch (err) {
        console.log(err);
    }
}


async function putUser(nombre, valor) {
    try {
        let r = await axios.put(url + "/up", null, {
            params: {
                nombre,
                valor
            }
        });
        console.log(r.data)
    } catch (err) {
        console.log(err);
    }
}

async function qUser(n) {
    try {
        let res = await axios.get(url + "/q",{
            params: {
                n
            }
        });
        console.log(res.data)
    } catch (err) {
        console.log(err);
    }
}


getUsers()
//qUser("bar")
//addUser("randomx")
//delUser("qux")
//putUser("sp", "super")