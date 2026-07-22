"""
=====================================================
Topic: List Comprehension in Python
File : 05_List_Comprehension.py

Description:
This file demonstrates:
1. Introduction to List Comprehension
2. Basic Syntax
3. List Comprehension with Conditions
4. if-else in List Comprehension
5. Nested List Comprehension
6. Real-World Examples
7. Best Practices

Author : Nikita Choudhary
Repository : Python Basics
=====================================================
"""

# =====================================================
# 1. What is List Comprehension?
# =====================================================

# List Comprehension provides a shorter and more
# readable way to create lists using a single line of code.

print("===== List Comprehension =====")

# =====================================================
# 2. Creating a List Using a Loop
# =====================================================

print("\n===== Using a For Loop =====")

numbers = []

for num in range(1, 6):
    numbers.append(num)

print(numbers)

# =====================================================
# 3. Creating a List Using List Comprehension
# =====================================================

print("\n===== Using List Comprehension =====")

numbers = [num for num in range(1, 6)]

print(numbers)

# =====================================================
# 4. Squares of Numbers
# =====================================================

print("\n===== Squares of Numbers =====")

squares = [num ** 2 for num in range(1, 11)]

print(squares)

# =====================================================
# 5. Even Numbers
# =====================================================

print("\n===== Even Numbers =====")

even_numbers = [num for num in range(1, 21) if num % 2 == 0]

print(even_numbers)

# =====================================================
# 6. Odd Numbers
# =====================================================

print("\n===== Odd Numbers =====")

odd_numbers = [num for num in range(1, 21) if num % 2 != 0]

print(odd_numbers)

# =====================================================
# 7. if-else in List Comprehension
# =====================================================

print("\n===== if-else Example =====")

numbers = [4, 7, 10, 15, 18]

result = ["Even" if num % 2 == 0 else "Odd" for num in numbers]

print(result)

# =====================================================
# 8. Working with Strings
# =====================================================

print("\n===== Convert to Uppercase =====")

languages = [
    "python",
    "java",
    "sql",
    "go"
]

uppercase_languages = [language.upper() for language in languages]

print(uppercase_languages)

# =====================================================
# 9. Extract First Letter
# =====================================================

print("\n===== First Letter =====")

cities = [
    "Jaipur",
    "Delhi",
    "Mumbai",
    "Chennai"
]

first_letters = [city[0] for city in cities]

print(first_letters)

# =====================================================
# 10. Nested List Comprehension
# =====================================================

print("\n===== Nested List Comprehension =====")

matrix = [
    [1, 2],
    [3, 4],
    [5, 6]
]

flattened = [number for row in matrix for number in row]

print(flattened)

# =====================================================
# 11. Real-World Example - Student Grades
# =====================================================

print("\n===== Student Grades =====")

marks = [91, 65, 82, 48, 74]

grades = [
    "Pass" if mark >= 50 else "Fail"
    for mark in marks
]

print(grades)

# =====================================================
# 12. Real-World Example - Available Seats
# =====================================================

print("\n===== Available Seats =====")

seat_numbers = list(range(1, 21))

available_seats = [
    seat
    for seat in seat_numbers
    if seat % 3 != 0
]

print(available_seats)

# =====================================================
# 13. Real-World Example - Product Prices
# =====================================================

print("\n===== Product Prices =====")

prices = [499, 899, 1299, 1999]

discounted_prices = [
    price * 0.9
    for price in prices
]

print(discounted_prices)

# =====================================================
# 14. Real-World Example - Email Usernames
# =====================================================

print("\n===== Email Usernames =====")

emails = [
    "rahul@gmail.com",
    "neha@yahoo.com",
    "aman@outlook.com"
]

usernames = [
    email.split("@")[0]
    for email in emails
]

print(usernames)

# =====================================================
# 15. Best Practices
# =====================================================

# ✔ Use list comprehension for simple transformations.
# ✔ Keep expressions short and readable.
# ✔ Avoid deeply nested comprehensions.
# ✔ Use descriptive variable names.
# ✔ Prefer normal loops when the logic becomes complex.

# =====================================================
# 16. Mini Practice
# =====================================================

# Try these on your own:
#
# 1. Create a list of cubes from 1 to 10.
# 2. Extract only even numbers from a list.
# 3. Convert a list of names to lowercase.
# 4. Replace numbers greater than 50 with "High".
# 5. Flatten a nested list.
# 6. Extract the first character from every word.
# 7. Create a list of numbers divisible by both 3 and 5.

# =====================================================
# End of Program
# =====================================================

print("\nCongratulations! You completed List Comprehension in Python. 🎉")