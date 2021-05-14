""" RECURSIVE PROGRAMS   """
# SUMMING THE ITEMS IN A LIST

def sumlist(intlist):
    lenlist= len(intlist)

    for n in range(lenlist):
        n = n +1
        print(n)

thelist = []
def listing(x):
    for i in range(x):
        thelist.append(i)
    print(thelist)

listing(10)
sumlist(thelist)
