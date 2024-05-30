const rangeInput = document.getElementById('precio_max');
const tooltip = document.getElementById('tooltip');
const maxOffsetPercentage = 80;

function updateTooltipPosition() {
  const value = rangeInput.value;
  const thumbWidth = parseFloat(getComputedStyle(rangeInput).getPropertyValue('--thumb-width')) || 28;
  const inputWidth = rangeInput.offsetWidth;
  const tooltipWidth = tooltip.offsetWidth;

  const offset = Math.max((value / rangeInput.max) * (inputWidth - thumbWidth), 0);
  const maxTooltipPosition = inputWidth - tooltipWidth;

  const tooltipPosition = Math.min(Math.max(offset - tooltipWidth / 2 + thumbWidth / 2, 0), maxTooltipPosition);

  tooltip.textContent = `Menos de $${value}`;
  tooltip.style.left = `${tooltipPosition}px`;
}

rangeInput.addEventListener('input', updateTooltipPosition);

window.addEventListener('resize', updateTooltipPosition);