#!/usr/bin/python

my_list = [1,9,8,4]

my_list2 = [ i*2 for i in my_list]

print my_list2

my_dict = {"server":"mpilgrim", "database":"master", "uid":"sa", "pwd":"secret"}
my_list = ["server database master uid pwd"]

print ["%s=%s" % (k,v) for k,v in my_dict.items()]

print my_dict.keys()
print my_dict.values()
print my_dict.items()

print "Joining Strings"

#Method 1
print ";".join(["%s=%s" % (k, v) for k, v in my_dict.items()])

#Method 2
s = ";".join(my_list)
print s

print s.split(" ")
