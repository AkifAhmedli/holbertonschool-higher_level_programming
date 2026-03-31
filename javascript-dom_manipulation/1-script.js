// ID-si 'red_header' olan elementi seçirik
const redHeaderDiv = document.querySelector('#red_header');

// Həmin elementə kliklədikdə icra olunacaq funksiyanı təyin edirik
redHeaderDiv.addEventListener('click', function() {
    // <header> elementini seçib rəngini qırmızı edirik
    const headerElement = document.querySelector('header');
    headerElement.style.color = '#FF0000';
});
