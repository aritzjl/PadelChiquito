document.addEventListener('DOMContentLoaded', function() {
    var languageCode = navigator.language.split('-')[0]; // Obtiene el código de idioma principal
console.log(languageCode);
 console.log("JKH");
    //////////////////////////////
    // BOTONES VERDESPAGINA PRINCIPAL
    ///////////////////////////////

    if (languageCode === 'es') {

    } else if (languageCode === 'it') {

        document.getElementById('all').innerText = 'Tutte';
        document.getElementById('best2024').innerText = 'Migliori pale 2024';
        document.getElementById('best150').innerText = 'Migliori pale < 150€';
        document.getElementById('power').innerText = 'Migliori pale Potenza';
        document.getElementById('control').innerText = 'Migliori pale Controllo';


        document.getElementById('tituloImagen').innerText = 'Immagine';
        document.getElementById('tituloTemporada').innerText = 'Stagione';
        document.getElementById('tituloMarca').innerText = 'Marca';
        document.getElementById('tituloNombre').innerText = 'Nome';
        document.getElementById('tituloForma').innerText = 'Forma';
        document.getElementById('tituloNivel').innerText = 'Livello';
        document.getElementById('tituloControl').innerText = 'Controllo';
        document.getElementById('tituloPotencia').innerText = 'Potenza';
        document.getElementById('tituloDefensa').innerText = 'Difesa';
        document.getElementById('tituloAtaque').innerText = 'Attacco';
        document.getElementById('tituloTotal').innerText = 'Punteggio Totale';

    } else {
        
        document.getElementById('all').innerText = 'All';
        document.getElementById('best2024').innerText = 'Best rackets 2024';
        document.getElementById('best150').innerText = 'Best rackets < €150';
        document.getElementById('power').innerText = 'Best Power rackets';
        document.getElementById('control').innerText = 'Best Control rackets';


        document.getElementById('tituloImagen').innerText = 'Image';
        document.getElementById('tituloTemporada').innerText = 'Season';
        document.getElementById('tituloMarca').innerText = 'Brand';
        document.getElementById('tituloNombre').innerText = 'Name';
        document.getElementById('tituloForma').innerText = 'Shape';
        document.getElementById('tituloNivel').innerText = 'Level';
        document.getElementById('tituloControl').innerText = 'Control';
        document.getElementById('tituloPotencia').innerText = 'Power';
        document.getElementById('tituloDefensa').innerText = 'Defense';
        document.getElementById('tituloAtaque').innerText = 'Attack';
        document.getElementById('tituloTotal').innerText = 'Total Rating';
    }

  

});