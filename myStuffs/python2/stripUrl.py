# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 15:06:31 2015

@author: PMohanasundaram
"""

import socket

resolved = 0

def resolveIp(domainname):
    try:
        data = socket.gethostbyname(domainname)
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

f1 = open("url.txt")
for i in f1:
    j = i.lstrip('http://').rstrip()
    list1.append(j.rstrip('/?'))
f1.close()

#print list1

f3 = open("foo.txt","wb")
for i in list1:
    if resolveIp(i[:(len(i)-1)]) == True:
        f3.write(i)
f3.close()


print "Total domains in the list: ",len(list1)
print resolved," domains resolved successfully."