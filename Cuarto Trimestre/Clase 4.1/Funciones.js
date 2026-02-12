function cambiarColor() {
     document.body.style.background = "lightblue";
}

function cambiarTexto() {
    document.getElementById("titulo").innerText = "Aprendiendo Java Script";
}

function cambiarImagen ()
{
    document.getElementById("imagen").src =
     "https://idbinvest.org/sites/default/files/styles/size936x656/public/2021-06/banner.jpg.webp?itok=-S5uxg8T";
}

function ocultarImagen ()
{
    document.getElementById("imagen").style.display = "none";
}

function crearNuevoBoton()
{
    var newboton = document.createElement("button");
    newboton.innerText = "Ocultar Botones";
    newboton.id = "nuevoBoton";
    document.body.appendChild(newboton);
    newboton.onclick = ocultarBotones;
}

function ocultarBotones()
{    
    document.getElementById("1").style.display = "none";
    document.getElementById("2").style.display = "none";
    document.getElementById("3").style.display = "none";
    document.getElementById("4").style.display = "none";
    document.getElementById("5").style.display = "none";
    document.getElementById("6").style.display = "none";
    document.getElementById("7").style.display = "none";
    document.getElementById("nuevoBoton").style.display = "none";

    var aparecer = document.createElement("button");
    aparecer.innerText = "Mostrar Botones";
    aparecer.id = "aparecer";
    document.body.appendChild(aparecer);
    aparecer.onclick = mostrarBotones;
}

function mostrarBotones()
{
    document.getElementById("1").style.display = "";
    document.getElementById("2").style.display = "";
    document.getElementById("3").style.display = "";
    document.getElementById("4").style.display = "";
    document.getElementById("5").style.display = "";
    document.getElementById("6").style.display = "";
    document.getElementById("7").style.display = "";
    document.getElementById("aparecer").style.display = "none";
}

function modoOscuro()
{
    document.body.style.background="black";
}

function aparecerImagen ()
{
    document.getElementById("imagen").style.display = "";
}