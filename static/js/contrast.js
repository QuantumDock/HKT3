function check(){
  var storedValue = sessionStorage.getItem('theme');
  if(storedValue == '1'){
    toggle(false);
  }
}
function toggle(special){
  var body = document.getElementsByTagName("body")[0];
  var grid = document.querySelectorAll(".grid__element");
  var navbar = document.querySelector(".navbar");
  var navbar_button = document.querySelector(".navbar__button");
  try {
    var questions = document.querySelector(".questions");
    questions.classList.toggle("high-contrast--special");
  } catch (TypeError) {
    //pass
  }
  if(special){
    var storedValue = sessionStorage.getItem('theme');
    sessionStorage.setItem('theme', (storedValue == 1 ? 0 : 1));
  }
  // Toggle the "high-contrast" class on the body element
  grid.forEach((gridElement) => {
    gridElement.classList.toggle("high-contrast--special");
  });
  navbar.classList.toggle("high-contrast--special");
  navbar_button.classList.toggle("high-contrast");
  body.classList.toggle("high-contrast");
  }
var toggleButton = document.getElementById("toggle-high-contrast");
toggleButton.addEventListener("click", function () {
  toggle(true);
});
