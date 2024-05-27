document.addEventListener('DOMContentLoaded', function() {
    var languageCode = navigator.language.split('-')[0]; // Obtiene el código de idioma principal
    console.log(languageCode);
 console.log("JKH");
    //////////////////////////////
    // HEADER
    ///////////////////////////////

    // Traducciones según el código de idioma
    if (languageCode === 'es') {
        // HEADER 
        try {
            var filtrarElement = document.getElementById('hamburgerMenu');
            if (filtrarElement) filtrarElement.innerText = 'Filtrar';
        } catch (error) {
            console.error('Error al traducir el elemento filtrar al español:', error);
        }

        try {
            var cerrarsesionElement = document.getElementById('cerrarsesion');
            if (cerrarsesionElement) cerrarsesionElement.innerText = 'Cerrar sesión';
        } catch (error) {
            console.error('Error al traducir el elemento cerrarsesion al español:', error);
        }

        try {
            var iniciarsesionElement = document.getElementById('iniciarsesion');
            if (iniciarsesionElement) iniciarsesionElement.innerText = 'Iniciar sesión';
        } catch (error) {
            console.error('Error al traducir el elemento iniciarsesion al español:', error);
        }
    } else if (languageCode === 'it') {
        // HEADER 
        try {
            var filtrarElement = document.getElementById('hamburgerMenu');
            if (filtrarElement) filtrarElement.innerText = 'Filtrare';
        } catch (error) {
            console.error('Error al traducir el elemento filtrar al italiano:', error);
        }

        try {
            var cerrarsesionElement = document.getElementById('hamburgerMenu');
            if (cerrarsesionElement) cerrarsesionElement.innerText = 'Chiudi sessione';
        } catch (error) {
            console.error('Error al traducir el elemento cerrarsesion al italiano:', error);
        }

        try {
            var iniciarsesionElement = document.getElementById('iniciarsesion');
            if (iniciarsesionElement) iniciarsesionElement.innerText = 'Accesso';
        } catch (error) {
            console.error('Error al traducir el elemento iniciarsesion al italiano:', error);
        }
    } else {
        // Por defecto en inglés
        // HEADER 
        try {
            var filtrarElement = document.getElementById('hamburgerMenu');
            if (filtrarElement) filtrarElement.innerText = 'Filter';
            if(filtrarElement) console.log("felement");
        } catch (error) {
            console.error('Error al traducir el elemento filtrar al inglés:', error);
        }

        try {
            var cerrarsesionElement = document.getElementById('cerrarsesion');
            if (cerrarsesionElement) cerrarsesionElement.innerText = 'Logout';
        } catch (error) {
            console.error('Error al traducir el elemento cerrarsesion al inglés:', error);
        }

        try {
            var iniciarsesionElement = document.getElementById('iniciarsesion');
            if (iniciarsesionElement) iniciarsesionElement.innerText = 'Login';
        } catch (error) {
            console.error('Error al traducir el elemento iniciarsesion al inglés:', error);
        }
    }



});