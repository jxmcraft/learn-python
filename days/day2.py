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
# range(start, number, increment) -> range is in fact an immutable sequence object instead of a list, [0, number)
# min(list) -> minimum of the list O(n)
# max(list) -> maximum of the list O(n)
# sum(list, number) -> sum of all elements in list + number
# Differences
# del Vs pop -> pop: reusing a single element; del: sdelete multiple elements
# ord() -> Gives the unicode of that character

# Fun fact about loops, the element i in the for loop is simply a copy of the element,
# not the actual element itself, so in the following code, numbers is unchanged.

numbers = range(1,6)
numbers = list(numbers)
for i in numbers:
    i = i ** 2

print(numbers)  

# To fix this, you need to access the elemnent square brackets 
# for i in range(len(numbers)): 
#   numbers[i] = i ** 2

## List comprehensions
# balls = [F(values) for values in range(something)]

## Splicing a list
# list[start: end] -> splits the list from start to end exclusive
#players = ['a' + chr(value) for value in range(0, 26)]
#print(players)
# ['a\x00', 'a\x01', 'a\x02', 'a\x03', 'a\x04', 'a\x05', 'a\x06', 'a\x07', 'a\x08', 'a\t', 'a\n', 'a\x0b', 'a\x0c', 'a\r', 'a\x0e', 'a\x0f', 'a\x10', 'a\x11', 'a\x12', 'a\x13', 'a\x14', 'a\x15', 'a\x16', 'a\x17', 'a\x18', 'a\x19']

players = [chr(ord('a') + value) for value in range(0, 26)]
print(players[0:2])

# From this example, we see that = copies that address of the original myfoods instead of creating new balls
myfoods = [players[0: 6]]
balls = myfoods
myfoods.append("ll")
print(myfoods)
print(balls)

# To make a new copy, we need to do this instead, which is shorthand for [myfoods[:]]
balls = [myfoods[:]]
myfoods.append("ll")
print(myfoods)
print(balls)

# tuple -> simply immutable lists that uses brackets instead of square brackets

# Until start of chapter 5 of python crash course 