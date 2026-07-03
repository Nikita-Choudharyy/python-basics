"""
=========================================================
Python Basics
=========================================================

Repository : python-basics
File       : 01_Basics.py
Author     : Nikita Choudhary

Description:
------------
This file demonstrates the fundamental concepts of Python,
including variables, data types, operators, conditional
statements, loops, and functions.

This repository documents my Python learning journey.
The examples are written for revision and to help other
beginners understand Python concepts.

Learning Objectives:
--------------------
✔ Understand variables and data types
✔ Perform arithmetic operations
✔ Use conditional statements
✔ Write loops
✔ Create reusable functions

=========================================================
"""

# =========================================================
# 1. VARIABLES
# =========================================================

# Variables are used to store data.
# Python automatically determines the data type of a variable.

name = "Nikita"
age = 21
is_student = True

print("\nVariables")
print("-" * 30)

print("Name      :", name)
print("Age       :", age)
print("Student   :", is_student)

print("\nData Types")
print("Type of name       :", type(name))
print("Type of age        :", type(age))
print("Type of is_student :", type(is_student))

# Expected Output:
#
# Variables
# ------------------------------
# Name      : Nikita
# Age       : 21
# Student   : True
#
# Data Types
# Type of name       : <class 'str'>
# Type of age        : <class 'int'>
# Type of is_student : <class 'bool'>


# =========================================================
# 2. ARITHMETIC OPERATORS
# =========================================================

# Operators are used to perform mathematical calculations.

marks = 85
bonus_marks = 5

print("\nArithmetic Operators")
print("-" * 30)

print("Addition       :", marks + bonus_marks)
print("Subtraction    :", marks - bonus_marks)
print("Multiplication :", marks * bonus_marks)
print("Division       :", marks / bonus_marks)
print("Floor Division :", marks // bonus_marks)
print("Modulus        :", marks % bonus_marks)
print("Exponent       :", marks ** bonus_marks)

# Expected Output:
#
# Addition       : 90
# Subtraction    : 80
# Multiplication : 425
# Division       : 17.0
# Floor Division : 17
# Modulus        : 0
# Exponent       : 4437053125


# =========================================================
# 3. CONDITIONAL STATEMENTS
# =========================================================

# Check whether a number is even or odd.

number = 7

print("\nConditional Statement")
print("-" * 30)

if number % 2 == 0:
    print(number, "is Even")
else:
    print(number, "is Odd")

# Expected Output:
#
# 7 is Odd


# =========================================================
# 4. LOOPS
# =========================================================

# A loop is used to execute a block of code repeatedly.

print("\nFor Loop")
print("-" * 30)

print("Numbers from 1 to 5:")

for i in range(1, 6):
    print(i)

# Expected Output:
#
# Numbers from 1 to 5:
# 1
# 2
# 3
# 4
# 5


# =========================================================
# 5. FUNCTIONS
# =========================================================


def square(num):
    """
    Return the square of a given number.

    Parameters:
        num (int or float): Number to be squared.

    Returns:
        int or float: Square of the given number.
    """
    return num * num


print("\nFunctions")
print("-" * 30)

print("Square of 4  :", square(4))
print("Square of 10 :", square(10))

# Expected Output:
#
# Square of 4  : 16
# Square of 10 : 100


# =========================================================
# BEST PRACTICES
# =========================================================

# ✔ Use meaningful variable names.
# ✔ Follow proper indentation.
# ✔ Write comments where necessary.
# ✔ Divide code into small reusable functions.
# ✔ Follow PEP 8 coding standards.
# ✔ Keep your code clean and readable.


# =========================================================
# COMMON BEGINNER MISTAKES
# =========================================================

# ❌ Example of an invalid variable name
#
# 2name = "Nikita"
#
# Variable names cannot start with a number.

# ✅ Correct

# name2 = "Nikita"


# =========================================================
# PRACTICE QUESTIONS
# =========================================================

# Q1. Create variables to store your name, age, and city.
#
# Q2. Print your favourite movie and favourite programming language.
#
# Q3. Take two numbers from the user and print:
#     - Addition
#     - Subtraction
#     - Multiplication
#     - Division
#
# Q4. Check whether a number is positive, negative, or zero.
#
# Q5. Print numbers from 1 to 10 using a for loop.
#
# Q6. Create a function that returns the cube of a number.


# =========================================================
# KEY TAKEAWAYS
# =========================================================

"""
Today You Learned:

✔ Variables
✔ Data Types
✔ print() Function
✔ type() Function
✔ Arithmetic Operators
✔ Conditional Statements
✔ for Loop
✔ Functions
✔ Python Best Practices

Happy Coding! 🚀
"""

# =========================================================
# End of File
# =========================================================
