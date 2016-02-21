import re

fp = open("regex_sum_224413.txt")

input = fp.read()

#print(input)

data = re.findall('[0-9]+',input)

sum = 0

for i in data:
    sum = sum + int(i)

print(sum)

fp.close()