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

        // Traducciones para los filtros
        document.getElementById('filtroPrecio').innerText = 'Prezzo';
        document.getElementById('filtroPotencia').innerText = 'Potenza';
        document.getElementById('filtroBandeja').innerText = 'Piastra';
        document.getElementById('filtroBajada').innerText = 'Punto Caduta';
        document.getElementById('filtroFondo').innerText = 'Fondo';
        document.getElementById('filtroRemate').innerText = 'Smatch';
        document.getElementById('filtroVolea').innerText = 'Volley';
        document.getElementById('filtroNivel').innerText = 'Livello';
        document.getElementById('filtroBalance').innerText = 'Bilanciamento';
        document.getElementById('filtroDureza').innerText = 'Durezza';
        document.getElementById('filtroForma').innerText = 'Forma';
        document.getElementById('filtroAplicar').innerText = 'Applica Filtro';

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
    
    
        // Translations for filters
        document.getElementById('filtroPrecio').innerText = 'Price';
        document.getElementById('filtroPotencia').innerText = 'Power';
        document.getElementById('filtroBandeja').innerText = 'Tray';
        document.getElementById('filtroBajada').innerText = 'Drop Shot';
        document.getElementById('filtroFondo').innerText = 'Baseline';
        document.getElementById('filtroRemate').innerText = 'Smash';
        document.getElementById('filtroVolea').innerText = 'Volley';
        document.getElementById('filtroNivel').innerText = 'Level';
        document.getElementById('filtroBalance').innerText = 'Balance';
        document.getElementById('filtroDureza').innerText = 'Hardness';
        document.getElementById('filtroForma').innerText = 'Shape';
        document.getElementById('filtroAplicar').innerText = 'Apply Filters';
    
    }

  

});