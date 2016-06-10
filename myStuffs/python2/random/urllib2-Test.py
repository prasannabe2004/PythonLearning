# This works with Python 2.7.6 Version
# Interesting website to test HTTP req/res and POST: http://httpbin.org/

import urllib2
import urllib

## that's the GET request
res = urllib2.urlopen('http://httpbin.org/ip')

print "The output of HTTP GET Request"
print res.read()

## post requests contain data, so here's how to make a POST request
params = {}

## set post parameters
params['article_id'] = 134
params['text_str'] = 'my_test_program'

## encode the data to percent format
data = urllib.urlencode(params)

req = urllib2.Request('http://httpbin.org/post',data)

## make request
res = urllib2.urlopen(req)

## print output
print "The output of HTTP POST Request"
print res.read()

