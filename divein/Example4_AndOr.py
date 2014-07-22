#!/usr/bin/python


print 'a' and 'b'

print '' and 'a'

print 'a' and 'b' and 'c'

print "hello"

print 'a' or 'b'

print '' or 'b'

print '' or [] or {}

def sidefx():
    print " in sidefx()"
    return 1

print 'a' or sidefx()

a="first"
b="second"

print 1 and a or b
print 0 and a or b