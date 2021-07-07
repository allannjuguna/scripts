#! /usr/bin/python3
import sys
import requests
import lxml.html as parser
import os
import subprocess
from urllib.parse import unquote

session=requests.Session()
red='\033[91m'
green='\033[92m'
blue='\033[94m'
yellow='\033[93m'
white='\033[0m'
arguments=sys.argv
scriptname=arguments[0]

def getcookie(url):
	url=(url.split('/'))
	rooturl=f'{url[0]}//{url[2]}'
	response=session.get(rooturl)
	cookie=response.headers.get("Set-Cookie","null")
	return (cookie)



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
	global session
	response=session.get(link,headers=custom_headers)
	value=response.content
	return value

def checklisting(url,content):
	if 'Index of'.lower() in content.lower():
		print(f'\n\n\n{yellow}[+] Directory listing found in {url} ... {green}passed{white}')
		return "passed"
	else:
		print(f'\t\t\t{red}[-] No Directory listing in {yellow}{url} ... {red}failed{white}')
		return "failed"



def iterate(checkurl):
	global main
	content,headers,status,value=getpage(checkurl,{})
	result=checklisting(checkurl,content)
	if (result == 'passed'): #The file has Directory listing
		try:
			root=parser.fromstring(content)
			values=root.xpath('//td/a/@href')
			parent=values[0]
			parentdir=values[0]
			values.remove(values[0])
			print(f'\n\n\t\t{white}[*] PARENTDIR {green}: {parentdir} {white} LOCATION : {yellow}{main[:-1]}  => {parentdir}{white} ...\n\n')
			# print(f'\n\n\t\t{white}[*] PARENTDIR {green}: {".".join(values)} ...\n\n')
			folders=[]
			files=[]
			for file in values:
				if (file[-1] != '/'):
					files.append(file)
				else:
					folders.append(file)

			for folder in folders:
				itemlocation=f'{checkurl}{folder}'
				localfolderpath=(f'{pwd}{itemlocation.replace(main,"")}')
				print(f'\n\n\t\t{white}[*] FOLDER {yellow}: {folder} {white} at {green}{itemlocation}{white} ...')
				mkdir=f'mkdir {localfolderpath}'
				cd=f'cd {localfolderpath}'

				os.system(mkdir)
				os.system(cd)
				iterate(itemlocation)
			
			for file in files:
				try:
					itemlocation=f'{checkurl}{file}'
					localfilepath=f'{pwd}{itemlocation.replace(main,"")}'
					print(f'\t\t{white}[*] FILE {green}: {file} {white} at {yellow}{itemlocation}{white} ...')
					filecontent=downloadfile(itemlocation)
					filehand=open(localfilepath,'wb')
					filehand.write(filecontent)
					filehand.close()
					print(f'\t\t{blue}[+] Written file to :  {localfilepath} ...')

				except:
					print(f'\t\t{red}[-] Failed to write to :  {localfilepath} ...')
					

		except:
			pass
	else:
		pass




if (len(arguments) > 1):	
	main=arguments[1]
	print(f'{green}[*] Starting ...')
	download='true'
	try:
		pwd="/tmp/results/"
		os.mkdir(pwd)
		print(f'{green}[+] Output directory created at {pwd}{white}')
	except:
		print(f'{red}[-] Failed to create output Directory {pwd}.Make sure /tmp/results does not exist and /tmp is writable {white}')
		exit()
	cookie=(getcookie(main))
	headerpath=arguments[1].split('/')[-2]
	custom_headers={"Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8","Connection" : "keep-alive","Host" : f'xxxxxxx.com', "User-Agent" : "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:87.0) Gecko/20100101 Firefox/87.0","Cookie":cookie}

	print(f'{green}[*] Using custom_headers \n {blue}{custom_headers} ...')
	iterate(main)


else:
	print(f"\n\n\n{blue}Usage{white}\t\t:\tpython3 {scriptname} url/")
	print(f"     \t\t:\tpython3 {scriptname} http://localhost/folderwithdirlisting/")
	print(f"     \t\t:\tpython3 {scriptname} http://localhost/tests/")
	exit()



