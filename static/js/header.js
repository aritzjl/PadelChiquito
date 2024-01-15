const form = document.getElementById('form');
const mobileContainer = document.getElementById('formContainerMobile');
const pcContainer = document.getElementById('formContainerPC');

function handleResize() {
  let screenWidth = window.innerWidth || document.documentElement.clientWidth || document.body.clientWidth;

  if (screenWidth >= 768) {
    moveFormToContainer(form, pcContainer);
  } else {
    moveFormToContainer(form, mobileContainer);
  }
}

function moveFormToContainer(formElement, container) {
  formElement.parentNode && formElement.parentNode.removeChild(formElement);

  container.appendChild(formElement);
}

document.addEventListener('DOMContentLoaded', handleResize);
window.addEventListener('resize', handleResize);

handleResize();