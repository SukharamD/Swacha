function showSection(sectionId) {
  const sections = document.querySelectorAll('.section');
  sections.forEach(section => section.style.display = 'none');
  document.getElementById(sectionId).style.display = 'block';

   if (sectionId === 'environment') {
      animateCount('recycled-count', 100);
      animateCount('composted-count', 50);
    }
    
    if (sectionId === 'contributions') {
      animateCount('trees-count', 10);
      animateCount('drives-count', 5);
    }

}
window.onload = () => {
  showSection('user-info');
};

function animateCount(id, target) {
  let count = 0;
  const element = document.getElementById(id);
  const interval = setInterval(() => {
    if (count < target) {
        count++;
        element.textContent = count;
      } else {
        clearInterval(interval);
      }
    }, 30);
  }

  