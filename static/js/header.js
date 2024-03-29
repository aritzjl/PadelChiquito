const form = document.getElementById('form');
const mobileContainer = document.getElementById('formContainerMobile');
const pcContainer = document.getElementById('formContainerPC');
const headerHamburgerMenu = document.getElementById('headerHamburgerMenu');
const menu = document.getElementById('menu');
const closeMenu = document.getElementById('closeMenu');

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

function toggleHamburgerMenu() {
  menu.classList.toggle('w-0');
  menu.classList.toggle('w-full');
}

document.addEventListener('DOMContentLoaded', () => {
  handleResize();
  headerHamburgerMenu.addEventListener('click', toggleHamburgerMenu);
  closeMenu.addEventListener('click', toggleHamburgerMenu);
});

window.addEventListener('resize', handleResize);