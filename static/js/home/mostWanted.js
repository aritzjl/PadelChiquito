function mostWantedHeaderResize() {
  const mostWantedHeader = document.getElementById('mostWantedHeader');
  const mostWanted = document.getElementById('mostWanted');
  
  mostWantedHeader.style.width = mostWanted.offsetWidth + 'px';
};

window.addEventListener('load', mostWantedHeaderResize);
window.addEventListener('resize', mostWantedHeaderResize);