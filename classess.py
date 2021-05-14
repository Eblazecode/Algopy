""" BASIC OOPS CONCEPTS"""
class simpeinterest:
    def __init__(self,prin, rate, time):
        # COPY OF PASSED PARAMETER TO BE USED BY THE METHODS
        self.sprin= prin
        self.srate = rate
        self.stime = time
        #METHOD

    def solving(self):
        result = self.sprin * self.srate * self.stime / 100
        print(result)

# OBJECTS
mysimps = simpeinterest( 1200, 2, 2)
mysimps.solving()


# INHERITANCE
class Rates(simpeinterest):
    def rating(self):
        ratesolver = 100 / self.sprin * self.stime
        print( ratesolver)


# OBJECT FOR RATE
myrates = Rates(3000, 2, 5)
myrates.rating()