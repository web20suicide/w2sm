<?php
require_once('settings.php');
mysql_connect($host,$user,$password) or die(mysql_error());
mysql_select_db($db) or die(mysql_error());

$page=$_REQUEST['page']; //Get the page number to show
if($page == "") $page=1; //If no page number is set, the default page is 1 


$query = "SELECT * FROM users ORDER BY id DESC LIMIT 10";
$result = mysql_query($query);

echo "<h1>TOP 10 of Latest Social Suiciders</h1>";
while($row = mysql_fetch_assoc($result)){
	$size = getimagesize("./profiles/img/".$row['picture']);
	$img_size = $size['3'];
	$div_size = $size['1'] + 115;
	echo "<div id='wall_entry' style=\"height:".$div_size."px;\">";
	echo "<div id='wall_details'><h1>".utf8_encode($row['username'])."</h1><br>";
  echo "<p class='testimonialsquestion'>committed Web2.0 suicide on:<br></p><p class='testimonialsanswer'>".$row['t_create']."</p>";
	echo "<p class='testimonialsquestion'>lost friends:</p><p class='testimonialsanswer'>".$row['friends']."</p>";
	if ($row['tweets'] != "0") {
			echo "<p class='testimonialsquestion'>lost tweets:</p><p class='testimonialsanswer'>".$row['tweets']."</p>";
	}
	echo "<p class='testimonialsquestion'>last words:</p><p class='testimonialsanswer'>".$row['lastwords']."</p>";
	echo "</div>";
	echo "<div id='logo_overlay'><img src='./img/small_".$row['command'].".png'></div>";
	echo "<div id='wall_picture'><div style='padding:0px 10px 7px 0px;height:".$size['1']."px;width:".$size['0'].";background:url(./img/drop_border.png) no-repeat bottom right;'> <img ".$img_size."src='../profiles/img/". $row['picture']."'></div></div>";
  echo "<div id='fakehr'><hr></div></div>";
}
?>
