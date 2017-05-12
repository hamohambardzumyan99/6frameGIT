//jQuery to collapse the navbar on scroll
$(window).scroll(function() {
  var st = $(this).scrollTop();
    if (st > 300) {
        $(".nav_base").addClass("nav_back");
        $(".nav").addClass("nav_menu_anim section-container");
    } else {
        $(".nav_base").removeClass("nav_back");
        $(".nav").removeClass(" nav_menu_anim section-container");

    }
});
$('body').scrollspy({ target: '.nav_base' });
$(window).scroll(function() {
  var st = $(this).scrollTop()/10;
  parseFloat(
    $(".Header").css({
      "transform" : "translate(0%, " + st + "%",
      "filter" : "blur(st + 'px')"
    })
  )
})
//jQuery for page scrolling feature - requires jQuery Easing plugin
$(function() {
    $('a.page-scroll').bind('click', function(event) {
        var $anchor = $(this);
        $('html, body').stop().animate({
            scrollTop: $($anchor.attr('href')).offset().top
        }, 1000, 'easeInOutQuint');
        event.preventDefault();
    });
});
