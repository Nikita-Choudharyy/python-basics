"""
=========================================================
Python map(), filter(), and reduce()
=========================================================

Repository : python-basics
File       : 03_Map_filter_reduce.py
Author     : Nikita Choudhary

Description:
------------
This file demonstrates the use of Python's map(),
filter(), and reduce() functions for processing
iterables in a functional programming style.

This repository documents my Python learning journey.
The examples are written for revision and to help other
beginners understand Python concepts.

Learning Objectives:
--------------------
✔ Understand map()
✔ Understand filter()
✔ Understand reduce()
✔ Process lists efficiently
✔ Apply lambda functions with built-in functions

=========================================================
"""

from functools import reduce

# =========================================================
# 1. map()
# =========================================================

# map() applies a function to every element of an iterable
# and returns a map object.

numbers = [1, 2, 3, 4, 5]

print("\nmap()")
print("-" * 30)

squares = list(map(lambda x: x * x, numbers))

print("Original List :", numbers)
print("Squares       :", squares)

# Expected Output:
#
# Original List : [1, 2, 3, 4, 5]
# Squares       : [1, 4, 9, 16, 25]


# =========================================================
# 2. filter()
# =========================================================

# filter() selects elements that satisfy a condition.

print("\nfilter()")
print("-" * 30)

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print("Even Numbers :", even_numbers)

# Expected Output:
#
# Even Numbers : [2, 4]


# =========================================================
# 3. reduce()
# =========================================================

# reduce() repeatedly applies a function to reduce
# an iterable into a single value.

print("\nreduce()")
print("-" * 30)

sum_of_numbers = reduce(lambda a, b: a + b, numbers)

print("Sum :", sum_of_numbers)

# Expected Output:
#
# Sum : 15


# =========================================================
# 4. MORE EXAMPLES
# =========================================================

print("\nMore Examples")
print("-" * 30)

# Convert strings to integers

string_numbers = ["1", "2", "3", "4"]

integer_numbers = list(map(int, string_numbers))

print("Integer List :", integer_numbers)

# Filter numbers greater than 3

greater_than_three = list(filter(lambda x: x > 3, numbers))

print("Greater Than 3 :", greater_than_three)

# Product using reduce()

product = reduce(lambda a, b: a * b, numbers)

print("Product :", product)

# Expected Output:
#
# Integer List   : [1, 2, 3, 4]
# Greater Than 3 : [4, 5]
# Product        : 120


# =========================================================
# 5. PRACTICAL EXAMPLES
# =========================================================

print("\nPractical Examples")
print("-" * 30)

# Double every number

doubled = list(map(lambda x: x * 2, numbers))

print("Doubled :", doubled)

# Filter odd numbers

odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))

print("Odd Numbers :", odd_numbers)

# Find maximum

maximum = reduce(lambda a, b: a if a > b else b, numbers)

print("Maximum :", maximum)

# Expected Output:
#
# Doubled     : [2, 4, 6, 8, 10]
# Odd Numbers : [1, 3, 5]
# Maximum     : 5


# =========================================================
# BEST PRACTICES
# =========================================================

# ✔ Use map() when transforming every element.
# ✔ Use filter() when selecting elements.
# ✔ Use reduce() only when a single final value is required.
# ✔ Keep lambda expressions short and readable.
# ✔ Prefer normal functions (def) for complex logic.


# =========================================================
# COMMON BEGINNER MISTAKES
# =========================================================

# ❌ Forgetting to convert map() or filter() to a list.

# map(lambda x: x * x, numbers)

# This returns a map object.

# ✅ Correct

# list(map(lambda x: x * x, numbers))


# Another common mistake:

# Forgetting to import reduce()

# from functools import reduce


# =========================================================
# PRACTICE QUESTIONS
# =========================================================

# Q1. Use map() to convert temperatures from Celsius to Fahrenheit.
#
# Q2. Use map() to calculate cubes of numbers.
#
# Q3. Use filter() to find all positive numbers.
#
# Q4. Use filter() to remove empty strings from a list.
#
# Q5. Use reduce() to calculate the product of all numbers.
#
# Q6. Use reduce() to find the minimum value in a list.


# =========================================================
# KEY TAKEAWAYS
# =========================================================

"""
Today You Learned:

✔ map()
✔ filter()
✔ reduce()
✔ Lambda Functions
✔ Functional Programming Basics

Happy Coding! 🚀
"""

# =========================================================
# End of File
# =========================================================
