"""
File: conditions.py
Topic: Conditional Statements in Python

This file covers:
- if statement
- if-else
- elif ladder
- logical operators
"""

# Simple if condition
age = 18
if age >= 18:
    print("Eligible to vote")

# if-else example
number = 7
if number % 2 == 0:
    print("Even number")
else:
    print("Odd number")

# elif ladder
marks = 82
if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
else:
    print("Grade D")

# Logical operators
username = "admin"
password = "1234"

if username == "admin" and password == "1234":
    print("Login successful")
else:
    print("Invalid credentials")
