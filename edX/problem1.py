# python 2
#
# Homework 3, Problem 1
#
# name:

from turtle import *
import time
from random import *

def poly( n, N ):
    """ draws n sides of an N-sided regular polygon """
    if n == 0:
        return
    else:
        forward( 50 )   # 50 is hard-coded at the moment...
        left( 360.0/N )
        poly( n-1, N )

def spiral( initialLength, angle, multiplier ):
  c = choice( ['green','red','blue'] )
  if initialLength < 1 or initialLength > 500:
    return
  else:
    color( c )
    forward(initialLength)    # turtle goes forward 100 steps
    left(angle)       # turtle turns right 90 degrees
    spiral( initialLength * multiplier, angle, multiplier )
    
#spiral(100,60,0.95)
#spiral(2, 135, 1.1)

def chai(size):
    """ our chai function! """
    if (size<9): 
        return
    else:
        forward(size)
        left(90)
        forward(size/2.0)
        right(90)
        chai(size/2)
        right(90)
        forward(size)
        left(90)
        chai(size/2)
        left(90)
        forward(size/2.0)
        right(90)
        backward(size)
        return
#chai(100)


def svtree(trunklength,levels):
    if levels <=1:
        return
    else:
        forward(trunklength)
        left(60)
        forward(trunklength/2)
        right(60)
        svtree(trunklength,levels-1)
        right(120)
        forward(trunklength/2) 
        left(60)
svtree(50,3)