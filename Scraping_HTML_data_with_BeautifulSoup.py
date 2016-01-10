import re
import urllib.request
import urllib
from bs4 import BeautifulSoup

url = str(input("Enter : "))

with urllib.request.urlopen(url) as url:
    html = url.read()

soup = BeautifulSoup(html, "html.parser")

tags = soup('span')
#print (tags)

sum=0
for tag in tags:
    a=re.findall('>([0-9]*?)<',str(tag))
    sum=sum+int(a[0])
print (sum)
