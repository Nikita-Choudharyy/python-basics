"""
=====================================================
Topic: Conditional Statements in Python
File : 01_Conditional_Statements.py

Description:
This file demonstrates:
1. Introduction to Conditional Statements
2. if Statement
3. if-else Statement
4. if-elif-else Statement
5. Real-World Examples
6. Best Practices

Author : Nikita Choudhary
Repository : Python Basics
=====================================================
"""

# =====================================================
# 1. What are Conditional Statements?
# =====================================================

# Conditional statements allow a program to make
# decisions based on whether a condition is True or False.

print("Conditional Statements help programs make decisions.")

# =====================================================
# 2. if Statement
# =====================================================

age = 20

print("\n===== if Statement =====")

if age >= 18:
    print("You are eligible to vote.")

# =====================================================
# 3. if-else Statement
# =====================================================

marks = 35

print("\n===== if-else Statement =====")

if marks >= 40:
    print("Result: Pass")
else:
    print("Result: Fail")

# =====================================================
# 4. if-elif-else Statement
# =====================================================

percentage = 82

print("\n===== if-elif-else Statement =====")

if percentage >= 90:
    print("Grade: A+")
elif percentage >= 75:
    print("Grade: A")
elif percentage >= 60:
    print("Grade: B")
elif percentage >= 40:
    print("Grade: C")
else:
    print("Grade: Fail")

# =====================================================
# 5. Real-World Example - ATM Withdrawal
# =====================================================

balance = 15000
withdraw_amount = 5000

print("\n===== ATM Withdrawal =====")

if withdraw_amount <= balance:
    balance -= withdraw_amount
    print("Withdrawal Successful.")
    print("Remaining Balance:", balance)
else:
    print("Insufficient Balance.")

# =====================================================
# 6. Real-World Example - Student Eligibility
# =====================================================

attendance = 85
marks = 76

print("\n===== Student Eligibility =====")

if attendance >= 75:
    if marks >= 40:
        print("Eligible for Final Exam.")
    else:
        print("Not Eligible due to Low Marks.")
else:
    print("Not Eligible due to Low Attendance.")

# =====================================================
# 7. Best Practices
# =====================================================

# ✔ Keep conditions simple and readable.
# ✔ Use meaningful variable names.
# ✔ Avoid unnecessary nesting.
# ✔ Use elif instead of multiple if statements
#   when checking multiple conditions.

# =====================================================
# 8. Mini Practice
# =====================================================

# Try these on your own:
#
# 1. Check whether a number is positive or negative.
# 2. Find the largest of two numbers.
# 3. Check whether a person is eligible to vote.
# 4. Assign grades based on marks.
# 5. Create a simple login system using if-else.

# =====================================================
# End of Program
# =====================================================

print("\nCongratulations! You completed Conditional Statements in Python. 🎉")