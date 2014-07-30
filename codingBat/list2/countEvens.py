# Assignments from http://codingbat.com/
# Warmup1

def count_evens(nums):
	j = 0
	n = len(nums)
	for i in range(n):
		if nums[i] % 2 == 0:
			j = j+1
	return j

a = count_evens([2,1,2,3,4])
print("Result = "+str(a))

a = count_evens([2,2,0])
print("Result = "+str(a))

a = count_evens([1,3,5])
print("Result = "+str(a))