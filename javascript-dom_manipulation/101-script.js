document.addEventListener('DOMContentLoaded', function () {
  const btnTranslate = document.getElementById('btn_translate');
  const langCodeElement = document.getElementById('language_code');
  const helloElement = document.getElementById('hello');

  btnTranslate.addEventListener('click', function () {
    const langCode = langCodeElement.value;

    // Əgər dil seçilməyibsə, sorğu göndərmirik
    if (langCode === '') {
      helloElement.textContent = 'Please select a language';
      return;
    }

    const url = `https://hellosalut.stefanbohacek.com/?lang=${langCode}`;

    fetch(url)
      .then(response => {
        if (!response.ok) {
          throw new Error('Şəbəkə xətası baş verdi');
        }
        return response.json();
      })
      .then(data => {
        // Gələn cavabdan 'hello' dəyərini ekrana yazırıq
        helloElement.textContent = data.hello;
      })
      .catch(error => {
        console.error('Xəta:', error);
        helloElement.textContent = 'Error fetching translation';
      });
  });
});
