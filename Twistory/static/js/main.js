$(window).bind('scroll', function() {
     if ($(window).scrollTop() > 50) {
     $('.navbar_wrapper').addClass('fixed');
     }
     else {
         $('.navbar_wrapper').removeClass('fixed');
    }
});
