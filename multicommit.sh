#! /bin/bash
TIMEOUT=60
FILENAME="README.md"
while true;do
	echo "" >> $FILENAME
	sh autocommit.sh
	sleep $TIMEOUT

done
