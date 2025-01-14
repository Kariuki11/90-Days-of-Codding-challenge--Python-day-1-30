import math
import datetime

# Input and Output
# Input allows you to take user input, and output allows you to display information to the user.

# Example of input and output
name = input("Enter your name: ")
print(f"Hello, {name}!")

# Loops
# Loops are used to repeat a block of code multiple times.

# Example of a for loop
for i in range(5):
    print(f"Iteration {i}")

# Example of a while loop
count = 0
while count < 5:
    print(f"Count is {count}")
    count += 1

# Data Structures
# Python has several built-in data structures, such as lists, tuples, sets, and dictionaries.

# Example of a list
fruits = ["apple", "banana", "cherry"]
print(fruits[0])  # Output: apple

# Example of a tuple
coordinates = (10, 20)
print(coordinates[1])  # Output: 20

# Example of a set
unique_numbers = {1, 2, 3, 4, 5}
print(unique_numbers)

# Example of a dictionary
person = {"name": "Alice", "age": 25}
print(person["name"])  # Output: Alice

# File Handling
# File handling allows you to read from and write to files.

# Example of writing to a file
with open("example.txt", "w") as file:
    file.write("Hello, world!")

# Example of reading from a file
with open("example.txt", "r") as file:
    content = file.read()
    print(content)  # Output: Hello, world!

# Error Handling
# Error handling allows you to handle exceptions gracefully using try, except, and finally blocks.

# Example of error handling
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
finally:
    print("This block is always executed.")

# Basic Modules
# Python has many built-in modules that you can import and use in your programs.

# Example of using the math module

print(math.sqrt(16))  # Output: 4.0

# Example of using the datetime module

now = datetime.datetime.now()
print(now)