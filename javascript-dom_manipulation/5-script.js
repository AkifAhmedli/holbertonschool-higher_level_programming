// Kliklənəcək elementi (id="update_header") seçirik
const updateHeaderDiv = document.querySelector('#update_header');

// Klik hadisəsini dinləyirik
updateHeaderDiv.addEventListener('click', function() {
  // <header> elementini seçirik
  const headerElement = document.querySelector('header');

  // Header-in mətnini yeni mətnlə əvəz edirik
  headerElement.textContent = 'New Header!!!';
});
