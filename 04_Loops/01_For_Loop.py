"""
=====================================================
Topic: For Loops in Python
File : 01_For_Loop.py

Description:
This file demonstrates:
1. Introduction to for Loops
2. Iterating Over range()
3. Using start, stop, and step
4. Iterating Over Strings
5. Iterating Over Lists
6. Nested for Loops
7. Real-World Examples
8. Best Practices

Author : Nikita Choudhary
Repository : Python Basics
=====================================================
"""

# =====================================================
# 1. What is a for Loop?
# =====================================================

# A for loop is used to iterate over a sequence
# such as a string, list, tuple, or range.

print("Python For Loop Examples")

# =====================================================
# 2. Iterating Using range()
# =====================================================

print("\n===== range(stop) =====")

for number in range(5):
    print(number)

# =====================================================
# 3. range(start, stop)
# =====================================================

print("\n===== range(start, stop) =====")

for number in range(1, 6):
    print(number)

# =====================================================
# 4. range(start, stop, step)
# =====================================================

print("\n===== range(start, stop, step) =====")

for number in range(2, 11, 2):
    print(number)

# =====================================================
# 5. Iterating Over a String
# =====================================================

print("\n===== String Iteration =====")

language = "Python"

for letter in language:
    print(letter)

# =====================================================
# 6. Iterating Over a List
# =====================================================

print("\n===== List Iteration =====")

fruits = ["Apple", "Banana", "Mango"]

for fruit in fruits:
    print(fruit)

# =====================================================
# 7. Nested for Loop
# =====================================================

print("\n===== Nested for Loop =====")

for row in range(1, 4):
    for column in range(1, 4):
        print(f"({row}, {column})", end=" ")
    print()

# =====================================================
# 8. Real-World Example - Student Marks
# =====================================================

print("\n===== Student Marks =====")

students = ["Aman", "Riya", "Rahul"]

for student in students:
    print(f"{student} has submitted the assignment.")

# =====================================================
# 9. Real-World Example - Shopping Cart
# =====================================================

print("\n===== Shopping Cart =====")

cart = [
    "Laptop",
    "Mouse",
    "Keyboard",
    "Headphones"
]

for item in cart:
    print(f"Purchased: {item}")

# =====================================================
# 10. Real-World Example - Attendance System
# =====================================================

print("\n===== Attendance =====")

students = ["Ankit", "Neha", "Rohan"]

for student in students:
    print(f"{student} is Present.")

# =====================================================
# 11. Best Practices
# =====================================================

# ✔ Use meaningful loop variable names.
# ✔ Keep loop bodies short and readable.
# ✔ Avoid unnecessary nested loops.
# ✔ Use range() whenever appropriate.

# =====================================================
# 12. Mini Practice
# =====================================================

# Try these on your own:
#
# 1. Print numbers from 1 to 20.
# 2. Print all even numbers from 2 to 20.
# 3. Print all odd numbers from 1 to 20.
# 4. Print every character of your name.
# 5. Print all items in a shopping list.
# 6. Print the multiplication table of 5.
# 7. Create a simple star (*) pattern.
# 8. Print the square of numbers from 1 to 10.

# =====================================================
# End of Program
# =====================================================

print("\nCongratulations! You completed For Loops in Python. 🎉")