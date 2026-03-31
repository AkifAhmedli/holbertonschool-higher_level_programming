// ID-si 'red_header' olan elementi (kliklənməli olan div) seçirik
const redHeaderDiv = document.querySelector('#red_header');

// Klikləmə hadisəsini (event) dinləyirik
redHeaderDiv.addEventListener('click', function() {
  // <header> elementini seçirik
  const headerElement = document.querySelector('header');

  // Header-ə 'red' klasını əlavə edirik
  headerElement.classList.add('red');
});
