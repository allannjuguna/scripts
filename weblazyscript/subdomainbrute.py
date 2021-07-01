#! /usr/bin/python3
import pyfiglet as figlet
import sys
import os
import re
import requests
import base64
session=requests.Session()


white='\033[0m'
red='\033[91m'
green='\033[92m'
yellow='\033[93m'
blue='\033[94m'
success=f'{green} [ OK ] '
fail=f'{red} [ FAIL ] '
stage=f'{blue} [#] '
alert=f'{yellow} [!] '
end=f'{white}'
arguments=sys.argv
url=arguments[1]
wordlist=arguments[2]
protocol=arguments[3]
custom_headers={}

def getpage(url,customheaders):
	try:
		response=session.get(url,headers=customheaders,timeout=2)
		headers=response.headers
		content=response.text
		status=response.status_code
		return content,(headers),status
	except:
		return "norhing",{},404

final=[]
others=[]
with open(wordlist,'r') as myfile:
	contents=(myfile.read()).split('\n')
	for subdomain in contents:
		subdomain=subdomain.strip()
		link=(f"{protocol}://{subdomain}.{url}")
		try:
			resp=getpage(link,{})
			status_code=resp[2]
			if int(status_code) == 200:
				print(f"{success}{link} {status_code}")
				final.append(link)
			elif int(status_code) != 404:
				print(f"{alert}{link} {status_code}{end}")
				others.append(link)
			else:
				print(f"{fail}{link} {status_code}")
				pass
		except:
			print(f"{fail} {link}{end}")


print(f"\n\n\n{success}{final}")
print(f"{alert}{others}")


