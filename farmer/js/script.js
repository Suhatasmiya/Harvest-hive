/*#############################################################################################*/
/* CONTACTS JS */

$(document).ready(function() {
    // Animate the "Get in Touch" heading on page load
    $('.text-center').animate({opacity: 1, top: '10px'}, 1000);
    
    // Animate the navbar brand on hover
    $('.navbar-brand').hover(function() {
      $(this).animate({fontSize: '40px'}, 500);
    }, function() {
      $(this).animate({fontSize: '30px'}, 500);
    });
  });
  
/*#############################################################################################*/

// Wrap every letter in a span
var textWrapper = document.querySelector('.ml1 .letters');
textWrapper.innerHTML = textWrapper.textContent.replace(/\S/g, "<span class='letter'>$&</span>");

anime.timeline({loop: true})
  .add({
    targets: '.ml1 .letter',
    scale: [0.3,1],
    opacity: [0,1],
    translateZ: 0,
    easing: "easeOutExpo",
    duration: 600,
    delay: (el, i) => 70 * (i+1)
  }).add({
    targets: '.ml1 .line',
    scaleX: [0,1],
    opacity: [0.5,1],
    easing: "easeOutExpo",
    duration: 700,
    offset: '-=875',
    delay: (el, i, l) => 80 * (l - i)
  }).add({
    targets: '.ml1',
    opacity: 0,
    duration: 1000,
    easing: "easeOutExpo",
    delay: 1000
  });

  /*#############################################################################################*/
/*#############################################################################################*/
const paragraph = document.querySelector('.glow');

paragraph.addEventListener('mouseover', () => {
  paragraph.classList.add('glow');
});

paragraph.addEventListener('mouseout', () => {
  paragraph.classList.remove('glow');
});
