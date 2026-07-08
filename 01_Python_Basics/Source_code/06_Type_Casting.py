"""
=====================================================
Topic: Type Casting in Python
File : 06_Type_Casting.py

Description:
This file demonstrates:
1. Implicit Type Casting
2. Explicit Type Casting
3. Common Type Conversion Functions
4. Type Casting with User Input
5. Real-World Examples
6. Best Practices

Author : Nikita Choudhary
Repository : Python Basics
=====================================================
"""

# =====================================================
# 1. Implicit Type Casting
# =====================================================

num1 = 10
num2 = 5.5

result = num1 + num2

print("Result:", result)
print("Type:", type(result))

# =====================================================
# 2. Explicit Type Casting - int()
# =====================================================

age = "21"

print("\nBefore:", age, type(age))

age = int(age)

print("After :", age, type(age))

# =====================================================
# 3. Explicit Type Casting - float()
# =====================================================

price = "499.99"

print("\nBefore:", price, type(price))

price = float(price)

print("After :", price, type(price))

# =====================================================
# 4. Explicit Type Casting - str()
# =====================================================

roll_number = 101

print("\nBefore:", roll_number, type(roll_number))

roll_number = str(roll_number)

print("After :", roll_number, type(roll_number))

# =====================================================
# 5. Explicit Type Casting - bool()
# =====================================================

print("\nBoolean Conversion Examples")

print(bool(1))
print(bool(0))
print(bool("Python"))
print(bool(""))
print(bool(None))

# =====================================================
# 6. Type Casting with User Input
# =====================================================

marks = int(input("\nEnter your marks: "))

print("Marks:", marks)
print("Type :", type(marks))

# =====================================================
# 7. Real-World Example
# =====================================================

product_price = float(input("\nEnter product price: "))

gst = 50

total_price = product_price + gst

print("\n===== Bill Summary =====")
print("Product Price :", product_price)
print("GST           :", gst)
print("Total Price   :", total_price)

# =====================================================
# 8. Using isinstance()
# =====================================================

number = 95

print("\nUsing isinstance()")

print(isinstance(number, int))
print(isinstance(number, float))

# =====================================================
# 9. Common Type Conversion Functions
# =====================================================

print("\nCommon Type Conversion Examples")

print(int(5.99))
print(float(10))
print(str(100))
print(list("Python"))
print(tuple([1, 2, 3]))
print(set([1, 2, 2, 3]))
print(dict([("Name", "Nikita"), ("Age", 21)]))

# =====================================================
# 10. Best Practices
# =====================================================

# ✔ Convert user input to the required data type.
# ✔ Always ensure the value can be converted.
# ✔ Use try-except when taking numeric input from users.
# ✔ Avoid unnecessary type conversions.

# =====================================================
# 11. Mini Practice
# =====================================================

# Try these on your own:
#
# 1. Convert a float to an integer.
# 2. Convert an integer to a string.
# 3. Take two numbers as input and print their sum.
# 4. Convert a string into a float.
# 5. Convert a list into a tuple.

# =====================================================
# End of Program
# =====================================================

print("\nCongratulations! You completed Type Casting in Python. 🎉")