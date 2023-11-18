const configurations = [
  ['precio_range_min', 'precio_range_max', 'precio_min', 'precio_max'],
  ['potencia_range_min', 'potencia_range_max', 'potencia_min', 'potencia_max'],
  ['bandeja_range_min', 'bandeja_range_max', 'bandeja_min', 'bandeja_max'],
  ['bajada_pared_range_min', 'bajada_pared_range_max', 'bajada_pared_min', 'bajada_pared_max'],
  ['fondo_pista_range_min', 'fondo_pista_range_max', 'fondo_pista_min', 'fondo_pista_max'],
  ['remate_range_min', 'remate_range_max', 'remate_min', 'remate_max'],
  ['volea_range_min', 'volea_range_max', 'volea_min', 'volea_max']
];

function setupInputSynchronization(rangeIdMin, rangeIdMax, inputIdMin, inputIdMax) {
  let rangeMin = document.getElementById(rangeIdMin);
  let rangeMax = document.getElementById(rangeIdMax);
  let inputMin = document.getElementById(inputIdMin);
  let inputMax = document.getElementById(inputIdMax);

  rangeMin.addEventListener('input', () => {
    inputMin.value = rangeMin.value;
  });

  rangeMax.addEventListener('input', () => {
    inputMax.value = rangeMax.value;
  });

  inputMin.addEventListener('input', () => {
    rangeMin.value = inputMin.value;
  });

  inputMax.addEventListener('input', () => {
    rangeMax.value = inputMax.value;
  });
}

// Call the function for each configuration
configurations.forEach(config => {
  setupInputSynchronization(...config);
});