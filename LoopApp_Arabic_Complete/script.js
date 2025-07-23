
// Script to handle basic interactions

document.addEventListener('DOMContentLoaded', function() {
    const musicButton = document.querySelector('.music-btn');
    const discordButton = document.querySelector('.discord-btn');
    
    // Button click events
    musicButton.addEventListener('click', function() {
        alert('Music toggle functionality goes here!');
    });

    discordButton.addEventListener('click', function() {
        window.open('https://discord.gg/DVTbMPnF', '_blank');
    });
});
