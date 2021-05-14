
fileobj = open("ope.txt","r")

for x in fileobj:
    print(x)

fileobj2 = open("fibo.txt","w")
if fileobj2:
      print("created successfully ")