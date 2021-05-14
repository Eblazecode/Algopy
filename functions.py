# infinite monkey theorem
"""
The theorem states that a monkey hitting keys
at random on a typewriter keyboard for an
 infinite amount of time will almost surely type a
  given text, such as the complete works
  of William Shakespeare


  Well, suppose we replace a monkey with a Python function.
  How long do you think it would take for a Python function
   to generate just one sentence of Shakespeare?
   The sentence we’ll shoot for is: “methinks it is like a weasel”

we’ll  simulate this is to write a function that generates
  a string that is 28 characters long by choosing random letters
from the 26 letters in the alphabet plus the space.
 We’ll write another function that will score each generated
  string by comparing the randomly generated string to the goal.

A third function will repeatedly call generate and score,
then if 100% of the letters are correct we are done.
 If the letters are not correct then we will generate a whole new string.
 To make it easier to follow your program’s progress this third function
  should print out the best string generated so far
  and its score every 1000 tries.
"""
import random

# String

import random
import string

letterarry=[]
charcarry=[]
def get_random_alphanumeric_string(length):
    letters_and_digits = string.ascii_lowercase
    result_str = ''.join((random.choice(letters_and_digits) for i in range(length)))
    print("Random String is:", result_str)
    letterarry.append(result_str) # converting the letter to a string array
    print(letterarry)
    for charc in letterarry:# converting the letter to an  characters array
        for aletter in charc:
            charcarry.append(aletter)
        print(charcarry)

get_random_alphanumeric_string(28)






n = 5
# NEWTON'S METHOD OF GUESSING FOR A SQUARE OF A METHOD
def squareroot(n):
    initilguess = n/2
    olguess = initilguess
    div= (n/olguess)


    baracket = olguess + div
    for k in range(20):
        initilguess = 0.5 * baracket
    print(initilguess)

squareroot(10)


