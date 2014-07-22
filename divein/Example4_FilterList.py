#!/usr/bin/python
import turtle

my_list = ["a", "mpilgrim", "foo", "b", "c", "b", "d", "d"]

print [ i for i in my_list if len(i) > 1]
print [ i for i in my_list if i != "b"]
print [ i for i in my_list if my_list.count(i) == 1]

def callinfo(myobject):
    methodList = [method for method in dir(myobject) if callable(getattr(myobject, method))]
    print methodList
    
callinfo(turtle)