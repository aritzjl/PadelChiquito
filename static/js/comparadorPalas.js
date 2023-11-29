// * Filters Scripts
// Input Synchronization

const configurations = [
  ['precio_range_min', 'precio_range_max', 'precio_min', 'precio_max'],
  ['potencia_range_min', 'potencia_range_max', 'potencia_min', 'potencia_max'],
  ['bandeja_range_min', 'bandeja_range_max', 'bandeja_min', 'bandeja_max'],
  ['bajada_pared_range_min', 'bajada_pared_range_max', 'bajada_pared_min', 'bajada_pared_max'],
  ['fondo_pista_range_min', 'fondo_pista_range_max', 'fondo_pista_min', 'fondo_pista_max'],
  ['remate_range_min', 'remate_range_max', 'remate_min', 'remate_max'],
  ['volea_range_min', 'volea_range_max', 'volea_min', 'volea_max']
];

const windowWidth = window.innerWidth || document.documentElement.clientWidth || document.body.clientWidth;

function setupInputSynchronization(rangeIdMin, rangeIdMax, inputIdMin, inputIdMax) {
  const rangeMin = document.getElementById(rangeIdMin);
  const rangeMax = document.getElementById(rangeIdMax);
  const inputMin = document.getElementById(inputIdMin);
  const inputMax = document.getElementById(inputIdMax);

  // Update input values when the corresponding range changes
  rangeMin.addEventListener('input', () => {
    inputMin.value = rangeMin.value;
  });

  rangeMax.addEventListener('input', () => {
    inputMax.value = rangeMax.value;
  });

  // Update range values when the corresponding input changes
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

// * Hamburger Menu
const hamburgerMenu = document.getElementById('hamburgerMenu');
const filters = document.getElementById('filters');

hamburgerMenu.addEventListener('click', () => {
  filters.classList.toggle('hidden');
});

// * Debounce function to limit the rate at which a function can fire
function debounce(func, delay) {
  let timeoutId;
  return function () {
    const context = this;
    const args = arguments;

    // Clear the previous timeout and set a new one
    clearTimeout(timeoutId);
    timeoutId = setTimeout(() => {
      func.apply(context, args);
    }, delay);
  };
}

// * Headerlist scripts
function moveHeaderList() {
  const headerList = document.getElementById('headerList');
  const windowWidth = window.innerWidth || document.documentElement.clientWidth || document.body.clientWidth;

  if (windowWidth < 768) {
    const header = document.querySelector('header');
    header.insertAdjacentElement('afterend', headerList);
  } else {
    if (document.body.contains(headerList)) {
      document.querySelector('nav').appendChild(headerList);
    }
  }
}

// * Filters Scripts
function moveFilters() {
  const filtersPC = document.getElementById('filtersPC');
  const filtersMobile = document.getElementById('filtersMobile');
  const filtersElementsPC = filtersPC.querySelectorAll(':scope > div');
  const filtersElementsMobile = filtersMobile.querySelectorAll(':scope > div');

  if (windowWidth < 768) {
    filtersElementsPC.forEach(filter => {
      filter.classList.remove('hidden');
      filter.classList.add('relative');
      filtersMobile.insertAdjacentElement('afterbegin', filter);
    });
  } else {
    filtersElementsMobile.forEach(filter => {
      filter.classList.add('hidden');
      filter.classList.add('relative');
      filtersPC.insertAdjacentElement('afterbegin', filter);
    })
  }
}

function flowbite() {
    if (windowWidth >= 768) {
    const script = document.createElement('script');
    script.src = 'https://cdnjs.cloudflare.com/ajax/libs/flowbite/2.1.1/flowbite.min.js';
    document.body.appendChild(script);
  }
}

document.addEventListener('DOMContentLoaded', flowbite);
document.addEventListener('DOMContentLoaded', moveHeaderList);
window.addEventListener('load', moveFilters);
window.addEventListener('resize', debounce(moveHeaderList, 100));
window.addEventListener('resize', debounce(moveFilters, 100));