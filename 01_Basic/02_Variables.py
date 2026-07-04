"""
=========================================================
Python Variables and Data Types
=========================================================

Repository : python-basics
File       : 02_Variables.py
Author     : Nikita Choudhary

Description:
------------
This file explains Python variables and the most commonly
used data types. It also demonstrates multiple variable
assignment, dynamic typing, and constant naming conventions.

This repository documents my Python learning journey.
The examples are written for revision and to help other
beginners understand Python concepts.

Learning Objectives:
--------------------
✔ Understand variables
✔ Learn common Python data types
✔ Check data types using type()
✔ Perform multiple variable assignment
✔ Understand dynamic typing
✔ Follow constant naming conventions

=========================================================
"""

# =========================================================
# 1. BASIC VARIABLE ASSIGNMENT
# =========================================================

# Variables are used to store information.
# Python automatically determines the data type.

name = "Alex"
age = 25
height = 5.8
is_student = True

print("\nBasic Variable Assignment")
print("-" * 30)

print("Name       :", name)
print("Age        :", age)
print("Height     :", height)
print("Is Student :", is_student)

# Expected Output:
#
# Name       : Alex
# Age        : 25
# Height     : 5.8
# Is Student : True


# =========================================================
# 2. COMMON DATA TYPES
# =========================================================

score = 95            # Integer
percentage = 89.5     # Float
grade = "A"           # String
passed = True         # Boolean

print("\nCommon Data Types")
print("-" * 30)

print("Score      :", score)
print("Percentage :", percentage)
print("Grade      :", grade)
print("Passed     :", passed)

print("\nData Types")
print("Type of score      :", type(score))
print("Type of percentage :", type(percentage))
print("Type of grade      :", type(grade))
print("Type of passed     :", type(passed))

# Expected Output:
#
# Score      : 95
# Percentage : 89.5
# Grade      : A
# Passed     : True
#
# Data Types
# Type of score      : <class 'int'>
# Type of percentage : <class 'float'>
# Type of grade      : <class 'str'>
# Type of passed     : <class 'bool'>


# =========================================================
# 3. MULTIPLE VARIABLE ASSIGNMENT
# =========================================================

# Python allows assigning multiple variables in one line.

x, y, z = 10, 20, 30

print("\nMultiple Variable Assignment")
print("-" * 30)

print("x =", x)
print("y =", y)
print("z =", z)

# Expected Output:
#
# x = 10
# y = 20
# z = 30


# =========================================================
# 4. DYNAMIC TYPING
# =========================================================

# Python allows changing the data type of a variable.

value = 100

print("\nDynamic Typing")
print("-" * 30)

print(value, type(value))

value = "Python"

print(value, type(value))

# Expected Output:
#
# 100 <class 'int'>
# Python <class 'str'>


# =========================================================
# 5. CONSTANT NAMING CONVENTION
# =========================================================

# Python does not have true constants.
# By convention, constant names are written in UPPER_CASE.

PI = 3.14159
MAX_LIMIT = 1000

print("\nConstant Naming Convention")
print("-" * 30)

print("PI        :", PI)
print("MAX_LIMIT :", MAX_LIMIT)

# Expected Output:
#
# PI        : 3.14159
# MAX_LIMIT : 1000


# =========================================================
# BEST PRACTICES
# =========================================================

# ✔ Use meaningful variable names.
# ✔ Follow snake_case naming convention.
# ✔ Use UPPER_CASE for constants.
# ✔ Avoid single-letter variable names unless necessary.
# ✔ Keep variable names descriptive and readable.


# =========================================================
# COMMON BEGINNER MISTAKES
# =========================================================

# ❌ Invalid variable names

# 2name = "Alex"
# my-name = "Alex"

# Variable names cannot start with numbers
# and cannot contain hyphens.

# ✅ Correct

# name2 = "Alex"
# my_name = "Alex"


# =========================================================
# PRACTICE QUESTIONS
# =========================================================

# Q1. Create variables to store your name, age, city, and country.
#
# Q2. Create one variable of each data type:
#     int, float, str, and bool.
#
# Q3. Print the data type of each variable using type().
#
# Q4. Assign three variables in a single line and print them.
#
# Q5. Create a variable and change its data type.
#
# Q6. Create two constants using UPPER_CASE naming.


# =========================================================
# KEY TAKEAWAYS
# =========================================================

"""
Today You Learned:

✔ Variables
✔ Data Types
✔ type() Function
✔ Multiple Variable Assignment
✔ Dynamic Typing
✔ Constant Naming Convention
✔ Variable Naming Best Practices

Happy Coding! 🚀
"""

# =========================================================
# End of File
# =========================================================
