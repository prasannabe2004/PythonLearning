# Assignments from http://codingbat.com/
# Warmup1

import math

def sum13(nums):
	j = 0
	flag = 0
	n = len(nums)
	for i in range(n):
		if flag:
			flag = 0
			continue
		if nums[i] != 13:
			j = j+nums[i]
		else:
			flag = 1

	return j

a = sum13([2,13,13,1,4])
print("Result = "+str(a))

a = sum13([2,2,0])
print("Result = "+str(a))

a = sum13([1,3,5])
print("Result = "+str(a))