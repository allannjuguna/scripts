#! /usr/bin/python3
import sys
import requests
import lxml.html as parser
import os
import subprocess

arguments=sys.argv
main=url=arguments[1]

session=requests.Session()
red='\033[91m'
green='\033[92m'
blue='\033[94m'
yellow='\033[93m'
white='\033[0m'


def getcookie(url):
	url=(url.split('/'))
	rooturl=f'{url[0]}//{url[2]}'
	response=session.get(rooturl)
	cookie=response.headers.get("Set-Cookie","null")
	return (cookie)

cookie=(getcookie(main))
custom_headers={"Cookie":cookie}

def getpage(url,headers):
	global custom_headers
	response=session.get(url,headers=custom_headers)
	value=response.content
	content=response.text
	headers=response.headers
	status=response.status_code
	return content,headers,status,value


def downloadfile(link):
	global custom_headers
	response=session.get(link,headers=custom_headers)
	value=response.content
	return value


if (cookie != 'null'):
	print(f'\t\t\t{green}[+] Cookie fetched {cookie} ... {green}passed{white}\n\n')
	print(downloadfile(arguments[1]))
	filecontent=(downloadfile(arguments[1]))
	filepath=(url.split('/'))[-1].strip()
	handler=open(filepath,'wb')
	handler.write(filecontent)
	handler.close()
	print(f'\t\t\t{green}[+] Written output to file {filepath} ... {green}passed{white}')

else:
	print(f'\t\t\t{red}[-] Cookie value is null ... {red}failed{white}')