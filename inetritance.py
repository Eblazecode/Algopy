#mutli-level inheritance

class Animals:
     def livinfthings(self):#TOP LEVEVL PARENT CLASS
        print("Animals are living things")
class Dogs(Animals):
    def response(self):
        print("Animals like dogs bark")
class puppies(Dogs):  #CHILD CLASS
    def nutrition(self): # METHOD
        print("Animals like dogs have puppies that loves taking milk")
        #METHOD OVERIDING
    def livinfthings(self):
        print("overiding: puppies are animals ")
bingo = puppies() #OBJECT
bingo.nutrition()
bingo.response()
bingo.livinfthings()


