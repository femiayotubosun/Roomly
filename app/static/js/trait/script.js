// A handler function
// get array from back end

var questionBank = data.questionBank;
var traits = data.traits;
let answerBank = data.answerBank;
var progress = document.querySelector("#progress-bar");
if (answerBank.length == 0) {
  answerBank = new Array(questionBank.length).fill("");
}
// roomieTraits = data.roomieTraits;

// console.log(userTraits);

// var answerBank = new Array(questionBank.length).fill("");
// Question Element
question = document.querySelector("#quiz-question");

// User Answer Buttons
userYesBtn = document.querySelector("#user-yes");
userNoBtn = document.querySelector("#user-no");

// Roomie Answer Buttons
roomieYesBtn = document.querySelector("#roomie-yes");
roomieNeutBtn = document.querySelector("#roomie-neutral");
roomieNoBtn = document.querySelector("#roomie-no");

// Buttons
backBtn = document.querySelector("#back");
nextBtn = document.querySelector("#next");
submitBtn = document.querySelector("#submit");

// Set the default postion in the array to be 0
let currentQuestion = 0;

function move() {
  width = ((currentQuestion + 1) / questionBank.length) * 470;
  progress.innerHTML = `${currentQuestion + 1}/${questionBank.length}`;
  progress.style.width = width + "px";
}
// Function that modifies the Question element based on the current
// Position in the Question array
function setOldAnswers() {
  answer = answerBank[currentQuestion];
  if (answer[0] === "True") {
    checkOption(userYesBtn);
    unCheckOption(userNoBtn);
  } else {
    unCheckOption(userYesBtn);
    checkOption(userNoBtn);
  }

  if (answer[1] === "True") {
    checkOption(roomieYesBtn);
    unCheckOption(roomieNeutBtn);
    unCheckOption(roomieNoBtn);
  } else if (answer[1] === "Neutral") {
    checkOption(roomieNeutBtn);
    unCheckOption(roomieYesBtn);
    unCheckOption(roomieNoBtn);
  } else {
    unCheckOption(roomieNeutBtn);
    unCheckOption(roomieYesBtn);
    checkOption(roomieNoBtn);
  }
}

function setCurrentQuestion() {
  // Display current Question
  question.innerHTML = `${questionBank[currentQuestion]}`;
  move();
  if (!answerBank[currentQuestion] == "") {
    setOldAnswers();
  } else {
    unCheckOption(userYesBtn);
    unCheckOption(userNoBtn);
    unCheckOption(roomieYesBtn);
    unCheckOption(roomieNeutBtn);
    unCheckOption(roomieNoBtn);
  }
}

// Increments postion in Question Array, calls setCurrentQuestion funtino
function nextQuestion() {
  // Add submit buttton

  if (currentQuestion === questionBank.length - 2) {
    nextBtn.classList.add("hidden");
    submitBtn.classList.remove("hidden");
  }
  let answer = [];
  if (userYesBtn.classList.contains("checked")) {
    answer[0] = "True";
  } else if (userNoBtn.classList.contains("checked")) {
    answer[0] = "False";
  } else {
    alert("Please pick an option before pressing next.");
    return null;
  }

  if (roomieYesBtn.classList.contains("checked")) {
    answer[1] = "True";
  } else if (roomieNeutBtn.classList.contains("checked")) {
    answer[1] = "Neutral";
  } else if (roomieNoBtn.classList.contains("checked")) {
    answer[1] = "False";
  } else {
    alert("Please pick an option before pressing next.");
    return null;
  }
  answerBank[currentQuestion] = answer;

  if (currentQuestion <= questionBank.length - 1) {
    currentQuestion++;
  }
  // Set answers if we hav answered the question
  if (!answerBank[currentQuestion] == "") {
    setOldAnswers();
  }
  setCurrentQuestion();
}

