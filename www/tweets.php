<?php
require_once('settings.php');
mysql_connect($host,$user,$password) or die(mysql_error());
mysql_select_db($db) or die(mysql_error());

$query = "SELECT tweets FROM users";
$result = mysql_query($query);

$i = 0;
while($row = mysql_fetch_assoc($result)){
	$i += $row['tweets']; 
}
$tweets = number_format($i*3);

$query = "SELECT friends FROM users";
$result = mysql_query($query);

$i = 0;
while($row = mysql_fetch_assoc($result)){
	$i += $row['friends']; 
}
$friends = number_format($i);

$users = number_format(mysql_num_rows(mysql_query("SELECT * FROM users")));

echo '<p><b> '.$friends.'</b> friends have been unfriended and<br><a href="#" class="buttonless"><img src="./img/nix.png" width="1" height="1"></a><b>'.$tweets.'</b> tweets have been removed since launching.</p><br><p><b>'.$users.'</b> people went before you!<br />Click <a id="link_latest" onclick="$(this).facebox()"  href="#latest" class="magenta" rel="facebox" >here</a> to watch the latest ones!<br><br>works for all platforms: <span class="version">(version 2.03.17)</span><br />Windows, Linux, Mac<br /></p><br /><p style="colour:red;">Please make sure you have <a href="http://get.adobe.com/flashplayer/" target="_blank">Flash Player 10</a> installed. </p><a class="buttonsignout" id="facebook" href="#"><img src="./img/button_commit.png"></a>';

?>
