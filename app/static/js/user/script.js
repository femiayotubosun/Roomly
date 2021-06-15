var loader = document.querySelector(".loader");
if (loader) {
  window.addEventListener("load", vanish);
}

function vanish() {
  loader.classList.add("disappear");
}

let btn = document.querySelector("#toggle-sidebar-btn");
let sidebar = document.querySelector(".sidebar");
let searchBtn = document.querySelector(".bx-search");

btn.onclick = function () {
  sidebar.classList.toggle("active");
  if (sessionStorage.getItem("hideSidebar") === "true") {
    sessionStorage.setItem("hideSidebar", false);
  } else if (
    sessionStorage.getItem("hideSidebar") === null ||
    sessionStorage.getItem("hideSidebar") === "false"
  ) {
    sessionStorage.setItem("hideSidebar", true);
  }
};

console.log(sessionStorage.getItem("hideSidebar"));

if (sessionStorage.getItem("hideSidebar") == "null") {
  sidebar.classList.remove("active");
} else if (sessionStorage.getItem("hideSidebar") == "true") {
  sidebar.classList.add("active");
}

// Alert box handler
var modal = document.getElementById("popupModal");
var closeModal = document.getElementsByClassName("close")[0];

if (closeModal) {
  closeModal.onclick = function () {
    modal.style.display = "none";
  };

  window.onclick = function (event) {
    if (event.target == modal) {
      modal.style.display = "none";
    }
  };
}

// localStorage.setItem("toggleState", true)
// Sidebar is hidden

// localStorage.getItem("toggelLState")
