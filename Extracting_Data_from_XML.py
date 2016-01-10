import re
import urllib
import urllib.request
import xml.etree.ElementTree as ET

serviceurl = 'http://python-data.dr-chuck.net/comments_221184.xml?'

address = str(input('Enter location: '))

url = serviceurl + urllib.parse.urlencode({'sensor':'false', 'address': address})
print ('Retrieving', url)
uh = urllib.request.urlopen(url)
data = str(uh.read())
print ('Retrieved',len(data),'characters')

print('Count: ',data.find("<comment>"))

y=re.findall('>([0-9]*?)<',data)

sum=0
for item in y:
    item=int(item)
    sum+=item
print('Sum: ',sum)
