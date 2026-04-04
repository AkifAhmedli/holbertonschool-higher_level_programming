document.addEventListener('DOMContentLoaded', function () {
  const url = 'https://hellosalut.stefanbohacek.com/?lang=fr';
  const helloElement = document.querySelector('#hello');

  fetch(url)
    .then(response => {
      return response.json();
    })
    .then(data => {
      // API-dən gələn 'hello' dəyərini HTML elementinə yazırıq
      helloElement.textContent = data.hello;
    })
    .catch(error => {
      console.error('Xəta baş verdi:', error);
    });
});
