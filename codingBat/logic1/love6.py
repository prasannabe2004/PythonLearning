# Assignments from http://codingbat.com/
# Warmup1

def love6(a, b):
	diff = abs(a -b)
	add = a+b
	if diff == 6 or add == 6 or a == 6 or b ==6 :
		return True
	else:
		return False

a = love6(6,4)
print("Result = "+str(a))

a = love6(16,10)
print("Result = "+str(a))

a = love6(1,7)
print("Result = "+str(a))