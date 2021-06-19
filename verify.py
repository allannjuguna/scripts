#! /usr/bin/python3
import subprocess,sys,json,re,requests,os,pyfiglet as figlet
session=requests.Session()
arguments=sys.argv
white='\033[0m'
red='\033[91m'
green='\033[92m'
yellow='\033[93m'
blue='\033[94m'
def banner():
	print(f"{yellow}{figlet.Figlet(font='larry3d').renderText('Verify')}")
	string=f"{yellow}\n\tUsage\t:\tpython3 {arguments[0]} domainnamehere/ipaddresshere domain/ip\n{yellow}\t     \t:\tpython3 {arguments[0]} google.com domain\n{yellow}\t     \t:\tpython3 {arguments[0]} 207.180.237.29 ip\n"
	print(string)

def runcommand(string):
	command=string.split(' ')
	handle=subprocess.Popen(command,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE,close_fds=True)
	error=handle.stderr.read().decode()
	output=handle.stdout.read().decode()

	result=output+error
	return result

def ping(domain):
	if "http" in domain.lower():
		print(f'{red}[ FAIL ] Make sure the domain name does not have http(s)://{white}')
		exit(-1)
	print(f'{green}[ OK ] Pinging the host {yellow}({domain}){white} ')
	result=(runcommand(f"ping -c 2 {domain}"))
	if 'time=' in result.lower() and 'ttl=' in result.lower():
		print(f'{green}[ OK ] The host ({domain}) is up and running')
		# Getting the ip address
		try:
			ip=((result.split(' ')[2]).replace("("," ")).replace(")","").strip()
			return ip
		except:
			print(f'{red}[ FAIL ] Failed to fetch the ip address')
	elif('100% packet loss' in result.lower()):
		print(f'{red}[ FAIL ] 100 % Packet Loss encountered')
		ip=((result.split(' ')[2]).replace("("," ")).replace(")","").strip()
		return ip
	else:
		print(f'{red}[ FAIL ] The host ({domain}) is offline')
	return "null"


def checkiplocation(ip):
	global RegistrationDate,OrganizationName,Address,City,Region,Country
	print(f'{green}[ OK ] Fetching information for the ip {yellow}({ip}){white}')
	custom_headers={"Referrer":"https://iplocation.com/","User-Agent":"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0"}
	payload={"ip":f"{str(ip)}"}
	response=session.post("https://iplocation.com",headers=custom_headers,data=payload)
	headers=response.headers
	status=response.status_code
	content=json.loads(response.text)
	print(f'{green}[ OK ] RESPONSE HEADERS {white}')
	for item in headers:
		value=headers.get(item,"Not found")
		print(f'\t{blue}{item} :  {yellow}{value}{white}')
	try:
		print(f'\n\n{green}[ OK ] IP INFORMATION (MACHINE HOSTING THE WEBSITE) {white}')
		for item in content:
			value=content.get(item,"Not found")
			if (item == 'country_name'):
				Country=str(value)+" from (iplocation.com)"
			elif(item == 'city'):
				City=str(value)+" from (iplocation.com)"
			elif(item == 'region_name'):
				Region=str(value)+" from (iplocation.com)"
			print(f'\t{blue}{item} :  {yellow}{value}{white}')
	except:
		print(f'{red}[ FAIL ] Failed to fetch ip information')

def whois(domain):
	print(f'\n\n{green}[ OK ] Running whois on the domain ({domain}){white}')
	# The domain should now have https:// 
	result=runcommand(f'whois {domain}')
	return result

def nslookup(domain):
	print(f'{green}[ OK ] Running nslookup on the domain ({domain}){white}')
	# The domain should now have https:// 
	result=runcommand(f'nslookup {domain}')
	print(f'{blue}{result}{white}\n\n\n\n')

def dig(domain):
	print(f'{green}[ OK ] Running dig on the domain ({domain}){white}')
	# The domain should not have https:// 
	result=runcommand(f'dig {domain}')
	print(f'{white}{result}{white}\n\n\n\n')

def getpage(url):
	global fulllink
	try:
		response=session.get(url,allow_redirects=True,timeout=14)
		historylist=response.history
		for item in historylist:
			print(f'\t{red}url :  {red}{item}{white}')
		print(f'\n\n\t{green}Redirections :  {yellow}{len(historylist)}{white}')
		print(f'\t{green}First url :  {yellow}{url}{white}')
		print(f'\t{blue}Last url :  {yellow}{response.url}{white}')
		fulllink=response.url
	except:
		print(f'{red}[ FAIL ] Unable to send request to ({url}){white}')



def trackurl(domain):
	print(f"\n\n{yellow}{figlet.Figlet(font='larry3d').renderText('trackurl')}")
	print(f'{green}[ OK ] Checking redirects in ({domain}){white}')
	getpage(domain)

