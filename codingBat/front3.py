# Assignments from http://codingbat.com/
# Warmup1

import math

def front3(name):
	if len(name) >= 3:
		return name[:3]+name[:3]+name[:3]
	return name
	
a = front3('candy')
print("Result = "+str(a))

a = front3('x')
print("Result = "+str(a))

a = front3('not bad')
print("Result = "+str(a))