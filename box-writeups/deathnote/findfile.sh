#! /bin/bash

filename="user.txt"
echo "Searching for $filename"
echo "======================="
echo ""
for line in $(strings dirpaths.txt | sed s/" "/""/g|sed s/$/"$filename"/g);do
	echo -e -n "[-] $line => " ;curl -sk -I -X GET $line | head -1
done
