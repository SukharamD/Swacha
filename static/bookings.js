document.addEventListener("DOMContentLoaded", function () {
  const dryOptions   = document.getElementById("dry-options");
  const garbageRadios = document.querySelectorAll('input[name="garbage_type"]');
  const bookingForm   = document.getElementById("bookingForm");
  const locationInput = document.getElementById("user-location");

  // Guard: if the form isn’t on this page, bail early (avoids errors on pages that also load this JS)
  if (!bookingForm) {
    console.warn("#bookingForm not found on this page. Skipping bookings.js.");
    return;
  }

  // Show/hide dry options safely
  garbageRadios.forEach((radio) => {
    radio.addEventListener("change", function () {
      if (!dryOptions) {
        console.warn("#dry-options not found");
        return;
      }
      dryOptions.style.display = this.value === "dry" ? "block" : "none";
    });
  });

  // Optional: set initial state on page load (in case "dry" is preselected)
  const selected = document.querySelector('input[name="garbage_type"]:checked');
  if (dryOptions) {
    dryOptions.style.display = selected && selected.value === "dry" ? "block" : "none";
  }

  // Submit with geolocation
  bookingForm.addEventListener("submit", function (e) {
    e.preventDefault();

    if (navigator.geolocation) {
      navigator.geolocation.getCurrentPosition(
        function (position) {
          const lat = position.coords.latitude;
          const lon = position.coords.longitude;
          if (locationInput) locationInput.value = `${lat},${lon}`;
          // alert(`Location captured: ${lat}, ${lon}`); // optional
          bookingForm.submit();
        },
        function () {
          // alert("Location access denied or unavailable."); // optional
          bookingForm.submit();
        }
      );
    } else {
      // alert("Geolocation not supported."); // optional
      bookingForm.submit();
    }
  });
});
