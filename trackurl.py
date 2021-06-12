#! /usr/bin/python3
import requests
import sys
import pyfiglet as figlet
arguments=sys.argv
session=requests.Session()

white='\033[0m'
red='\033[91m'
green='\033[92m'
yellow='\033[93m'
blue='\033[94m'
""

def banner():
	scriptname=arguments[0].replace("./","")
	print(f"{yellow}{figlet.Figlet(font='larry3d').renderText((scriptname.replace('.py','')))}")
	string=f"{yellow}\n\tUsage\t:\tpython3 {arguments[0]} https://url\n{yellow}\t     \t:\tpython3 {arguments[0]} https://google.com \n"

	print(string)


def getpage(url):
	response=session.get(url,allow_redirects=True)
	historylist=response.history
	for item in historylist:
		print(f'\t{blue}url :  {red}{item}{white}')
	
	print(f'\n\n\t{green}First url :  {yellow}{url}{white}')
	print(f'\t{blue}Last url :  {yellow}{response.url}{white}')

if __name__ == "__main__":
	if (len(arguments) < 2):
		banner()
	else:
		banner()
		getpage(arguments[1])




"""
Red flags in a website
1.Too many redirections
2.No encryption
3.Asks you to perform any action to get something else in return
4.Check for additional links
5.Looks to good to be true
6.Asking for personal information
7.uppercase the link in the address bar for a clear view.Check for grammatical errors
8.Check the domain age here https://whois.domaintools.com/
"""




"""
Created on 2021-06-03

https://www.scamvoid.net/check/passtechusa.com/
https://www.scamvoid.net/check/safcom.club/





< script >
    var cl1 = 0;
var max_val = 10;
$('document').ready(function () {
    $('.whatsapp').click(function () {
        cl1++;
    });
    $('.final').click(function (e) {
        if (cl1 < max_val) {
            alert("You must invite 10 Friends or Groups!! You have " + eval(parseInt(max_val) - parseInt(cl1)) + " Groups or Friend Invites to finalize verification ");
            e.preventDefault();
        } else {
            window.location.href = 'https://www.passtechusa.com/s7pm6r3d?key=373dc756d2f581fb4b19b65f82cf8943';
        }
    });
}); < /script>


oungimuk.net/pfe/current/micro.tag.min.js?z=4121348&sw=/sw-check-permissions-ab6ea.js

"""



"""


Safaricom is the leading communications company in Kenya with the widest Network coverage.
According to my research the site is legitimate because:
The site makes use of encryption(HTTPS)  hence no sniffing of network traffic by hackers
The site was not set up lately(most malicious websites are under 5 years old)
There are not grammatical errors in the domain name or url
The site does not have any suspicious redirections to other third party websites(Redirections to other websites may be a sign of cross site scripting or unrestricted redirects vulnerabilities is https://*.safaricom.co.ke)

	"""