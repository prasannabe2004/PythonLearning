#!/bin/python2
# python 2
#
# Homework 3, Problem 2
#
# Name:
#

def isOdd(num):
    if num%2 == 0:
        return False
    else:
        return True
    
print isOdd(42)
print isOdd(43)

print '--------------------------'

def numToBinary(N):
  """
  """
  if N == 0:
    return ''
  elif N%2 == 1:
    return numToBinary(N/2) + '1'
  else:
    return numToBinary(N/2) + '0'
    
print numToBinary(5)
print numToBinary(12)
print numToBinary(1)

print '--------------------------'

def binaryToNum(S):
  """
  """
  if S == '':
    return 0

  # if the last digit is a '1'
  elif S[-1] == '1': 
    return  2*binaryToNum(S[:-1])+ 1
  else: # last digit must be '0'
    return  2*binaryToNum(S[:-1])+ 0
    
print binaryToNum('101010')
print binaryToNum("1100100")
print binaryToNum("")
print binaryToNum("0")

print '--------------------------'

def increment(S):
    if S == '11111111':
        return  '0'*8
    x = binaryToNum(S)
    x = x+1
    y = numToBinary(x)
    return '0'* (8-len(y)) + y
    
print increment('00000000')
print increment('00000001')
print increment('00000111')
print increment('11111111')

print '--------------------------'

def count(S, n):
    for i in range(n+1):
        print S
        S = increment(S)
        

count("00000000", 4)
print '--------------------------'
count("11111110", 5)
print '--------------------------'



def numToTernary(num):
    return None
    
numToTernary(42)

