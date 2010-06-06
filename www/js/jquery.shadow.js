/*
 * Shadow
 * Created by Edgar Verle
 * Shadow is made for the jQuery library.
 * http://www.edgarverle.com/shadow
 */

/* 
 * @name shadow
 * @type jQuery
 * @param Map options Optional settings
 * @option Number cornerHeight The height in pixels of the corners of the shadow. Default: 8
 * @option Number width The width in pixels of the shadow. Default: 4
 * @option Number startOpacity This is the opacity at the closest point to the object. Default: 80
 * @option Number endOpacity The opacity at the furthest point in the shadow from the object. Default: 20
 * @option String color The color of the shadow. Default: black
 */
 
jQuery.fn.extend({
	shadow: function(options) {
		DropShadow(this, options);
	}
});

function DropShadow(element, options){
	var cornerHeight = 8;
	var width = 4;
	var startOpacity = 80;
	var endOpacity = 20;
	var color = "black";
	
	if(options){
		if(options["cornerHeight"] != null)
			cornerHeight = parseInt(options["cornerHeight"]);
		if(options["width"] != null)
			width = parseInt(options["width"]);
		if(options["startOpacity"] != null)
			startOpacity = parseFloat(options["startOpacity"]);
		if(options["endOpacity"] != null)
			endOpacity = parseFloat(options["endOpacity"]);
		if(options["color"] != null)
			color = options["color"];
			
		if(startOpacity < 1)
			startOpacity = Math.round(startOpacity*100);
		
		if(endOpacity < 1)
			endOpacity = Math.round(endOpacity * 100);
	}
	
	if($(element.id+"_shadow").length > 0)
		$(element.id+"_shadow").remove();
	
	element = $(element);
	
	var id = element[0].id + "_shadow";
	var html = "<div id='"+id+"' style='";
	
	if(element.css("position") == "absolute" || element.css("position") == "relative"){
		html += "position: " + element.css("position")+"; ";
		element.css("position", "");
	}
	
	if(element.css("top")){
		html += "top:"+element.css("top")+"; ";
		element.css("top", "");
	}

	if(element.css("left")){
		html += "left:"+element.css("left")+"; ";
		element.css("left", "");		
	}
	
	html += "'><table style='float:left;' cellpadding='0px' cellspacing='0px'><tr class='shadowFirstRow'>"+
		"<td colspan='2' rowspan='2'></td></tr></table></div>";
	
	element.wrap(html);
		
	html = "<td colspan='"+width+"' style='width:"+width+"px; height:"+cornerHeight+"px;'><table cellpadding='0px' cellspacing='0px'>";
	
	var opacity = startOpacity;
	
	for(var i = 0; i < cornerHeight; i++){
		html += "<tr>";
		
		for(var j = 0; j < width; j++){
			opacity = Math.round((i - j * (cornerHeight / width)) * 10);
			
			if(opacity < 0)
				opacity = 0;
			else if(opacity < 10)
				opacity = "0"+opacity;
				
			html += "<td style='height:1px; width:1px; background-color: "+color+"; opacity:0."+opacity+"; filter:Alpha(opacity="+opacity+");'></td>"
		}
		
		html += "</tr>";
	}
	
	html += "</table></td>";
	
	$("#"+id).children().children().children(".shadowFirstRow").append(html);
	
	html = "<tr>";
	
	for(var i = startOpacity; i >= endOpacity; i -= (startOpacity - endOpacity) / (width - 1)){
		opacity = Math.round(i);
		
		if(opacity < 10)
			opacity = "0" + opacity;
			
		html += "<td style='background-color:"+color+"; padding:0px; margin:0px; height:"+(element.height()- cornerHeight + 12)+"px; opacity:0."+opacity+"; filter:Alpha(opacity="+opacity+");'></td>";
	}
	
	html += "</tr>";
	
	html += "<tr><td rowspan='"+width+"' style='width:"+cornerHeight+"px; height:"+width+"px;'><table cellpadding='0px' cellspacing='0px'>";
	for(var i = 0; i < width; i++){
		html += "<tr>";
		
		for(var j = 0; j < cornerHeight; j++){
			opacity = Math.round((0 - i * (cornerHeight / width) + j)*10);
			
			if(opacity < 0)
				opacity = 0;
			else if(opacity < 10)
				opacity = "0"+opacity;
				
			html += "<td style='width:1px; height:1px; background-color:"+color+"; opacity:0."+opacity+"; filter:Alpha(opacity="+opacity+");'></td>";
		}
		
		html += "</tr>";
	}
	
	html += "</table></td>";
	
	var temp = element.width() + 4;
	
	if($.browser.msie)
		temp -= cornerHeight + 4;
	
	for(var i = startOpacity; i >= endOpacity; i -= (startOpacity - endOpacity) / (width - 1)){
		if(i != startOpacity)
			html += "<tr>";
		
		opacity = Math.round(i);
		
		if(opacity < 10)
			opacity = "0"+opacity;
			
		html += "<td style='height:1px; width:"+temp+"px; background-color:"+color+"; opacity:0."+opacity+"; filter:Alpha(opacity="+opacity+");'></td>";
					
		for(var j = startOpacity; j >= endOpacity; j -= (startOpacity - endOpacity) / (width - 1)){
			opacity = Math.round(j);
			
			if(opacity > i)
				opacity = Math.round(i);
			
			
			if(opacity < 10)
				opacity = "0"+opacity;
				
			html += "<td style='width:1px; height:1px; background-color:"+color+"; opacity:0."+opacity+"; filter:Alpha(opacity="+opacity+");'></td>";
		}
		
		html += "</tr>";
	}
	
	$("#"+id).children("table").append(html);
}
