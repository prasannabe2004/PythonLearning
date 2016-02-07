# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 08:59:51 2015

@author: PMohanasundaram
"""
import socket

duplicate = 0
resolved = 0

def resolveIp(domainname):
    data = socket.gethostbyname(domainname)
    if repr(data):
        print "resolved IP's for ", domainname, " is ", repr(data)
        global resolved
        resolved +=1
        return True
    else:
        print "unresolved"
        return False

# Lets remove the duplicates and put all into a list
f1 = open("url1Copy.txt")
f2 = open("url2Copy.txt")
list1 = []

for line1 in f1:
    list1.append(line1)
f1.close()

for line2 in f2:
    if line2 not in list1:
        list1.append(line2)
    else:
        duplicate = duplicate + 1
f2.close()

#put the list into a file
f3 = open("foo.txt","wb")
for i in list1:
    if resolveIp(i[:(len(i)-1)]) == True:
        f3.write(i)
f3.close()


#Result
print "Found ",duplicate,"duplicates."
print resolved," resolved successfully."