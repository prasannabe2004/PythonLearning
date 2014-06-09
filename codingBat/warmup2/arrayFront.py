# Assignments from http://codingbat.com/
# Warmup1

import math

def frontArray(array):
	n = len(array)
	for i in range(n-1):
		if array[i] == 9 :
			return True
	else:
		return False

a = frontArray([9,2])
print("Result = "+str(a))

a = frontArray([1,2,3,4,9])
print("Result = "+str(a))

a = frontArray([1,2,3,4,5])
print("Result = "+str(a))