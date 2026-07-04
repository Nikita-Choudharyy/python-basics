"""
=========================================================
Python Conditional Statements
=========================================================

Repository : python-basics
File       : 05_Conditional_statements.py
Author     : Nikita Choudhary

Description:
------------
This file demonstrates conditional statements in Python.
It covers if, if-else, elif ladder, and logical operators.

This repository documents my Python learning journey.
The examples are written for revision and to help other
beginners understand Python concepts.

Learning Objectives:
--------------------
✔ Understand the if statement
✔ Learn if-else statements
✔ Use elif ladder
✔ Work with logical operators
✔ Build decision-making logic

=========================================================
"""

# =========================================================
# 1. IF STATEMENT
# =========================================================

# The if statement executes a block of code only when
# the given condition is True.

age = 18

print("\nIf Statement")
print("-" * 30)

if age >= 18:
    print("Eligible to vote")

# Expected Output:
#
# Eligible to vote


# =========================================================
# 2. IF-ELSE STATEMENT
# =========================================================

# if-else allows Python to choose between two blocks
# of code.

number = 7

print("\nIf-Else Statement")
print("-" * 30)

if number % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")

# Expected Output:
#
# Odd Number


# =========================================================
# 3. ELIF LADDER
# =========================================================

# elif is used when multiple conditions need to be checked.

marks = 82

print("\nElif Ladder")
print("-" * 30)

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
else:
    print("Grade D")

# Expected Output:
#
# Grade B


# =========================================================
# 4. LOGICAL OPERATORS
# =========================================================

# Logical operators combine multiple conditions.

username = "admin"
password = "1234"

print("\nLogical Operators")
print("-" * 30)

if username == "admin" and password == "1234":
    print("Login Successful")
else:
    print("Invalid Credentials")

# Expected Output:
#
# Login Successful


# =========================================================
# 5. PRACTICAL EXAMPLE
# =========================================================

# Check whether a student has passed or failed.

passing_marks = 33
student_marks = 55

print("\nPractical Example")
print("-" * 30)

if student_marks >= passing_marks:
    print("Result : Pass")
else:
    print("Result : Fail")

# Expected Output:
#
# Result : Pass


# =========================================================
# BEST PRACTICES
# =========================================================

# ✔ Keep conditions simple and readable.
# ✔ Use meaningful variable names.
# ✔ Avoid deeply nested if statements.
# ✔ Use elif instead of multiple if statements when checking
#   related conditions.
# ✔ Maintain proper indentation.


# =========================================================
# COMMON BEGINNER MISTAKES
# =========================================================

# ❌ Wrong

# if age = 18:

# '=' is used for assignment.

# ✅ Correct

# if age == 18:

# '==' is used for comparison.

# Another common mistake:

# Forgetting indentation after an if statement.


# =========================================================
# PRACTICE QUESTIONS
# =========================================================

# Q1. Check whether a person is eligible to vote.
#
# Q2. Check whether a number is positive, negative,
#     or zero.
#
# Q3. Find the largest of two numbers.
#
# Q4. Display grades based on marks using elif.
#
# Q5. Create a login system using username and password.
#
# Q6. Check whether a year is a leap year.
#
# Q7. Check whether a number is divisible by both
#     3 and 5.


# =========================================================
# KEY TAKEAWAYS
# =========================================================

"""
Today You Learned:

✔ if Statement
✔ if-else Statement
✔ elif Ladder
✔ Logical Operators
✔ Decision Making in Python

Happy Coding! 🚀
"""

# =========================================================
# End of File
# =========================================================
