// Mobile Menu Toggle
(function ($) {
   $('.mobile-menu-toggle').click(function(){
      $('.mobile-menu').addClass('mobile-menu-active');
   });
   $('.mobile-menu-toggle-close').click(function(){
      $('.mobile-menu').removeClass('mobile-menu-active');
   });
}(jQuery));


// Preloader Animation
$(window).on("load",function(){
   $(".loader-container").fadeOut(500);
});


// Topbar Animation
$(function() {
   prettyPrint()
   function resetToDefaults() {
      topbar.config({
         autoRun      : true,
         barThickness : 2,
         barColors    : {'0': 'rgba(26, 162, 96, 1)',},
         shadowBlur   : 0,
         shadowColor  : 'rgba(0,   0,   0,   .6)',
         className    : 'topbar'
      })
   }
   // Page load
   resetToDefaults()
   topbar.show()
   setTimeout(function() {
      $('#main_content').fadeIn('slow')
      topbar.hide()
   }, 1000)
})


// Infinity Quote
var slides = document.querySelectorAll('.infinity-quote .slide');
var currentSlide = 0;
var slideInterval = setInterval(nextSlide,7000);

function nextSlide(){
	slides[currentSlide].className = 'slide';
	currentSlide = (currentSlide+1)%slides.length;
	slides[currentSlide].className = 'slide showing';
}


// Placeholder Animation
superplaceholder({
   el: searchInput,
      sentences: ['জনপ্রিয় সার্চঃ অমর একুশে...', 'জনপ্রিয় সার্চঃ পেডোফিলিয়া...', 'জনপ্রিয় সার্চঃ মারভেলের ইতিহাস...'],
   options: {
      letterDelay: 80,
      loop: true,
      startOnFocus: false
   }
});
superplaceholder({
   el: mobileSearchInput,
      sentences: ['জনপ্রিয় সার্চঃ অমর একুশে...', 'জনপ্রিয় সার্চঃ পেডোফিলিয়া...', 'জনপ্রিয় সার্চঃ মারভেলের ইতিহাস...'],
   options: {
      letterDelay: 80,
      loop: true,
      startOnFocus: false
   }
});


// Share button
function copylink() {
   var shareLink = document.getElementById("share-link").value;
   navigator.clipboard.writeText(shareLink)

   var tooltip = document.getElementById("share-tooltip");
   tooltip.innerHTML = "Copied!";
}

function outFunc() {
   var tooltip = document.getElementById("share-tooltip");
   tooltip.innerHTML = "Copy to clipboard";
}



