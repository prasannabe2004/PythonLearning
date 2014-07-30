# Assignments from http://codingbat.com/
# Warmup1

def date_fashion(you, date):
	if you <= 2 or date <= 2:
		result = 0
	elif you >= 8 or  date >= 8:
		result = 2
	else:
		result = 1
	return result 

a = date_fashion(10,2)
print("Result = "+str(a))

a = date_fashion(5,2)
print("Result = "+str(a))

a = date_fashion(5,5)
print("Result = "+str(a))