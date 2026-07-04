"""
=========================================================
Python Type Casting
=========================================================

Repository : python-basics
File       : 03_Type_casting.py
Author     : Nikita Choudhary

Description:
------------
This file demonstrates type casting in Python. It covers
conversion between strings, integers, floats, booleans,
and user input.

This repository documents my Python learning journey.
The examples are written for revision and to help other
beginners understand Python concepts.

Learning Objectives:
--------------------
✔ Understand type casting
✔ Convert strings to integers
✔ Convert strings to floats
✔ Convert integers to strings
✔ Learn Boolean casting
✔ Convert user input into numeric values

=========================================================
"""

# =========================================================
# 1. STRING TO INTEGER
# =========================================================

# int() converts a string into an integer.

a = "10"
b = "20"

print("\nString to Integer")
print("-" * 30)

print("Before Casting")
print(type(a), type(b))

a = int(a)
b = int(b)

print("\nAfter Casting")
print(type(a), type(b))
print("Sum:", a + b)

# Expected Output:
#
# Before Casting
# <class 'str'> <class 'str'>
#
# After Casting
# <class 'int'> <class 'int'>
# Sum: 30


# =========================================================
# 2. STRING TO FLOAT
# =========================================================

# float() converts a string into a floating-point number.

x = "3.5"
y = "2.5"

x = float(x)
y = float(y)

print("\nString to Float")
print("-" * 30)

print("Addition:", x + y)

# Expected Output:
#
# Addition: 6.0


# =========================================================
# 3. INTEGER TO STRING
# =========================================================

# str() converts any value into a string.

num = 100
num_str = str(num)

print("\nInteger to String")
print("-" * 30)

print("Number           :", num)
print("String Value     :", num_str)
print("Type After Cast  :", type(num_str))

# Expected Output:
#
# Number           : 100
# String Value     : 100
# Type After Cast  : <class 'str'>


# =========================================================
# 4. BOOLEAN CASTING
# =========================================================

# bool() converts values into True or False.

print("\nBoolean Casting")
print("-" * 30)

print("bool(0)        :", bool(0))
print("bool(1)        :", bool(1))
print('bool("")       :', bool(""))
print('bool("Python") :', bool("Python"))

# Expected Output:
#
# bool(0)        : False
# bool(1)        : True
# bool("")       : False
# bool("Python") : True


# =========================================================
# 5. USER INPUT WITH TYPE CASTING
# =========================================================

# input() always returns a string.
# Convert it into an integer before performing calculations.

num1 = int(input("\nEnter first number: "))
num2 = int(input("Enter second number: "))

print("Multiplication:", num1 * num2)

# Example Input:
#
# Enter first number: 5
# Enter second number: 6
#
# Expected Output:
#
# Multiplication: 30


# =========================================================
# BEST PRACTICES
# =========================================================

# ✔ Always verify the value before casting.
# ✔ Use int() only with valid integer strings.
# ✔ Use float() for decimal numbers.
# ✔ Remember that input() returns a string.
# ✔ Handle invalid input using exception handling (covered later).


# =========================================================
# COMMON BEGINNER MISTAKES
# =========================================================

# ❌ Invalid integer conversion

# int("10.5")

# This raises a ValueError because "10.5"
# is not a valid integer string.

# ✅ Correct

# int(float("10.5"))

# Another common mistake:

# "5" + "10"

# Output:
# 510

# Correct:

# int("5") + int("10")

# Output:
# 15


# =========================================================
# PRACTICE QUESTIONS
# =========================================================

# Q1. Convert the string "50" into an integer.
#
# Q2. Convert the string "25.75" into a float.
#
# Q3. Convert an integer into a string.
#
# Q4. Check the output of:
#     bool(0)
#     bool(-1)
#     bool("")
#     bool("Hello")
#
# Q5. Take two numbers as input and print:
#     - Sum
#     - Difference
#     - Product
#     - Division
#
# Q6. Try converting an invalid string such as "abc"
#     into an integer and observe the error.


# =========================================================
# KEY TAKEAWAYS
# =========================================================

"""
Today You Learned:

✔ Type Casting
✔ int()
✔ float()
✔ str()
✔ bool()
✔ User Input Conversion
✔ Common Casting Mistakes

Happy Coding! 🚀
"""

# =========================================================
# End of File
# =========================================================
