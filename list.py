#welcome to my list 
message = "hello world"
print(message)
subjects = ["physics","chemistry","bioogy","maths"]
print((subjects))

#printing
for x in subjects:
    print(x)

#updating
subjects[2]= "zoology"
print("the new subjects are \n")
print(subjects)

#methods
subjects.append("botany")
print(subjects)
#copying method
books1 = subjects.copy()
newsub = ["geography", "earth science", "astronomy"]
books2 = subjects.extend(newsub)
print(books1)
print("using extend method")
print(subjects)

#sorting
subjects.sort()
print("sorting")
print(subjects)



# ARRAY NUMBERS
numbers = [1,3,4,5,6,1]
for x in numbers:
    print(x)

# exponentiating each output
for x in numbers:
    x **=x
    print(x)

# program to find perfect square from 1 - 100
squares = [1,2,3,4,5,6,7,8,9]
print("perfect squares 1-100\n")
for x in squares:
    x **=2
    print(x)

number = 3
for y in range(1,10):
    print(y,"*",number,"=" ,y * number)

