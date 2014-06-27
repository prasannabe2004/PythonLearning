#Python 2.7.0

from sys import argv

argc = len(argv)

if  argc == 4:
	script, first, second, third = argv
else:
	script=raw_input("Enter the script name: ")
	first=raw_input("Enter the first argument: ")
	second=raw_input("enter the second argument: ")
	third=raw_input("enter the third argument: ")

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third
