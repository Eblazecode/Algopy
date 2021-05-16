""" MERGE SORT
"""

def merge_sort(numslist):
    list_len = len(numslist)
    if list_len > 1:
        mid = list_len // 2
        leftlist = numslist[:mid]
        rigthlist= numslist[mid:]

    #RECURSIVE CALL OF EACH HALF.
        merge_sort(leftlist)
        merge_sort(rigthlist)

    #ITERATOR FOR EACH HALF
        x = 0
        y = 0

    #ITERATOR FOR MAIN LIST NUMLSIT
        k = 0
        while x < len(leftlist) and  y < len(rigthlist):
            if leftlist[x] < rigthlist[y]:
                numslist[k] = leftlist[x]
                x += 1

            else:
                numslist[k] = rigthlist[y]
                y += 1
            k += 1
        while x < len(leftlist):
            numslist[k] = leftlist[x]
            x += 1
            k += 1
        while y < len(rigthlist):
            numslist[k] = rigthlist[y]
            y += 1
            k += 1

mylist = [1,40,6,47,9,12,73,5,2,10]
merge_sort(mylist)
print(mylist)

# USING PYTHON  SORT METHOD ---(<-O  O- >)  lol
mylist2= mylist.copy()
mylist2.sort()
print(mylist2)