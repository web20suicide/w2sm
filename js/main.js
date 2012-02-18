jQuery(document).ready(function($) {
	// turn off ajax caching
	$.ajaxSetup ({ cache: false });

	selected = "twitter";

	// set background opacity for facebox
	$.facebox.settings.opacity = 0.6; /* add this line */ 

	// make direct links like URL#faq popup in facebox
  if (document.location.toString().split('#')[1]) 
	{
		var url = document.location.toString().split('#')[1];	
		if (url == "latest") {
			jQuery.facebox(function() {
				jQuery.get('http://www.suicidemachine.org/latest.php', function(data) {
					jQuery.facebox(data)
				})
			}) 
		}
		else {
			jQuery.facebox(function() {
				jQuery.get('./static/'+url+'.html', function(data) {
						jQuery.facebox("<div id='"+url+"'>"+data+ "</div>")
				})
			}) 
		}

	}
	// load quovolver for changing quotes
	$('blockquote').quovolver();
	// hide some divs from the beginning
	$('#login').css('display','none');

	// load some static html
//$('#signout_others_os').load("http://www.suicidemachine.org/tweets.php");
	$('#signout_others_os').load("static/stats.html");
	$('#feature_header').html('Faster, Safer, Smarter, Better');
	$('#movie').load("static/movie.html");
	$('#worm').load("static/worm.html");
	$('#faq').load("static/faq.html");
	$('#movie_twitter').load("static/movie_twitter.html");

	// round corners
	$("#innerfooter").corner("8px");

	$('#feature_content_left').html('<h2>Tired of your Social Network?</h2><br />Liberate your newbie friends with a Web2.0 suicide! This machine lets you delete all your energy sucking social-networking profiles, kill your fake virtual friends, and completely do away with your Web2.0 alterego. The machine is just a metaphor for the website which moddr_ is hosting; the belly of the beast where the web2.0 suicide scripts are maintained. Our service currently runs with Facebook, Myspace, Twitter and LinkedIn! Commit NOW!<br><br><span style="color:#FF3F84;">Feel free like a real bird again and untwitter yourself. Watch it <a href="#movie_twitter" rel="facebox" class="subfeature">here</a>!</span>');
	// apply fancy facebox to all anchor with rel=facebox
	$('a[rel*=facebox]').facebox({
		loading_image : 'loading.gif',
		close_image   : 'closelabel.gif'
	})

	// fetch button clicks for wall-of-fame pagination
	$('.pagination').live("click",function() {
		var getthat = this;
		$.post("http:/www.suicidemachine.org/test.php", {page: $(this).html()}, function(data){
				$(getthat).parent().html(data);
			});
		return false;
	});

	$('#latest').live("click",function() {
		jQuery.facebox(function() {
			jQuery.get('http://www.suicidemachine.org/latest.php', function(data) {
				jQuery.facebox(data)
			})
		}) 
		//return false;
	});

	// switch web20 logos in signout
	$(".button_signout").live("click", function() { 
		selected = $(this).attr('id');
		$('#login_facebook').hide();
		$('#login_myspace').hide();
		$('#login_linkedin').hide();
		$('#login_twitter').hide();
		$('#signout_others_os').show();
		$('#signout').css('background-image','url(img/signout.png)');
		$('#signout_hold').hide();
		$('#signout_hold').css('background-image','url(img/signout_' + selected + '.png)'); 
		$('#signout_hold').fadeIn("slow");
	});
	
		$("a[class=buttonsignout]").live("click", function() { 
				$('#signout_others_os').fadeOut(); $('#login_'+ selected).fadeIn("slow");
		});
	
	// for debugging it refers to a hidden button
	$("a[class=buttonless]").live("click", function() { 
		$('#signout_others_os').fadeOut();
		$('#login_'+ selected).fadeIn("slow");
	});

	$('a[class=fukkr]').click( function() {
		var callsite = (this.id);
		if (callsite == "navi_review") {
			callsite = "review";
			$('#innerfooter').animate({height: "550"},600);
			$("#subcontent").load('static/'+ callsite + '.html');
		}
		else if (callsite == "navi_contact") {
			callsite = "contact";
			$('#innerfooter').animate({height: "220"},600);
			$("#subcontent").load('static/'+ callsite + '.html');
		}
		else if (callsite == "navi_credits") {
			callsite = "credits";
			$('#innerfooter').animate({height: "365"},600);
			$("#subcontent").load('static/'+ callsite + '.html');
		}
		$("#subcontent").fadeIn("slow");
	});
	$('a[class=sublinks]').click( function() {
		var callsite = ($(this).attr('id'));
		$("#subcontent").load('static/'+ callsite + '.html');

		if (callsite == "press") {
			$('#innerfooter').animate({height: "785"},600);
		}
		else if (callsite == "contact") {
			$('#innerfooter').animate({height: "220px"},600);
		}
		else if (callsite == "credits") {
			$('#innerfooter').animate({height: "365px"},600);
		}
		else if (callsite == "review") {
			$('#innerfooter').animate({height: "550px"},600);
		}
		else {
			$('#innerfooter').animate({height: "105px"},600);
			$("#subcontent").empty();
			// open new tab for facebook etc
		}
		$("#subcontent").fadeIn("slow");
		return false;
	});
	$.fn.preventDoubleSubmit = function() {
		$(this).submit(function() {
			if (this.beenSubmitted){
				alert("you already submitted!");
				return false;
			}
			else {
				this.beenSubmitted = true;
			}
		});
	};

	$('form').each( function() {
		// clear all forms onload and validate them properly
		$(this).clearForm();
		// validaaaaaaaaaaaaaaaaaaattttttttte
		$(this).validate({
			rules: {
				username: {
				email: true,
				required: true
				},
				password: {
				required: true,
				minlength: 6 
				}
			},
			//set messages to appear inline
			messages: { username: "Malformed login (killer@suicide.net for e.g.)" },
			submitHandler: function(form) { 
				if (!this.beenSubmitted) {
				this.beenSubmitted = true;
				// call bash script which checks available XVNC session
				var datadata = "id=" + form.id + "&" + $(form).serialize() ;
				var job_id = "1";
								// collect all form fields
								var dataString = $(form).serialize();
								// remove trailing whitespaces or CR...
								dataString = "id=" + job_id + "&" + dataString;
								$.ajax({  	type: "POST",
										url: "../cgi-bin/web20_dump.cgi",
										data: dataString,
										// if form data VALID launch VNC and hide input fields
										success: function(r) { 
											//alert("lets begin" + dataString);
										}
								});
							}
				else {
					jQuery.facebox('<div style="width:500px;">Sorry, you were clicking the submit button more than once.<br><br> To prevent multiple sessions this action is not allowed!<br><br>Thanks your understanding!</div>');
				}
				}
			});
	});
});

