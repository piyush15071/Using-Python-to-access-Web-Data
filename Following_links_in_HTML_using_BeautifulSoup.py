from urllib.request
import urlopen
from bs4 import BeautifulSoup

position = 17
count = 7

url = 'https://pr4e.dr-chuck.com/tsugi/mod/python-data/data/known_by_Yva.html'
taglist = list()
urllist = list()
urllist.append(url)

for i in range(count):
    html = urlopen(urllist[-1])
    soup = BeautifulSoup(html)
    tags = soup('a')
    taglist = list()
    for tag in tags:
        taglist.append(tag)
    url = taglist[position].get('href', None)
    print ('Retrieving: ', url)
    urllist.append(url)
print ('Last Url: ', urllist[-1])
