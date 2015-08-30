# paste your code here
import random

user = input("Choose your weapon: ")
comp = random.choice(['rock','paper','scissors'])

print('the user (you) chose', user)
print('the comp (I) chose', comp)

if user == 'rock':
    print('Ha! I really chose paper -- I WIN!')