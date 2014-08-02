#!/usr/bin/python
from sys import argv
from sys import path

print('The command line arguments are:')
for i in argv:
    print i

print '\n\nThe PYTHONPATH is', path, '\n'