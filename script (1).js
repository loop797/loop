
// Script to handle basic interactions

document.addEventListener('DOMContentLoaded', function() {
    const musicButton = document.querySelector('.music-btn');
    const discordButton = document.querySelector('.discord-btn');
    
    // Adding fade-in effect for the page
    document.body.style.opacity = 0;
    setTimeout(function() {
        document.body.style.transition = 'opacity 2s ease';
        document.body.style.opacity = 1;
    }, 100);

    // Button click events
    musicButton.addEventListener('click', function() {
        alert('Music toggle functionality goes here!');
    });

    discordButton.addEventListener('click', function() {
        window.open('https://discord.gg/DVTbMPnF', '_blank');
    });
});
