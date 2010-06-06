<?php
require_once('settings.php');
mysql_connect($host,$user,$password) or die(mysql_error());
mysql_select_db($db) or die(mysql_error());


$id=(int)$_REQUEST['id']; //Get the page number to show

$query = "SELECT * FROM users WHERE id=".$id;
$result = mysql_query($query);

?>

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN"
"http://www.w3.org/TR/html4/strict.dtd">

<html lang="en-US" xml:lang="en-US" dir="ltr">

<!--**********************************************************************************************************************************-->
<!--  this is not radical 'chic' like seppuko.com - we are just radical ! 																														-->
<!--       ___                                                          ___																														-->           
<!--    .-'   `-.      death to the author                           .-'   `-.																												-->
<!--   / /\   /\ \                                                  / /\   /\ \																												--> 
<!--  . /__\ /__\ .    web2.0suicide machine was first released    . /__\ /__\ .																											-->
<!--  |___  ^  ___|    at a suicide party in worm 09/01/2009       |___  ^  ___|																											-->
<!--      |   |        look here:                                      |   |																													-->
<!--      |[[[|                                                        |[[[|																													-->
<!--																																																																	--> 
<!--http://agenda.wormweb.nl/tekstpagina_1kolom.php?request=service&item=worm_archief&returnitem=worm_archief&baseitem=130&id=2336    -->
<!--************ a project by www.moddr.net supported by www.wormweb.nl coded by fresco gamba																					--> 
<!--**********************************************************************************************************************************-->
	<head>
		<meta content="text/html; charset=UTF-8" http-equiv="Content-Type"/>
		<meta content="web suicide, facebook death, suicide machine, web 2.0 suicide, committing suicide, delete linkedin, erase profile, myspace, facebook, netart, online death, social network suicide" name="keywords"/>
		<title>Web 2.0 Suicide Machine - Meet your Real Neighbours again! - Sign out forever!</title>
		<link href="./css/suicide.css" type="text/css" rel="stylesheet" />
		<link rel="shortcut icon" href="favicon.ico" >
	</head>
	<body>
		<div id="wrapper" class="wrapper">
<?
//Create and print the Navigation bar
$Nav="";
echo "<div id='page_navi'>";
for($i = 1 ; $i <= $NumberOfPages ; $i++) {
	if($i == $page) {
		$Nav .= "&nbsp;<B>$i&nbsp;|</B>";
	}
	else	{
		$Nav .= "&nbsp;<a class=\"pagination\" style='color:#FF3F84;' id=\"page".$i."\" href=\"#\">$i</a>&nbsp;<b>|</b>";
	}
}
echo "</div><br /><br />" . $Nav;
while($row = mysql_fetch_assoc($result)){
	$size = getimagesize("./profiles/img/".$row['picture']);
	$img_size = $size['3'];
	$div_size = $size['1'] + 50;
	echo "<div id='wall_entry' style=\"height:".$div_size."px;\"><div id='deathcross'></div>";
	echo "<div id='wall_details'><h1>".utf8_encode($row['username'])."</h1><br>";
  echo "<p class='testimonialsquestion'>committed Web2.0 suicide on:<br></p><p class='testimonialsanswer'>".$row['t_create']."</p>";
	echo "<p class='testimonialsquestion'>lost friends:</p><p class='testimonialsanswer'>".$row['friends']."</p>";
	echo "<p class='testimonialsquestion'>last words:</p><p class='testimonialsanswer'>".$row['lastwords']."</p></div>";
	echo "<div id='logo_overlay'><img src='./img/small_".$row['command'].".png'></div>";
	echo "<div id='wall_picture'><div style='padding:0px 10px 7px 0px;height:".$size['1'].";width:".$size['0'].";background:url(./img/drop_border.png) no-repeat bottom right;'> <img ".$img_size."src='../profiles/img/". $row['picture']."'></div></div>";
  echo "</div>";
}
?></div></body></html>
