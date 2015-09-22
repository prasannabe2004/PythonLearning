#!/bin/python2
# python 2
#
# Homework 3, Problem 1
#
# name:

from turtle import *
import time
import random

def poly( n, N ):
    """ draws n sides of an N-sided regular polygon """
    if n == 0:
        return
    else:
        forward( 50 )   # 50 is hard-coded at the moment...
        left( 360.0/N )
        poly( n-1, N )
        
#poly(7,7)


def spiral( initialLength, angle, multiplier ):
    """ draws n sides of an N-sided regular polygon """
    c = random.choice(['green','blue','red'])
    color(c)
    if initialLength < 1:
        return
    else:
        forward( initialLength )   # 50 is hard-coded at the moment...
        left( angle )
        spiral( initialLength*multiplier,angle,multiplier)
    
#spiral(2,135,1.1)

def chai(size):
    """ our chai function! """
    if (size<9): 
        return
    else:
        forward(size)
        left(90)
        forward(size/2.0)
        right(90)
        #chai(size/2)
        right(90)
        forward(size)
        left(90)
        #chai(size/2.0)
        left(90)
        forward(size/2.0)
        right(90)
        backward(size)
        
        return
        
#chai(100)

def svtree(size,levels):
    """ our chai function! """
    if (size<9) or levels == 0: 
        return
    else:
        forward(size)        
        left(30)
        forward(size/2.0)
        svtree(size/2,levels-1)        
        right(180)
        forward(size/2.0)
        left(120)
        forward(size/2.0)
        svtree(size/2,levels-1)
        backward(size/2.0)
        left(30)
        backward(size)
        return
        
svtree(100,4)

def flakeside(sidelength, levels):
    if levels == 0.0:
        forward(sidelength/3)
    else:
        right(60)        
        forward((sidelength/3)*2)
        
        left(120)
        forward((sidelength/3)*2)
        
        
        flakeside(sidelength,levels-1)
    
#flakeside(100,2)

def snowflake(sidelength, levels):
    """ fractal snowflake function
          sidelength: pixels in the largest-scale triangle side
          levels: the number of recursive levels in each side
    """
    flakeside( sidelength, levels )
    left(120)
    flakeside( sidelength, levels )
    left(120)
    flakeside( sidelength, levels )
    left(120)




exitonclick()