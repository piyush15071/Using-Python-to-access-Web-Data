import urllib
import json
import re

serviceurl = 'http://python-data.dr-chuck.net/comments_221188.json?'
flag=0
while flag==0:
    address = raw_input('Enter location: ')
    if len(address) < 1 : break

    url = serviceurl + urllib.urlencode({'sensor':'false', 'address': address})
    print 'Retrieving', url
    uh = urllib.urlopen(url)
    data = uh.read()
    print 'Retrieved',len(data),'characters'

    js = json.loads(str(data))
    
    def func():
        return json.dumps(js, indent=4)
    
    string = str(func())
    
    y = string.split('"')
    count = 0
    for item in y:
        if item=="name":
            count+=1

    print "Count:", count

    a=re.findall(': ([0-9]*?),',string)
    sum = 0
    for item in a:
        item=int(item)
        sum+=item
    print 'Sum:',sum

    flag=1