// Decrements postion in Question Array, call setCurrentQuestion function
function previousQuestion() {
  if (currentQuestion <= 0) {
    null;
  }

  // If the any option is checked, set it.
  let answer = [];

  if (userYesBtn.classList.contains("checked")) {
    answer[0] = "True";
  } else if (userNoBtn.classList.contains("checked")) {
    answer[0] = "False";
  } else {
    null;
  }

  if (roomieYesBtn.classList.contains("checked")) {
    answer[1] = "True";
  } else if (roomieNeutBtn.classList.contains("checked")) {
    answer[1] = "Neutral";
  } else if (roomieNoBtn.classList.contains("checked")) {
    answer[1] = "False";
  } else {
    null;
  }

  if (answer.length > 0) {
    answerBank[currentQuestion] = answer;
  }

  if (currentQuestion >= 1) {
    currentQuestion--;
  }
  if (!(currentQuestion === questionBank.length - 3)) {
    nextBtn.classList.remove("hidden");
    submitBtn.classList.add("hidden");
  }
  setCurrentQuestion();
}

function checkOption(el) {
  if (!el.classList.contains("checked")) {
    el.classList.add("checked");
  }
  if (!el.firstElementChild.classList.contains("bx-checkbox-checked")) {
    el.firstElementChild.classList.add("bx-checkbox-checked");
  }
}

function unCheckOption(el) {
  if (el.classList.contains("checked")) {
    el.classList.remove("checked");
  }
  if (el.firstElementChild.classList.contains("bx-checkbox-checked")) {
    el.firstElementChild.classList.remove("bx-checkbox-checked");
  }
}

function setUserYes() {
  checkOption(userYesBtn);
  unCheckOption(userNoBtn);
}

function setUserNo() {
  checkOption(userNoBtn);
  unCheckOption(userYesBtn);
}
function setRoomieYes() {
  checkOption(roomieYesBtn);
  unCheckOption(roomieNeutBtn);
  unCheckOption(roomieNoBtn);
}
function setRoomieNeut() {
  unCheckOption(roomieYesBtn);
  checkOption(roomieNeutBtn);
  unCheckOption(roomieNoBtn);
}
function setRoomieNo() {
  unCheckOption(roomieYesBtn);
  unCheckOption(roomieNeutBtn);
  checkOption(roomieNoBtn);
}

function createTraits(traits) {
  console.log("Sending Answers to Room.ly...");
  fetch("/traitQuiz/quiz", {
    mode: "cors", // no-cors, *cors, same-origin
    cache: "no-cache", // *default, no-cache, reload, force-cache, only-if-cached
    credentials: "same-origin", // include, *same-origin, omit
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(traits),
  })
    .then(function (response) {
      return response.json();
    })
    .then(function (data) {
      if (data.message === "success") {
        window.location = "/traitQuiz/endquiz";
      } else {
        alert("Something went wrong");
      }
    });
}

function submitAnswers() {
  // Get answers
  let answer = [];

  if (userYesBtn.classList.contains("checked")) {
    answer[0] = "True";
  } else if (userNoBtn.classList.contains("checked")) {
    answer[0] = "False";
  } else {
    alert("Please pick an option before pressing next.");
    return null;
  }

  if (roomieYesBtn.classList.contains("checked")) {
    answer[1] = "True";
  } else if (roomieNeutBtn.classList.contains("checked")) {
    answer[1] = "Neutral";
  } else if (roomieNoBtn.classList.contains("checked")) {
    answer[1] = "False";
  } else {
    alert("Please pick an option before pressing next.");
    return null;
  }
  answerBank[currentQuestion] = answer;
  createTraits({
    answerBank,
  });
  // console.log(answerBank);
}

// Handle next and previous buttons
nextBtn.addEventListener("click", nextQuestion);
backBtn.addEventListener("click", previousQuestion);
submitBtn.addEventListener("click", submitAnswers);

userYesBtn.addEventListener("click", setUserYes);
userNoBtn.addEventListener("click", setUserNo);
roomieYesBtn.addEventListener("click", setRoomieYes);
roomieNeutBtn.addEventListener("click", setRoomieNeut);
roomieNoBtn.addEventListener("click", setRoomieNo);

setCurrentQuestion();
