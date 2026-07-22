"""
=====================================================
Topic: Dictionary Comprehension in Python
File : 06_Dictionary_Comprehension.py

Description:
This file demonstrates:
1. Introduction to Dictionary Comprehension
2. Basic Syntax
3. Dictionary Comprehension with Conditions
4. if-else in Dictionary Comprehension
5. Nested Dictionary Comprehension
6. Real-World Examples
7. Best Practices

Author : Nikita Choudhary
Repository : Python Basics
=====================================================
"""

# =====================================================
# 1. What is Dictionary Comprehension?
# =====================================================

# Dictionary Comprehension provides a concise
# and readable way to create dictionaries
# using a single line of code.

print("===== Dictionary Comprehension =====")

# =====================================================
# 2. Creating a Dictionary Using a Loop
# =====================================================

print("\n===== Using a For Loop =====")

square_dict = {}

for number in range(1, 6):
    square_dict[number] = number ** 2

print(square_dict)

# =====================================================
# 3. Creating a Dictionary Using Dictionary Comprehension
# =====================================================

print("\n===== Using Dictionary Comprehension =====")

square_dict = {number: number ** 2 for number in range(1, 6)}

print(square_dict)

# =====================================================
# 4. Dictionary with Even Numbers
# =====================================================

print("\n===== Even Numbers =====")

even_numbers = {
    number: number ** 2
    for number in range(1, 11)
    if number % 2 == 0
}

print(even_numbers)

# =====================================================
# 5. if-else in Dictionary Comprehension
# =====================================================

print("\n===== if-else Example =====")

marks = [92, 45, 78, 30, 86]

result = {
    mark: "Pass" if mark >= 50 else "Fail"
    for mark in marks
}

print(result)

# =====================================================
# 6. Working with Strings
# =====================================================

print("\n===== Word Length =====")

words = [
    "Python",
    "Machine",
    "Learning",
    "Git"
]

word_length = {
    word: len(word)
    for word in words
}

print(word_length)

# =====================================================
# 7. Converting Values
# =====================================================

print("\n===== Temperature Conversion =====")

temperatures = {
    "Jaipur": 38,
    "Delhi": 40,
    "Mumbai": 33
}

fahrenheit = {
    city: (temp * 9/5) + 32
    for city, temp in temperatures.items()
}

print(fahrenheit)

# =====================================================
# 8. Swapping Keys and Values
# =====================================================

print("\n===== Swap Keys and Values =====")

employee_ids = {
    "Rahul": 101,
    "Neha": 102,
    "Aman": 103
}

swapped = {
    value: key
    for key, value in employee_ids.items()
}

print(swapped)

# =====================================================
# 9. Nested Dictionary Comprehension
# =====================================================

print("\n===== Nested Dictionary =====")

multiplication_table = {
    number: {
        multiplier: number * multiplier
        for multiplier in range(1, 6)
    }
    for number in range(1, 4)
}

print(multiplication_table)

# =====================================================
# 10. Real-World Example - Student Grades
# =====================================================

print("\n===== Student Grades =====")

students = {
    "Aman": 82,
    "Neha": 94,
    "Rahul": 67,
    "Priya": 48
}

grades = {
    name: "Pass" if marks >= 50 else "Fail"
    for name, marks in students.items()
}

print(grades)

# =====================================================
# 11. Real-World Example - Product Prices
# =====================================================

print("\n===== Discounted Prices =====")

prices = {
    "Laptop": 60000,
    "Keyboard": 2500,
    "Mouse": 1200
}

discounted_prices = {
    item: price * 0.9
    for item, price in prices.items()
}

print(discounted_prices)

# =====================================================
# 12. Real-World Example - Employee Bonus
# =====================================================

print("\n===== Employee Bonus =====")

salary = {
    "Rahul": 50000,
    "Neha": 65000,
    "Aman": 45000
}

bonus = {
    employee: amount + 5000
    for employee, amount in salary.items()
}

print(bonus)

# =====================================================
# 13. Real-World Example - Username Length
# =====================================================

print("\n===== Username Length =====")

usernames = [
    "nikita_ai",
    "python_dev",
    "ml_engineer"
]

username_length = {
    username: len(username)
    for username in usernames
}

print(username_length)

# =====================================================
# 14. Best Practices
# =====================================================

# ✔ Use dictionary comprehension for simple transformations.
# ✔ Keep expressions short and readable.
# ✔ Use descriptive key and value names.
# ✔ Prefer normal loops when logic becomes complex.
# ✔ Avoid deeply nested comprehensions unless necessary.

# =====================================================
# 15. Mini Practice
# =====================================================

# Try these on your own:
#
# 1. Create a dictionary of numbers and their cubes.
# 2. Store only even numbers as keys.
# 3. Convert all names to uppercase.
# 4. Swap keys and values of a dictionary.
# 5. Apply a 15% discount to product prices.
# 6. Create a dictionary of city names and their lengths.
# 7. Create a multiplication table using nested dictionary comprehension.

# =====================================================
# End of Program
# =====================================================

print("\nCongratulations! You completed Dictionary Comprehension in Python. 🎉")