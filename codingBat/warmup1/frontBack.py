# Assignments from http://codingbat.com/
# Warmup1

import math

def frontBack(name):
	n = len(name)
	if n <= 1:
		return name
		
	first=name[0]
	last=name[n-1]
	return last+name[1:n-1]+first

a = frontBack('Prasanna')
print("Result = "+str(a))

a = frontBack('abc')
print("Result = "+str(a))

a = frontBack('a')
print("Result = "+str(a))