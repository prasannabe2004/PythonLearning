import urllib
from BeautifulSoup import *

url = raw_input('Enter: ')
count = int(raw_input('Enter count: '))
position = int(raw_input('Enter Position: '))

i = 1

while(count>=0):
    # Look at the parts of a tag
    html = urllib.urlopen(url).read()
    print 'Retriving ', url
    soup = BeautifulSoup(html)
    tags = soup('a')
    for tag in tags:
        if i == position:
            #print 'TAG:',tag
            #print 'URL:',tag.get('href', None)
            #print 'Contents:',tag.contents[0]
            #print 'Attrs:',tag.attrs
            url = tag.get('href', None)
            break
        i += 1
    i = 1
    count -= 1