jQuery(document).ready(function($) {
	// turn off ajax caching
	$.ajaxSetup ({ cache: false });

//w2sm_check();
services = new Array('facebook', 'myspace', 'twitter', 'linkedin');
selected = "twitter";
function w2sm_check() { 
 $.ajax({
	 type: "GET",
	 url: "./cgi-bin/available.cgi",
	 success: function(msg){
		var single=msg.split("<|>"); 
		//single.shift();
		//alert(single);
		var image_urls = "";
		for (var j in services) {
				if ($.inArray(services[j],single) != "-1") {
					image_urls += "<img src='./img/small_" + services[j] + "_grey.png' border='0'>";
				}
				else {
					image_urls += "<a href=\"#\" class=\"button_signout\" id=\"" + services[j] + "\"><img id=\"button_" + services[j] + "\" alt=\"signout_" + services[j] + "\" src=\"./img/small_" + services[j] + ".png\"></a>";
				}
		
}
		//alert(image_urls);
		$('#signout_buttons').html(image_urls);
	 }
 });
}
//var holdTheInterval = setInterval(w2sm_check, 10000); 

	// default networkk
	//var selected = "twitter";

	// set background opacity for facebox
	$.facebox.settings.opacity = 0.6; /* add this line */ 

	// make direct links like URL#faq popup in facebox
  if (document.location.toString().split('#')[1]) 
	{
		var url = document.location.toString().split('#')[1];	
		if (url == "latest") {
			jQuery.facebox(function() {
				jQuery.get('./latest.php', function(data) {
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
	// load faceboxes for static pages
	// hide some divs from the beginning
	$('#login').css('display','none');

	//jQuery.get('./static/suicide.html', function(data) {
	//	jQuery.facebox(data)
	//})

// --- by k0a1a -- 

/*
jQuery.facebox('<div style="padding:15px;width:700px;font-style:normal"><span style="font-size:160%;font-style:italic;">Web 2.0 Suicide Machine meets its lawyer<object width="560" height="315"><param name="allowfullscreen" value="true" /><param name="allowscriptaccess" value="always" /><param name="movie" value="http://vimeo.com/moogaloop.swf?clip_id=10021067&amp;server=vimeo.com&amp;show_title=0&amp;show_byline=0&amp;show_portrait=0&amp;color=00ADEF&amp;fullscreen=1" /><embed src="http://vimeo.com/moogaloop.swf?clip_id=10021067&amp;server=vimeo.com&amp;show_title=0&amp;show_byline=0&amp;show_portrait=0&amp;color=00ADEF&amp;fullscreen=1" type="application/x-shockwave-flash" allowfullscreen="true" allowscriptaccess="always" width="560" height="315"></embed></object><br><br>Just what is it that makes today\'s Cease &amp; Desist letters so different?<br><object width="560" height="315"><param name="allowfullscreen" value="true" /><param name="allowscriptaccess" value="always" /><param name="movie" value="http://vimeo.com/moogaloop.swf?clip_id=10019937&amp;server=vimeo.com&amp;show_title=0&amp;show_byline=0&amp;show_portrait=0&amp;color=00ADEF&amp;fullscreen=1" /><embed src="http://vimeo.com/moogaloop.swf?clip_id=10019937&amp;server=vimeo.com&amp;show_title=0&amp;show_byline=0&amp;show_portrait=0&amp;color=00ADEF&amp;fullscreen=1" type="application/x-shockwave-flash" allowfullscreen="true" allowscriptaccess="always" width="560" height="315"></embed></object><br><br>Facebook excommunicates WORM because of the Web 2.0 Suicide Machine<object width="560" height="315"><param name="allowfullscreen" value="true" /><param name="allowscriptaccess" value="always" /><param name="movie" value="http://vimeo.com/moogaloop.swf?clip_id=8223187&amp;server=vimeo.com&amp;show_title=0&amp;show_byline=0&amp;show_portrait=0&amp;color=00ADEF&amp;fullscreen=1" /><embed src="http://vimeo.com/moogaloop.swf?clip_id=9532862&amp;server=vimeo.com&amp;show_title=0&amp;show_byline=0&amp;show_portrait=0&amp;color=00ADEF&amp;fullscreen=1" type="application/x-shockwave-flash" allowfullscreen="true" allowscriptaccess="always" width="560" height="315"></embed></object></span><br /><span style="font-size:110%;font-style:normal;"><b>Rotterdam, 18th of February 2010<br><br>Facebook excommunicates WORM because of the Web2.0 Suicide Machine</b><br><br><blockquote><p>It is with great sorrow that we announce that Facebook Inc. has decided that WORM, the producer of the Web 2.0 Suicide Machine, will be excommunicated from Facebook.<br><br>The initiative to build the Web 2.0 Suicide Machine came from Moddr_, WORM’s media lab. By threatening WORM, Facebook is trying to take down the Suicide Machine.<br><br>The Web 2.0 Suicide Machine allows users of - among others - Facebook to commit ‘social network suicide’. Facebook threatens WORM with further legal action if WORM doesn’t stop targeting the FaceBook platform via the SuicideMachine. In addition, it has now also demanded that WORM immediately deletes its own Facebook profile (WORM_Rotterdam). According to Facebook and its lawyer, the Web 2.0 Suicide Machine has violated Facebook’s Terms of Service and with that WORM has forfeited it’s right to keep using the platform. WORM does not want to engage in a fight over this matter with Facebook. The idea behind the Web 2.0 Suicide Machine was to be able to ‘unfriend’ in an automated fashion and to make users of social networks aware that they should always be in control of their own data. Facebook won’t allow for this control and is also not willing to enter into this debate. We are pretty much done with that and are left with no other choice than to commit online suicide ourselves. The conditions and attitude of Facebook leave no other option as far as WORM is concerned.</p><br><p>WORM deeply regrets the current situation. The web 2.0 Suicide Machine was never intended to target Facebook as such, but meant as a tool for people who, for whatever reason, are tired of their online life. Facebook wants all access to their service, personal data of their users included, to run via their own ‘connect’ platform. In this way, Facebook can set, interpret and change its own rules as it sees fit...</p><br><p>The excommunication of WORM illustrates that data freedom and net neutrality of users is merely an illusion on many social network sites. Not only is it not allowed for people to unfriend (in an automated manner), but companies also have the power to expel users they do not like. Facebook shows that a user only has the rights that Facebook grants it.</p><br><p>Facebook claims all rights. WORM does not want to continue living in this 2.0 world. Which is why we say goodbye to all our friends. We wish you all the best.</p><br><p>No flowers, no speeches.</p><br></blockquote><i>moddr_labs,<br>WORM, Rotterdam<br><a href="http://worm.org">worm.org</a><br><a href="http://moddr.net">moddr.net</a><br><a href="http://suicidemachine.org">suicidemachine.org</a><br><br><small><a href="download/web_20_suicide_note.pdf">download press release pdf</a></small></span></div>');

*/

	//jQuery.facebox('<div style="padding:15px;width:600px;font-style:normal"><span style="font-size:160%;font-style:italic;">2010 starts with a Facebook Ban!</span><br><br><img src="./img/happy2010_web.png"><br><br><img src="./img/restricted.png" border="0"><br><br><p>After more than 50.000 friends being unfriended and more than 500 forever "signed-out" users, Facebook started to block our suicidemachine from their servers without any comment! We are currently looking in ways to circumvent this ungrounded restriction imposed on our service!</p><br>Thanks for your understanding<br>Sincerly,<br>Your 2.0 suicide team<br><br><span style="font-size:80%">PS: If you wanna support us and can set up a decent proxy server, please do not hesitate to contact us at suicide[[at]]moddr[[dot]]net</span></div>');
	//jQuery.facebox('<div style="padding:15px;width:500px;font-style:italic"><h1>Because we care!</h1><img src="./img/happy2010_web.png" border="0"><p>We apologize to all our users for the slowdown of our service! Within the last hours the huge demand for 2.0 suicides completely overblew our bandwidth resources!<br /><br />We are currently considering to relocate to another serverfarm. Please consider suicide at a later moment and accept our apologies!<br><br>You can still try to catch a free slot, but chances are quite low at the moment!</p></div>');
jQuery.facebox('<div style="padding:15px;width:600px;font-style:italic"><span style="font-size:160%;font-style:italic;">Stan Marsh commits web 2.0 suicide!</span><br /><br /><img src="./img/stanmarsh.png" border="0"><p>The web2.0 suicidemachine has been featured in one of the latest Southpark Episodes. Please download, watch and seed it NOW! Here\'s the link to a popular torrent-file: <br /><br /> <a href="http://thepiratebay.org/torrent/5505157">http://thepiratebay.org/torrent/5505157</a><br /><br /></p></div>');
	// load some static html
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
		$.post("test.php", {page: $(this).html()}, function(data){
				$(getthat).parent().html(data);
			});
		return false;
	});

	$('#link_latest').live("click",function() {
		jQuery.facebox(function() {
			jQuery.get('./latest.php', function(data) {
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
	// load login screen
	$("#click_suicide").live("click", function() { 
		//$('#signout_others_os').fadeOut();
		//$('#login_'+ selected).fadeIn("slow");
	});
	
		$("a[class=buttonsignout]").live("click", function() { 
		//jQuery.facebox('<div style="padding:15px;width:500px;"><p>Sorry our machine is currently shutdown due to server maintenance caused by the huge amount of requests and reactions we\'ve received in the last hours!<br /><br />Please consider suicide at a later moment and accept our apologies!<br><br>We\'ll hit back!</p></div>');
		var datadata = "selected=" + selected;
		var job_id = "";
		$.ajax({  	
				type: "POST",
				url: "./cgi-bin/list2.cgi",
				data: datadata,
				success: function(job_id) { 
					// trim trailing CR and NL characters 
					job_id = jQuery.trim(job_id);
					//job_id = '1';
					// if list.cgi returns none eq. all VNC sessions are busy
					if (job_id == 'none') {
			//					jQuery.facebox('<div style="padding:15px;width:500px;"><p>Sorry our machine is currently shutdown due to server maintenance caused by recent changes on Facebook and Twitter platform!<br /><br />We are looking into the problems but can\'t estimate the exact relaunch time. Please consider suicide at a later moment and accept our apologies!<br /><br />In case you just want to permanently delete your Facebook account, please follow this <a href="http://www.facebook.com/group.php?gid=16929680703" target="_blank">tutorial</a>! Another tutorial for Twitter is <a href="http://help.twitter.com/forums/10711/entries/15358" target="_blank">here</a> and there is another <a href="http://www.tech-recipes.com/rx/3955/myspace-how-to-cancel-your-account/" target="_blank">one</a> for MySpace!</p></div>');
						jQuery.facebox('<div style="padding:15px;width:500px;"><p>It seems like that our machine is currently busy! We know that this is very annoying and we hope that soon there are more suicidemachine-servers available in the Internet!<br /><br />At the moment approx. only 10% of 2.0 suicides succeed in getting a free slot due to limitations of the suicidemachine which can execute only a very limited amount of suicides at the same time and some accounts need a couple of hours to get totally unfriended, untwittered, etc..!<br /><br />Please consider suicide at a later moment and accept our apologies!<br /><br />In case you just want to permanently delete your Facebook account, please follow this <a href="http://www.facebook.com/group.php?gid=16929680703" target="_blank">tutorial</a>! Another tutorial for Twitter is <a href="http://help.twitter.com/forums/10711/entries/15358" target="_blank">here</a> and there is another <a href="http://www.tech-recipes.com/rx/3955/myspace-how-to-cancel-your-account/" target="_blank">one</a> for MySpace!</p></div>');
					}
					// if VNC available post user-data and launch flashVNC...
					else {
					$('#signout_others_os').fadeOut(); $('#login_'+ selected).fadeIn("slow");
					}
				}
			});
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
				var job_id = "";
				$.ajax({  	
						type: "POST",
						url: "./cgi-bin/list.cgi",
						data: datadata,
						success: function(job_id) { 
							// trim trailing CR and NL characters 
							job_id = jQuery.trim(job_id);
							//job_id = '1';
							// if list.cgi returns none eq. all VNC sessions are busy
							if (job_id == 'none') {
								jQuery.facebox('<div style="padding:15px;width:500px;"><p>Sorry our machine is currently shutdown due to server maintenance caused by recent changes on Facebook and Twitter platform!<br /><br />We are looking into the problems but can\'t estimate the exact relaunch time. Please consider suicide at a later moment and accept our apologies!<br /><br />In case you just want to permanently delete your Facebook account, please follow this <a href="http://www.facebook.com/group.php?gid=16929680703" target="_blank">tutorial</a>! Another tutorial for Twitter is <a href="http://help.twitter.com/forums/10711/entries/15358" target="_blank">here</a> and there is another <a href="http://www.tech-recipes.com/rx/3955/myspace-how-to-cancel-your-account/" target="_blank">one</a> for MySpace!</p></div>');
							}
							// if VNC available post user-data and launch flashVNC...
							else {
								// collect all form fields
								var dataString = $(form).serialize();
								// remove trailing whitespaces or CR...
								dataString = "id=" + job_id + "&" + dataString;
								$.ajax({  	type: "POST",
										url: "./cgi-bin/web20_dump.cgi",
										data: dataString,
										// if form data VALID launch VNC and hide input fields
										success: function(r) { 
											//startVNC("5905");	
											vncport = "590" + job_id;
											//alert(vncport);
											jQuery.facebox('<embed width="800px" height="600px" allowscriptaccess="sameDomain" quality="high" bgcolor="#000000" play="true" expressinstall="true" type="application/x-shockwave-flash" src="../FLViewer.swf" pluginspage="http://www.adobe.com/go/getflashplayer" flashvars="host=suicidemachine.org&password=killer&port='+vncport+'&viewOnly=true&autoConnect=false&shared=true"/>');
											//startVNC(vncport);	
										}
								});
							}
						}
					});
				}
				else {
					jQuery.facebox('<div style="width:500px;">Sorry, you were clicking the submit button more than once.<br><br> To prevent multiple sessions this action is not allowed!<br><br>Thanks your understanding!</div>');
				}
				}
			});
	});

	// initialize the vnc session (parsing portnumber!)
	function startVNC (vnc) {
		}
});

