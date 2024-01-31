document.addEventListener('DOMContentLoaded', function() {
    var languageCode = navigator.language.split('-')[0]; // Obtiene el código de idioma principal

 
    //////////////////////////////
    // BOTONES VERDESPAGINA PRINCIPAL
    ///////////////////////////////

    if (languageCode === 'es') {
        document.getElementById('privacidad').innerText = 'Políticas de Privacidad';
        document.getElementById('cookies').innerText = 'Políticas de Cookies';
        document.getElementById('terminos').innerText = 'Términos y Condiciones';
    } else if (languageCode === 'it') {
        document.getElementById('privacidad').innerText = 'Politiche sulla Privacy';
        document.getElementById('cookies').innerText = 'Politiche sui Cookie';
        document.getElementById('terminos').innerText = 'Termini e Condizioni';
    } else {
        // Por defecto en inglés u otro idioma
        document.getElementById('privacidad').innerText = 'Privacy Policy';
        document.getElementById('cookies').innerText = 'Cookie Policy';
        document.getElementById('terminos').innerText = 'Terms and Conditions';
    }
});