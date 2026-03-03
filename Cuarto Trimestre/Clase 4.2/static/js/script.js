let carrito = JSON.parse(localStorage.getItem('carrito')) || [];

function actualizarContador() {
 let contador = document.getElementById("contador");
 if (contador) {
 contador.textContent = carrito.length;
 }
}
actualizarContador();

function agregarProducto(nombre, precio) {
    carrito.push({ nombre: nombre, precio: precio });
    localStorage.setItem('carrito', JSON.stringify(carrito));
    // Actualizar contador y UI inmediatamente después de agregar
    actualizarContador();
}

function mostrarCarrito() {
    let lista = document.getElementById("listaCarrito");
    let total = 0;

    if (lista) {
        lista.innerHTML = "";

        for (let i = 0; i < carrito.length; i++) {
            let item = document.createElement("li");
            item.textContent = carrito[i].nombre + " - $" + carrito[i].precio;
            lista.appendChild(item);
            total = total + carrito[i].precio;
        }

        document.getElementById("total").textContent = total;
    }
}

mostrarCarrito();

function totalCarrito() {
    let total = 0;
    for (let i = 0; i < carrito.length; i++) {
        total = total + carrito[i].precio;
    }
    return total;
}

function vaciarCarrito(){
    carrito = []; // 1️⃣ Vaciar arreglo
    
    localStorage.setItem('carrito', JSON.stringify(carrito)); // 2️⃣ Actualizar almacenamiento
    
    actualizarContador(); // 3️⃣ Actualizar contador
    
    mostrarCarrito(); // 4️⃣ Actualizar lista en pantalla
}