# A MODULE FOR BASIC MATHS CALCULATIONS
class mathssolver:
    def __init__(self, principal, rate,time,):
        self.principal = principal
        self.rate = rate
        self.time = time

    def simpleint(self):
        calculate = (self.principal  * self.rate *self.time)/100
        vals= {
            "P": self.principal,
            "R": self.rate,
            "T": self.time
        }
        for x, y in vals.items():
            print(x,"==", y)
        print("The simple interest is \n=", "\nthe value")
        print(calculate)
