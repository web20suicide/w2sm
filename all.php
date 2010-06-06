<?php
require_once('settings.php');
mysql_connect($host,$user,$password) or die(mysql_error());
mysql_select_db($db) or die(mysql_error());

$query = "SELECT friends FROM users";
$result = mysql_query($query);

$i = 0;
while($row = mysql_fetch_assoc($result)){
	$i += $row['friends']; 
}
echo number_format($i);
?>
