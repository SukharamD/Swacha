document.addEventListener("DOMContentLoaded", function () {
  const dryOptions = document.getElementById("dry-options");
  const garbageRadios = document.querySelectorAll('input[name="garbage_type"]');
  const bookingForm = document.getElementById("bookingForm");
  const successMsg = document.getElementById("successMessage");
  const locationInput = document.getElementById("user-location");

  // Show dry options
  garbageRadios.forEach(radio => {
    radio.addEventListener("change", function () {
      dryOptions.style.display = this.value === "dry" ? "block" : "none";
    });
  });

  // Get location on form submit
  bookingForm.addEventListener("submit", function (e) {
    e.preventDefault();

    if (navigator.geolocation) {
      navigator.geolocation.getCurrentPosition(function (position) {
        const lat = position.coords.latitude;
        const lon = position.coords.longitude;
        const coords = `${lat},${lon}`;
        alert("Location captured: " + lat + ", " + lon);

        // Save to hidden input
        locationInput.value = coords;

        // Submit the form after setting location
        bookingForm.submit();
      }, function (error) {
        alert("Location access denied or unavailable.");
        bookingForm.submit(); // Optional: submit anyway without location
      });
    } else {
      alert("Geolocation is not supported by this browser.");
      bookingForm.submit(); // Optional fallback
    }
  });
});
