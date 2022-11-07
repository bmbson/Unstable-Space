// Element selection
let progressBar = document.querySelector(".progressBar");
let playbackBar = document.querySelector(".playbackBar");
let playButton = document.querySelector(".playButton");
let download = document.querySelector(".download");
let volume = document.querySelector(".volume");
let share = document.querySelector(".share");
let mute = document.querySelector(".mute");
let audio = document.querySelector('.audio');

//test elements will be migrated to a db
playButton.addEventListener('click', () => {
    let audio = document.querySelector('.audio');
    audio.play();
});

volume.addEventListener('input', (e) => {
    const value = e.target.value;
    audio.volume = value / 100;
});