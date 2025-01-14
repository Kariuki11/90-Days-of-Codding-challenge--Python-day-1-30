import math
from math import pi

# Introduction to Python

# Python is a high-level, interpreted programming language known for its simplicity and readability.
# It supports multiple programming paradigms, including procedural, object-oriented, and functional programming.

# Important Concepts in Python:

# 1. Variables:
# Variables are used to store data that can be used and manipulated throughout a program.
# In Python, you don't need to declare the type of a variable; it is inferred from the value assigned to it.

# Example:
x = 10
y = "Hello, World!"
z = 3.14

# 2. Data Types:
# Python has several built-in data types, including:
# - int: Integer numbers
# - float: Floating-point numbers
# - str: Strings (text)
# - bool: Boolean values (True or False)
# - list: Ordered, mutable collections
# - tuple: Ordered, immutable collections
# - dict: Unordered, mutable collections of key-value pairs
# - set: Unordered collections of unique elements

# Examples:
integer_var = 42
float_var = 3.14159
string_var = "Python is awesome!"
boolean_var = True
list_var = [1, 2, 3, 4, 5]
tuple_var = (1, 2, 3, 4, 5)
dict_var = {"name": "Alice", "age": 30}
set_var = {1, 2, 3, 4, 5}

# 3. Control Structures:
# Python provides various control structures for decision-making and looping.

# if-elif-else:
if x > 5:
    print("x is greater than 5")
elif x == 5:
    print("x is equal to 5")
else:
    print("x is less than 5")

# for loop:
for i in range(5):
    print(i)

# while loop:
count = 0
while count < 5:
    print(count)
    count += 1

# 4. Functions:
# Functions are reusable blocks of code that perform a specific task.
# They are defined using the `def` keyword.

# Example:
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))

# 5. Classes and Objects:
# Python supports object-oriented programming (OOP) with classes and objects.
# A class is a blueprint for creating objects, and an object is an instance of a class.

# Example:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"My name is {self.name} and I am {self.age} years old."

person1 = Person("Bob", 25)
print(person1.introduce())

# 6. Modules and Packages:
# Modules are files containing Python code, and packages are directories containing multiple modules.
# They help organize and reuse code.

# Example:
# Importing a built-in module
print(math.sqrt(16))

# Importing a specific function from a module
print(pi)

# This is a brief introduction to Python and some of its important concepts.
# As you continue learning, you'll discover more advanced features and libraries that make Python a powerful and versatile language.