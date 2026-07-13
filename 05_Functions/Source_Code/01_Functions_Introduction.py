"""
=====================================================
Topic: Functions in Python
File : 01_Functions_Introduction.py

Description:
This file demonstrates:
1. What are Functions?
2. Why Use Functions?
3. Defining a Function
4. Calling a Function
5. Parameters and Arguments
6. Return Statement
7. Real-World Examples
8. Best Practices

Author : Nikita Choudhary
Repository : Python Basics
=====================================================
"""

# =====================================================
# 1. What are Functions?
# =====================================================

# A function is a reusable block of code that performs
# a specific task.

print("Functions help us write reusable and organized code.")

# =====================================================
# 2. Defining and Calling a Function
# =====================================================

print("\n===== Defining and Calling a Function =====")

def greet():
    print("Welcome to Python Programming!")

greet()

# =====================================================
# 3. Function with Parameters
# =====================================================

print("\n===== Function with Parameters =====")

def greet_user(name):
    print(f"Hello, {name}!")

greet_user("Nikita")
greet_user("Rahul")

# =====================================================
# 4. Function with Multiple Parameters
# =====================================================

print("\n===== Multiple Parameters =====")

def student_details(name, course):
    print(f"Name   : {name}")
    print(f"Course : {course}")

student_details("Nikita", "Python Basics")

# =====================================================
# 5. Function with Return Statement
# =====================================================

print("\n===== Return Statement =====")

def add_numbers(num1, num2):
    return num1 + num2

result = add_numbers(15, 25)

print("Sum:", result)

# =====================================================
# 6. Function Returning Multiple Values
# =====================================================

print("\n===== Returning Multiple Values =====")

def calculate(a, b):
    return a + b, a * b

addition, multiplication = calculate(10, 5)

print("Addition      :", addition)
print("Multiplication:", multiplication)

# =====================================================
# 7. Real-World Example - Student Result
# =====================================================

print("\n===== Student Result =====")

def calculate_percentage(total_marks, obtained_marks):
    percentage = (obtained_marks / total_marks) * 100
    return percentage

percentage = calculate_percentage(500, 435)

print(f"Percentage: {percentage:.2f}%")

# =====================================================
# 8. Real-World Example - Shopping Bill
# =====================================================

print("\n===== Shopping Bill =====")

def calculate_bill(price, quantity):
    return price * quantity

bill = calculate_bill(799, 3)

print("Total Bill: ₹", bill)

# =====================================================
# 9. Best Practices
# =====================================================

# ✔ Give functions meaningful names.
# ✔ Keep each function focused on one task.
# ✔ Use parameters instead of hardcoding values.
# ✔ Return values whenever possible.
# ✔ Write reusable functions.

# =====================================================
# 10. Mini Practice
# =====================================================

# Try these on your own:
#
# 1. Create a function to print your name.
# 2. Create a function that adds two numbers.
# 3. Create a function that finds the square of a number.
# 4. Create a function that calculates the area of a rectangle.
# 5. Create a function that returns the maximum of two numbers.

# =====================================================
# End of Program
# =====================================================

print("\nCongratulations! You completed Functions Introduction in Python. 🎉")