def cleanwhois(results):
	global RegistrationDate,OrganizationName,Address,City,Region,Country
	print(f'{green}[ OK ] Checking for relevant whois information{white}')
	checkfor=['Creation Date:','Registrant Organization','Registrant Street','Registrant City','Registrant State/Province','Registrant Country']
	results=results.split('\n')
	for detail in checkfor:
		for line in results:
			if (detail.lower()).strip() in (line.lower()).strip():
				if (checkfor[0] in line.strip()):
					RegistrationDate=line.replace("Creation Date:","")
				elif((detail.lower()).strip() == (checkfor[1].lower()).strip()):
					OrganizationName=line.replace("Registrant Organization:","")
				elif((detail.lower()).strip() == (checkfor[2].lower()).strip()):
					Address=line.replace("Registrant Street:","")
				elif((detail.lower()).strip() == (checkfor[3].lower()).strip()):
					City=line.replace("Registrant City:","")
				elif((detail.lower()).strip() == (checkfor[4].lower()).strip()):
					Region=line.replace("Registrant State/Province:","")
				elif((detail.lower()).strip() == (checkfor[5].lower()).strip()):
					Country=line.replace("Registrant Country:","")
	print(f'{green}[ OK ] Done getting whois information ...{white}')

def actions(domain,ip):
	global fulllink
	if (ip != "null"):
		checkiplocation(ip)
		nslookup(domain)
		dig(domain)
		results=whois(domain)
		print(f'{green}[ OK ] Showing whois information {white}')
		print(f'{white}{results}{white}\n\n\n\n')
		cleanwhois(results)
		trackurl(f"http://{domain}")

		# Making the final report
		print(f'\n\n{green}[ OK ] Generating the final report{white}')
		report={'Registration Date':RegistrationDate,'Organization Name':OrganizationName,'Address':Address,'City':City,'Region':Region,'Country':Country}
		print(f'\t{blue}Ip address :  {yellow}{ipaddress}{white}')
		for item in report:
			value=report.get(item,"Not found")
			print(f'\t{blue}{item} :  {yellow}{value}{white}')
		print(f'\t{blue}Full Link :  {yellow}{fulllink}{white}')


		print(f'\n\n\t{green}More  IP info :  {white}https://who.is/whois-ip/ip-address/{ipaddress}{white}')
		print(f'\t{green}More  Domain info :  {white}https://who.is/whois/{fulldomain}{white}')
		print(f'\t{green}More  Domain info :  {white}https://whois.domaintools.com/{fulldomain}{white}')
		print(f'\t{green}Safety info :  {white}https://www.scamvoid.net/check/{fulldomain}/{white}')
		print(f'\t{green}Scam info :  {white}https://www.scamadviser.com/check-website/{fulldomain}/{white}')
	else:
		print(f'{red}[ FAIL ] Ip value is null')


if __name__ == "__main__":
	# For purposes of the result
	fulllink="Not found"
	RegistrationDate=OrganizationName=Address=City=Region=Country=Redirects="Ownership Information unavailable"
	if (len(arguments) < 3):
		banner()
	elif(len(arguments) == 3 and arguments[2] == "domain"):
		banner()
		fulldomain=domain=str(arguments[1].strip())
		ipaddress=ip=(ping(domain)).strip()
		actions(domain,ip)
	elif(len(arguments) == 3 and arguments[2] == "ip"):
		banner()
		fulldomain=ipaddress=ip=domain=str(arguments[1].strip())
		print(f'{green}[ OK ] Performing reverse DNS on the ip {yellow} ({domain}){white}')
		fulldomain=ipaddress=ip=(ping(domain)).strip()
		actions(domain,ip)
	else:
		banner()
	

# Actions to perform
# 	Ping to see whether the host is up and running
# 	Whois
# 	Dig Gives a summary of domain names and ip addresses (better than nslookup)
# 	nslookup - Gives domain names and ip addresses
# 	whatweb
# 	Reverse whois
# 	tracert
# reversedns



# 	Possible threats
# 	If the site is using http;then say that credentials passed to the website can be sniffed hence not safe


# https://gbhackers.com/latest-google-dorks-list/



# Registration Date	
# Organisation Name	
# Address	
# City
# Region
# Country


# What the site does
# When it was started and its effect on the end User-Agent
# Recommendations


# According to the research the site is legitimate because:
# 1. The site makes use of encryption(HTTPS)  hence no sniffing of network traffic by hackers
# 2. The site was not set up lately(most malicious websites are under 5 years old)
# 3. There are not grammatical errors in the domain name or URL
# 4. The site does not have any suspicious redirections to other third party websites



# Info:
# The website seems like it is owned by an individual and is about filling surveys
# I do not recommend visiting the website since its intent is still unknown



# I do not recommend visiting this site
# Reasons why i do not recommend visiting the site:
# 	Lacking some of the domain info
# 	The website lacks encryption hence network traffic can be sniffed by hackers



# No threats associated with this link have been found ,However, i do not recommend visiting the link.






# Info:


# No threats associated with this link have been found ,However, i do not recommend visiting the link.


# A015496241V
# Martinkonyu1.