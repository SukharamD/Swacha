const loginBtn = document.getElementById("loginBtn");
const dropdownMenu = document.getElementById("dropdownMenu");

loginBtn.addEventListener("click", function (event) {
  dropdownMenu.style.display =
    dropdownMenu.style.display === "block" ? "none" : "block";
  event.stopPropagation();
});

document.addEventListener("click", function (event) {
  if (!loginBtn.contains(event.target)) {
    dropdownMenu.style.display = "none";
  }
});


const counters = document.querySelectorAll('.counter');

const animateCounter = (counter) => {
  const updateCount = () => {
    const target = +counter.getAttribute('data-target');
    const current = +counter.innerText;
    const increment = Math.ceil(target / 100); // Speed factor

    if (current < target) {
      counter.innerText = Math.min(current + increment, target);
      setTimeout(updateCount, 10); // Speed
    } else {
      counter.innerText = target.toLocaleString();
    }
  };
  updateCount();
};

  // Optional: Animate when section is in view
  const observer = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const counter = entry.target;
        animateCounter(counter);
        observer.unobserve(counter); // Run once
      }
    });
  }, { threshold: 1.0 });

counters.forEach(counter => observer.observe(counter));