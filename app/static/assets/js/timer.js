let timerInterval = null;
let timeLeft = 300; // 5 daqiqa
let audio = new Audio("/static/assets/sounds/timer-end.mp3");

function startTimer() {
  if (timerInterval) return;

  timeLeft = 300;
  updateTimerDisplay();

  timerInterval = setInterval(() => {
    timeLeft--;
    updateTimerDisplay();

    if (timeLeft <= 0) {
      clearInterval(timerInterval);
      timerInterval = null;
      audio.play();
    }
  }, 1000);
}

function stopTimer() {
  if (timerInterval) {
    clearInterval(timerInterval);
    timerInterval = null;
  }
}

function updateTimerDisplay() {
  const minutes = Math.floor(timeLeft / 60);
  const seconds = timeLeft % 60;
  const display = `${minutes.toString().padStart(2, "0")}:${seconds.toString().padStart(2, "0")}`;

  document.getElementById("modal-timer-display").textContent = display;

  if (timeLeft <= 60) {
    document.getElementById("modal-timer-display").classList.add("text-danger");
  } else {
    document.getElementById("modal-timer-display").classList.remove("text-danger");
  }
}
