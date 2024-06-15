// DOM Elements
const filterByMaxPriceForm = document.getElementById('filterByMaxPriceForm');
const filterByOrderForm = document.getElementById('filterByOrdenForm');
const filterByBrandForm = document.getElementById('filterByBrandForm');
const filterByLevelForm = document.getElementById('filterByLevelForm');

let ordenSelect = document.getElementById('ordenSelect');
let levelSelect = document.getElementById('levelSelect');
let filterRangePrice = document.getElementById('filter_price_max');
let maxPrice = document.getElementById('filter_price_max_number');
const caracteristics = document.getElementById('caracteristics');

const checkboxes = filterByBrandForm.querySelectorAll('input[type="checkbox"]');
const dropdowns = caracteristics.querySelectorAll('div > div:nth-child(1)');

const dropdownArrows = {
  arrowDown: document.getElementById('arrow-down'),
  arrowUp: document.getElementById('arrow-up')
}

function sendForm(form) {
  form.submit();
}

function handlePriceRangeChange() {
  maxPrice.textContent = `${filterRangePrice.value} \u20AC`;
  sendForm(filterByMaxPriceForm);
}

function handleOrderChange() {
  sendForm(filterByOrderForm);
}

function handleLevelChange() {
  sendForm(filterByLevelForm);
}

function handleCheckboxChange(event) {
  const { parentElement, checked } = event.target;
  parentElement.classList.toggle('bg-black', checked);
  parentElement.classList.toggle('text-white', checked);
  parentElement.classList.toggle('bg-gray-fog', !checked);
  parentElement.classList.toggle('text-black', !checked);
}

// Event Listeners and main logic
ordenSelect.addEventListener('change', handleOrderChange);
levelSelect.addEventListener('change', handleLevelChange);
filterRangePrice.addEventListener('input', handlePriceRangeChange);

checkboxes.forEach(checkbox => {
  checkbox.addEventListener('change', handleCheckboxChange);
});

dropdowns.forEach(dropdown => {
  dropdown.addEventListener('click', () => {
    filterByLevelForm.classList.toggle('hidden');
    dropdownArrows.arrowDown.classList.toggle('hidden');
    dropdownArrows.arrowUp.classList.toggle('hidden');
  })
});