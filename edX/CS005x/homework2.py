#!/bin/python2

# paste your code here

# python 2
#
# Homework 2, Problem 2
#
# Name:
# Date:
#


def dbl(x):
    """  output: dbl returns twice its input
         input x: a number (int or float)
         Spam is great, and dbl("spam") is better!
    """
    return 2*x
    
print dbl(21)


def tpl(x):
    """ output: tpl returns thrice its input
         input x: a number (int or float)
    """
    return 3*x

print tpl(5)


def sq(x):
    """ Squares the number
    """
    return x*x
    
print sq(5)


def interp(low,hi,fraction):
   """ formula is (hi-low)*fraction + low
   """
   return ((hi-low)*fraction)+low

print interp(24, 42, 0)
print interp(102, 117, -4.0)


def checkends(s):
  if s == '' or s[0] == s[len(s)-1]:
    return True
  else:
    return False

print checkends('no match')
print checkends('hah! a match')
print checkends('q')
print checkends(' ')


def flipside( s ):
    """ put your docstring here
    """
    x = int(len(s)/2)
    return s[x:]+s[:x]
    
print flipside('homework')
print flipside('carpets')


def convertFromSeconds( s ):
    days = s / (24*60*60)  # # of days
    
    s = s % (24*60*60)     # the leftover
    hours = s/(60*60)
    
    s=s%(60*60)
    minutes = s/60
    
    s = s%60
    seconds = s
    
    return [days, hours, minutes, seconds]
    
print convertFromSeconds(100000)


def front3(str):
  return str[:3]*3
  