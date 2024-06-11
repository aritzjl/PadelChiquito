function tableResize() {
  let paddlesContainerWidth = document.getElementById('paddlesContainer');
  let table = document.getElementById('table');
  
  table.style.width = paddlesContainerWidth.offsetWidth + 'px';
}

window.addEventListener('load', tableResize);
window.addEventListener('resize', tableResize);