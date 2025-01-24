// menu item open
const menuItems = document.getElementById("menuItems");
const menuOpenButton = document.getElementById("menuOpenButton");

// created a event listener
menuOpenButton.addEventListener("click", () => {
  menuItems.classList.toggle("hidden");
});
