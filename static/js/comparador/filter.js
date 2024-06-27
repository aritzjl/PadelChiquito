// * DOM Elements
const bannerElement = document.getElementById('banner');
const filtersContainer = document.getElementById('filtersContainer');
const openFilterBtn = document.getElementById('openFilterBtn');
const closeFilterBtn = document.getElementById('closeFilterBtn');
const openFiltersContainer = document.getElementById('openFiltersContainer');

let scrollPosition = 0;

function disableScroll() {
  scrollPosition = window.scrollY || document.documentElement.scrollTop;
  window.addEventListener('scroll', noScroll);
}

function enableScroll() {
  window.removeEventListener('scroll', noScroll);
  window.scrollTo(0, scrollPosition);
}

function noScroll() {
  window.scrollTo(0, scrollPosition);
}

function toggleFilter() {
  filtersContainer.classList.toggle('px-12');
  filtersContainer.classList.toggle('w-0');
  filtersContainer.classList.toggle('h-0');
  filtersContainer.classList.toggle('w-full');
  filtersContainer.classList.toggle('h-screen');
  openFiltersContainer.classList.toggle('hidden');
}

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

// * Event Listeners
openFilterBtn.addEventListener('click', () => {
  toggleFilter();
  disableScroll();
});

closeFilterBtn.addEventListener('click', () => {
  toggleFilter();
  enableScroll();
});

document.addEventListener('DOMContentLoaded', event => {
  if (window.innerWidth >= 1080) {
    observeElementById(
      bannerElement,
      element => {
        filtersContainer.classList.add('md:relative', 'lg:h-auto');
        filtersContainer.classList.remove('md:sticky', 'lg:h-screen');
      },
      element => {
        filtersContainer.classList.remove('md:relative', 'lg:h-auto');
        filtersContainer.classList.add('md:sticky', 'lg:h-screen');
      }
    );
  }
});