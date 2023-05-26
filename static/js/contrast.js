var toggleButton = document.getElementById("toggle-high-contrast");

toggleButton.addEventListener("click", function () {
  // Get the body element
  var body = document.getElementsByTagName("body")[0];
  var grid = document.querySelectorAll(".grid__element");
  var navbar = document.querySelector(".navbar");
  var navbar_button = document.querySelector(".navbar__button");
  // Toggle the "high-contrast" class on the body element
  grid.forEach((gridElement) => {
    gridElement.classList.toggle("high-contrast--special");
  });
  navbar.classList.toggle("high-contrast--special");
  navbar_button.classList.toggle("high-contrast");
  body.classList.toggle("high-contrast");
});
