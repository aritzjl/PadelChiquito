document.addEventListener('DOMContentLoaded', function() {
    var languageCode = navigator.language.split('-')[0]; // Obtiene el código de idioma principal


    if(languageCode=="es"){

    }else if(languageCode=="it"){
// Cambia Password
try {
    document.getElementById('contraTitle').innerText = 'Nuova Password';
} catch (error) {
    console.error("Errore nell'aggiornare 'contraTitle':", error.message);
}

try {
    document.getElementById('bienvenido').innerText = 'Bentornato. Inserisci la tua nuova password per completare il processo.';
} catch (error) {
    console.error("Errore nell'aggiornare 'bienvenido':", error.message);
}

try {
    document.getElementById('contraTag').innerText = 'Password';
} catch (error) {
    console.error("Errore nell'aggiornare 'contraTag':", error.message);
}

try {
    document.getElementById('confirmar').innerText = 'Conferma';
} catch (error) {
    console.error("Errore nell'aggiornare 'confirmar':", error.message);
}

// Conferma Email
try {
    document.getElementById('revisaMail').innerText = 'Controlla la tua email';
} catch (error) {
    console.error("Errore nell'aggiornare 'revisaMail':", error.message);
}

try {
    document.getElementById('revisaMailMensaje').innerText = 'Saluti da Padel Chiquito. Controlla la tua email, ti abbiamo inviato un messaggio importante.';
} catch (error) {
    console.error("Errore nell'aggiornare 'revisaMailMensaje':", error.message);
}

// Password Dimenticata
try {
    document.getElementById('hasOlvidado').innerText = 'Hai dimenticato la password?';
} catch (error) {
    console.error("Errore nell'aggiornare 'hasOlvidado':", error.message);
}

try {
    document.getElementById('introduceMail').innerText = 'Inserisci il tuo indirizzo email per ricevere un link per il ripristino della password.';
} catch (error) {
    console.error("Errore nell'aggiornare 'introduceMail':", error.message);
}

try {
    document.getElementById('email').innerText = 'Email';
} catch (error) {
    console.error("Errore nell'aggiornare 'email':", error.message);
}

// Accedi
try {
    document.getElementById('iniTitle').innerText = 'Accedi';
} catch (error) {
    console.error("Errore nell'aggiornare 'iniTitle':", error.message);
}

try {
    document.getElementById('iniMSG').innerText = 'Collegati per accedere al tuo account.';
} catch (error) {
    console.error("Errore nell'aggiornare 'iniMSG':", error.message);
}

try {
    document.getElementById('emailTag').innerText = 'Email';
} catch (error) {
    console.error("Errore nell'aggiornare 'emailTag':", error.message);
}

try {
    document.getElementById('iniBtn').innerText = 'Accedi';
} catch (error) {
    console.error("Errore nell'aggiornare 'iniBtn':", error.message);
}

try {
    document.getElementById('contraOlv').innerText = 'Hai dimenticato la password?';
} catch (error) {
    console.error("Errore nell'aggiornare 'contraOlv':", error.message);
}

try {
    document.getElementById('noCuenta').innerText = 'Non hai un account?';
} catch (error) {
    console.error("Errore nell'aggiornare 'noCuenta':", error.message);
}

try {
    document.getElementById('crearCuenta').innerText = 'Crea un account';
} catch (error) {
    console.error("Errore nell'aggiornare 'crearCuenta':", error.message);
}

// Sezione Registra
try {
    document.getElementById('regiTitle').innerText = 'Registrati';
} catch (error) {
    console.error("Errore nell'aggiornare 'regiTitle':", error.message);
}

try {
    document.getElementById('regiMSG').innerText = "È veloce e semplice.";
} catch (error) {
    console.error("Errore nell'aggiornare 'regiMSG':", error.message);
}

try {
    document.getElementById('nombreTag').innerText = 'Nome*';
} catch (error) {
    console.error("Errore nell'aggiornare 'nombreTag':", error.message);
}

try {
    document.getElementById('dniTag').innerText = 'Città';
} catch (error) {
    console.error("Errore nell'aggiornare 'dniTag':", error.message);
}

try {
    document.getElementById('apellidosTag').innerText = 'Cognome';
} catch (error) {
    console.error("Errore nell'aggiornare 'apellidosTag':", error.message);
}

try {
    document.getElementById('nacimientoTag').innerText = 'Data di nascita*';
} catch (error) {
    console.error("Errore nell'aggiornare 'nacimientoTag':", error.message);
}

try {
    document.getElementById('contraTag2').innerText = 'Ripeti la password*';
} catch (error) {
    console.error("Errore nell'aggiornare 'contraTag2':", error.message);
}

try {
    document.getElementById('deseoRecibir').innerText = 'Desidero ricevere informazioni sui prodotti e servizi di Padel.';
} catch (error) {
    console.error("Errore nell'aggiornare 'deseoRecibir':", error.message);
}

try {
    document.getElementById('aceptoPo').innerHTML = '*Accetto l<a href="{% static \'pdfs/privacidad.doc\' %}" class="text-blue-500 transition-colors hover:text-blue-400">a Privacy Policy</a> e le <a href="{% static \'pdfs/condiciones.doc\' %}" class="text-blue-500 transition-colors hover:text-blue-400">Condizioni Generali di Contratto</a>.';

} catch (error) {
    console.error("Errore nell'aggiornare 'aceptoPo':", error.message);
}

try {
    document.getElementById('regiBtn').innerText = 'Registrati';
} catch (error) {
    console.error("Errore nell'aggiornare 'regiBtn':", error.message);
}

try {
    document.getElementById('yaCuenata').innerText = 'Hai già un account?';
} catch (error) {
    console.error("Errore nell'aggiornare 'yaCuenata':", error.message);
}

    }else{
       // Change Password
try {
    document.getElementById('contraTitle').innerText = 'New Password';
} catch (error) {
    console.error("Error updating 'contraTitle':", error.message);
}

try {
    document.getElementById('bienvenido').innerText = 'Welcome back. Please enter your new password to complete the process.';
} catch (error) {
    console.error("Error updating 'bienvenido':", error.message);
}

try {
    document.getElementById('contraTag').innerText = 'Password';
} catch (error) {
    console.error("Error updating 'contraTag':", error.message);
}

try {
    document.getElementById('confirmar').innerText = 'Confirm';
} catch (error) {
    console.error("Error updating 'confirmar':", error.message);
}

// Email Confirmation
try {
    document.getElementById('revisaMail').innerText = 'Check your email';
} catch (error) {
    console.error("Error updating 'revisaMail':", error.message);
}

try {
    document.getElementById('revisaMailMensaje').innerText = 'Greetings from Padel Chiquito. Please check your email, we have sent you an important message.';
} catch (error) {
    console.error("Error updating 'revisaMailMensaje':", error.message);
}

// Forgot Password
try {
    document.getElementById('hasOlvidado').innerText = 'Forgot your password?';
} catch (error) {
    console.error("Error updating 'hasOlvidado':", error.message);
}

try {
    document.getElementById('introduceMail').innerText = 'Enter your email address to receive a password reset link.';
} catch (error) {
    console.error("Error updating 'introduceMail':", error.message);
}

try {
    document.getElementById('email').innerText = 'Email';
} catch (error) {
    console.error("Error updating 'email':", error.message);
}

// Log In
try {
    document.getElementById('iniTitle').innerText = 'Log In';
} catch (error) {
    console.error("Error updating 'iniTitle':", error.message);
}

try {
    document.getElementById('iniMSG').innerText = 'Connect to access your account.';
} catch (error) {
    console.error("Error updating 'iniMSG':", error.message);
}

try {
    document.getElementById('emailTag').innerText = 'Email';
} catch (error) {
    console.error("Error updating 'emailTag':", error.message);
}

try {
    document.getElementById('iniBtn').innerText = 'Log In';
} catch (error) {
    console.error("Error updating 'iniBtn':", error.message);
}

try {
    document.getElementById('contraOlv').innerText = 'Forgot your password?';
} catch (error) {
    console.error("Error updating 'contraOlv':", error.message);
}

try {
    document.getElementById('noCuenta').innerText = "Don't have an account?";
} catch (error) {
    console.error("Error updating 'noCuenta':", error.message);
}

try {
    document.getElementById('crearCuenta').innerText = 'Create Account';
} catch (error) {
    console.error("Error updating 'crearCuenta':", error.message);
}

// Register Section
try {
    document.getElementById('regiTitle').innerText = 'Sign Up';
} catch (error) {
    console.error("Error updating 'regiTitle':", error.message);
}

try {
    document.getElementById('regiMSG').innerText = "It's quick and easy.";
} catch (error) {
    console.error("Error updating 'regiMSG':", error.message);
}

try {
    document.getElementById('nombreTag').innerText = 'Name*';
} catch (error) {
    console.error("Error updating 'nombreTag':", error.message);
}

try {
    document.getElementById('dniTag').innerText = 'City';
} catch (error) {
    console.error("Error updating 'dniTag':", error.message);
}

try {
    document.getElementById('apellidosTag').innerText = 'Last Name';
} catch (error) {
    console.error("Error updating 'apellidosTag':", error.message);
}

try {
    document.getElementById('nacimientoTag').innerText = 'Date of Birth*';
} catch (error) {
    console.error("Error updating 'nacimientoTag':", error.message);
}

try {
    document.getElementById('contraTag2').innerText = 'Repeat Password*';
} catch (error) {
    console.error("Error updating 'contraTag2':", error.message);
}

try {
    document.getElementById('deseoRecibir').innerText = 'I want to receive information about Padel products and services.';
} catch (error) {
    console.error("Error updating 'deseoRecibir':", error.message);
}

try {
    document.getElementById('aceptoPo').innerText = '*I accept the Privacy Policy and the General Terms and Conditions.';
} catch (error) {
    console.error("Error updating 'aceptoPo':", error.message);
}

try {
    document.getElementById('regiBtn').innerText = 'Sign Up';
} catch (error) {
    console.error("Error updating 'regiBtn':", error.message);
}

try {
    document.getElementById('yaCuenata').innerText = 'Already have an account?';
} catch (error) {
    console.error("Error updating 'yaCuenata':", error.message);
}


    }

});