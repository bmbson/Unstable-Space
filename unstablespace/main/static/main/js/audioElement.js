// Element selection
let progressBar = document.querySelector(".progressBar");
let playbackBar = document.querySelector(".playbackBar");
let playButtons = document.querySelectorAll(".playButton");
let download = document.querySelector(".download");
let volumeButtons = document.querySelectorAll(".volume");
let share = document.querySelector(".share");
let mute = document.querySelector(".mute");
let audio = document.querySelectorAll('.audio');
let ids = document.querySelectorAll('id')

//test elements will be migrated to a db

function playAudio() {
    audioX = this.closest('.rightSide').previousElementSibling.previousElementSibling;
    audioX.play();
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

