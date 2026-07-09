"""
=====================================================
Topic: Operators in Python
File : 01_Operators_Overview.py

Description:
This file provides an overview of Python operators,
their purpose, and the different categories available
in Python.

Author : Nikita Choudhary
Repository : Python Basics
=====================================================
"""

# =====================================================
# 1. What are Operators?
# =====================================================

# Operators are special symbols used to perform
# operations on variables and values.

a = 10
b = 5

print("Value of a:", a)
print("Value of b:", b)

# =====================================================
# 2. Why Do We Use Operators?
# =====================================================

# Operators help us:
# ✔ Perform calculations
# ✔ Compare values
# ✔ Assign values
# ✔ Combine conditions
# ✔ Work with bits
# ✔ Check object identity
# ✔ Check membership

print("\nOperators make programming easier and more efficient.")

# =====================================================
# 3. Categories of Python Operators
# =====================================================

print("\nPython Operators")

print("1. Arithmetic Operators")
print("2. Assignment Operators")
print("3. Comparison Operators")
print("4. Logical Operators")
print("5. Identity Operators")
print("6. Membership Operators")
print("7. Bitwise Operators")

# =====================================================
# 4. Quick Preview
# =====================================================

print("\nArithmetic Example:")
print("10 + 5 =", a + b)

print("\nComparison Example:")
print("10 > 5 =", a > b)

print("\nLogical Example:")
print(True and False)

print("\nIdentity Example:")
print(a is b)

print("\nMembership Example:")
numbers = [10, 20, 30]
print(20 in numbers)

print("\nBitwise Example:")
print(a & b)

# =====================================================
# 5. Real-World Example
# =====================================================

product_price = 500
discount = 50

final_price = product_price - discount

print("\n===== Shopping Bill =====")

print("Original Price :", product_price)
print("Discount       :", discount)
print("Final Price    :", final_price)

# =====================================================
# 6. Operators Covered in This Section
# =====================================================

print("\nIn the upcoming lessons, you will learn:")

print("- Arithmetic Operators")
print("- Assignment Operators")
print("- Comparison Operators")
print("- Logical Operators")
print("- Identity Operators")
print("- Membership Operators")
print("- Bitwise Operators")

# =====================================================
# 7. Best Practices
# =====================================================

# ✔ Choose the correct operator for the task.
# ✔ Use parentheses to improve readability.
# ✔ Avoid writing overly complex expressions.
# ✔ Write clean and understandable code.

# =====================================================
# 8. Mini Practice
# =====================================================

# Try these on your own:
#
# 1. Create two variables and perform addition.
# 2. Compare two numbers using > and <.
# 3. Check if a value exists in a list.
# 4. Use the and operator with two conditions.
# 5. Explore a bitwise operator.

# =====================================================
# End of Program
# =====================================================

print("\nCongratulations! You completed the Introduction to Operators. 🎉")