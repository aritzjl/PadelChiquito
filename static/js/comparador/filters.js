// DOM Elements
const filterByMaxPriceForm = document.getElementById('filterByMaxPriceForm');
const filterByOrderForm = document.getElementById('filterByOrdenForm');
const filterByBrandForm = document.getElementById('filterByBrandForm');
const filterByLevelForm = document.getElementById('filterByLevelForm');

let ordenSelect = document.getElementById('ordenSelect');
let levelSelect = document.getElementById('levelSelect');
let balanceSelect = document.getElementById('balanceSelect');
let rangePrice = document.getElementById('filter_price_max');
let maxPrice = document.getElementById('filter_price_max_number');
const caracteristics = document.getElementById('caracteristics');

const checkboxes = filterByBrandForm.querySelectorAll('input[type="checkbox"]');
const dropdowns = caracteristics.querySelectorAll('div > div > div:nth-child(1)');

function sendForm(form) {
  form.submit();
}

function handlePriceRangeChange() {
  maxPrice.textContent = `${rangePrice.value} \u20AC`;
  sendForm(filterByMaxPriceForm);
}

function handleOrderChange() {
  sendForm(filterByOrderForm);
}

function handleLevelChange() {
  sendForm(filterByLevelForm);
}

function handleBalanceChange() {
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
balanceSelect.addEventListener('change', handleLevelChange);
rangePrice.addEventListener('input', handlePriceRangeChange);

checkboxes.forEach(checkbox => {
  checkbox.addEventListener('change', handleCheckboxChange);
});

dropdowns.forEach(dropdown => {
  const form = dropdown.nextElementSibling;
  const arrows = dropdown.querySelectorAll('picture');

  const dropdownArrows = {
    arrowDown: arrows[0],
    arrowUp: arrows[1]
  };

  dropdown.addEventListener('click', () => {
    form.classList.toggle('hidden');
    dropdownArrows.arrowDown.classList.toggle('hidden');
    dropdownArrows.arrowUp.classList.toggle('hidden');
  });
});