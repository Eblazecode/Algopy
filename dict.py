#PYTHON DICTIONARY
import randomfunctions
books ={
    "novels": "things fall a part",
    "science" : "Physics text",
    "motivational" : "Richest man in babylon",
}
print(books["novels"])
#updating the values
books["motivational"] = "think big"
print(books)

#printing the values of dict using a loop
for x in books.values():
    print(x)
print(len(books))

#changeing to a list
mylist = list(books.keys())
print(type(mylist))
print(mylist)
print(mylist[2])
for x in mylist:
    print(x)

print("EMPLOYEE DETAILS")
employee = {
    "name" : "musa",
    "dept" : "IT",
    "degree" : "BSC",
    "state" : "Kano",
    "hobby" : "chess",
}
print(employee)
# new details
employee["name"] = str(input())
employee["dept"] = str(input())
employee["degree"] = str(input())
employee["state"] = str(input())
employee["hobby"] = str(input())

for x,y in employee.items():
    print(x,":",y)
#A MODULE CREATED
randomfunctions.nameteller(employee["name"],employee["state"],employee["degree"])