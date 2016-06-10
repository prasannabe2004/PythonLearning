# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 15:53:32 2015

@author: PMohanasundaram
"""

import urllib2 as url
import myStuffs.python2.socket

resolved = 0

def resolveIp(domainname):
    try:
        data = myStuffs.python2.socket.gethostbyname_ex(domainname)
    except:
        print domainname, " Unresolved"
        return False
    else:
        if repr(data):
            print "resolved IP for ", domainname, " is ", repr(data)
            global resolved
            resolved +=1
            return True

list1 = []
for i in range(0,20):
    urlname = "http://www.alexa.com/topsites/global;"+str(i)
    response = url.urlopen(urlname)
    data = response.read()
    while True:
        start = data.find("href=\"/siteinfo/")
        if start!=-1:    
            end = data.find(".",start+1)
            domain = data[start+16:end+4]
            domain = domain.rstrip('"')
            resolveIp(domain)
            list1.append(domain)            
            data=data[end:]
        else:
            break
    
print list1,len(list1),resolved