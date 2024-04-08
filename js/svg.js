// Obtener referencia a los SVGs y al texto
const icon1 = document.querySelector('.icon--contactme');
const icon2 = document.querySelector('.icon--mail');
const icon3 = document.querySelectorAll('.icon--mail')[1]; // El tercer icono tiene la clase repetida, por lo que seleccionamos el segundo con [1]
const contactText = document.getElementById('contactText');

// Función para cambiar la visibilidad del texto
function toggleTextVisibility() {
  contactText.classList.toggle('hidden');
}

// Agregar eventos de clic a los SVGs para cambiar la visibilidad del texto
icon1.addEventListener('click', toggleTextVisibility);
icon2.addEventListener('click', toggleTextVisibility);
icon3.addEventListener('click', toggleTextVisibility);