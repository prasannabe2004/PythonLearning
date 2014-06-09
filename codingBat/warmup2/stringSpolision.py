# Assignments from http://codingbat.com/
# Warmup1

import math

def stringSpolision(name):
	n = len(name)
	result = ''
	for i in range(n):
		result = result+name[:i+1]
	return result

a = stringSpolision('candy')
print("Result = "+str(a))

a = stringSpolision('x')
print("Result = "+str(a))

a = stringSpolision('ab')
print("Result = "+str(a))