#! /usr/bin/python3
# Author 		: xubzero
# Date 			: 22 June 2021
# Version		: 1.0
# Description	: Basic search on php source code to find common vulnerabilities

import pyfiglet as figlet
import sys
import os
import re

arguments=sys.argv

# Define colors
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

def render(string,font):
	return (figlet.Figlet(font=font).renderText(string))

def banner():
	final=''
	string="PHP vulnscan"
	final+=f'{yellow}{render(string,"shimrod")}{end}'
	final+=f'\t\t\t\t{blue}version 1.0{end}\n'
	final+=f"{blue}-------------------------------------------------\n{end}"
	final+=f" {blue}PHP Source Code Security Scanner v1.0{end}\n"
	final+=f" {blue}Author : xubzero{end}\n"
	final+=f" {blue}Description : Find low hanging fruit bugs{end}\n"
	final+=f"{blue}-------------------------------------------------\n{end}"

	print(final)

banner()


def usage():
	final=f"{blue}usage: "
	final+=f"\t{blue}python3 {arguments[0].replace('./','')} filename.php\n"
	final+=f"\t{blue}python3 {arguments[0].replace('./','')} /var/www/html folder\n"
	final+=f"\t{blue}python3 {arguments[0].replace('./','')} /var/www/html recursive\n{end}"
	print(final)


def readfile(filename):
	try:
		with open(filename,'r') as myfile:
			contents=myfile.read()
			actions(filename,contents)
	except:
		print(f"{fail} Unable to read file {yellow}{filename}{end}")	


def xssregex(filename,array,begin):
	if (len(array) > 0):
		for item in array:
			if (len(item) > 0):
				try:
					if "($" not in item:
					# if (item[int(item.index("$"))-1] != "("):
						try:
							item=item.strip()
							result=(f"{begin} {item[:50]}.. in : {green}{filename}")
						except:
							result=(f"{begin} {item}.. in : {green}{filename}")
						if '$_post' in item:
							result+=f" {red}(POST){end}"
						elif '$_get' in item:
							result+=f" {red}(GET){end}"
						elif '$_server' in item:
							result+=f" {red}(SERVER){end}"
						elif '$_session' in item:
							result+=f" {red}(SESSION){end}"
						elif '$_files' in item:
							result+=f" {yellow}(FILES){end}"							

						elif '$_cookie' in item:
							result+=f" {red}(COOKIE){end}"
						else:
							result+=f"{end}"
						print("[XSS] "+result)
						xss.append(result)
					else:
						pass
				except:
					pass



def unvalidatedregex(filename,array,begin):
	if (len(array) > 0):
		for item in array:
			if (len(item) > 0):
				checker=item
				if 'echo' not in checker.lower():
					# if "($" not in item:
					if "($" not in item:
					# if (item[int(item.index("$"))-1] != "("):
						try:
							item=item.strip()
							result=(f"{begin} {item[:50]}.. in : {green}{filename}")
						except:
							result=(f"{begin} {item}.. in : {green}{filename}")
						if '$_post' in item:
							result+=f" {red}(POST){end}"
						elif '$_get' in item:
							result+=f" {red}(GET){end}"
						elif '$_server' in item:
							result+=f" {red}(SERVER){end}"
						elif '$_session' in item:
							result+=f" {red}(SESSION){end}"
						elif '$_files' in item:
							result+=f" {yellow}(FILES){end}"	

						elif '$_cookie' in item:
							result+=f" {red}(COOKIE){end}"
						else:
							result+=f"{end}"
						print("[Unvalidated] "+result)
						unvalidated.append(result)
					else:
						pass
				else:
					pass
def checkxss(filename,contents):
	global xss
	pattern=r"echo.+\$\_[a-zA-Z0-9]+\[.+\]+.*" #strict
	pattern=r"echo.+\$[-_!@#$%^&*()+a-zA-Z0-9]+.*" #even variables
	regex=re.findall(pattern,contents)
	xssregex(filename,regex,f"{blue}\t| {alert}")

def checkunvalidated(filename,contents):
	global unvalidated
	pattern=r".+\$\_[a-zA-Z0-9]+\[.+\]"
	newregex=re.findall(pattern,contents)
	# print(regex)
	unvalidatedregex(filename,newregex,f"{blue}\t| {alert}")


# https://gist.github.com/mccabe615/b0907514d34b2de088c4996933ea1720
# https://stackoverflow.com/questions/3115559/exploitable-php-functions
def checkdangerfunctions(filename,contents):
	global dangerfunctions,important
	array=['private key','system(','eval(','exec(','passthru(','shell_exec(','popen(','proc_open(','pcntl_exec(','exec(','include($_','assert(','fopen(','file_put_contents(','preg_replace(','create_function(','require($_','require_once($_']
	contents=contents.split('\n')
	for line in contents:
		for function in array:
			if function in line.lower():
				result=(f"{blue}\t| {alert} {line}.. in : {green}{filename} {red}({function[:-1]}){end}")
				if 'include' in function:
					important.append(result)
				else:
					pass
				dangerfunctions.append(result)
			else:
				pass


def actions(filename,contents):
	checkxss(filename,contents.lower())
	checkunvalidated(filename,contents.lower())
	checkdangerfunctions(filename,contents.lower())

def main():
	# folder="/opt/lampp/htdocs/projects/garagemgt/"
	if mode == "file":
		filename=arguments[1]
		readfile(filename)
	elif mode == "folder":
		folder=arguments[2]
		pass
	elif mode == "recursive":
		folder=arguments[1]
		print(f"{yellow} [*] Scanning recursively{end}\n")
		for dirpath,dirname,files in os.walk(folder):
			for file in files:
				filename=(f'{os.path.join(dirpath,file)}')
				if '.php'.lower() in filename.lower() or '.json'.lower() in filename.lower() or '.log'.lower() in filename.lower():
					readfile(filename)
						# print(f"{fail} Unable to read file {yellow}{filename}{end}")	
				else:
					pass 


if __name__ == "__main__":
	xss=[]
	unvalidated=[]
	dangerfunctions=[]
	important=[]
	if len(arguments) < 2:
		usage()
		sys.exit()
	elif (len(arguments) == 2):
		mode="file"
	elif (len(arguments) == 3 and arguments[2] == "folder"):
		mode="folder"
	elif (len(arguments) == 3 and arguments[2] == "recursive"):
		mode="recursive"

	main()
	print(f"\n\n\n")
	print(f"{stage} Checking for xss{end}")
	print('\n'.join(set(xss))+f"\n\n{yellow}\tTOTAL : {white}{len(set(xss))}{end}")
	print(f"\n\n\n")

	print(f"{stage} Checking for unvalidated fields{end}")
	print('\n'.join(set(unvalidated))+f"\n\n{yellow}\tTOTAL : {white}{len(set(unvalidated))}{end}")
	
	print(f"\n\n\n")
	print(f"{stage} Checking for dangerfunctions fields{end}")
	print('\n'.join(set(dangerfunctions))+f"\n\n{yellow}\tTOTAL : {white}{len(set(dangerfunctions))}{end}")

	print('\n'.join(set(important))+f"\n\n{yellow}\tTOTAL : {white}{len(set(important))}{end}")