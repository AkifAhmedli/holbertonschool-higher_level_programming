// Kliklənəcək elementi (id="toggle_header") seçirik
const toggleDiv = document.querySelector('#toggle_header');

// Klik hadisəsini dinləyirik
toggleDiv.addEventListener('click', function() {
  // <header> elementini seçirik
  const headerElement = document.querySelector('header');

  // Əgər 'red' varsa onu silib 'green' əlavə edir, yoxdursa əksini edir
  if (headerElement.classList.contains('red')) {
    headerElement.classList.remove('red');
    headerElement.classList.add('green');
  } else {
    headerElement.classList.remove('green');
    headerElement.classList.add('red');
  }
});
