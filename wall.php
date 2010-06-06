<?php
$query = "";
$result = "";
$row = "";
$page = "";
$size = "";

require_once('settings.php');
mysql_connect($host,$user,$password) or die(mysql_error());
mysql_select_db($db) or die(mysql_error());

$page=$_REQUEST['page']; //Get the page number to show
if($page == "") $page=1; //If no page number is set, the default page is 1 

$NumberOfResults = mysql_num_rows(mysql_query("SELECT * FROM users"));
$Limit = 4; //Number of results per page
$NumberOfPages=ceil($NumberOfResults/$Limit); 

$query = "SELECT * FROM users ORDER BY friends DESC LIMIT ".(intval($page)-1)*$Limit . ",$Limit";
$result = mysql_query($query);

echo "<h1>Who's Who of Social Suiciders</h1>";

while($row = mysql_fetch_assoc($result)){
	$size = getimagesize("./profiles/img/".$row['picture']);
	$img_size = $size['3'];
	$div_size = $size['1'] + 50;
	echo "<div id='wall_entry' style='height:".$div_size."px;'><div id='deathcross'><img src='./img/deathcross.png'></div>";
	echo "<div id='wall_details'><h1>".$row['username']."</h1><br />";
  echo "<p class='testimonialsquestion'>committed Web2.0 suicide on:<br /></p><p class='testimonialsanswer'>".$row['t_create']."</p>";
	echo "<p class='testimonialsquestion'>lost friends:</p><p class='testimonialsanswer'>".$row['friends']."</p>";
	echo "<p class='testimonialsquestion'>last words:</p><p class='testimonialsanswer'>".$row['lastwords']."</p></div>";
	echo "<div id='logo_overlay'><img src='./img/small_".$row['command'].".png'></div>";
	echo "<div id='wall_picture'><div style='padding:0px 10px 10px 0px;height:".$size['1'].";width:".$size['0'].";background:url(./img/drop_border.png) no-repeat bottom right;'> <img ".$img_size."src='../profiles/img/". $row['picture']."'></div></div>";
  echo "<div id='fakehr'><hr></div></div></div>";
}

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
?>
