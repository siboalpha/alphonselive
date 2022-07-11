(function($) {
  $(function() {
    $('nav ul li > a:not(:only-child)').click(function(e) {
      $(this)
        .siblings('.nav-dropdown')
        .slideToggle()
      $('.nav-dropdown')
        .not($(this).siblings())
        .hide()
      e.stopPropagation()
    })
    $('html').click(function() {
      $('.nav-dropdown').hide()
    })
    // Toggle open and close nav styles on click
    $('#nav-toggle').click(function() {
      $('nav ul').slideToggle();
    });
    $('#nav-toggle').on('click', function() {
      this.classList.toggle('active')
    })
  })
})(jQuery)

jQuery(function($){
    var $navbar = $('.navigation')
    $(window).scroll(function(event){
        var $current = $(this).scrollTop();
        if($current > 50){
            $navbar.addClass('navigation-bar-black');
        } else{
            $navbar.removeClass('navigation-bar-black');
        }
    });
});
