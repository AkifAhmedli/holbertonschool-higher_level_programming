// Select the trigger element by its ID
const updateButton = document.querySelector('#update_header');

// Select the header element directly
const headerElement = document.querySelector('header');

// Add a click event listener to the trigger element
updateButton.addEventListener('click', () => {
  // Update the text content of the header
  headerElement.textContent = 'New Header!!!';
});
