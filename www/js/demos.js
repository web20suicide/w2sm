function demoInstanceInfo(myPlayer, myInfo) {
	var jPlayerInfo = "<p>This jPlayer instance is running in your browser using ";
	if(myPlayer.jPlayerGetInfo("html5")) {
		jPlayerInfo += "<strong>HTML5</strong> with ";
		if(myPlayer.jPlayerGetInfo("canPlayOGG")) {
			jPlayerInfo += "<strong>OGG</strong>";
		} else {
			jPlayerInfo += "<strong>MP3</strong>";
		}
	} else {
		jPlayerInfo += "<strong>Flash</strong> with <strong>MP3</strong>";
	}
	jPlayerInfo += " files.<br />This instance has the constructor option ";
	if(myPlayer.jPlayerGetInfo("oggSupport")) {
		jPlayerInfo += "set to <code>$(\"#jpId\").jPlayer({oggSupport: true})</code>";
	} else {
		jPlayerInfo += "defaulting to <code>$(\"#jpId\").jPlayer({oggSupport: false})</code>";
	}
	jPlayerInfo += "</p>";
	myInfo.html(jPlayerInfo);
}
