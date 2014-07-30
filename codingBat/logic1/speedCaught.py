# Assignments from http://codingbat.com/
# Warmup1

def speed(limit, birthday):
	if (birthday and limit <= 60+5) or (limit <= 60):
		result = 0
	elif (birthday and limit <= 80+5) or (limit <= 80):
		result = 1
	else:
		result = 2
	return result

a = speed(81,False)
print("Result = "+str(a))

a = speed(65, False)
print("Result = "+str(a))

a = speed(81, True)
print("Result = "+str(a))