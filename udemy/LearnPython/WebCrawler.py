import urllib.request
import re

#u = input("Enter the stock name: ")
stocks = ['GOOG','FB','DATA']

for u in stocks:
    url = "https://www.google.com/finance?q=" + u
    data = urllib.request.urlopen(url).read()
    data = data.decode('utf-8')
    d1 = re.search('meta itemprop=\"price\"',data)
    final = data[d1.start():d1.end()+25]
    f1 = re.search("content=",final)
    f2 = final[f1.end()+1:-2]
    print('The value of %s is %s'%(u,f2))