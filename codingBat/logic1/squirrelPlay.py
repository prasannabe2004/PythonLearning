# Codingbat

def squirrel_play(temp, is_summer):
	if is_summer == False and temp >= 60 and temp <=90:
		return True
	elif is_summer == True and temp >= 60 and temp <=100:
		return True
	else:
		return False

a = squirrel_play(70,False)
print("result is " + str(a))
a = squirrel_play(95,False)
print("result is " + str(a))
a = squirrel_play(95,True)
print("result is " + str(a))