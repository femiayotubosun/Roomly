let btn = document.querySelector("#toggle-sidebar-btn");
let sidebar = document.querySelector(".sidebar");
let searchBtn = document.querySelector(".bx-search");

btn.onclick = function () {
  sidebar.classList.toggle("active");
};

searchBtn.onclick = function () {
  sidebar.classList.toggle("active");
};

// Alert box handler
var modal = document.getElementById("popupModal");
var closeModal = document.getElementsByClassName("close")[0];
console.log(closeModal);

closeModal.onclick = function () {
  modal.style.display = "none";
};

window.onclick = function (event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
};
