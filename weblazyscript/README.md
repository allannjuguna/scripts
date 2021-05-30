## Web lazy Scripts
This scripts is used to spot low hanging fruits in web applications mainly during ctfs
Used to find flags in  the following 
	- robots.txt
	- git folders 
	- uncommon headers
	- common directories like /admin
	- And many more

Usage :
	python3 weblazyscript.py http://urlhere /				-> For the root path 
	python3 weblazyscript.py http://urlhere /somefolder/			> For the custom path 