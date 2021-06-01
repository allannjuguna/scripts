## Web lazy Script
This scripts is used to spot low hanging fruits in web applications mainly during ctfs<br>
Used to find flags in  the following
``` 
	- robots.txt
	- git folders 
	- uncommon headers
	- common directories like /admin
	- And many more
```
**Usage** :
```
	python3 weblazyscript.py http://urlhere /				-> For the root path 
	python3 weblazyscript.py http://urlhere /somefolder/			> For the custom path 
```	

**Example Output**:
```
HOST : https://subdomain.target.com 
PATH : /
SERVER : Apache/2.4.46 (Ubuntu)
COOKIE : PHPSESSID=9u2cvpd9iu2jcd2sfs483sgrr6; path=/,
PHPSESSION : 


SUMMARY
The website server :  Apache/2.4.46 (Ubuntu)  
 [+] Git file exposed at : https://subdomain.target.com/.git/HEAD  (200)
 [+] Admin page found at : https://subdomain.target.com/admin for leads (301).
 [+] Admin page found at : https://subdomain.target.com/admin/ for leads (303).
 [+] Developer file found at : https://subdomain.target.com/.gitattributes,check for sensitive info disclosure (200).
 [+] Developer file found at : https://subdomain.target.com/composer.json,check for sensitive info disclosure (200).
 [+] Developer file found at : https://subdomain.target.com/composer.lock,check for sensitive info disclosure (200).
 [+] Developer file found at : https://subdomain.target.com/.gitattributes,check for sensitive info disclosure (200).
 [+] Developer file found at : https://subdomain.target.com/package.json,check for sensitive info disclosure (200).

```

