import sys

try:
    score_input = input("Enter your scrore between 0.0 and 1.0: ")
    score = float(score_input)
    if score > 1.0 or score < 0.0:
        print ("Enter a valid input")
        sys.exit()
        
except:
	print ('Enter a valid input')
    
if score >= 0.9:
    print ('A')
elif score >= 0.8 and score < 0.9:
    print ('B')
elif score >= 0.7 and score < 0.8:
    print ('C')
elif score >= 0.6 and score < 0.7:
    print ('D')
elif score < 0.6:
	print ('F')
else:
    print ('Unknown score')
