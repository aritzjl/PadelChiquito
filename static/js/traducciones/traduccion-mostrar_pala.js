document.addEventListener('DOMContentLoaded', function() {
    var languageCode = navigator.language.split('-')[0]; // Obtiene el código de idioma principal

    if(languageCode=="it"){
// TITOLI Statistiche
document.getElementById('temporada').innerHTML = '<strong class="font-semibold text-gray-600">Stagione:</strong> ';// + palaData.temporada
document.getElementById('materialMarco').innerText = '';
document.getElementById('materialMarco').innerHTML = '<strong class="font-semibold text-gray-600">Materiale Telaio:</strong> ' ;//+ palaData.materialMarco
document.getElementById('materialPlano').innerHTML = '<strong class="font-semibold text-gray-600">Materiale Faccia:</strong> ';// + palaData.materialPlano
document.getElementById('materialGoma').innerHTML = '<strong class="font-semibold text-gray-600">Materiale Gomma:</strong> ';// + palaData.materialGoma
document.getElementById('tacto').innerHTML = '<strong class="font-semibold text-gray-600">Tocco:</strong> ' ;//+ palaData.tacto
document.getElementById('forma').innerHTML = '<strong class="font-semibold text-gray-600">Forma:</strong> ' ;//+ palaData.forma
document.getElementById('peso').innerHTML = '<strong class="font-semibold text-gray-600">Peso:</strong> ' ;//+ palaData.peso
document.getElementById('balance').innerHTML = '<strong class="font-semibold text-gray-600">Equilibrio:</strong> ';// + palaData.balance

document.getElementById('mejorPrecio').innerText = 'Miglior Prezzo';
document.getElementById('puntuacion').innerText = 'Valutazione';

// ETICHETTE A BARRE
document.getElementById('control').innerText = 'Controllo: ' + palaData.control;
document.getElementById('potencia').innerText = 'Potenza: ' + palaData.potencia;
document.getElementById('defensa').innerText = 'Difesa: ' + palaData.defensa;
document.getElementById('ataque').innerText = 'Attacco: ' + palaData.ataque;
document.getElementById('manejabilidad').innerText = 'Manovrabilità: ' + palaData.manejabilidad;
document.getElementById('remate').innerText = 'Smash: ' + palaData.remate;
document.getElementById('salidaBola').innerText = 'Uscita Palla: ' + palaData.salidaBola;
document.getElementById('volea').innerText = 'Volley: ' + palaData.volea;
document.getElementById('puntoDulce').innerText = 'Punto Dolce: ' + palaData.puntoDulce;
document.getElementById('bajada').innerText = 'Caduta Palla: ' + palaData.bajada;
document.getElementById('fondoPista').innerText = 'Profondità del Campo: ' + palaData.fondoDePista;
document.getElementById('bandeja').innerText = 'Vassoio: ' + palaData.bandeja;
document.getElementById('puntuacionTotal').innerText = 'Valutazione Totale: ' + palaData.puntuacionTotal;

// NEGOZI E PREZZI
document.getElementById('tiendasPrecios').innerText = 'Negozi e Ultimi Prezzi';
try{
    document.getElementById('codigos').innerHTML = '<span class="text-sm text-gray-800">Codice Promozionale: {{ precio.tienda.codigo_promocional }}</span>';
    document.getElementById('descuentos').innerHTML = '<span class="text-sm text-gray-800">Sconto: {{ precio.tienda.descuento }}%</span>';
}catch(error){

}

document.getElementById('historialPrecios').innerText = 'Cronologia dei Prezzi';

// SEZIONE RACCHETTE SIMILI
document.getElementById('palasSimilares').innerText = 'Racchette Simili';
//document.getElementById('similarMarca').innerHTML = '<span class="text-sm text-gray-500">Marca: {{ pala_similar.marca }}</span>';

// SEZIONE RECENSIONI
document.getElementById('reviewsPala').innerText = 'Recensioni per la Racchetta ' + palaData.palaNombre;
document.getElementById('noreviews').innerText = 'Nessuna recensione per questa racchetta ancora.';

// SEZIONE COMMENTI
document.getElementById('tituloComentarios').innerText = 'Commenti';
document.getElementById('tuComentario').innerText = 'Il Tuo Commento';
document.getElementById('agregarComentario').value = 'Aggiungi commento';
try{
    document.getElementById('nocomentarios').innerText = 'Ancora nessun commento.';
}catch(error){
    
}
    }
    else if(languageCode=="es"){

    }else{
        
    // TITLES Statistics
    document.getElementById('temporada').innerHTML = '<strong class="font-semibold text-gray-600">Season:</strong> '; // + palaData.temporada

    document.getElementById('materialMarco').innerHTML = '<strong class="font-semibold text-gray-600">Frame Material:</strong> '; // + palaData.materialMarco
    document.getElementById('materialPlano').innerHTML = '<strong class="font-semibold text-gray-600">Face Material:</strong> '; // + palaData.materialPlano
    document.getElementById('materialGoma').innerHTML = '<strong class="font-semibold text-gray-600">Rubber Material:</strong> '; //+ palaData.materialGoma
    document.getElementById('tacto').innerHTML = '<strong class="font-semibold text-gray-600">Touch:</strong> '; //+ palaData.tacto
    document.getElementById('forma').innerHTML = '<strong class="font-semibold text-gray-600">Shape:</strong> '; //+ palaData.forma
    document.getElementById('peso').innerHTML = '<strong class="font-semibold text-gray-600">Weight:</strong> '; //+ palaData.peso
    document.getElementById('balance').innerHTML = '<strong class="font-semibold text-gray-600">Balance:</strong> '; //+ palaData.balance

    document.getElementById('mejorPrecio').innerText = 'Best Price';
    document.getElementById('puntuacion').innerText = 'Rating';

    // BAR LABELS
    document.getElementById('control').innerText = 'Control: ' + palaData.control;
    document.getElementById('potencia').innerText = 'Power: ' + palaData.potencia;
    document.getElementById('defensa').innerText = 'Defense: ' + palaData.defensa;
    document.getElementById('ataque').innerText = 'Attack: ' + palaData.ataque;
    document.getElementById('manejabilidad').innerText = 'Maneuverability: ' + palaData.manejabilidad;
    document.getElementById('remate').innerText = 'Smash: ' + palaData.remate;
    document.getElementById('salidaBola').innerText = 'Ball Exit: ' + palaData.salidaBola;
    document.getElementById('volea').innerText = 'Volley: ' + palaData.volea;
    document.getElementById('puntoDulce').innerText = 'Sweet Spot: ' + palaData.puntoDulce;
    document.getElementById('bajada').innerText = 'Ball Drop: ' + palaData.bajada;
    document.getElementById('fondoPista').innerText = 'Court Depth: ' + palaData.fondoDePista;
    document.getElementById('bandeja').innerText = 'Tray: ' + palaData.bandeja;
    document.getElementById('puntuacionTotal').innerText = 'Total Rating: ' + palaData.puntuacionTotal;

    // STORES AND PRICES
    document.getElementById('tiendasPrecios').innerText = 'Stores and Latest Prices';
    try{
        document.getElementById('codigos').innerHTML = '<span class="text-sm text-gray-800">Promo Code: {{ precio.tienda.codigo_promocional }}</span>';
        document.getElementById('descuentos').innerHTML = '<span class="text-sm text-gray-800">Discount: {{ precio.tienda.descuento }}%</span>';
    }catch(error){

    }

    document.getElementById('historialPrecios').innerText = 'Price History';

    // SIMILAR RACKETS SECTION
    document.getElementById('palasSimilares').innerText = 'Similar Rackets';
    //document.getElementById('similarMarca').innerText = 'Brand: ';

    // REVIEWS SECTION
    document.getElementById('reviewsPala').innerText = 'Reviews for' + palaData.palaNombre + ' Racket';
    document.getElementById('noreviews').innerText = 'No reviews for this racket yet.';

    // COMMENTS SECTION
    document.getElementById('tituloComentarios').innerText = 'Comments';
    document.getElementById('tuComentario').innerText = 'Your Comment';
    document.getElementById('agregarComentario').value = 'Add comment';
    try{
        document.getElementById('nocomentarios').innerText = 'No comments yet.';
    }catch(error){

    }
    

    

    }



});