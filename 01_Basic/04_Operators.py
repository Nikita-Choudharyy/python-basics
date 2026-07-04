"""
=========================================================
Python Operators
=========================================================

Repository : python-basics
File       : 04_Operators.py
Author     : Nikita Choudhary

Description:
------------
This file demonstrates different types of operators in
Python, including arithmetic, comparison, logical,
assignment, membership, and identity operators.

This repository documents my Python learning journey.
The examples are written for revision and to help other
beginners understand Python concepts.

Learning Objectives:
--------------------
✔ Understand arithmetic operators
✔ Learn comparison operators
✔ Use logical operators
✔ Work with assignment operators
✔ Understand membership operators
✔ Learn identity operators

=========================================================
"""

# =========================================================
# 1. ARITHMETIC OPERATORS
# =========================================================

# Arithmetic operators perform mathematical calculations.

a = 10
b = 3

print("\nArithmetic Operators")
print("-" * 30)

print("Addition       :", a + b)
print("Subtraction    :", a - b)
print("Multiplication :", a * b)
print("Division       :", a / b)
print("Floor Division :", a // b)
print("Modulus        :", a % b)
print("Exponent       :", a ** b)

# Expected Output:
#
# Addition       : 13
# Subtraction    : 7
# Multiplication : 30
# Division       : 3.3333333333333335
# Floor Division : 3
# Modulus        : 1
# Exponent       : 1000


# =========================================================
# 2. COMPARISON OPERATORS
# =========================================================

# Comparison operators compare two values
# and return either True or False.

print("\nComparison Operators")
print("-" * 30)

print("a == b :", a == b)
print("a != b :", a != b)
print("a > b  :", a > b)
print("a < b  :", a < b)
print("a >= b :", a >= b)
print("a <= b :", a <= b)

# Expected Output:
#
# a == b : False
# a != b : True
# a > b  : True
# a < b  : False
# a >= b : True
# a <= b : False


# =========================================================
# 3. LOGICAL OPERATORS
# =========================================================

# Logical operators combine multiple conditions.

x = True
y = False

print("\nLogical Operators")
print("-" * 30)

print("x and y :", x and y)
print("x or y  :", x or y)
print("not x   :", not x)

# Expected Output:
#
# x and y : False
# x or y  : True
# not x   : False


# =========================================================
# 4. ASSIGNMENT OPERATORS
# =========================================================

# Assignment operators update the value of a variable.

num = 5

print("\nAssignment Operators")
print("-" * 30)

num += 3
print("After += :", num)

num -= 2
print("After -= :", num)

num *= 2
print("After *= :", num)

# Expected Output:
#
# After += : 8
# After -= : 6
# After *= : 12


# =========================================================
# 5. MEMBERSHIP OPERATORS
# =========================================================

# Membership operators check whether a value
# exists inside a sequence.

numbers = [1, 2, 3, 4, 5]

print("\nMembership Operators")
print("-" * 30)

print("3 in numbers       :", 3 in numbers)
print("10 not in numbers  :", 10 not in numbers)

# Expected Output:
#
# 3 in numbers      : True
# 10 not in numbers : True


# =========================================================
# 6. IDENTITY OPERATORS
# =========================================================

# Identity operators compare memory locations.

list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1

print("\nIdentity Operators")
print("-" * 30)

print("list1 is list2     :", list1 is list2)
print("list1 is list3     :", list1 is list3)
print("list1 is not list2 :", list1 is not list2)

# Expected Output:
#
# list1 is list2     : False
# list1 is list3     : True
# list1 is not list2 : True


# =========================================================
# 7. PRACTICAL EXAMPLE
# =========================================================

# Check whether a number is positive and even.

num = 8

print("\nPractical Example")
print("-" * 30)

print("Positive and Even :", num > 0 and num % 2 == 0)

# Expected Output:
#
# Positive and Even : True


# =========================================================
# BEST PRACTICES
# =========================================================

# ✔ Use descriptive variable names.
# ✔ Use parentheses when expressions become complex.
# ✔ Avoid writing unnecessary comparisons.
# ✔ Keep logical conditions readable.
# ✔ Use identity operators only when checking object identity.


# =========================================================
# COMMON BEGINNER MISTAKES
# =========================================================

# ❌ Wrong

# if x = 10:

# '=' is an assignment operator.

# ✅ Correct

# if x == 10:

# '==' is a comparison operator.


# Another common mistake:

# list1 == list2
# Checks values.

# list1 is list2
# Checks whether both variables refer to the same object.


# =========================================================
# PRACTICE QUESTIONS
# =========================================================

# Q1. Perform all arithmetic operations on two numbers.
#
# Q2. Compare two numbers using all comparison operators.
#
# Q3. Create two Boolean variables and use:
#     - and
#     - or
#     - not
#
# Q4. Demonstrate +=, -=, *=, and /= operators.
#
# Q5. Check whether a value exists in a list.
#
# Q6. Create two lists and compare them using
#     both == and is.
#
# Q7. Check whether a number is positive,
#     negative, and even.


# =========================================================
# KEY TAKEAWAYS
# =========================================================

"""
Today You Learned:

✔ Arithmetic Operators
✔ Comparison Operators
✔ Logical Operators
✔ Assignment Operators
✔ Membership Operators
✔ Identity Operators

Happy Coding! 🚀
"""

# =========================================================
# End of File
# =========================================================
print("Positive and even:", num > 0 and num % 2 == 0)
