"""
=========================================================
Python Tuples
=========================================================

Repository : python-basics
File       : 02_Tuples.py
Author     : Nikita Choudhary

Description:
------------
This file demonstrates Python tuples, including tuple
creation, indexing, slicing, unpacking, tuple methods,
nested tuples, and tuple immutability.

This repository documents my Python learning journey.
The examples are written for revision and to help other
beginners understand Python concepts.

Learning Objectives:
--------------------
✔ Create tuples
✔ Access tuple elements
✔ Perform slicing
✔ Understand tuple unpacking
✔ Use tuple methods
✔ Learn tuple immutability

=========================================================
"""

# =========================================================
# 1. CREATING TUPLES
# =========================================================

# A tuple is an ordered and immutable collection.

empty_tuple = ()
fruits = ("apple", "banana", "cherry")
single_element = ("apple",)
numbers = tuple([1, 2, 3, 4])

print("\nCreating Tuples")
print("-" * 30)

print("Empty Tuple    :", empty_tuple)
print("Fruits Tuple   :", fruits)
print("Single Element :", single_element)
print("Numbers Tuple  :", numbers)

# Expected Output:
#
# Empty Tuple    : ()
# Fruits Tuple   : ('apple', 'banana', 'cherry')
# Single Element : ('apple',)
# Numbers Tuple  : (1, 2, 3, 4)


# =========================================================
# 2. ACCESSING ELEMENTS
# =========================================================

print("\nTuple Indexing")
print("-" * 30)

print("First Fruit :", fruits[0])
print("Last Fruit  :", fruits[-1])
print("Slice       :", fruits[0:2])

# Expected Output:
#
# First Fruit : apple
# Last Fruit  : cherry
# Slice       : ('apple', 'banana')


# =========================================================
# 3. TUPLE UNPACKING
# =========================================================

apple, banana, cherry = fruits

print("\nTuple Unpacking")
print("-" * 30)

print(apple)
print(banana)
print(cherry)

# Expected Output:
#
# apple
# banana
# cherry


# =========================================================
# 4. TUPLE METHODS
# =========================================================

sample = (1, 2, 2, 3, 4, 2)

print("\nTuple Methods")
print("-" * 30)

print("Count of 2 :", sample.count(2))
print("Index of 3 :", sample.index(3))

# Expected Output:
#
# Count of 2 : 3
# Index of 3 : 3


# =========================================================
# 5. NESTED TUPLES
# =========================================================

nested = (1, 2, ("A", "B"))

print("\nNested Tuples")
print("-" * 30)

print("Nested Tuple   :", nested)
print("Nested Element :", nested[2][0])

# Expected Output:
#
# Nested Tuple   : (1, 2, ('A', 'B'))
# Nested Element : A


# =========================================================
# 6. TUPLE IMMUTABILITY
# =========================================================

# Tuples cannot be modified after creation.

colors = ("Red", "Green", "Blue")

print("\nTuple Immutability")
print("-" * 30)

print(colors)

# ❌ This will raise an error.
#
# colors[0] = "Yellow"

# Expected Output:
#
# ('Red', 'Green', 'Blue')


# =========================================================
# 7. PRACTICAL EXAMPLES
# =========================================================

# Swap two variables using tuple unpacking.

x = 5
y = 10

x, y = y, x

print("\nSwap Variables")
print("-" * 30)

print("x =", x)
print("y =", y)

# Expected Output:
#
# x = 10
# y = 5


# Count occurrences in a tuple.

nums = (1, 2, 3, 2, 4, 2)

print("\nCount Occurrences")
print("-" * 30)

print("Occurrences of 2 :", nums.count(2))

# Expected Output:
#
# Occurrences of 2 : 3


# =========================================================
# BEST PRACTICES
# =========================================================

# ✔ Use tuples for data that should not change.
# ✔ Use meaningful variable names.
# ✔ Use tuple unpacking for cleaner code.
# ✔ Remember that tuples are immutable.


# =========================================================
# COMMON BEGINNER MISTAKES
# =========================================================

# ❌ Wrong

# fruits[0] = "Mango"

# Tuples do not support item assignment.

# ✅ Correct

# Create a new tuple if changes are required.


# =========================================================
# PRACTICE QUESTIONS
# =========================================================

# Q1. Create a tuple of five numbers.
#
# Q2. Print the first and last element.
#
# Q3. Perform tuple slicing.
#
# Q4. Unpack a tuple into three variables.
#
# Q5. Count occurrences of an element.
#
# Q6. Find the index of an element.
#
# Q7. Create a nested tuple and access an inner element.
#
# Q8. Try modifying a tuple and observe the error.


# =========================================================
# KEY TAKEAWAYS
# =========================================================

"""
Today You Learned:

✔ Creating Tuples
✔ Indexing
✔ Slicing
✔ Tuple Unpacking
✔ Tuple Methods
✔ Nested Tuples
✔ Tuple Immutability

Happy Coding! 🚀
"""

# =========================================================
# End of File
# =========================================================
