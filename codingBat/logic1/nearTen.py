# Codingbat

def near_ten(num):
	remain = num%10
	if remain <= 2 or remain >= 8:
		return True
	else:
		return False
a = near_ten(12)
print("result is " + str(a))
a = near_ten(17)
print("result is " + str(a))
a = near_ten(19)
print("result is " + str(a))