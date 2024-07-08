document.addEventListener('DOMContentLoaded', function() {
    const formularioContacto = document.getElementById('formularioContacto');

    formularioContacto.addEventListener('submit', function(event) {
        
        if (!validarFormulario()) {
            event.preventDefault(); 
        }
    });

    const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    function validateEmail(email) {
        // Utilizar expresión regular para validar el formato del correo electrónico
        return regex.test(email);
    }

    function validarFormulario() {
        const nombre = document.getElementById('nombre').value;
        const email = document.getElementById('email').value;
        const mensaje = document.getElementById('mensaje').value;

        if (nombre === '' || email === '' || mensaje === '') {
            alert('Por favor completa todos los campos.');
            return false; 
        } else if (nombre.length < 3) {
            alert('El nombre debe tener al menos 3 caracteres.');
            return false; 
        } else if (!validateEmail(email)) {
            alert('Ingresa un correo electrónico válido.');
            return false; 
        } else if (mensaje.length < 10) {
            alert('El mensaje debe tener al menos 10 caracteres.');
            return false; 
        }
        return true;
    }
});