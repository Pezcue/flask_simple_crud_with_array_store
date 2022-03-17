let log = console.log;
let domainServer = "http://localhost:3000";

let elUsuarios = document.getElementById("usuarios");
let btnUsuario = document.getElementById("btn_usuarios");

async function usuarios() {
    try {
        let r = await axios.get(domainServer + "/usuarios");
        elUsuarios.innerHTML = r.data;
        log(r.data)
    } catch (err) {
        log(err)
    }
}

btnUsuario.addEventListener("click", ()=>{
    usuarios();
});

