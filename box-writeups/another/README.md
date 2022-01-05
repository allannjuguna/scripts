#  box writeup


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

## Bruteforcing directories
```
python3.7 dirsearch.py -u http://192.168.50.55/ -r

  _|. _ _  _  _  _ _|_    v0.4.2
 (_||| _) (/_(_|| (_| )

Extensions: php, aspx, jsp, html, js | HTTP method: GET | Threads: 30 | Wordlist size: 10903

Output File: /media/xubzero/STUFF/mytools/dirsearch/reports/192.168.50.55/-_22-01-04_13-14-30.txt

Error Log: /media/xubzero/STUFF/mytools/dirsearch/logs/errors-22-01-04_13-14-30.log

Target: http://192.168.50.55/

[13:14:30] Starting: 
[13:14:31] 403 -  278B  - /.ht_wsr.txt
[13:14:31] 403 -  278B  - /.htaccess.orig
[13:14:31] 403 -  278B  - /.htaccess.save
[13:14:31] 403 -  278B  - /.htaccess_extra
[13:14:31] 403 -  278B  - /.htaccessOLD
[13:14:31] 403 -  278B  - /.htaccess.sample
[13:14:31] 403 -  278B  - /.htaccessBAK
[13:14:31] 403 -  278B  - /.htaccess_orig
[13:14:31] 403 -  278B  - /.htaccess_sc
[13:14:31] 403 -  278B  - /.htm
[13:14:31] 403 -  278B  - /.html
[13:14:31] 403 -  278B  - /.htpasswd_test
[13:14:31] 403 -  278B  - /.htpasswds
[13:14:31] 403 -  278B  - /.httr-oauth
[13:14:32] 403 -  278B  - /.php
[13:14:33] 403 -  278B  - /.htaccess.bak1
[13:14:33] 403 -  278B  - /.htaccessOLD2
[13:14:41] 200 -   10KB - /index.html
[13:14:45] 200 -   12B  - /robots.txt
[13:14:45] 200 -    4B  - /secret/     (Added to queue)
[13:14:45] 301 -  315B  - /secret  ->  http://192.168.50.55/secret/
[13:14:45] 403 -  278B  - /server-status
[13:14:45] 403 -  278B  - /server-status/     (Added to queue)
[13:14:49] Starting: secret/
[13:14:50] 403 -  278B  - /secret/.ht_wsr.txt
[13:14:50] 403 -  278B  - /secret/.htaccess.bak1
[13:14:50] 403 -  278B  - /secret/.htaccess.sample
[13:14:50] 403 -  278B  - /secret/.htaccess.orig
[13:14:50] 403 -  278B  - /secret/.htaccess_extra
[13:14:50] 403 -  278B  - /secret/.htaccess_orig
[13:14:50] 403 -  278B  - /secret/.htaccess.save
[13:14:50] 403 -  278B  - /secret/.htaccess_sc
[13:14:50] 403 -  278B  - /secret/.htaccessBAK
[13:14:50] 403 -  278B  - /secret/.htaccessOLD
[13:14:50] 403 -  278B  - /secret/.htaccessOLD2
[13:14:50] 403 -  278B  - /secret/.htm
[13:14:50] 403 -  278B  - /secret/.html
[13:14:50] 403 -  278B  - /secret/.htpasswds
[13:14:50] 403 -  278B  - /secret/.htpasswd_test
[13:14:50] 403 -  278B  - /secret/.httr-oauth
[13:14:51] 403 -  278B  - /secret/.php
[13:15:01] 200 -    4B  - /secret/index.html
[13:15:07] Starting: server-status/
[13:15:07] 404 -  275B  - /server-status/%2e%2e//google.com



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

