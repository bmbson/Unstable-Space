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

//test elements will be migrated to a db

function playAudio() {
    audio = this.closest('.rightSide').previousElementSibling.previousElementSibling;
    audio.play();
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
        console.log(progressBar);
        const currentTime = audio.currentTime;
        const duration = audio.duration;
        const progressBarPosition = (currentTime / duration) * 100;
        progressBar.value = progressBarPosition;
    })
})