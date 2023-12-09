const [firstStep, secondStep, username, email, nextButton, nextButtonText, nextButtonSvg, comeBack, errorElement] = [
  '#firstStep',
  '#secondStep',
  '#username',
  '#email',
  '#nextButton',
  '#nextButtonText',
  '#nextButtonSvg',
  '#comeBack',
  '#error',
].map((id) => document.querySelector(id));

function toggleButtonState() {
  const emailRegex = /^\w+@\w+\.\w+$/;
  const isEmailValid = emailRegex.test(email.value);
  if (username.value && email.value && isEmailValid) {
    nextButtonSvg.classList.add('hidden');
    nextButtonText.classList.remove('hidden');
    nextButton.disabled = false;
  } else {
    nextButtonSvg.classList.remove('hidden');
    nextButtonText.classList.add('hidden');
    nextButton.disabled = true;
  }
}

username.addEventListener('input', toggleButtonState);
email.addEventListener('input', toggleButtonState);
toggleButtonState();

// Handle click event on next button
nextButton.addEventListener('click', e => {
  e.preventDefault();
  firstStep.classList.add('hidden');
  secondStep.classList.remove('hidden');
  comeBack.classList.remove('hidden');
  animate(secondStep, 'right');
});

// Handle click event on come back link
comeBack.addEventListener('click', e => {
  e.preventDefault();
  animate(secondStep, 'left');
  requestAnimationFrame(() => {
    firstStep.classList.remove('hidden');
    secondStep.classList.add('hidden');
    comeBack.classList.add('hidden');
    animate(firstStep, 'left');
  });
});

// Animate element
function animate(element, direction) {
  // Set initial style
  element.style.opacity = 0;
  element.style.transform = `translateX(${direction === 'left' ? '-35px' : '35px'})`;
  element.style.transition = 'opacity 0.5s, transform 0.5s';

  // Trigger reflow to ensure initial style is applied
  void element.offsetWidth;

  // Set final style
  element.style.opacity = 1;
  element.style.transform = 'translateX(0)';
}

// Show error message if present
if (typeof Swal === 'undefined') {
  console.error('SweetAlert2 library is not loaded');
} else {
  const errorMessage = errorElement.value;
  Swal.fire({
    icon: 'error',
    title: errorMessage,
    showConfirmButton: false,
    timer: 1000,
    confirmButtonColor: '#d03d23'
  });
}