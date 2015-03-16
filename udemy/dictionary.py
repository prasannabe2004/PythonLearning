import re
import urllib.request


try:
    word = input("Enter your word: ")
    url = "http://dictionary.reference.com/browse/" + word
    data = urllib.request.urlopen(url).read()
    data1 = data.decode("utf-8")
    m = re.search('meta name="description" content="',data1)
    d1 = data1[m.end():m.start()+200]
    m1 = re.search('See more',d1)
    print("Your word definition is %s" % d1[:m1.start()])
except:
    print("Word not found")
