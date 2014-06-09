# Assignments from http://codingbat.com/
# Warmup1

import math

def stringTimes(name, n):
	result = ''
	for i in range(0,n):
		result = result + name
	return result

a = stringTimes('candy',5)
print("Result = "+str(a))

a = stringTimes('x',10)
print("Result = "+str(a))

a = stringTimes('not bad',3)
print("Result = "+str(a))