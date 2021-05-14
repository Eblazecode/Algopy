"""ADVANCE  LISTING"""
subject = ["maths", "Eng", "Geo", "phy"]
# printing all items
print(subject)
# Singles
for x in subject:
    print(x)

# printing items with "e"

for y in subject:
    subject2 = [x for x in range(len(subject))]
    print(subject2)
    #printing the second element of n the array
    firstindex = subject2[2]
    print(firstindex)

# SORTING
desc = subject.sort(reverse=True)
print(desc)



arrynum1 = [0,34,54,43, 32, 24, 6, 78, 887, 23, 1, 3]
arrynum2 = []
print(arrynum1[5: 10])
for x in arrynum1:
    if x > 1 :
        x = x/2
        arrynum2.append(x)
        print(arrynum2)