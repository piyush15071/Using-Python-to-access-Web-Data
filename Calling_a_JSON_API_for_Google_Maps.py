import urllib
import json

serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'
flag=0
while flag==0:
    address = raw_input('Enter location: ')
    if len(address) < 1 : break

    url = serviceurl + urllib.urlencode({'sensor':'false', 'address': address})
    print 'Retrieving', url
    uh = urllib.urlopen(url)
    data = uh.read()
    print 'Retrieved',len(data),'characters'

    try: js = json.loads(str(data))
    except: js = None
    if 'status' not in js or js['status'] != 'OK':
        print '==== Failure To Retrieve ===='
        print data
        continue

    def func():
        return json.dumps(js, indent=4)
    
    string = str(func())
    
    y = string.split('"')
    
    for item in y:
        if len(item)==27:
            print 'Place id',item
            break
    flag=1
