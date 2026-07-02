"""
File: variables.py
Topic: Python Variables and Data Types

This file covers:
- Variable declaration
- Common data types
- Multiple assignment
- Type checking
"""

# ----------------------------
# Basic Variable Assignment
# ----------------------------
name = "Nikita"
age = 22
height = 5.4
is_student = True

print(name, age, height, is_student)

# ----------------------------
# Data Types in Python
# ----------------------------
score = 95            # int
percentage = 89.5     # float
grade = "A"           # str
passed = True         # bool

# Type checking
print(type(score))
print(type(percentage))
print(type(grade))
print(type(passed))

# ----------------------------
# Multiple Variable Assignment
# ----------------------------
x, y, z = 10, 20, 30
print(x, y, z)

# ----------------------------
# Dynamic Typing in Python
# ----------------------------
value = 100
print(value, type(value))

value = "Python"
print(value, type(value))

# ----------------------------
# Constant Naming Convention
# ----------------------------
PI = 3.14159
MAX_LIMIT = 1000

print(PI, MAX_LIMIT)
