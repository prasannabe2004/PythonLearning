# Assignments from http://codingbat.com/
# Warmup1

import math

def bigDiff(nums):
	min = nums[0]
	max = nums[0]
	n = len(nums)
	for i in range(n):
		if min>nums[i]:
			min = nums[i]
	for i in range(n):
		if max<nums[i]:
			max = nums[i]
	diff = max - min	
	return abs(diff)
	
a = bigDiff([2,13,13,1,4])
print("Result = "+str(a))

a = bigDiff([2,2,0])
print("Result = "+str(a))

a = bigDiff([1,3,5])
print("Result = "+str(a))