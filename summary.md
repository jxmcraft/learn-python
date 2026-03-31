# Day 1-4
# Learnt methods
title() -> Upper case every first letter of each word
upper() -> All upper
lower() -> All lower
rstrip() -> removes extra whitespaces from the right
lstrip() -> removes extra whitespaces from the left
strip() -> something.rstrip().lstrip()
append() -> append to the back of the list
insert(i, string) -> append string to the ith index
pop(i) -> removes the last element (or the ith element) and returns that element
remove(object) -> removes the object from the list without knowing its index
sort(reverse = boolean) -> sorts the list alphabetically or whatever the parameter tells it to (does not return anything)
reverse() -> reverses the list (does not return anything)
items() -> returns a view object containing all dictionary key-value pairs as a list of tuple 
keys() -> returns keys of a dictionary
values() -> returns values of a dictionary

# Learnt statements
del array[i] -> deletes the ith index from array
for something in somethings -> iterates through all element from somethings starting from 0th index
if elif else -> if statement
while (something) -> while loop 
break -> break loop
continue -> continue

# Learnt functions
len(object) -> tells you the length of the object
range(start, number, increment) -> range is in fact an immutable sequence object instead of a list, [0, number)
min(list) -> minimum of the list O(n)
max(list) -> maximum of the list O(n)
sum(list, number) -> sum of all elements in list + number
Differences
del Vs pop -> pop: reusing a single element; del: sdelete multiple elements
ord() -> Gives the unicode of that character
input("words") -> takes in console input

# Dictionaries
{'key1' : 'result1', 'key2' : 'result2', ...}, access the element by using square brackets
to add more elements, simply do dictionary['something'] = something2  
dictionaries with loops: for key, value in dictionary.items()
you can also access the value by for key value in dictionary: function(dictionary[key])

# Functions
def function(parameter1 = default, paramter2, ...) -> normal functions
function(parameter1 = "", paramter2 = "") -> to avoid confusion
Note: when passing a list as a parameter, it references the list instead of just copying it
If you want to pass a copy, simply pass list[:] into the parameter

# Day 5

# Modules 
if we want to use a module, we first import module_name, then module_name.function_name()
we can also import a specific function by from module_name import function_name
we can also give it an alias by from module_name important function_name as alias
we can import all the functions from a module by from module_name import * 
import module_name vs from module_name import * : the first requires you to call the module_name to access the functions
i.e. module_name.function() whereas the latter allows wildcard import, i.e. you can call the function
without needing the name, i.e. function()


