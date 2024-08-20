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