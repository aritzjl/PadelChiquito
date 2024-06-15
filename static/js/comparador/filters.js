// DOM Elements
const filterByMaxPriceForm = document.getElementById('filterByMaxPriceForm');
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
const caracteristics = document.getElementById('caracteristics');

const checkboxes = filterByBrandForm.querySelectorAll('input[type="checkbox"]');
const dropdowns = caracteristics.querySelectorAll('div > div > div:nth-child(1)');

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

// Event Listeners and main logic
handleInputChange(ordenSelect, filterByOrderForm);
handleInputChange(levelSelect, filterByLevelForm);
handleInputChange(balanceSelect, filterByBalanceForm);
handleInputChange(toughnessSelect, filterByToughnessForm);
handleInputChange(shapeSelect, filterByShapeForm);
rangePrice.addEventListener('input', () => {
  maxPrice.textContent = `${rangePrice.value} \u20AC`;
  sendForm(filterByMaxPriceForm);
});

checkboxes.forEach(checkbox => {
  checkbox.addEventListener('change', handleCheckboxChange);
});

dropdowns.forEach(dropdown => {
  const form = dropdown.nextElementSibling;
  const [arrowDown, arrowUp] = dropdown.querySelectorAll('picture');

  dropdown.addEventListener('click', () => {
    form.classList.toggle('hidden');
    arrowDown.classList.toggle('hidden');
    arrowUp.classList.toggle('hidden');
  });
});