document.addEventListener('DOMContentLoaded', function () {
  // Lazımi elementləri seçirik
  const addItem = document.getElementById('add_item');
  const removeItem = document.getElementById('remove_item');
  const clearList = document.getElementById('clear_list');
  const myList = document.querySelector('.my_list');

  // 1. Yeni element əlavə etmək (Add item)
  addItem.addEventListener('click', function () {
    const newItem = document.createElement('li');
    newItem.textContent = 'Item';
    myList.appendChild(newItem);
  });

  // 2. Sonuncu elementi silmək (Remove item)
  removeItem.addEventListener('click', function () {
    const lastItem = myList.lastElementChild;
    if (lastItem) {
      myList.removeChild(lastItem);
    }
  });

  // 3. Bütün siyahını təmizləmək (Clear list)
  clearList.addEventListener('click', function () {
    myList.innerHTML = '';
  });
});
