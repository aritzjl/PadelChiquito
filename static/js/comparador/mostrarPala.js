function handleProgressBar(elementId, value) {
  let progressBar = document.getElementById(elementId);
  progressBar.style.width = `${value * 10}%`;
}

document.addEventListener("DOMContentLoaded", () => {
  handleProgressBar('palaPotenciaBarra', document.getElementById('palaPotencia').value);
  handleProgressBar('palaControlBarra', document.getElementById('palaControl').value);
  handleProgressBar('palaSalidaBolaBarra', document.getElementById('palaSalidaBola').value);
  handleProgressBar('palaManejabilidadBarra', document.getElementById('palaManejabilidad').value);
  handleProgressBar('palaPuntoDulceBarra', document.getElementById('palaPuntoDulce').value);
  handleProgressBar('palaFondoPistaBarra', document.getElementById('palaFondoPista').value);
  handleProgressBar('palaVoleaBarra', document.getElementById('palaVolea').value);
  handleProgressBar('palaBajadaParedBarra', document.getElementById('palaBajadaPared').value);
  handleProgressBar('palaBandejaBarra', document.getElementById('palaBandeja').value);
  handleProgressBar('palaDefensaBarra', document.getElementById('palaDefensa').value);
  handleProgressBar('palaRemateBarra', document.getElementById('palaRemate').value);
  handleProgressBar('palaAtaqueBarra', document.getElementById('palaAtaque').value);
  handleProgressBar('palaPuntuacionTotalBarra', document.getElementById('palaPuntuacionTotal').value);
});