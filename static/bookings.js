document.addEventListener("DOMContentLoaded", function () {

  const bookingForm   = document.getElementById("bookingForm");
  const dryOptions    = document.getElementById("dry-options");
  const locationInput = document.getElementById("user-location");
  const garbageRadios = document.querySelectorAll('input[name="garbage_type"]');
  const successMsg    = document.getElementById("successMessage"); // optional (may not exist)
  const submitBtn     = bookingForm?.querySelector('button[type="submit"]');

  // If this JS is loaded on a page without the form, bail out safely.
  if (!bookingForm) {
    console.warn("#bookingForm not found on this page. Skipping bookings.js.");
    return;
  }

  // ---- Toggle dry options on radio change ----
  function setDryOptionsVisibility() {
    if (!dryOptions) return;
    const selected = document.querySelector('input[name="garbage_type"]:checked');
    dryOptions.style.display = selected && selected.value === "dry" ? "block" : "none";
  }

  // Initial state (in case of preselected radio on back/refresh)
  setDryOptionsVisibility();

  // React to changes
  garbageRadios.forEach((radio) => {
    radio.addEventListener("change", setDryOptionsVisibility);
  });

  // ---- Submit with geolocation (captures coords, then submits) ----
  bookingForm.addEventListener("submit", function (e) {
    e.preventDefault();

    // Optional success banner toggle (won't error if missing)
    if (successMsg) successMsg.style.display = "block";

    // Prevent double submits
    if (submitBtn) submitBtn.disabled = true;

    // Helper to submit safely and re-enable the button afterward if needed
    const doSubmit = () => {
      bookingForm.submit();
    };

    // Geolocation capture
    if ("geolocation" in navigator) {
      navigator.geolocation.getCurrentPosition(
        (pos) => {
          const lat = pos.coords.latitude;
          const lon = pos.coords.longitude;
          if (locationInput) locationInput.value = `${lat},${lon}`;
          doSubmit();
        },
        (_err) => {
          // User denied or unavailable -> submit without location
          doSubmit();
        },
        { enableHighAccuracy: false, timeout: 8000, maximumAge: 60000 }
      );
    } else {
      // No geolocation support -> submit without location
      doSubmit();
    }
  });
});
