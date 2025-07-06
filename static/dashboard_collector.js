const loginBtn = document.getElementById("loginBtn");
const dropdownMenu = document.getElementById("dropdownMenu");


loginBtn.addEventListener("click", function (event) {
  dropdownMenu.classList.toggle("show");
  event.stopPropagation();
});

document.addEventListener("click", function (event) {
  if (!loginBtn.contains(event.target)) {
    dropdownMenu.classList.remove("show");
  }
});
