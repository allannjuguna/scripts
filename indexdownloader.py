#! /usr/bin/python3
import sys
import requests
import lxml.html as parser
session=requests.Session()
arguments=sys.argv
scriptname=arguments[0]

red='\033[91m'
green='\033[92m'
blue='\033[94m'
yellow='\033[93m'
white='\033[0m'




def getpage(url,headers):
	response=session.get(url,headers=headers)
	content=response.text
	headers=response.headers
	status=response.status_code
	return content,headers,status


def checklisting(url,content):
	if 'Index of'.lower() in content.lower():
		print(f'\n\n\n{yellow}[+] Directory listing found in {url} ... {green}passed{white}')
		return "passed"
	else:
		print(f'\t\t\t{red}[-] No Directory listing in {yellow}{url} ... {red}failed{white}')
		return "failed"


def iterate(url):
	content,headers,status=getpage(url,{})
	result=checklisting(url,content)

	if (result == 'passed'): #The file has Directory listing
		try:
			root=parser.fromstring(content)
			values=root.xpath('//td/a/@href')
			parentdir=values[0]
			values.remove(values[0])
			print(f'\n\n\t\t{white}[*] PARENTDIR {green}: {parentdir} {white} LOCATION : {yellow}{url[:-1]}{parentdir}{white} ...\n\n')
			folders=[]
			files=[]
			for file in values:
				if (file[-1] != '/'):
					files.append(file)
				else:
					folders.append(file)
			for file in files:
				print(f'\t\t{white}[*] FILE {green}: {file} {white} LOCATION : {yellow}{url}{file} ({status}) {white} ...')
			for folder in folders:
				print(f'\n\n\t\t{white}[*] FOLDER {yellow}: {folder} {white} LOCATION : {green}{url}{folder}{white} ...')
				newurl=f'{url}{folder}'
				print(newurl)
				iterate(newurl)
		except:
			pass
	else:
		pass

if (len(arguments) > 1):
	url=arguments[1]
	iterate(url)




else:
	print(f"\n\n\n{blue}Usage{white}\t\t:\tpython3 {scriptname} url/")
	print(f"     \t\t:\tpython3 {scriptname} http://localhost/folderwithdirlisting/")