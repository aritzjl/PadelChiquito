const bannerElement = document.getElementById('banner');
const filtersContainer = document.getElementById('filtersContainer');

function observeElementById(element, onIntersect, onLeave) {
  if (!element) {
    console.warn(`Elemento con id ${element.id} no encontrado.`);
    return;
  }

  const observer = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        onIntersect(entry.target);
      } else {
        onLeave(entry.target);
      }
    });
  });

  observer.observe(element);
}

document.addEventListener('DOMContentLoaded', (event) => {
  observeElementById(
    bannerElement,
    function (element) {
      console.log(`El elemento con id ${element.id} es visible en el viewport.`);
      filtersContainer.classList.add('md:relative');
      filtersContainer.classList.add('lg:h-auto');
      filtersContainer.classList.remove('md:fixed');
      filtersContainer.classList.remove('lg:h-screen');
    },
    function (element) {
      console.log(`El elemento con id ${element.id} no es visible en el viewport.`)
      filtersContainer.classList.remove('md:relative');
      filtersContainer.classList.remove('lg:h-auto');
      filtersContainer.classList.add('md:fixed');
      filtersContainer.classList.add('lg:h-screen');
    }
  );
});