# I'll try to finish until chapter 10

# Normal class
# class restaurant():
#     def __init__(self, name, type):
#         self.name = name
#         self.type = type
#         self.isOpen = 0
#         self.number_served = 0
    
#     def describe(self):
#         print(self.name + " " + self.type + " " + str(self.number_served))
    
#     def open(self):
#         self.isOpen = 1
#         print(self.name + " is open")
#     def set(self, number):
#         self.number_served = number
#     def incremenet(self):
#         self.number_served = self.number_served + 1 

# gay = restaurant("ball", "china")
# print(gay.name, gay.type)

# gay.describe()

# gay.open()

# gay.set(100)
# gay.describe()
# gay.incremenet()
# gay.describe()

# # Inheritance

# class iceCreamStand(restaurant):
#     def __init__(self, name):
#         super().__init__(name, "ice cream stand")
#         self.flavours = ["vanilla", "choco", "mint"]
    
#     def print_flavours(self):
#         for flavour in self.flavours:
#             print(flavour)

# ice = iceCreamStand("new ice")
# ice.print_flavours()
# ice.describe()

# from day5_3 import user
# from day5_2 import permissions

# class admin(user):
#     def __init__(self, first, last):
#         super().__init__(first, last)
#         self.permission = permissions()
    



# bob = admin("Bob", "Load")
# bob.greet()
# bob.increment()
# print(bob.login_attempts)
# bob.reset()
# print(bob.login_attempts)
# bob.permission.show_perms()

# file objects
# file_path = "/Users/jeromeparungao/learnpython/learn-python/days/texig.txt"
# try:
#     # with open(file_path, "w") as file_object:
#     #     while(True):
#     #         name = str(input("Enter your name"))
#     #         if (name == "-1"):
#     #             break
#     #         file_object.write(name + "\n")
#     with open(file_path, "r") as file_object:
#         contents = file_object.read()
#         print(contents.rstrip())
# except FileNotFoundError:
#     print("File not found")

# try except
# try:
#     print(5/0)
# except ZeroDivisionError:
#     print("Dividing by 0")

# function
# split(), splits the sentence into a list of words with " " as the delimeter

# file_path = "/Users/jeromeparungao/learnpython/learn-python/days/book.txt"
# dictionary = {}
# with open(file_path, "r") as file_object:
#     contents = file_object.read()
#     words = contents.split()
#     for word in words:
#         dictionary[word.lower()] = dictionary.get(word.lower(), 0) + 1

# sorted_words = sorted(dictionary.items(), key=lambda item: item[1], reverse=True)
# file_path = "/Users/jeromeparungao/learnpython/learn-python/days/balls.txt"
# with open(file_path, "w") as file_object:
#     for word, count in sorted_words:
#         file_object.write(word + " " + str(count) + "\n")

# import json
# numbers = [2, 3, 5, 7, 11, 13]
# filename = 'numbers.json'
# with open(filename, 'w') as f_obj:
#     json.dump(numbers, f_obj)

# unit testing
# import unittest
# from name_function import get_formatted_name

# class NamesTestCase(unittest.TestCase):
#     """Tests for 'name_function.py'."""

#     def test_first_last_name(self):
#     """Do names like 'Janis Joplin' work?"""
#     formatted_name = get_formatted_name('janis', 'joplin')
#     self.assertEqual(formatted_name, 'Janis Joplin')

# unittest.main()

# assertEqual(a, b) Verify that a == b
# assertNotEqual(a, b) Verify that a != b
# assertTrue(x) Verify that x is True
# assertFalse(x) Verify that x is False
# assertIn(item, list) Verify that item is in list
# assertNotIn(item, list) Verify that item is not in list

# def setUp(): -> automatically runs setUp() before running tests

import unittest

class Employer():
    def __init__(self, first, last, salary):
        self.first = first
        self.last = last
        self.salary = salary
    
    def raiseSalary(self, increase = 5000):
        self.salary  = self.salary + increase

class EmployerTestCase(unittest.TestCase):
    def setUp(self):
        self.user = Employer("John", "Doe", 0)
    
    def test_give_default_raise(self):
        self.user.raiseSalary()
        self.assertEqual(self.user.salary, 5000)
    
    def test_give_special_raise(self):
        self.user.raiseSalary(1000)
        self.assertEqual(self.user.salary, 1000)

unittest.main()
