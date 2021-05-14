
# STACK OPERATIONS
""" function revstring(mystr) that uses a stack to reverse the characters in a string. """
def stringreverse (word):
    characterlist = []  # list constructor 
    for x in word.upper():
        characterlist.append(x)
    print("popped item>>", characterlist.pop()) # popping the last item of the list
    print("push item>>", characterlist.append('E'))  # Doesnt not return any value
    reversal = characterlist.reverse()
    print(characterlist)
    print("REVERSED STRING ", reversal)

stringreverse("Awesome")