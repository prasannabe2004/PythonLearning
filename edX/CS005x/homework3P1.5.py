#!/bin/python2
# python 2
#
# Homework 3, Problem 1.5
#
# Name:
#
# Date:
# Overall comments:
#

#
# mylen example from class
#
def mylen( s ):
    """ mylen outputs the length of s
              input: s, which can be a string or list

    """
    if s == '' or s == []:   # if empty string or empty list
        return 0
    else:
        return 1 + mylen( s[1:] )
        
#print mylen('cs50')

def flipside(s):
   """ flipside swaps s's sides
       input s: a string
   """
   x = len(s)/2
   return s[x:] + s[:x]

#
# Tests
#
#print "flipside('carpets')    petscar ==", flipside('carpets')
#print "flipside('homework')  workhome ==", flipside('homework')
#print "flipside('flipside')  sideflip ==", flipside('flipside')
#print "flipside('az')              za ==", flipside('az')
#print "flipside('a')                a ==", flipside('a')
#print "flipside('')                   ==", flipside('')


def mult( n, m ):
    """ mult returns the product of its two inputs
            inputs: n and m are both integers
            output: the result upon multiplying n and m
    """
    if n == 0 or m == 0:
        return 0
    else:
        if n > 0 and m > 0:
            return abs(m) + mult(n-1,m)
        elif n > 0 and m < 0:
            return m + mult(n-1,m)
        elif m > 0 and n < 0:
            return n + mult(n,m-1)
        else:
            return abs(abs(m) + mult(n-1,abs(m)))

#print "mult(6,7)    42 ==", mult(6,7)
#print "mult(6,-7)  -42 ==", mult(6,-7)
#print "mult(-6,7)  -42 ==", mult(-6,7)
#print "mult(-6,-7)  42 ==", mult(-6,-7)
#print "mult(6,0)     0 ==", mult(6,0)
#print "mult(0,7)     0 ==", mult(0,7)
#print "mult(0,0)     0 ==", mult(0,0)    




def dot(L,K):
    if len(L) != len(K):
        return 0.0
    if L == []:
        return 0.0
    else:
        return L[0]*K[0] + dot(L[1:],K[1:])
#
# Tests
#
#print "dot( [5,3], [6,4] )     42.0 ==", dot( [5,3], [6,4] ) 
#print "dot( [1,2,3,4], [10,100,1000,10000] )  43210.0 ==", dot( [1,2,3,4], [10,100,1000,10000] ) 
#print "dot( [5,3], [6] )        0.0 ==", dot( [5,3], [6] ) 
#print "dot( [], [6] )           0.0 ==", dot( [], [6] ) 
#print "dot( [], [] )            0.0 ==", dot( [], [] ) 


def ind(e,L):
    if e in L:
        return L.index(e)
    else:
        return len(L)

#
# Tests
#
#print "ind( 42, [ 55, 77, 42, 12, 42, 100 ])  2 ==", ind( 42, [ 55, 77, 42, 12, 42, 100 ])
#print "ind(42, range(0,100))                  42 ==", ind(42, range(0,100))
#print "ind('hi', [ 'hello', 42, True ])       3 ==", ind('hi', [ 'hello', 42, True ])
#print "ind('hi', [ 'well', 'hi', 'there' ])   1 ==", ind('hi', [ 'well', 'hi', 'there' ])
#print "ind('i', 'team')                       4 ==", ind('i', 'team')
#print "ind(' ', 'outer exploration')          5 ==", ind(' ', 'outer exploration')



def letterScore( let ):
    
    if let.upper() in 'AEILNORSTU':
        return 1
    elif let.upper() in 'DG':
        return 2
    elif let.upper() in 'BCMP':
        return 3
    elif let.upper() in 'FHVWY':
        return 4
    elif let.upper() in 'K':
        return 5
    elif let.upper() in 'JX':
        return 8
    elif let.upper() in 'QZ':
        return 10
    else:
        return 0

#print letterScore('%')

def scrabbleScore( S ):
    if S == '':
        return 0
    else:
        return letterScore(S[0]) + scrabbleScore(S[1:])
        
#
# Tests
#
#print "scrabbleScore('quetzal'):  25 ==", scrabbleScore('quetzal')
#print "scrabbleScore('jonquil'):  23 ==", scrabbleScore('jonquil')
#print "scrabbleScore('syzygy'):   25 ==", scrabbleScore('syzygy')
#print "scrabbleScore('abcdefghijklmnopqrstuvwxyz'):  87 ==", scrabbleScore('abcdefghijklmnopqrstuvwxyz')
#print "scrabbleScore('?!@#$%^&*()'):  0 ==", scrabbleScore('?!@#$%^&*()')
#print "scrabbleScore(''):          0 ==", scrabbleScore('')



def one_dna_to_rna( c ):
    """ converts a single-character c from DNA
        nucleotide to complementary RNA nucleotide """
    if c == 'A': return 'U'
    elif c == 'C': return 'G'
    elif c == 'G': return 'C'
    elif c == 'T': return 'A'
    else:
        return ''
    
    
def transcribe( S ):
    if S == '':
        return ''
    else:
        return one_dna_to_rna(S[0]) + transcribe(S[1:])
      
#
# Tests
#
#print "transcribe('ACGT TGCA'):  'UGCAACGU' ==", transcribe('ACGT TGCA')
#print "transcribe('GATTACA'):     'CUAAUGU' ==", transcribe('GATTACA')
#print "transcribe('cs5') :               '' ==", transcribe('cs5')
#print "transcribe('') :                  '' ==", transcribe('')


    
