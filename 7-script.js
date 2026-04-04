// Məlumatın götürüləcəyi URL
const url = 'https://swapi-api.hbtn.io/api/films/?format=json';

// Filmlərin siyahıya alınacağı HTML elementi (ul)
const listMovies = document.querySelector('#list_movies');

// Fetch API vasitəsilə sorğu göndəririk
fetch(url)
  .then(response => {
    // Cavabın uğurlu olub-olmadığını yoxlayırıq
    return response.json();
  })
  .then(data => {
    // 'data.results' filmlərin siyahısını ehtiva edən massivdir (array)
    data.results.forEach(film => {
      // Hər film üçün yeni bir 'li' elementi yaradırıq
      const listItem = document.createElement('li');
      // Filmin adını 'li' elementinin içinə yazırıq
      listItem.textContent = film.title;
      // Hazırkı 'li' elementini HTML-dəki 'ul' elementinə əlavə edirik
      listMovies.appendChild(listItem);
    });
  })
  .catch(error => {
    // Hər hansı bir xəta baş verərsə konsola çıxarırıq
    console.error('Xəta baş verdi:', error);
  });
