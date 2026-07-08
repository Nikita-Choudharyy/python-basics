"""
02_Print_and_Input.py

This script demonstrates the basics of Python's print() and input() functions.
"""

# ---------------------------------------------------
# Printing Strings
# ---------------------------------------------------

print("Hello, World!")
print("Welcome to Python Programming!")

# ---------------------------------------------------
# Printing Numbers
# ---------------------------------------------------

print(10)
print(3.14)

# ---------------------------------------------------
# Printing Multiple Values
# ---------------------------------------------------

print("Name:", "Nikita")
print("Age:", 21)

# ---------------------------------------------------
# Using sep Parameter
# ---------------------------------------------------

print("2026", "07", "08", sep="-")

# ---------------------------------------------------
# Using end Parameter
# ---------------------------------------------------

print("Hello", end=" ")
"""
=====================================================
Topic: Print and Input in Python
File : 02_Print_and_Input.py

Description:
This file demonstrates how to:
1. Display output using print()
2. Print different data types
3. Print multiple values
4. Use sep and end parameters
5. Take user input using input()
6. Convert input into different data types

Author : Nikita Choudhary
Repository : Python Basics
=====================================================
"""

# =====================================================
# 1. Basic print() Function
# =====================================================

print("Hello, World!")
print("Welcome to Python Programming!")

# =====================================================
# 2. Printing Different Data Types
# =====================================================

print("Python")
print(100)
print(99.99)
print(True)

# =====================================================
# 3. Printing Multiple Values
# =====================================================

print("Name:", "Nikita")
print("Age:", 21)
print("Course:", "Python Basics")

# =====================================================
# 4. Using the sep Parameter
# =====================================================

print("2026", "07", "08", sep="-")
print("Python", "Java", "C++", sep=" | ")

# =====================================================
# 5. Using the end Parameter
# =====================================================

print("Hello", end=" ")
print("Python!")

print("Learning", end=" -> ")
print("Coding")

# =====================================================
# 6. Taking User Input
# =====================================================

name = input("Enter your name: ")

print("Hello,", name)

# =====================================================
# 7. Taking Multiple Inputs
# =====================================================

city = input("Enter your city: ")
age = input("Enter your age: ")

print("City :", city)
print("Age  :", age)

# =====================================================
# 8. Type Conversion with User Input
# =====================================================

marks = int(input("Enter your marks: "))
print("Marks:", marks)

price = float(input("Enter product price: "))
print("Price:", price)

# =====================================================
# 9. Real-World Example
# =====================================================

student_name = input("\nEnter student name: ")
student_marks = float(input("Enter student marks: "))

print("\n----- Student Report -----")
print("Name  :", student_name)
print("Marks :", student_marks)

# =====================================================
# 10. Mini Practice
# =====================================================

# Try these on your own:
#
# 1. Take your favourite color as input and print it.
# 2. Take your age as input and print it.
# 3. Take two numbers as input and print their sum.
# 4. Print today's date using the sep parameter.
# 5. Print two words on the same line using the end parameter.

# =====================================================
# End of Program
# =====================================================

print("\nCongratulations! You completed Print and Input in Python. 🎉")