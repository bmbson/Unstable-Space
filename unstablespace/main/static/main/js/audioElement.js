// Element selection
let progressBars = document.querySelectorAll(".progressBar");
let playbackBar = document.querySelector(".playbackBar");
let playButtons = document.querySelectorAll(".playButton");
let download = document.querySelector(".download");
let volumeButtons = document.querySelectorAll(".volume");
let share = document.querySelector(".share");
let mute = document.querySelector(".mute");
let audios = document.querySelectorAll('.audio');
let ids = document.querySelectorAll('id')
let timers = document.querySelector('.timer')

//test elements will be migrated to a db

function playAudio() {
    audio = this.closest('.rightSide').previousElementSibling.previousElementSibling;
    if (audio.paused) {
        audio.play();
      } else {
        audio.pause();
      }
};

function calculateTime(secs) {
    const minutes = Math.floor(secs / 60);
    const seconds = Math.floor(secs % 60);
    const returnedSeconds = seconds < 10 ? `0${seconds}` : `${seconds}`;
    return `${minutes}:${returnedSeconds}`;
};

playButtons.forEach(playButton => {
    playButton.addEventListener('click', playAudio, false);
});

volumeButtons.forEach(volumeButton => {
    volumeButton.addEventListener('input', () => {
        audio = volumeButton.closest('.rightSide').previousElementSibling.previousElementSibling;
        const volume = volumeButton.value;
        audio.volume = volume / 100;
    })
});

audios.forEach(audio => {
    audio.addEventListener('timeupdate', (event) => {
        progressBar = audio.closest('.audioStreamWrapper').querySelector('.rightSide').querySelector('.middleBar').querySelector('.progressBar')
        const currentTime = audio.currentTime;
        const duration = audio.duration;
        const progressBarPosition = (currentTime / duration) * 100;
        progressBar.value = progressBarPosition;
    })
});

audios.forEach(audio => {
    progressBar = audio.closest('.audioStreamWrapper').querySelector('.rightSide').querySelector('.middleBar').querySelector('.progressBar')
    progressBar.addEventListener("input", (event) => {
        audio.currentTime = (progressBar.value / 100) * audio.duration
    })
});

audios.forEach(audio => {
    audio.addEventListener('timeupdate', (event) => {
        timer = audio.closest('.audioStreamWrapper').querySelector('.rightSide').querySelector('.bottomBar').querySelector('.timer');
        timer.innerHTML = String(calculateTime(audio.currentTime)) + " / " + String(calculateTime(audio.duration));
    })
});



