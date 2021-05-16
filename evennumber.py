"""TEST FOR ODD AND EVEN NUMBER
"""

class Numbertype :
    def __init__(self, n ):
        self. n = n

    def evennum(self):
        result = self.n % 2
        if result > 0 :
            print(" the number ", self.n , "is ODD")
        else:
            print(" the  number is even " , self.n)
    def findeven(self):
        numarrry = []
        for x in range(self.n):

            #creating of n integers
            numarrry.append(x)
            for i in numarrry:
                even = i % 2
                if even == 0:
                    numarrry.append(i)


tester = Numbertype(4)
tester.evennum()
tester.findeven()