guest = ["Mike", "Michael", "Manny"]
# Learnt methods
# title() -> Upper case every first letter of each word
# upper() -> All upper
# lower() -> All lower
# rstrip() -> removes extra whitespaces from the right
# lstrip() -> removes extra whitespaces from the left
# strip() -> something.rstrip().lstrip()
# append() -> append to the back of the list
# insert(i, string) -> append string to the ith index
# pop(i) -> removes the last element (or the ith element) and returns that element
# remove(object) -> removes the object from the list without knowing its index
# sort(reverse = boolean) -> sorts the list alphabetically or whatever the parameter tells it to (does not return anything)
# reverse() -> reverses the list (does not return anything)

# Learnt statements
# del array[i] -> deletes the ith index from array
# for something in somethings -> iterates through all element from somethings starting from 0th index

# Learnt functions
# len(object) -> tells you the length of the object
# range(start, number) -> range is in fact an immutable sequence object instead of a list, [0, number)

# Differences
# del Vs pop -> pop: reusing a single element; del: sdelete multiple elements
# 
balls = range(4)
print(balls)