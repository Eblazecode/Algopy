"""
CODILITY DEMO
A non-empty array A consisting of N integers is given. The array contains an odd number
 of elements, and each element of the array can be paired with another element that
 has the same value, except for one element that is left unpaired.

For example, in array A such that:

  A[0] = 9  A[1] = 3  A[2] = 9
  A[3] = 3  A[4] = 9  A[5] = 7
  A[6] = 9
the elements at indexes 0 and 2 have value 9,
the elements at indexes 1 and 3 have value 3,
the elements at indexes 4 and 6 have value 9,
the element at index 5 has value 7 and is unpaired.
Write a function:

class Solution { public int solution(int[] A); }

that, given an array A consisting of N integers fulfilling the above conditions, returns the value of the unpaired element.

For example, given array A such that:

  A[0] = 9  A[1] = 3  A[2] = 9
  A[3] = 3  A[4] = 9  A[5] = 7
  A[6] = 9
the function should return 7, as explained in the example above.

"""


def unpaired(Arey):
    arraylen = len(Arey)
    uppperbound = arraylen - 1
    lowerbound = 0
    mid = arraylen // 2

    for i in range(0, arraylen,2):

        for j in range(0, arraylen,2):
            if Arey[i] == Arey[j] and i != j:
                return False
            else:
                return Arey[i]



thelist = [9, 3, 9, 3, 9, 7, 9]
thelist.sort()
result = unpaired(thelist)
print(result)



# The sum of two odd numbers are even  e'g 3 = 3 = 6 , 9+ 9 = 18 , 21 + 21 = 42
# Thus we find from the array the sum of number of occurrence of an element if it is even or odd
 # TESTING EVEN- NESS
# if EVEN : using the modulo division of 2 remainder == 0 solution is not found
# if ODD : using the modulo division of 2 remainder  == 1 solution is  found

def oddoccurence( odds):
    arraylen = len(odds)

    for i in odds:
        #this checks for number of time a particular element occurs in the list
        if odds.count(i) % 2 == 1:
            return i
        else:
            continue


thelist = [9, 3, 9, 3, 9, 7, 9]
result = oddoccurence(thelist)
print(result)
