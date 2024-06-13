// DOM Elements
const filterByMaxPriceForm = document.getElementById('filterByMaxPriceForm');
const filterByOrderForm = document.getElementById('filterByOrdenForm');
const filterByBrandForm = document.getElementById('filterByBrandForm');
const orden = document.getElementById('orden');
let filterRangePrice = document.getElementById('filter_price_max');
let maxPrice = document.getElementById('filter_price_max_number');

const checkboxes = filterByBrandForm.querySelectorAll('input[type="checkbox"]');

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

function handleCheckboxChange(event) {
  const { parentElement, checked } = event.target;
  parentElement.classList.toggle('bg-black', checked);
  parentElement.classList.toggle('text-white', checked);
  parentElement.classList.toggle('bg-gray-fog', !checked);
  parentElement.classList.toggle('text-black', !checked);
}

// Event Listeners and main logic
orden.addEventListener('change', handleOrderChange);
filterRangePrice.addEventListener('input', handlePriceRangeChange);

checkboxes.forEach(checkbox => {
  checkbox.addEventListener('change', handleCheckboxChange);
});