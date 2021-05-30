import requests
import lxml.html as parser
url="https://ekastech.com/"
session=requests.Session()


response=session.get(url)
content=response.text
headers=response.headers
root=parser.fromstring(content)
words=root.xpath('//text()')
print(words)
print(response.text)
print('done')


strings big.txt | tr '[:upper:]' '[:lower:]' | sort | uniq | awk 'length($0)==3'| wc -l