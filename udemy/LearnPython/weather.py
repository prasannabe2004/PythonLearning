import re
import urllib.request

city = input("Enter your city: ")

url = "http://www.weather-forecast.com/locations/" + city +"/forecasts/latest"

data = urllib.request.urlopen(url).read()

data1 = data.decode("utf-8")

m = re.search('span class="phrase">',data1)

d1 = data1[m.end():m.start()+300]

m = re.search('</span>',d1)
print(d1[:m.start()])

