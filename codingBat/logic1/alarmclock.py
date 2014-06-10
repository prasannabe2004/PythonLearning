# Codingbat

def alarm_clock(day, vacation):
	if day >=1 and day <= 5:
		if vacation:
			return '10:00'
		else:
			return '7:00'
	else:
		if vacation:
			return 'off'
		else:
			return '10:00'

a = alarm_clock(1,False)
print("result is " + str(a))
a = alarm_clock(5,False)
print("result is " + str(a))
a = alarm_clock(0,False)
print("result is " + str(a))