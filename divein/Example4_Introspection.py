#!/usr/bin/python
from apihelper import info
import odbchelper
import turtle
import types

li = []
#info(li)

print

#info(turtle)
#info(odbchelper, 30)
#info(odbchelper, 30, 0)
#info(odbchelper, spacing=20, collapse = 1)
#info(odbchelper, collapse = 0)
info(collapse=0, spacing=0, object=odbchelper)

#Introducing type
print type(1)
print type("string")
print type([])
print type(turtle)
print type(())
print type({})
print type(info)
if type(odbchelper) == types.ModuleType:
    print True
    
#Introducing str
print str(1)
horsemen = ['war', 'pestilence', 'famine']
horsemen.append("Powerbuilder")
print str(horsemen)
print str(odbchelper)
print str(None)

#Introducing dir
print dir([])
print dir(())
print dir({})
print dir(odbchelper)

#Introducing callable
import string
print string.punctuation
print string.join
print callable(string.punctuation)
print callable(string.join)
import __builtin__
print info(__builtin__, 20)



    

