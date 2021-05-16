"""
PALINDROME CHECKER
"""


def palindrome(word):
    # reversing the word and checking for consistency
    if word[::-1] == word:
        print(" A PAL")
    else:
        return False

theword = "HANNAH".lower()
result = palindrome(theword)
print(result)

# CHARACTER BY CHARACTER ITERATIVE METHOD
def palindrome_checker(word1):
    wordlen = len(word1)
    mid =  wordlen//2
    upper = wordlen - 1

    for i in range(0, mid):
        if word1[i] != word1[upper - i]:
            return False
        else:
            return True


word2 = "HANNAH!3323"
word2 = word2[1:5] # Slcing the non elements char that stop HANNAH from being a palindrome
result1 = palindrome_checker(word2)
print(result1)