# Assignments from http://codingbat.com/
# Warmup1

import math

def sumDouble(a, b):
	if a != b:
		return a+b
	else:
		return 2*(a+b)

a = sumDouble(1,2)
print("Result = "+str(a))

a = sumDouble(2,3)
print("Result = "+str(a))

a = sumDouble(2,2)
print("Result = "+str(a))