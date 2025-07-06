document.addEventListener("DOMContentLoaded", function () {
  const dryOptions = document.getElementById("dry-options");
  const garbageRadios = document.querySelectorAll('input[name="garbage_type"]');
  const bookingForm = document.getElementById("bookingForm");
  const successMsg = document.getElementById("successMessage");

  garbageRadios.forEach(radio => {
    radio.addEventListener("change", function () {
      if (this.value === "dry") {
        dryOptions.style.display = "block";
      } else {
        dryOptions.style.display = "none";
      }
    });
  });

  bookingForm.addEventListener("submit", function (e) {
    e.preventDefault();
    successMsg.style.display = "block";

    // Optional: Send data to backend here using fetch/AJAX
    // or let Django handle it via form submission
  });
});
