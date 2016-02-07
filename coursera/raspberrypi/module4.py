import RPi.GPIO as GPIO

import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(11,GPIO.IN)

GPIO.setup(7,GPIO.OUT)
GPIO.output(7,0)

while True:
	#GPIO.output(7, GPIO.input(11))
	if(GPIO.input(11) == True):
		print("switch pressed")
		GPIO.output(7,True)
	else:
		GPIO.output(7,True)
		time.sleep(0.5)
		GPIO.output(7,False)
		time.sleep(0.5)

