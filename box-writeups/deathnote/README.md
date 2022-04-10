#  box writeup


## Machine Configuration
```
IP:192.168.88.53
```

## Credentials for debugging network connectivity
```

```


## Ports open
```
nmap -T4 --max-retries 1 -Pn -p- -sV --script=vuln $x -v

Starting Nmap 7.60 ( https://nmap.org ) at 2022-04-03 11:06 EAT
NSE: Loaded 142 scripts for scanning.
NSE: Script Pre-scanning.
Initiating NSE at 11:06
Completed NSE at 11:06, 10.00s elapsed
Initiating NSE at 11:06
Completed NSE at 11:06, 0.00s elapsed
Initiating Parallel DNS resolution of 1 host. at 11:06
Completed Parallel DNS resolution of 1 host. at 11:06, 13.00s elapsed
Initiating Connect Scan at 11:06
Scanning 192.168.88.53 [65535 ports]
Discovered open port 22/tcp on 192.168.88.53
Discovered open port 80/tcp on 192.168.88.53
Completed Connect Scan at 11:06, 2.36s elapsed (65535 total ports)
Initiating Service scan at 11:06
Scanning 2 services on 192.168.88.53
Completed Service scan at 11:06, 6.03s elapsed (2 services on 1 host)
NSE: Script scanning 192.168.88.53.
Initiating NSE at 11:06
NSE: [firewall-bypass] lacks privileges.
NSE: [tls-ticketbleed] Not running due to lack of privileges.
Completed NSE at 11:07, 23.82s elapsed
Initiating NSE at 11:07
Completed NSE at 11:07, 0.12s elapsed
Nmap scan report for 192.168.88.53
Host is up (0.0077s latency).
Not shown: 65533 closed ports
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.9p1 Debian 10+deb10u2 (protocol 2.0)
80/tcp open  http    Apache httpd 2.4.38 ((Debian))
|_http-csrf: Couldn't find any CSRF vulnerabilities.
|_http-dombased-xss: Couldn't find any DOM based XSS.
| http-enum: 
|   /wordpress/: Blog
|   /robots.txt: Robots file
|   /wordpress/wp-login.php: Wordpress login page.
|_  /manual/: Potentially interesting folder
|_http-server-header: Apache/2.4.38 (Debian)
|_http-stored-xss: Couldn't find any stored XSS vulnerabilities.
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

NSE: Script Post-scanning.
Initiating NSE at 11:07
Completed NSE at 11:07, 0.00s elapsed
Initiating NSE at 11:07
Completed NSE at 11:07, 0.00s elapsed
Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 73.04 seconds


```

## WP Users
```
[{"id":1,"name":"kira","url":"http:\/\/deathnote.vuln\/wordpress","description":"","link":"http:\/\/deathnote.vuln\/wordpress\/index.php\/author\/kira\/","slug":"kira","avatar_urls":{"24":"http:\/\/1.gravatar.com\/avatar\/1019994ac6a06c163a21d4109310712b?s=24&d=mm&r=g","48":"http:\/\/1.gravatar.com\/avatar\/1019994ac6a06c163a21d4109310712b?s=48&d=mm&r=g","96":"http:\/\/1.gravatar.com\/avatar\/1019994ac6a06c163a21d4109310712b?s=96&d=mm&r=g"},"meta":[],"_links":{"self":[{"href":"http:\/\/deathnote.vuln\/wordpress\/index.php\/wp-json\/wp\/v2\/users\/1"}],"collection":[{"href":"http:\/\/deathnote.vuln\/wordpress\/index.php\/wp-json\/wp\/v2\/users"}]}}]
```
## Nikto
```
nikto -h http://deathnote.vuln
- Nikto v2.1.5
---------------------------------------------------------------------------
+ Target IP:          192.168.88.53
+ Target Hostname:    deathnote.vuln
+ Target Port:        80
+ Start Time:         2022-04-03 11:36:21 (GMT3)
---------------------------------------------------------------------------
+ Server: Apache/2.4.38 (Debian)
+ Server leaks inodes via ETags, header found with file /, fields: 0xc5 0x5cb285991624e 
+ The anti-clickjacking X-Frame-Options header is not present.
+ No CGI Directories found (use '-C all' to force check all possible dirs)
+ "robots.txt" retrieved but it does not contain any 'disallow' entries (which is odd).
+ Allowed HTTP Methods: GET, POST, OPTIONS, HEAD 
+ OSVDB-3092: /manual/: Web server manual found.
+ OSVDB-3268: /manual/images/: Directory indexing found.
+ OSVDB-3233: /icons/README: Apache default file found.
+ Uncommon header 'link' found, with contents: <http://deathnote.vuln/wordpress/index.php/wp-json/>; rel="https://api.w.org/"
+ /wordpress/: A Wordpress installation was found.
+ 6544 items checked: 0 error(s) and 9 item(s) reported on remote host

```

## Bruteforcing directories
```
ffuf -c -r -w /usr/share/dirb/wordlists/common.txt -u http://deathnote.vuln/FUZZ

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v1.3.1-dev
________________________________________________

 :: Method           : GET
 :: URL              : http://deathnote.vuln/FUZZ
 :: Wordlist         : FUZZ: /usr/share/dirb/wordlists/common.txt
 :: Follow redirects : true
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200,204,301,302,307,401,403,405
________________________________________________

.hta                    [Status: 403, Size: 279, Words: 20, Lines: 10, Duration: 3ms]
                        [Status: 200, Size: 197, Words: 23, Lines: 10, Duration: 4ms]
.htaccess               [Status: 403, Size: 279, Words: 20, Lines: 10, Duration: 5ms]
.htpasswd               [Status: 403, Size: 279, Words: 20, Lines: 10, Duration: 7ms]
index.html              [Status: 200, Size: 197, Words: 23, Lines: 10, Duration: 6ms]
manual                  [Status: 200, Size: 626, Words: 14, Lines: 13, Duration: 6ms]
robots.txt              [Status: 200, Size: 68, Words: 11, Lines: 5, Duration: 6ms]
server-status           [Status: 403, Size: 279, Words: 20, Lines: 10, Duration: 6ms]
wordpress               [Status: 200, Size: 17961, Words: 583, Lines: 144, Duration: 60ms]
:: Progress: [4614/4614] :: Job [1/1] :: 5228 req/sec :: Duration: [0:00:03] :: Errors: 0 ::

```

## Hints
```
i am Soichiro Yagami, light's father
i have a doubt if L is true about the assumption that light is kira
i can only help you by giving something important
login username : user.txt
i don't know the password.
find it by yourself 
but i think it is in the hint section of site

iamjustic3

```

## Fuzzing php files
```

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

