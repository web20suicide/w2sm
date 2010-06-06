<?php
require_once('settings.php');
mysql_connect($host,$user,$password) or die(mysql_error());
mysql_select_db($db) or die(mysql_error());

echo $NumberOfResults = mysql_num_rows(mysql_query("SELECT * FROM users"));
?>
