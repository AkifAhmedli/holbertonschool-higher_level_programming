// Kliklənəcək elementi (id="add_item") seçirik
const addItemDiv = document.querySelector('#add_item');

// Klik hadisəsini dinləyirik
addItemDiv.addEventListener('click', function() {
  // 1. Yeni bir 'li' elementi yaradırıq
  const newListItem = document.createElement('li');

  // 2. İçərisinə "Item" mətnini əlavə edirik
  newListItem.textContent = 'Item';

  // 3. Siyahını (class="my_list") seçirik
  const myList = document.querySelector('.my_list');

  // 4. Yeni yaratdığımız 'li'-ni siyahının sonuna əlavə edirik
  myList.appendChild(newListItem);
});
