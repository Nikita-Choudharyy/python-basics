"""
=========================================================
Python Functions
=========================================================

Repository : python-basics
File       : 01_Functions.py
Author     : Nikita Choudhary

Description:
------------
This file demonstrates Python functions, including
function definition, parameters, return values,
default arguments, keyword arguments, and practical
examples.

This repository documents my Python learning journey.
The examples are written for revision and to help other
beginners understand Python concepts.

Learning Objectives:
--------------------
✔ Define functions
✔ Pass arguments to functions
✔ Use default parameters
✔ Return values from functions
✔ Understand keyword arguments
✔ Use *args
✔ Solve simple problems using functions

=========================================================
"""

# =========================================================
# 1. DEFINING A FUNCTION
# =========================================================

# A function is a reusable block of code.

def greet():
    print("Hello, welcome to Python Functions!")

print("\nDefining a Function")
print("-" * 30)

greet()

# Expected Output:
#
# Hello, welcome to Python Functions!


# =========================================================
# 2. FUNCTION WITH PARAMETERS
# =========================================================

# Parameters allow functions to receive values.

def add(a, b):
    return a + b

print("\nFunction with Parameters")
print("-" * 30)

result = add(5, 3)

print("Addition Result :", result)

# Expected Output:
#
# Addition Result : 8


# =========================================================
# 3. DEFAULT PARAMETERS
# =========================================================

def greet_user(name="User"):
    print("Hello", name)

print("\nDefault Parameters")
print("-" * 30)

greet_user()
greet_user("Alex")

# Expected Output:
#
# Hello User
# Hello Alex


# =========================================================
# 4. KEYWORD ARGUMENTS
# =========================================================

def student(name, age):
    print("Name :", name)
    print("Age  :", age)

print("\nKeyword Arguments")
print("-" * 30)

student(age=20, name="Amit")

# Expected Output:
#
# Name : Amit
# Age  : 20


# =========================================================
# 5. RETURNING MULTIPLE VALUES
# =========================================================

def calculate(a, b):
    total = a + b
    difference = a - b
    return total, difference

print("\nReturning Multiple Values")
print("-" * 30)

total, difference = calculate(10, 5)

print("Sum        :", total)
print("Difference :", difference)

# Expected Output:
#
# Sum        : 15
# Difference : 5


# =========================================================
# 6. *ARGS
# =========================================================

# *args allows passing multiple arguments.

def addition(*numbers):
    return sum(numbers)

print("\nUsing *args")
print("-" * 30)

print(addition(10, 20))
print(addition(1, 2, 3, 4, 5))

# Expected Output:
#
# 30
# 15


# =========================================================
# 7. FUNCTION INSIDE A LOOP
# =========================================================

def square(num):
    return num * num

print("\nFunction Inside Loop")
print("-" * 30)

for i in range(1, 6):
    print(f"Square of {i} :", square(i))

# Expected Output:
#
# Square of 1 : 1
# Square of 2 : 4
# Square of 3 : 9
# Square of 4 : 16
# Square of 5 : 25


# =========================================================
# 8. PRACTICAL EXAMPLE - EVEN OR ODD
# =========================================================

def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    return "Odd"

print("\nEven or Odd")
print("-" * 30)

print(check_even_odd(10))
print(check_even_odd(7))

# Expected Output:
#
# Even
# Odd


# =========================================================
# 9. PRACTICAL EXAMPLE - MAXIMUM NUMBER
# =========================================================

def find_max(a, b):
    if a > b:
        return a
    return b

print("\nMaximum Number")
print("-" * 30)

print("Maximum Value :", find_max(15, 20))

# Expected Output:
#
# Maximum Value : 20


# =========================================================
# BEST PRACTICES
# =========================================================

# ✔ Keep functions small and focused.
# ✔ Use meaningful function names.
# ✔ Return values instead of printing whenever possible.
# ✔ Write reusable functions.
# ✔ Add docstrings for larger functions.


# =========================================================
# COMMON BEGINNER MISTAKES
# =========================================================

# ❌ Wrong

# print(add())

# Missing required arguments.

# ❌ Wrong

# return outside a function

# This raises a SyntaxError.

# ✅ Correct

# Define the function first,
# then call it with valid arguments.


# =========================================================
# PRACTICE QUESTIONS
# =========================================================

# Q1. Write a function to calculate the cube of a number.
#
# Q2. Write a function to calculate the area of a rectangle.
#
# Q3. Write a function to find the largest of three numbers.
#
# Q4. Write a function to check whether a number is prime.
#
# Q5. Create a function with default arguments.
#
# Q6. Create a function using *args.
#
# Q7. Return multiple values from a function.


# =========================================================
# KEY TAKEAWAYS
# =========================================================

"""
Today You Learned:

✔ Defining Functions
✔ Parameters
✔ Default Parameters
✔ Keyword Arguments
✔ Returning Values
✔ Returning Multiple Values
✔ *args
✔ Functions Inside Loops

Happy Coding! 🚀
"""

# =========================================================
# End of File
# =========================================================
