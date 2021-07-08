#! /usr/bin/python3
import requests
import sys
import os
import pyfiglet as figlet
session=requests.Session()
arguments=sys.argv
scriptname="LAZYSCRIPT" 			#arguments[0].replace("./","")
white='\033[0m'


def banner():
	yellow='\033[093m'
	green='\033[091m'
	print(f"{yellow}{figlet.Figlet(font='shimrod').renderText(f'{scriptname}')}")
	string=f"{yellow}\n\tUsage\t:\tpython3 {arguments[0]} http://urlhere /    (For the root path)\n{yellow}\t     \t:\tpython3 {arguments[0]} http://urlhere /somefolder/    (For custom folder){white}\n"
	print(string)



try:
	#Website details that we need
	host=sys.argv[1] #Enter http+ip Dont enter the path
	path=sys.argv[2] #Enter the path ending and starting with a front slash
except:
	banner()
	exit(-1)

bold='\033[1m'
failed=red='\033[91m'
# green='\033[32m'
success=yellow=bold+'\033[92m'
green=blue='\033[093m'
checking='\033[94m'
summary=[]

commonpages=['admin','index.php','assets','admin.php','main.py','app.py','login.php','register.php','admin/','includes/','storage/logs/','logs','api','api/','phpmyadmin','public/']
challengename='' # For writing the output to a file
phpsession=''
# custom_headers={"Cookie":f'PHPSESSID={phpsession}'}
custom_headers={"Cookie":f'_ga=GA1.3.1698812970.1617878897; ssupp.vid=viIR7-p1HnBex; ssupp.visits=4; XSRF-TOKEN=eyJpdiI6IlZ6M0tlTThJWGNlQk1CVk94cUJDOEE9PSIsInZhbHVlIjoiYWZ1b3JucFVUM3BqcDVNcFBlSHRiNkVCZEJoSVBGVzN0YnE2N1Y0YS90Y01NblcxYXo0NjdCcWZ0Qy9kSWcvZk9FS2t3bDJqZHhjblVHTE5yRnY0S3krd04rblpBYWJzT3N6L0FvUUZ3YWxMU01KUnRoUFY1OGhWbGlOVDV1cm4iLCJtYWMiOiI1NzBlNDFjNmQ2ZjZiMmZkY2ZkMjJjYzU1ZmM0ZGYzY2M0MWI1NDU0YTY0NmVhMGMzMzViNWE1MmRiNDBlMGExIn0%3D; zalego_session=eyJpdiI6InEvRXN2Yk9VeFVYUUErNGZsdWROOVE9PSIsInZhbHVlIjoiZzY0L3paRThuWTZzODA4c0gvWGRrY3NEWlF2T2dESEVzZkVnVzVFdnVVTCs1dm04NkJxZ1czVEpHQ3ZyejVzSWh4clBHamM1SXpkWDBrazNYUDV1dWc4RXNNM2hyR0k1K1p1TGRLTy85SlhVSlFvM1dOYVBteXhmNjJsaW1UQXMiLCJtYWMiOiI4OGNmZjEyMzZhMzI4MjA0MzJiMmYzMTFhMTdiZmI4ODIwMmQ3MjAyMDNjNWIyOTM5MDlmY2MxMmI4OWFmNGE3In0%3D; _gid=GA1.3.994024796.1618173378'}
server=''
cookie=''
banner()	



folder=host[8:].split('.')[0]
print(f'\n\n{green}[*] Creating output file at {folder} {white}... ')
try:
	os.system(f'cd output && mkdir {folder}')
	print(f'\n\t[+] {success}Created folder {folder.encode()} {white}... ')

except:
	pass


folder="output/"+folder
known_headers=['location','expires','cache-control','pragma','etag','content-encoding','content-type','date', 'server', 'vary', 'accept-ranges', 'connection', 'transfer-encoding', 'content-language','keep-alive','last-modified','content-length','e-tag','accept']
#Making the headers readable
def cleanheaders(headers):
	global cookie,server
	print('HEADERS\n')
	for item in headers:
		if item.lower() == 'set-cookie':
			cookie+=headers.get(item)+','
		elif item.lower() == 'server':
			server=headers.get(item)
		else:
			check=(item.lower()).strip()
			if check not in known_headers:
				printme=(f'{success} [+] Unknown header {blue}{check} : {headers.get(item)}{success} found{white}\n')
				summary.append(printme)
			else:
				pass
		print(f'\t{checking}'+item + ' : '+headers.get(item))


#For performing get requests
def getpage(url,headers):
	global custom_headers
	print(f'\t{green}[+] Getting : {url}{white}\n')
	if (len(custom_headers) == 0):
		response=session.get(url)
	else:
		response=session.get(url,headers=custom_headers,allow_redirects=False)
	
	return response.text,response.headers,response.status_code

