"""SUMMING N EVEN INTEGERS USING A LIST """

sumint = []  #.. LIST  CONSTRUCTOR CREATED
i = 0
while i < 10:  # While loop to declared or created the list items
    i = i + 1  # iterating
    # Appending or adding the items to the list
    sumint.append(i)
    # summing the elements in the ist  using the sum function
    y = sum(sumint)
    print(i)
print(sumint)
print( y )



# FOR LOOP
listforlp = []
for n in range(1,11,1):
    showitems = print(n)
    listforlp.append(n)
showlist = print(listforlp)
sumitems = sum(listforlp)
print(sumitems)
