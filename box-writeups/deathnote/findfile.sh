#! /bin/bash
#  @author: ransomhare🐰
#  @date: 2022-4-10
#  @description: This script tries to find specific files in the wordpress deathnote box

filename="admin.php"
filename="user.txt"
echo "Searching for $filename"
echo "======================="
echo ""
for line in $(strings dirpaths.txt | sed s/" "/""/g|sed s/$/"$filename"/g);do
	echo -e -n "[-] $line => " ;curl -sk -I -X GET $line | head -1
done
