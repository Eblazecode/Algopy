""" RECURSIVE PROGRAMS   """
# SUMMING THE ITEMS IN A LIST

# FACTORIAL NUMBER
import math

import turtle
def factorials(n):
    if n <= 1:
        print(" n! = ", 1)
    else:
        fact = 1
        for x in range(1,n+1):
            fact = fact * x
        print(fact)
factorials(5)

# MATHS FACTORIALS
print(math.factorial(5))


myTurtle = turtle.Turtle()
myWin = turtle.Screen()



#FIBONNACI SEQUENCE
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

def fibonacci(n):

    if n <= 0:
        return n
    else:
        firstterm = 0
        secterm = 1

        counter = 0
        seq= []
        while counter < n:
            next = firstterm + secterm
            firstterm = secterm
            secterm = next
            counter+=1
            seq.append(firstterm)

    print(seq)
fibonacci(10)


def fibo(n):
    if n < 0:
        print("ONLY POSTIVE")
    else:
        n1 =0
        n2 =1
    return fibo()