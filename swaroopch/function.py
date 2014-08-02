#!/usr/bin/python

def total(initial=5, *numbers, **keywords):
    ''' 
    This is test function
    It does nothing.
    '''
    print initial
    print numbers
    print keywords
    count = initial
    for number in numbers:
        count += number
    print count
    for key in keywords:
        count += keywords[key]
    return count
x=2
print total(10, 1, 2, 3, vegetables=50, fruits=100)
print total.__doc__
print dir()
del(x)
print dir()
print dir('print')
print vars()