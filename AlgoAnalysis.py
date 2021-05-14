"""SUMMING N EVEN INTEGERS USING A FUNCTION
 AND TESTING FOR TIME OF COMPLETION- BENCH MARKING"""

import time
def summation(n):
    start1 = time.time()
    i = 0
    for x in range(i,n):
        y = (n * (1 + n)) / 2
    print(y)
    end1 = time.time()
    print(start1,end1)
summation(10)



# PYTHON FUNCTION TO FIND THE MINIMUN, MAX  AND MEDIAN OF A  NUMBER IN A LIST

def listitemss(n):
    listnum = []
    for x in range(1,n+1):
     listnum.append(x)

    max_value = max(listnum)
    max_index = listnum.index(max_value)

    min_value = min(listnum)
    min_index = listnum.index(min_value)
    median_index = int((min_index + max_index / 2))
    median_value = listnum[median_index]

    print(listnum)
    print("max num = ", max_value)
    print("max index = ", max_index)
    print("min num",min_value)
    print("min index",min_index)
    print("median index" , median_index)
    print("median val" , median_value)
listitemss(15)




def sumOfN3(n):
    sttart12 = time.time()
    return (n*(n+1))/2
    end2 = time.time()
print(sumOfN3(10))