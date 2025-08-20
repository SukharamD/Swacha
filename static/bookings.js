document.addEventListener("DOMContentLoaded", function () {
  // ---- Element refs ----
  const bookingForm   = document.getElementById("bookingForm");
  if (!bookingForm) {
    console.warn("#bookingForm not found on this page. Skipping bookings.js.");
    return;
  }

  const dryOptions    = document.getElementById("dry-options");
  const locationInput = document.getElementById("user-location");
  const garbageRadios = document.querySelectorAll('input[name="garbage_type"]');
  const successMsg    = document.getElementById("successMessage"); // optional
  const submitBtn     = bookingForm.querySelector('button[type="submit"]');

  // ---- Toggle dry options on radio change ----
  function setDryOptionsVisibility() {
    if (!dryOptions) return;
    const selected = document.querySelector('input[name="garbage_type"]:checked');
    dryOptions.style.display = selected && selected.value === "dry" ? "block" : "none";
  }

  // Initial state
  setDryOptionsVisibility();

  // React to changes
  garbageRadios.forEach((radio) => {
    radio.addEventListener("change", setDryOptionsVisibility);
  });

  // ---- Submit with geolocation (captures coords, then submits) ----
  bookingForm.addEventListener("submit", function (e) {
    e.preventDefault();

    // ✅ Guarded success message
    if (successMsg) {
      successMsg.style.display = "block";
    }

    // Prevent double submits
    if (submitBtn) submitBtn.disabled = true;

    const doSubmit = () => bookingForm.submit();

    if ("geolocation" in navigator) {
      navigator.geolocation.getCurrentPosition(
        (pos) => {
          const lat = pos.coords.latitude;
          const lon = pos.coords.longitude;
          if (locationInput) locationInput.value = `${lat},${lon}`;
          doSubmit();
        },
        () => {
          // denied/unavailable -> submit without location
          doSubmit();
        },
        { enableHighAccuracy: false, timeout: 8000, maximumAge: 60000 }
      );
    } else {
      doSubmit();
    }
  });
});
