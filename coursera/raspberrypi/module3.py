#!/bin/python

i = 1
mylist = []
while(i<=3):
    n = input("Enter the Number:")
    mylist.append(int(n))
    i = i + 1

print("Before Sorting: ")
print(mylist)
mylist.sort()
print("After Sorting: ")
print(mylist)
