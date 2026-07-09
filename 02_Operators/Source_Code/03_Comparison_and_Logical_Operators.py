"""
=====================================================
Topic: Comparison and Logical Operators in Python
File : 03_Comparison_and_Logical_Operators.py

Description:
This file demonstrates:
1. Comparison Operators
2. Logical Operators
3. Combining Conditions
4. Real-World Examples
5. Best Practices

Author : Nikita Choudhary
Repository : Python Basics
=====================================================
"""

# =====================================================
# 1. Creating Variables
# =====================================================

num1 = 20
num2 = 15

print("First Number :", num1)
print("Second Number:", num2)

# =====================================================
# 2. Comparison Operators
# =====================================================

print("\n===== Comparison Operators =====")

print(f"{num1} == {num2} :", num1 == num2)   # Equal to
print(f"{num1} != {num2} :", num1 != num2)   # Not equal to
print(f"{num1} > {num2}  :", num1 > num2)    # Greater than
print(f"{num1} < {num2}  :", num1 < num2)    # Less than
print(f"{num1} >= {num2} :", num1 >= num2)   # Greater than or equal to
print(f"{num1} <= {num2} :", num1 <= num2)   # Less than or equal to

# =====================================================
# 3. Logical Operators
# =====================================================

print("\n===== Logical Operators =====")

age = 22
has_id = True

# Logical AND
print("\nUsing AND")
print(age >= 18 and has_id)

# Logical OR
print("\nUsing OR")
print(age >= 18 or has_id)

# Logical NOT
print("\nUsing NOT")
print(not has_id)

# =====================================================
# 4. Combining Multiple Conditions
# =====================================================

marks = 82
attendance = 90

eligible = marks >= 40 and attendance >= 75

print("\n===== Eligibility Check =====")
print("Marks      :", marks)
print("Attendance :", attendance)
print("Eligible   :", eligible)

# =====================================================
# 5. Real-World Example
# =====================================================

username = "admin"
password = "python123"

print("\n===== Login System =====")

entered_username = "admin"
entered_password = "python123"

is_logged_in = (
    entered_username == username
    and entered_password == password
)

print("Login Successful:", is_logged_in)

# =====================================================
# 6. Truth Table Examples
# =====================================================

print("\n===== Truth Table =====")

print("True and True   :", True and True)
print("True and False  :", True and False)
print("False and False :", False and False)

print()

print("True or True    :", True or True)
print("True or False   :", True or False)
print("False or False  :", False or False)

print()

print("not True  :", not True)
print("not False :", not False)

# =====================================================
# 7. Best Practices
# =====================================================

# ✔ Write readable conditions.
# ✔ Avoid deeply nested logical expressions.
# ✔ Use parentheses when combining multiple conditions.
# ✔ Give boolean variables meaningful names.

# Good Example
is_eligible = age >= 18 and has_id

# Bad Example
x = age >= 18 and has_id

# =====================================================
# 8. Mini Practice
# =====================================================

# Try these on your own:
#
# 1. Compare two numbers using all comparison operators.
# 2. Check whether a student passed using marks.
# 3. Check if a user is eligible to vote.
# 4. Create a login system using username and password.
# 5. Experiment with AND, OR, and NOT operators.

# =====================================================
# End of Program
# =====================================================

print("\nCongratulations! You completed Comparison and Logical Operators in Python. 🎉")