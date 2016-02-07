# -*- coding: utf-8 -*-
"""
Created on Tue Sep 08 10:24:40 2015

@author: PMohanasundaram
"""

import urllib
page = urllib.urlopen('https://www.riamoneytransfer.com/countries/send-money-to-india')

data = page.read()

index = data.find('\"ExchangeRate\":')

start = index+15
end = start+5

print data[start:end]