"""
=====================================================
Topic: String Formatting in Python
File : 03_String_Formatting.py

Description:
This file demonstrates:
1. Old Style (%) Formatting
2. str.format() Method
3. f-Strings
4. Alignment Formatting
5. Number Formatting
6. Precision Formatting
7. Real-World Examples
8. Best Practices

Author : Nikita Choudhary
Repository : Python Basics
=====================================================
"""

# =====================================================
# 1. Old Style (%) Formatting
# =====================================================

print("===== Old Style Formatting =====")

name = "Nikita"
age = 21

print("Name: %s" % name)
print("Age : %d" % age)

# =====================================================
# 2. str.format() Method
# =====================================================

print("\n===== str.format() =====")

city = "Jaipur"
state = "Rajasthan"

print("City: {}".format(city))
print("State: {}".format(state))

print("{} is located in {}.".format(city, state))

# =====================================================
# 3. f-Strings (Recommended)
# =====================================================

print("\n===== f-Strings =====")

language = "Python"
version = 3.13

print(f"Programming Language: {language}")
print(f"Latest Version: {version}")

# =====================================================
# 4. Formatting Numbers
# =====================================================

print("\n===== Number Formatting =====")

price = 15499.5678

print(f"Original Price : {price}")
print(f"Rounded Price  : {price:.2f}")

# =====================================================
# 5. Formatting Percentages
# =====================================================

print("\n===== Percentage Formatting =====")

accuracy = 0.96875

print(f"Model Accuracy: {accuracy:.2%}")

# =====================================================
# 6. Width and Alignment
# =====================================================

print("\n===== Alignment =====")

course = "Python"

print(f"|{course:<15}| Left")
print(f"|{course:^15}| Center")
print(f"|{course:>15}| Right")

# =====================================================
# 7. Formatting Large Numbers
# =====================================================

print("\n===== Large Numbers =====")

population = 1450000000

print(f"Population: {population:,}")

# =====================================================
# 8. Real-World Example - Student Report
# =====================================================

print("\n===== Student Report =====")

student = "Ananya"
marks = 91.456

print(f"Student Name : {student}")
print(f"Final Marks  : {marks:.2f}")

# =====================================================
# 9. Real-World Example - Employee Salary Slip
# =====================================================

print("\n===== Salary Slip =====")

employee = "Rahul"

salary = 87500

print(f"Employee : {employee}")
print(f"Salary   : ₹{salary:,}")

# =====================================================
# 10. Real-World Example - Invoice
# =====================================================

print("\n===== Invoice =====")

product = "Mechanical Keyboard"

quantity = 2

price = 3499

total = quantity * price

print(f"Product  : {product}")
print(f"Quantity : {quantity}")
print(f"Price    : ₹{price:,}")
print(f"Total    : ₹{total:,}")

# =====================================================
# 11. Real-World Example - Weather Report
# =====================================================

print("\n===== Weather Report =====")

city = "Delhi"

temperature = 34.567

humidity = 72

print(f"City        : {city}")
print(f"Temperature : {temperature:.1f}°C")
print(f"Humidity    : {humidity}%")

# =====================================================
# 12. Best Practices
# =====================================================

# ✔ Prefer f-strings in modern Python.
# ✔ Use .2f for decimal precision.
# ✔ Use commas for large numbers.
# ✔ Keep formatted strings readable.
# ✔ Avoid old (%) formatting in new projects.

# =====================================================
# 13. Mini Practice
# =====================================================

# Try these on your own:
#
# 1. Print your name and age using an f-string.
# 2. Display a price with two decimal places.
# 3. Print a large number with commas.
# 4. Center-align a word within 20 spaces.
# 5. Create a formatted invoice.
# 6. Display a percentage with two decimal places.
# 7. Create a formatted student report card.

# =====================================================
# End of Program
# =====================================================

print("\nCongratulations! You completed String Formatting in Python. 🎉")