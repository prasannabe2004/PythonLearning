# Assignments from http://codingbat.com/
# Warmup1

def diff21(n):
	diff1 = abs(100 - n) 
	diff2 = abs(200 - n)
	if diff1 <=10 or diff2 <= 10 :
		return True
	else:
		return False

in_num = input("Enter the number:")
a = diff21(int(in_num))

print("Result = "+str(a))