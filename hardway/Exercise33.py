#Python 2.7.0

i = 0
numbers = []

def function(i, j):
    i = i+j
    numbers.append(i)
    print "Numbers now: ", numbers


for i in range(0,6):
    function(i,2)

print "The numbers: "

for num in numbers:
    print num

"""
At the top i is 0
Numbers now: [0]
At the bottom i is 1
At the top i is 1
Numbers now: [0,1]
At the bottom i is 2
At the top i is 2
Numbers now: [0,1,2]
At the bottom i is 3
At the top i is 3
Numbers now: [0,1,2,3]
At the bottom i is 4
At the top i is 4
Numbers now: [0,1,2,3,4]
At the bottom i is 4
At the top i is 5
Numbers now: [0,1,2,3,4,5]
At the bottom i is 6
The numbers:
0
1
2
3
4
5
"""