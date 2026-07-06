"""
=========================================================
Python Lambda Functions
=========================================================

Repository : python-basics
File       : 02_Lambda_functions.py
Author     : Nikita Choudhary

Description:
------------
This file demonstrates Python lambda functions, including
basic syntax, multiple arguments, conditional expressions,
and practical use with map() and filter().

This repository documents my Python learning journey.
The examples are written for revision and to help other
beginners understand Python concepts.

Learning Objectives:
--------------------
✔ Understand lambda functions
✔ Use lambda with multiple arguments
✔ Return lambda functions from another function
✔ Use conditional expressions
✔ Apply lambda with map() and filter()

=========================================================
"""

# =========================================================
# 1. BASIC LAMBDA FUNCTION
# =========================================================

# A lambda function is a small anonymous function
# written in a single line.

square = lambda x: x * x

print("\nBasic Lambda Function")
print("-" * 30)

print("Square of 5 :", square(5))

# Expected Output:
#
# Square of 5 : 25


# =========================================================
# 2. LAMBDA WITH MULTIPLE ARGUMENTS
# =========================================================

add = lambda a, b: a + b

print("\nLambda with Multiple Arguments")
print("-" * 30)

print("Addition :", add(10, 20))

# Expected Output:
#
# Addition : 30


# =========================================================
# 3. LAMBDA INSIDE A FUNCTION
# =========================================================

def multiply_by(n):
    return lambda x: x * n

double = multiply_by(2)
triple = multiply_by(3)

print("\nLambda Inside a Function")
print("-" * 30)

print("Double of 5 :", double(5))
print("Triple of 5 :", triple(5))

# Expected Output:
#
# Double of 5 : 10
# Triple of 5 : 15


# =========================================================
# 4. CONDITIONAL LAMBDA
# =========================================================

check_even_odd = lambda x: "Even" if x % 2 == 0 else "Odd"

print("\nConditional Lambda")
print("-" * 30)

print("7  :", check_even_odd(7))
print("10 :", check_even_odd(10))

# Expected Output:
#
# 7  : Odd
# 10 : Even


# =========================================================
# 5. LAMBDA WITH MAP()
# =========================================================

numbers = [1, 2, 3, 4, 5]

squares = list(map(lambda x: x * x, numbers))

print("\nLambda with map()")
print("-" * 30)

print(squares)

# Expected Output:
#
# [1, 4, 9, 16, 25]


# =========================================================
# 6. LAMBDA WITH FILTER()
# =========================================================

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print("\nLambda with filter()")
print("-" * 30)

print(even_numbers)

# Expected Output:
#
# [2, 4]


# =========================================================
# 7. PRACTICAL EXAMPLES
# =========================================================

max_num = lambda a, b: a if a > b else b

print("\nMaximum of Two Numbers")
print("-" * 30)

print(max_num(15, 20))

cube = lambda x: x ** 3

print("\nCube")
print("-" * 30)

print(cube(3))

# Expected Output:
#
# 20
# 27


# =========================================================
# BEST PRACTICES
# =========================================================

# ✔ Use lambda only for short expressions.
# ✔ Use def for complex logic.
# ✔ Prefer meaningful variable names.
# ✔ Use lambda mainly with map(), filter(), and sorted().


# =========================================================
# COMMON BEGINNER MISTAKES
# =========================================================

# ❌ Wrong

# lambda x:
#
# Incomplete lambda expression.

# ❌ Wrong

# Writing multiple statements inside a lambda.

# Lambda functions can contain only one expression.

# ✅ Correct

# Use a normal function (def) for complex logic.


# =========================================================
# PRACTICE QUESTIONS
# =========================================================

# Q1. Create a lambda function to calculate the square.
#
# Q2. Create a lambda function to multiply two numbers.
#
# Q3. Use map() to double every number in a list.
#
# Q4. Use filter() to find all odd numbers.
#
# Q5. Create a lambda function to find the minimum of two numbers.
#
# Q6. Use lambda to check whether a number is positive or negative.


# =========================================================
# KEY TAKEAWAYS
# =========================================================

"""
Today You Learned:

✔ Lambda Functions
✔ Multiple Arguments
✔ Conditional Lambda
✔ map()
✔ filter()
✔ Returning Lambda Functions

Happy Coding! 🚀
"""

# =========================================================
# End of File
# =========================================================
