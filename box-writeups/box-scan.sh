#! /bin/bash


# @ author 			: yourstruly

# @ description		: This script will fetch the following
#            		   -> scan for open ports
#            		   -> Perform dirsearch on the machine



# Declaring variables
DEPTH="3"
white="\033[0m"
red="\033[91m"
green="\033[92m"
yellow="\033[93m"
end="$white"
success="  [${green}+${white}] $green"
fail="  [${red}-${white}] $red"
warn="[${yellow}!${white}] $yellow"


arguments=${#}

if [[ arguments -lt 1 ]]
then

	echo ""
	echo -e "Usage : box-scan x.x.x.x"
	echo -e "Example : box-scan 192.168.8.1"
	exit
else
	IP=$1
	echo -e "\t\t\t$success Starting Basic Enumeration $white"

	# Performing a simple network scan
	
	echo ""
	echo -e "$warn Starting nmap Scan(Fast Scan) $white"
	nmap $IP
	echo -e "\n=================================================================================="


	# Performing a simple dirsearch scan
	echo ""
	depth=3
	echo -e "$warn Performing Basic Dirsearch (DEPTH : $depth) $white"
	dirsearch="python3.7 /media/xubzero/STUFF/mytools/dirsearch/dirsearch.py"
	$dirsearch -u http://$IP/ -e php,html,txt -f -r --recursion-depth $depth -w /home/xubzero/wordlists/Discovery/Web-Content/common.txt
	echo -e "\n=================================================================================="

	# Performing full network scan
	echo ""
	echo -e "$warn Starting nmap Scan(Best Scan) $white"
	nmap -T4 -Pn -p- --max-retries 1 -sV -sC $IP -v
	echo -e "\n=================================================================================="


fi