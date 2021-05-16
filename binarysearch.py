"""
PSUEDOCODE
Procedure binary_search
   A ← sorted array
   n ← size of array
   x ← value to be searched

   Set lowerBound = 1
   Set upperBound = n

   while x not found
      if upperBound < lowerBound
         EXIT: x does not exists.

      set midPoint = lowerBound + ( upperBound - lowerBound ) / 2

      if A[midPoint] < x
         set lowerBound = midPoint + 1

      if A[midPoint] > x
         set upperBound = midPoint - 1

      if A[midPoint] = x
         EXIT: x found at location midPoint
   end while

end procedure
"""
"""
"""
# recursive method  method
def binarysearch( numarry ,  lower_bd, upper_bd, key):
    if upper_bd >= lower_bd:

        mid = (lower_bd + (upper_bd - lower_bd))//2

        if (numarry[mid] == key ):
            return mid
        elif ( numarry[mid] > key ):

            # the key item search can be found in the lower bound half of the array
            # calling for recursive operation on the mid value for new upper bound
            return binarysearch(numarry, lower_bd, mid-1, key)
        else:
            # the key item search can be found in the upper bound half of the array
            return binarysearch(numarry, mid+1, upper_bd, key)
    else:
        return  -1

thelist = [1, 4, 5, 10, 13, 20 , 15,59]
upperbound = len(thelist) - 1
result = binarysearch(thelist, 0, upperbound, 1)
if thelist != -1:
     print( " Element can be found at ", result, "precisely = ", thelist[result] )

else:
    print("Element is not in the array")

