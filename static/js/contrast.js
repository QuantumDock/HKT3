function check() {
  var storedValue = sessionStorage.getItem("theme");
  if (storedValue == "1") {
    toggle(false);
  }
}
function toggle(special) {
  var body = document.getElementsByTagName("body")[0];
  var grid = document.querySelectorAll(".grid__element");
  var navbar = document.querySelector(".navbar");
  var navbar_button = document.querySelector(".navbar__button");
  var navbar_page = document.querySelector(".navbar__main-page");

  try {
    var scam = document.querySelectorAll(".grid__scam--h1");
    scam.forEach((i) => {
      i.classList.toggle("high-contrast--special");
    });
  } catch (TypeError) {
    //pass
  }
  try {
    var img_contrast = document.querySelector(".title__img");
    img_contrast.src = "/static/img/senior_contrast.png";
  } catch (TypeError) {
    //pass
  }
  try {
    var questions = document.querySelector(".questions");
    questions.classList.toggle("high-contrast--special");
  } catch (TypeError) {
    //pass
  }
  try {
    var times = document.querySelectorAll(".hc-time");
    times.forEach((i) => {
      i.classList.toggle("high-contrast--special");
    });
  } catch (TypeError) {
    //pass
  }
  try {
    var title__heading = document.querySelector(".title__heading");
    title__heading.classList.toggle("high-contrast");
  } catch (TypeError) {
    //pass
  }
  try {
    var grid = document.querySelectorAll(".grid__element");
    grid.forEach((gridElement) => {
      gridElement.classList.toggle("high-contrast--special");
    });
  } catch (TypeError) {
    //pass
  }
  if (special) {
    var storedValue = sessionStorage.getItem("theme");
    sessionStorage.setItem("theme", storedValue == 1 ? 0 : 1);
  }
  navbar.classList.toggle("high-contrast--special");
  navbar_button.classList.toggle("high-contrast");
  navbar_page.classList.toggle("high-contrast");
  body.classList.toggle("high-contrast");
}
var toggleButton = document.getElementById("toggle-high-contrast");
toggleButton.addEventListener("click", function () {
  toggle(true);
});
