let playButton = document.getElementById('play')
let muteButton = document.getElementById('mute')
let volume = document.getElementById('volume')

let timer = document.getElementsByClassName('timer')
timer = timer[0]

let audioFile = document.getElementsByClassName('audio')
audioFile = audioFile[0]

let progressBar = document.getElementsByClassName('progressBar')
progressBar = progressBar[0]

function playImg(element) {
    alert()
    if (element.src == "/static/main/img/controls/player-play.png") {
        element.src = "/static/main/img/controls/player-pause.png";
    } else {
        element.src =  "/static/main/img/controls/player-play.png";
    }
}

function playAudio() {
    audio = audioFile
    if (audio.paused) {
        audio.play();
        play.src = "/static/main/img/controls/player-pause.png";
      } else {
        audio.pause();
        play.src = "/static/main/img/controls/player-play.png";
      }
};

function muteAudio() {
    audio = audioFile
    if (audio.muted == false) {
        audio.muted = true
        muteButton.src = "/static/main/img/controls/mute.png";
      } else if (audio.muted == true) {
        audio.muted = false
        muteButton.src = "/static/main/img/controls/high-volume.png";
      }
};

function calculateTime(secs) {
    const minutes = Math.floor(secs / 60);
    const seconds = Math.floor(secs % 60);
    const returnedSeconds = seconds < 10 ? `0${seconds}` : `${seconds}`;
    return `${minutes}:${returnedSeconds}`;
};

function showVolumeBar() {
    volume.style.display="block";
}

function removeVolumeBar() {
    volume.style.display="none";
}



playButton.addEventListener('click', playAudio, false);

volume.addEventListener('input', () => {
    audio = audioFile
    const volumeAmount = volume.value;
    audio.volume = volumeAmount / 100;
});

audioFile.addEventListener('timeupdate', (event) => {
    progressBar = progressBar
    const currentTime = audio.currentTime;
    const duration = audio.duration;
    const progressBarPosition = (currentTime / duration) * 100;
    progressBar.value = progressBarPosition;
});

progressBar.addEventListener("input", (event) => {
    audio.currentTime = (progressBar.value / 100) * audio.duration
});

audioFile.addEventListener('timeupdate', (event) => {
    timer.innerHTML = String(calculateTime(audio.currentTime)) + " / " + String(calculateTime(audio.duration));
});

muteButton.addEventListener('click', muteAudio);

muteButton.addEventListener('mouseover', showVolumeBar, false)
muteButton.addEventListener("mouseout", removeVolumeBar, false);
volume.addEventListener('mouseover', showVolumeBar, false)
volume.addEventListener('mouseout', removeVolumeBar, false)

