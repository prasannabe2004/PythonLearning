# Assignments from http://codingbat.com/
# Warmup1

import math

def missingChar(str,n):
	front=str[0:n]
	back=str[n+1:]
	return front+back

a = missingChar("Prasanna",int(7))

print("Result = "+str(a))