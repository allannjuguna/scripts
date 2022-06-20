#  box writeup


## Ports open
```
Simple scan 

Starting Nmap 7.80 ( https://nmap.org ) at 2022-06-14 16:43 EAT
Nmap scan report for 10.0.0.129
Host is up (0.38s latency).
Not shown: 994 filtered ports
PORT     STATE  SERVICE
21/tcp   open   ftp
22/tcp   closed ssh
80/tcp   open   http
443/tcp  open   https
7070/tcp closed realserver
8084/tcp closed unknown



nmap -sV -sT -sC

Starting Nmap 7.80 ( https://nmap.org ) at 2022-06-14 16:47 EAT
Nmap scan report for 10.0.0.129
Host is up (0.38s latency).
Not shown: 994 filtered ports
PORT     STATE  SERVICE    VERSION
21/tcp   open   ftp        vsftpd 3.0.3
22/tcp   closed ssh
80/tcp   open   http       Apache httpd 2.4.29 ((Ubuntu))
|_http-server-header: Apache/2.4.29 (Ubuntu)
|_http-title: Apache2 Ubuntu Default Page: It works
443/tcp  open   ssl/https  Apache/2.4.29 (Ubuntu)
|_http-server-header: Apache/2.4.29 (Ubuntu)
|_http-title: Apache2 Ubuntu Default Page: It works
7070/tcp closed realserver
8084/tcp closed unknown
Service Info: OS: Unix

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 189.75 seconds


Completed NSE at 16:58, 2.09s elapsed
NSE: Starting runlevel 2 (of 2) scan.
Initiating NSE at 16:58
Completed NSE at 16:58, 2.11s elapsed
Nmap scan report for venom (10.0.0.129)
Host is up, received user-set (0.0010s latency).
Scanned at 2022-06-14 16:55:24 EAT for 171s
Not shown: 65529 filtered ports
Reason: 65371 no-responses and 158 host-unreaches
PORT     STATE  SERVICE    REASON       VERSION
21/tcp   open   ftp        syn-ack      vsftpd 3.0.3
22/tcp   closed ssh        conn-refused
80/tcp   open   http       syn-ack      Apache httpd 2.4.29 ((Ubuntu))
443/tcp  open   ssl/https  syn-ack      Apache/2.4.29 (Ubuntu)
7070/tcp closed realserver conn-refused
8084/tcp closed unknown    conn-refused
Service Info: OS: Unix

Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 171.03 seconds


```

## COmments
```
<!...<5f2a66f947fa5690c26506f66bde5c23> follow this to get access on somewhere.....--> 
translates to hostinger
```

### Nikto
```
- Nikto v2.1.5
---------------------------------------------------------------------------
+ Target IP:          10.0.0.129
+ Target Hostname:    venom
+ Target Port:        80
+ Start Time:         2022-06-14 16:59:25 (GMT3)
---------------------------------------------------------------------------
+ Server: Apache/2.4.29 (Ubuntu)
+ Server leaks inodes via ETags, header found with file /, fields: 0x2afc 0x5c2c31c3ee320 
+ The anti-clickjacking X-Frame-Options header is not present.
+ No CGI Directories found (use '-C all' to force check all possible dirs)
+ Allowed HTTP Methods: GET, POST, OPTIONS, HEAD 
+ OSVDB-3233: /icons/README: Apache default file found.
+ 6544 items checked: 0 error(s) and 4 item(s) reported on remote host
+ End Time:           2022-06-14 16:59:32 (GMT3) (7 seconds)
---------------------------------------------------------------------------
+ 1 host(s) tested

```

### ftp
```
Credentials are both hostinger

  ➤ cat hint.txt 
	Hey there... 

T0D0 --

* You need to follow the 'hostinger' on WXpOU2FHSnRVbWhqYlZGblpHMXNibHBYTld4amJWVm5XVEpzZDJGSFZuaz0= also aHR0cHM6Ly9jcnlwdGlpLmNvbS9waXBlcy92aWdlbmVyZS1jaXBoZXI=
* some knowledge of cipher is required to decode the dora password..
* try on venom.box
password -- L7f9l8@J#p%Ue+Q1234 -> deocode this you will get the administrator password 


Have fun .. :)

```

### Logging in
```

E7r9t8@Q#h%Hy+M1234 => dora account
```

## Bruteforcing directories
```


```

## Payload/Exploit
```

```
find / -perm -u=s -type f 2>/dev/null
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

## Priviledge Escalation
```

```