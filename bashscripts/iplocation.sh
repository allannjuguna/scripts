#! /bin/bash
arguments=${#}


if [ $arguments -eq 1 ]
then
	curl -X POST -d "ip=`echo $1`" -H "Accept: */*" -H "Connection: keep-alive" -H "User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:90.0) Gecko/20100101 Firefox/90.0" -H "X-Requested-With" https://iplocation.com/
else
	echo "Usage : ${0} x.x.x.x"
	echo "      : ${0} 172.217.170.206"
fi



