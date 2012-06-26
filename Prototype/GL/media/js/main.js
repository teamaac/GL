$(document).ready(function(){
	$('#menu a').click( function () {
		$('#menu a').removeClass("active");
		$(this).addClass("active");
	});

	$("a[data-id^='fancybox-portfolio']").fancybox({
		'overlayShow'	: true,
		'overlayColor'	: '#000',
		'transitionIn'	: 'elastic',
		'transitionOut'	: 'elastic',
		'height'        : 800,
		'width'	        : 800
	});

	$('#menu a, #logo, .scrol').click(function() {
		var elementClicked = $(this).attr("href");
		var destination = $(elementClicked).offset().top;
		$("html:not(:animated),body:not(:animated)").animate({ scrollTop: destination-0}, 1000 );
		return false;
	});
});

jQuery(document).ready(function(){
	jQuery("#about_box a").hover(
		function(){jQuery(this).find("img").stop().animate({opacity:0.4}, 400);}, 
		function(){jQuery(this).find("img").stop().animate({opacity:1  }, 400);});
});

jQuery(document).ready(function(){
	jQuery("#portfolio_box a").hover(
		function(){jQuery(this).find("img").stop().animate({opacity:0.4}, 400);},
		function(){jQuery(this).find("img").stop().animate({opacity:1  }, 400);});
});

(function($){
	$(function(){
		/** Add the next and previous buttons with JavaScript to gracefully degrade */
		var cycle_container = $('#slide-container');
		cycle_container.append('<div id="cycle-next"></div><div id="cycle-prev"></div>');
		cycle_start(cycle_container, 0);
		/** Restart the slideshow when someone resizes the browser to ensure that sliding distance matches the correct viewport */
		$(window).resize(function(){
			var current_slide = cycle_container.find('.slide:visible').index();
			if(window.console&&window.console.log) { console.log('current_slide'+current_slide); }
			cycle_container.cycle('destroy');
			new_window_width = $(window).width();
			cycle_container.find('.slide').width(new_window_width);
			cycle_start(cycle_container, current_slide);
		});
	});
	/** Cycle configurations */
	function cycle_start(container, index){
		var window_width = $(window).width();
		container.find('.slide').width(window_width);
		if (container.length > 0){
			container.cycle({
				timeout: 0,
				speed: 600,
				pager: '#cycle-pager',
				slideExpr: '.slide',
				fx: 'scrollHorz',
				easeIn: 'linear',
				easeOut: 'swing',
				startingSlide: index,
				pagerAnchorBuilder: cycle_paginate
	});}}

	function cycle_paginate(ind, el) {return '<a href="#slide-'+ind+'"><span>'+ind+'</span></a>';}
})(jQuery);