#Printing the headers and the page content in an organised manner
def show(headers,content):
	print(f'{cleanheaders(headers)}\n\n\n{blue}[*] CONTENT{white}\n{content}\n\n\n')




#Reading the robots.txt file
def checkrobots():
	global host
	robots_file=host+'/robots.txt'
	print(f'{green}[*] Reading Robots.txt file at {robots_file} ...{white}\n') 
	content,headers,status=getpage(robots_file,'')
	if 'not found' in content.lower():
		printme=(f'{failed} [-] The flag might not be in the robots.txt : {robots_file} {white}{failed} ({status}){white}\n')
		show(headers,content)
	else:
		printme=(f'{success} [+] The flag might be in robots.txt {robots_file} ({status})\n')
		show(headers,content)
	print(printme)
	summary.append(printme)

def checkserver():
	global host
	print(f'{green}[*] Checking which server the website is running on ...{white}\n')
	content,headers,status=getpage(host+path,'')
	for header in headers:
		header=header.lower()
		if header == 'server':
			value=headers.get(header,'Not found')
			server=value
			if 'werkzeug' in server.lower() or 'python' in server.lower() or 'jinja' in server.lower():
				printme=(f'{success} [+] The website is running on the werkzeug server : {server}.Try exploiting using the {server} {red} console exploit {white} \n')
			else:
				printme=(f'The website server : {yellow} {server} {white} \n')
			print(printme)
			summary.append(printme)
		else:
			pass


def checksitemap():
	global host
	sitemap_file=host+'/sitemap.xml'
	print(f'{green}[*] Reading Sitemap.xml file at {sitemap_file} ...{white}\n') 
	content,headers,status=getpage(sitemap_file,'')
	if 'not found' in content.lower():
		show(headers,content)
		printme=(f'{failed} [-] The flag might not be in the sitemap.xml : {sitemap_file} {white}{failed} ({status}){white}\n')
	else:
		printme=(f'{success} [+] The flag might be in sitemap.xml {sitemap_file} ({status})\n')
	print(printme)
	summary.append(printme)

def checkcookies():
	printme=(f'{success} [*] PLEASE CHECK COOKIES MANUALLY {white}\n\n')
	print(printme)
	summary.append(printme)

def checkgit():
	global host
	gitlocation='/.git/HEAD'
	gitfile=host+f'{gitlocation}'
	# gitfile=host+path+f'{gitlocation}'
	print(f'{green}[*] Reading gitfile(without path) file at {gitfile} ...{white}\n') 
	content,headers,status=getpage(gitfile,'')
	if str(status) == '404' or str(status) == '406' or 'not found' in content.lower():
		show(headers,content)
		printme=(f'{failed} [-] Git file is not exposed in the root folder : {gitfile} {white}{failed} ({status}){white}\n')
	elif 'not found' in content.lower():
		show(headers,content)
		printme=(f'{failed} [-] The flag might not be in the gitfile: {gitfile} {white}{failed} ({status}){white}\n')
	else:
		printme=(f'{success} [+] Git files may be exposed at {blue}{gitfile}{success} ({status}) ,check for {failed}sensitive info disclosure{success}.You may need to use gittools for this{white}\n')
	print(printme)
	summary.append(printme)


def checkgitpath():
	global host
	gitlocation='.git/HEAD'
	gitfile=host+path+f'{gitlocation}'
	print(f'{green}[*] Reading gitfile(with path) file at {gitfile} ...{white}\n') 
	content,headers,status=getpage(gitfile,'')
	if str(status) == '404' or str(status) == '406' or 'not found' in content.lower():
		show(headers,content)
		printme=(f'{failed} [-] Git file is not exposed in path: {gitfile} {white}{failed} ({status}){white}\n')
	else:
		printme=(f'{success} [+] Git files may be exposed at {blue}{gitfile}{success} ({status}) ,check for {failed}sensitive info disclosure{success}.You may need to use gittools for this{white}\n')
	print(printme)
	summary.append(printme)


def checkmaincookie():
	global host
	target=host+f'/public/'
	print(f'{checking}[*] Getting the main cookie at {target} ...{white}\n') 
	content,headers,status=getpage(target,'')
	print(headers)
	# if str(status) == '404' or str(status) == '406' or 'not found' in content.lower():
	# 	printme=''
	# else:
		# printme=(f'{success} [+] Check the source code of : {blue}{target}{success} for leads ({status}).{white}\n')
	# print(printme)
	# summary.append(printme)]




