"""
=====================================================
Topic: Recursive Functions in Python
File : 04_Recursive_Functions.py

Description:
This file demonstrates:
1. Introduction to Recursion
2. Base Case
3. Recursive Case
4. Factorial using Recursion
5. Sum of Natural Numbers
6. Fibonacci Series
7. Real-World Examples
8. Best Practices

Author : Nikita Choudhary
Repository : Python Basics
=====================================================
"""

# =====================================================
# 1. What is Recursion?
# =====================================================

# Recursion is a technique where a function
# calls itself until a stopping condition
# (base case) is reached.

print("Recursive Function Examples")

# =====================================================
# 2. Factorial using Recursion
# =====================================================

print("\n===== Factorial =====")

def factorial(number):

    if number == 0 or number == 1:
        return 1

    return number * factorial(number - 1)

print("Factorial of 5:", factorial(5))

# =====================================================
# 3. Sum of Natural Numbers
# =====================================================

print("\n===== Sum of Natural Numbers =====")

def natural_sum(number):

    if number == 1:
        return 1

    return number + natural_sum(number - 1)

print("Sum:", natural_sum(10))

# =====================================================
# 4. Fibonacci Series
# =====================================================

print("\n===== Fibonacci =====")

def fibonacci(number):

    if number <= 1:
        return number

    return fibonacci(number - 1) + fibonacci(number - 2)

for i in range(8):
    print(fibonacci(i), end=" ")

print()

# =====================================================
# 5. Reverse a String
# =====================================================

print("\n===== Reverse String =====")

def reverse_text(text):

    if len(text) == 0:
        return ""

    return text[-1] + reverse_text(text[:-1])

print(reverse_text("Python"))

# =====================================================
# 6. Real-World Example - Countdown
# =====================================================

print("\n===== Rocket Countdown =====")

def countdown(number):

    if number == 0:
        print("🚀 Liftoff!")
        return

    print(number)

    countdown(number - 1)

countdown(5)

# =====================================================
# 7. Real-World Example - Folder Levels
# =====================================================

print("\n===== Folder Levels =====")

def show_levels(level):

    if level == 0:
        print("Root Folder")
        return

    print(f"Folder Level {level}")

    show_levels(level - 1)

show_levels(4)

# =====================================================
# 8. Best Practices
# =====================================================

# ✔ Always define a base case.
# ✔ Ensure recursion moves toward the base case.
# ✔ Avoid unnecessary recursion for simple tasks.
# ✔ Use recursion when the problem has
#   a recursive structure.

# =====================================================
# 9. Mini Practice
# =====================================================

# Try these on your own:
#
# 1. Find the power of a number using recursion.
# 2. Calculate the product of two numbers recursively.
# 3. Find the sum of digits of a number.
# 4. Check whether a string is a palindrome.
# 5. Count the number of characters in a string recursively.

# =====================================================
# End of Program
# =====================================================

print("\nCongratulations! You completed Recursive Functions in Python. 🎉")