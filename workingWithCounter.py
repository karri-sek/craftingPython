from collections import Counter
myList = [1,2,3,3,1,3,55,5,4,34,34,3,323,3,1,1,13,4,55]

print("Counter ",Counter(myList))

print(" Counter values ", Counter(myList).values())

print(" Counter keys ", Counter(myList).keys())

print(" Counter entries ", Counter(myList).items())

#Search for element in counter

print(" is element present return or 1", Counter(myList)[599])
