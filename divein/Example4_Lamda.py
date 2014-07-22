#!/usr/bin/python



def f(x):
    return x*2

print f(3)

g = lambda x: x*2

print g(3)

(lambda x: x*2)(3)

s = "this   is\na\ttest"

print " ".join(s.split())
