"""
=====================================================
Topic: Arithmetic Operators in Python
File : 02_Arithmetic_Operators.py

Description:
This file demonstrates:
1. Addition Operator (+)
2. Subtraction Operator (-)
3. Multiplication Operator (*)
4. Division Operator (/)
5. Floor Division Operator (//)
6. Modulus Operator (%)
7. Exponentiation Operator (**)
8. Operator Precedence
9. Real-World Example
10. Best Practices

Author : Nikita Choudhary
Repository : Python Basics
=====================================================
"""

# =====================================================
# 1. Creating Variables
# =====================================================

num1 = 20
num2 = 6

print("First Number :", num1)
print("Second Number:", num2)

# =====================================================
# 2. Addition Operator (+)
# =====================================================

addition = num1 + num2

print("\nAddition")
print(f"{num1} + {num2} = {addition}")

# =====================================================
# 3. Subtraction Operator (-)
# =====================================================

subtraction = num1 - num2

print("\nSubtraction")
print(f"{num1} - {num2} = {subtraction}")

# =====================================================
# 4. Multiplication Operator (*)
# =====================================================

multiplication = num1 * num2

print("\nMultiplication")
print(f"{num1} * {num2} = {multiplication}")

# =====================================================
# 5. Division Operator (/)
# =====================================================

division = num1 / num2

print("\nDivision")
print(f"{num1} / {num2} = {division}")

# =====================================================
# 6. Floor Division Operator (//)
# =====================================================

floor_division = num1 // num2

print("\nFloor Division")
print(f"{num1} // {num2} = {floor_division}")

# =====================================================
# 7. Modulus Operator (%)
# =====================================================

remainder = num1 % num2

print("\nModulus")
print(f"{num1} % {num2} = {remainder}")

# =====================================================
# 8. Exponentiation Operator (**)
# =====================================================

power = num1 ** 2

print("\nExponentiation")
print(f"{num1} ** 2 = {power}")

# =====================================================
# 9. Operator Precedence
# =====================================================

result = 10 + 5 * 2

print("\nOperator Precedence")
print("10 + 5 * 2 =", result)

result = (10 + 5) * 2

print("(10 + 5) * 2 =", result)

# =====================================================
# 10. Real-World Example
# =====================================================

product_price = 1500
quantity = 3
discount = 250

total_price = product_price * quantity
final_price = total_price - discount

print("\n===== Shopping Bill =====")

print("Product Price :", product_price)
print("Quantity      :", quantity)
print("Total Price   :", total_price)
print("Discount      :", discount)
print("Final Price   :", final_price)

# =====================================================
# 11. Best Practices
# =====================================================

# ✔ Use meaningful variable names.
# ✔ Use parentheses to improve readability.
# ✔ Avoid dividing by zero.
# ✔ Understand the difference between / and //.
# ✔ Use ** instead of repeated multiplication for powers.

# =====================================================
# 12. Mini Practice
# =====================================================

# Try these on your own:
#
# 1. Create two numbers and perform all arithmetic operations.
# 2. Find the square of a number.
# 3. Find the cube of a number.
# 4. Calculate the remainder when 45 is divided by 7.
# 5. Calculate the total cost of 5 items priced at ₹299 each.

# =====================================================
# End of Program
# =====================================================

print("\nCongratulations! You completed Arithmetic Operators in Python. 🎉")