def checkcommonpages():
	global commonpages
	global host
	for page in commonpages:
		target=host+f'{path}{page}'
		print(f'{checking}[*] Reading common file {target} file at {target} ...{white}\n') 
		content,headers,status=getpage(target,'')
		if str(status) == '404' or str(status) == '406' or 'not found' in content.lower():
			printme=''
		elif 'not found' in content.lower():
			printme=''
		else:
			if 'public' in page.lower():
				checkdevfilespublic()
			else:
				printme=(f'{success} [+] Interesting page found.Check the link at : {blue}{target}{success} for leads ({status}).{white}\n')
		print(printme)
		summary.append(printme)


def checkdevfiles():
	print(f'{checking}[*] Checking for exposed development files ...{white}\n') 
	devfiles=[".gitignore",'.env','env.swp','wp-content','.gitattributes',"artisan","composer.json","composer.lock",".editorconfig",".env",".env.example",".gitattributes",".gitignore","package.json","phpunit.xml","readme.md","server.php",".styleci.yml","webpack.mix.js","node_modules","vendor",".env.backup",".phpunit.result.cache","Homestead.json","Homestead.yaml","npm-debug.log","yarn-error.log","error_log","public/hot","public/storage","storage/key"]
	global host
	commonpages=devfiles
	for page in commonpages:
		target=host+f'{path}{page}'
		content,headers,status=getpage(target,'')
		print(f'\t\t{white}[*] Reading development file {target} file at {target} ({status}) ...{white}\n') 
		if str(status) == '404' or 'not found' in content.lower():
			printme=''
		elif ('not found' in content.lower()):
			printme=''
		else:
			filename=folder+f'/{page}'
			try:
				file=open(filename,'w')
				file.write(content)
				print(f'\t\t[+] Written to {filename}')
			except:
				pass
			printme=(f'{success} [+] Developer file found at : {blue}{target}{success}  ,check for {failed}sensitive info disclosure{success} ({status}).{white}\n')
		print(printme)
		summary.append(printme)



def checkdevfilespublic():
	print(f'{checking}[*] Checking for exposed development files in public ...{white}\n') 
	devfiles=[".gitignore",'.gitattributes',"artisan","composer.json","composer.lock",".editorconfig",".env",".env.example",".gitattributes",".gitignore","package.json","phpunit.xml","readme.md","server.php",".styleci.yml","webpack.mix.js","node_modules","vendor",".env.backup",".phpunit.result.cache","Homestead.json","Homestead.yaml","npm-debug.log","yarn-error.log","error_log","hot","storage","key"]
	global host
	commonpages=devfiles
	for page in commonpages:
		target=host+f'/public/{page}'
		print(f'\t\t{white}[*] Reading development file {target} file at {target} ...{white}\n') 
		content,headers,status=getpage(target,'')
		if str(status) == '404' or str(status) == '406':
			printme=''
		elif ('not found' in content.lower()):
			printme=''
		else:
			printme=(f'{success} [+] Developer file found at : {blue}{target}{success}  ,check for {failed}sensitive info disclosure{success} ({status}).{white}\n')
		print(printme)
		summary.append(printme)


#Checking files in suspicious folders(UNFINISHED)
folders='inc includes hint secret flag js css app api'.split(' ')
def checkfolders():
 pass

#Reading file source code of main files eg. index.php,index.html,index,js
def readsource(custom_headers):
	global host
	print(f'{blue}[*] Reading main file at {host+path} {white}...\n') 
	content,headers,status=getpage(host+path,custom_headers)
	show(headers,content)

#Reading file by filename
def readfile(filename,custom_headers):
	print(f'[*] Reading {filename} ...\n') 
	content,headers,status=getpage(filename,custom_headers)
	show(headers,content)





# checkmaincookie()

#Checking which server the website is using
checkserver()


#Checking for git files in the root folder
checkgit()

#Checking for git files in the path
checkgitpath()

#Checking robots.txt file
checkrobots()

#Checking for a sitemap file
checksitemap()

#Checking for famous pages
checkcommonpages()

#Checking for development and configuration files
checkdevfiles()



#Reading page source of the main file(index files)
readsource('')

#Checking for cookies
checkcookies()




print(f'\nHOST : {blue}{host}{white}\nPATH : {blue}{path}{white}\nSERVER : {blue}{server}{white}\nCOOKIE : {blue}{cookie}{white}\nPHPSESSION : {blue}{phpsession}{white}')


print(f'\n\n{green}SUMMARY{white}\n'+''.join(summary))





# NOT NECESSARY FOR NOW
# #Checking for development and configuration files
# checkdevfilespublic()


#Reading a file on the server by filename
# readfile(f'{host}/login.php','')