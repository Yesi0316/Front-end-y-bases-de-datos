const btn = document.getElementById("btnInfo");
const modal = document.getElementById("modal");
const cerrar = document.getElementById("cerrar"); 

btn.addEventListener("click", () => {
  modal.style.display = "flex";
});

cerrar.addEventListener("click", () => {
  modal.style.display = "none";
});

// Agregar un evento para cerrar el modal al hacer clic fuera del contenido
window.addEventListener("click", (event) => {
  if (event.target === modal) {
    modal.style.display = "none";
  }
});