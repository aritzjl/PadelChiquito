// * DOM Elements
const filterByMaxPriceForm = document.getElementById('filterByMaxPriceForm');

// Nota padelchiquito
const filterByBaseline = document.getElementById('filterByBaseline');
const filterByWallSmash = document.getElementById('filterByWallSmash');
const filterByVolley = document.getElementById('filterByVolley');

let rangePrice = document.getElementById('filter_price_max');
let rangeBaseline = document.getElementById('rangeBaseline');
let rangeWallSmash = document.getElementById('rangeWallSmash');
let rangeVolley = document.getElementById('rangeVolley');

let maxPrice = document.getElementById('filter_price_max_number');
let minBaseline = document.getElementById('fondo_pista_min_number');
let minWallSmash = document.getElementById('bajada_pared_min_number');
let minVolley = document.getElementById('volea_min_number');

const notaPadelChiquito = document.getElementById('notaPadelChiquito');
const dropdownsNotaPadelChiquito = notaPadelChiquito.querySelectorAll('div > div > div:nth-child(1)');

//caracteristics
const filterByOrderForm = document.getElementById('filterByOrdenForm');
const filterByBrandForm = document.getElementById('filterByBrandForm');
const filterByLevelForm = document.getElementById('filterByLevelForm');
const filterByBalanceForm = document.getElementById('filterByBalanceForm');
const filterByToughnessForm = document.getElementById('filterByToughnessForm');
const filterByShapeForm = document.getElementById('filterByShapeForm');

let ordenSelect = document.getElementById('ordenSelect');
let levelSelect = document.getElementById('levelSelect');
let balanceSelect = document.getElementById('balanceSelect');
let toughnessSelect = document.getElementById('toughnessSelect');
let shapeSelect = document.getElementById('shapeSelect');

const caracteristics = document.getElementById('caracteristics');
const checkboxes = filterByBrandForm.querySelectorAll('input[type="checkbox"]');
const dropdownsCaracteristics = caracteristics.querySelectorAll('div > div > div:nth-child(1)');

//Functions
function sendForm(form) {
  form.submit();
}

function handleInputChange(inputElement, formElement) {
  inputElement.addEventListener('change', () => sendForm(formElement));
}

function handleCheckboxChange(event) {
  const { parentElement, checked } = event.target;
  parentElement.classList.toggle('bg-black', checked);
  parentElement.classList.toggle('text-white', checked);
  parentElement.classList.toggle('bg-gray-fog', !checked);
  parentElement.classList.toggle('text-black', !checked);
}

function toggleDropdown(dropdowns, shouldToggleFlex) {
  dropdowns.forEach(dropdown => {
    const form = dropdown.nextElementSibling;
    const [arrowDown, arrowUp] = dropdown.querySelectorAll('picture');

    dropdown.addEventListener('click', () => {
      form.classList.toggle('hidden');
      if (shouldToggleFlex) {
        form.classList.toggle('flex');
      }
      arrowDown.classList.toggle('hidden');
      arrowUp.classList.toggle('hidden');
    });
  });
};

function updateAndSubmitForm (rangeElement, displayElement, form) {
  rangeElement.addEventListener('change', () => {
    displayElement.textContent = rangeElement.value + (rangeElement === rangePrice ? ' \u20AC' : '');
    sendForm(form);
  });
};

// Event Listeners and main logic
handleInputChange(ordenSelect, filterByOrderForm);
handleInputChange(levelSelect, filterByLevelForm);
handleInputChange(balanceSelect, filterByBalanceForm);
handleInputChange(toughnessSelect, filterByToughnessForm);
handleInputChange(shapeSelect, filterByShapeForm);

toggleDropdown(dropdownsCaracteristics, false);
toggleDropdown(dropdownsNotaPadelChiquito, true);

updateAndSubmitForm(rangePrice, maxPrice, filterByMaxPriceForm);
updateAndSubmitForm(rangeBaseline, minBaseline, filterByBaseline);
updateAndSubmitForm(rangeWallSmash, minWallSmash, filterByWallSmash);
updateAndSubmitForm(rangeVolley, minVolley, filterByVolley);

checkboxes.forEach(checkbox => {
  checkbox.addEventListener('change', handleCheckboxChange);
});