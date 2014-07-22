#!/usr/bin/python
my_list = ["Larry", "Curly"]

print my_list.pop

print getattr(my_list,"append")("Prasanna")
print getattr(my_list,"append")("Moahansundaram")

print getattr(my_list,"pop")
print getattr(my_list,"pop")()
print my_list

print getattr({},"clear")
print getattr([],"append")
#print getattr((),"pop") # Tuples doesnt have any functions. so error.

#getattr with modules

import odbchelper
print odbchelper.buildConnectionString
print getattr(odbchelper, "buildConnectionString")

my_object = odbchelper
method = "buildConnectionString"
print getattr(my_object, method).__doc__
print type(getattr(my_object,method).__doc__)
print callable(getattr(my_object,method).__doc__)


import statsout

def myoutput(data, myformat="text"):
    output_function = getattr(statsout, "output_%s" % myformat)
    return output_function(data)