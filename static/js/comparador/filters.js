// DOM Elements
const filterByMaxPriceForm = document.getElementById('filterByMaxPriceForm');

// Nota padelchiquito
const filterByBaseline = document.getElementById('filterByBaseline');

let rangeBaseline = document.getElementById('rangeBaseline');

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
let rangePrice = document.getElementById('filter_price_max');
let maxPrice = document.getElementById('filter_price_max_number');
let minBaseline = document.getElementById('fondo_pista_min_number');

const caracteristics = document.getElementById('caracteristics');
const checkboxes = filterByBrandForm.querySelectorAll('input[type="checkbox"]');
const dropdownsCaracteristics = caracteristics.querySelectorAll('div > div > div:nth-child(1)');

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

// Event Listeners and main logic
handleInputChange(ordenSelect, filterByOrderForm);
handleInputChange(levelSelect, filterByLevelForm);
handleInputChange(balanceSelect, filterByBalanceForm);
handleInputChange(toughnessSelect, filterByToughnessForm);
handleInputChange(shapeSelect, filterByShapeForm);

//ranges
rangePrice.addEventListener('change', () => {
  maxPrice.textContent = `${rangePrice.value} \u20AC`;
  sendForm(filterByMaxPriceForm);
});

rangeBaseline.addEventListener('change', () => {
  minBaseline.textContent = rangeBaseline.value;
  sendForm(filterByBaseline);
});

checkboxes.forEach(checkbox => {
  checkbox.addEventListener('change', handleCheckboxChange);
});

toggleDropdown(dropdownsCaracteristics, false);
toggleDropdown(dropdownsNotaPadelChiquito, true);