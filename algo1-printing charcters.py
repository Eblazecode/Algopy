""" PRINTING CHARACTER OF A WORD LIST """
subject = ["maths", "Eng", "Geo", "phy"]
letterlist=[] #list constructor
for aword in subject:  # >> iterates over the list
    for aletter in aword:
        letterlist.append(aletter)
print(letterlist)

#SPECIFIC
letterlist2=[]
for aword1 in subject:
    for aletter1 in aword1:
        if "a" in aletter1:
            aletter1.replace("a","b")
            letterlist2.append(aletter1)
print(letterlist2)


# CREATING A SQUARE LIST - MULTIPIES OF 5
multipliers = [0,1,2,3,4,5,6,7,8,9,10,11,12]
multipier= []
for x in multipliers:
    x *=5
    multipier.append(x)
# multiples of 5 in a lsit
print(multipier)
# single printing out
for y in multipier:
    print(y)

#Even numbers in the multipliers
Evenmul = []
for even in multipier:
    even % 2
    if even == 0:
        Evenmul.append(even)
print(Evenmul)




