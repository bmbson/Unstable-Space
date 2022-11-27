// Element selection
let progressBar = document.querySelector(".progressBar");
let playbackBar = document.querySelector(".playbackBar");
let playButtons = document.querySelectorAll(".playButton");
let download = document.querySelector(".download");
let volume = document.querySelector(".volume");
let share = document.querySelector(".share");
let mute = document.querySelector(".mute");
let audio = document.querySelectorAll('.audio');
let ids = document.querySelectorAll('id')

//test elements will be migrated to a db
function playAudio() {
    audio = this.closest('.rightSide').previousElementSibling.previousElementSibling;
    audio.play();
};

playButtons.forEach(playButton => {
    playButton.addEventListener('click', playAudio, false);
});



volume.addEventListener('input', (e) => {
    const value = e.target.value;
    audio.volume = value / 100;
});