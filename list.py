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
