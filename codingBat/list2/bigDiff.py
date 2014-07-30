# Assignments from http://codingbat.com/
# Warmup1

def bigDiff(nums):
	my_min = nums[0]
	my_max = nums[0]
	n = len(nums)
	for i in range(n):
		if my_min>nums[i]:
			my_min = nums[i]
	for i in range(n):
		if my_max<nums[i]:
			my_max = nums[i]
	diff = my_max - my_min	
	return abs(diff)
	
a = bigDiff([2,13,13,1,4])
print("Result = "+str(a))

a = bigDiff([2,2,0])
print("Result = "+str(a))

a = bigDiff([1,3,5])
print("Result = "+str(a))