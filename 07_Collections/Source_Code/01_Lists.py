"""
=====================================================
Topic: Lists in Python
File : 01_Lists.py

Description:
This file demonstrates:
1. Introduction to Lists
2. Creating Lists
3. Accessing List Elements
4. Indexing
5. Negative Indexing
6. List Slicing
7. Updating List Elements
8. Nested Lists
9. Membership Operators
10. List Length
11. Real-World Examples
12. Best Practices

Author : Nikita Choudhary
Repository : Python Basics
=====================================================
"""

# =====================================================
# 1. What is a List?
# =====================================================

# A list is an ordered, mutable collection
# that can store multiple items of different
# data types.

print("===== Python Lists =====")

# =====================================================
# 2. Creating Lists
# =====================================================

print("\n===== Creating Lists =====")

fruits = ["Apple", "Banana", "Mango"]

numbers = [10, 20, 30, 40]

mixed_data = ["Python", 3.13, True, 95]

print(fruits)
print(numbers)
print(mixed_data)

# =====================================================
# 3. Accessing List Elements
# =====================================================

print("\n===== Accessing Elements =====")

courses = [
    "Python",
    "SQL",
    "Machine Learning",
    "Git"
]

print(courses[0])
print(courses[2])

# =====================================================
# 4. Positive Indexing
# =====================================================

print("\n===== Positive Indexing =====")

print(courses[1])
print(courses[3])

# =====================================================
# 5. Negative Indexing
# =====================================================

print("\n===== Negative Indexing =====")

print(courses[-1])
print(courses[-2])

# =====================================================
# 6. List Slicing
# =====================================================

print("\n===== List Slicing =====")

print(courses[0:2])

print(courses[1:])

print(courses[:3])

print(courses[::-1])

# =====================================================
# 7. Updating List Elements
# =====================================================

print("\n===== Updating List =====")

cities = [
    "Delhi",
    "Mumbai",
    "Kolkata"
]

print("Before:", cities)

cities[1] = "Jaipur"

print("After :", cities)

# =====================================================
# 8. Nested Lists
# =====================================================

print("\n===== Nested Lists =====")

student_data = [
    ["Rahul", 92],
    ["Aman", 88],
    ["Neha", 95]
]

print(student_data)

print(student_data[0])

print(student_data[2][1])

# =====================================================
# 9. Membership Operators
# =====================================================

print("\n===== Membership Operators =====")

languages = [
    "Python",
    "Java",
    "C++"
]

print("Python" in languages)

print("Go" in languages)

print("Rust" not in languages)

# =====================================================
# 10. Finding Length
# =====================================================

print("\n===== len() =====")

projects = [
    "Portfolio",
    "Weather App",
    "Calculator",
    "Chatbot"
]

print("Total Projects:", len(projects))

# =====================================================
# 11. Real-World Example - Shopping Cart
# =====================================================

print("\n===== Shopping Cart =====")

cart = [
    "Laptop",
    "Mouse",
    "Keyboard"
]

print("Items in Cart:")

for item in cart:
    print("-", item)

# =====================================================
# 12. Real-World Example - Top Movies
# =====================================================

print("\n===== Favourite Movies =====")

movies = [
    "Interstellar",
    "Inception",
    "3 Idiots",
    "The Martian"
]

print("First Movie :", movies[0])

print("Last Movie  :", movies[-1])

# =====================================================
# 13. Real-World Example - Monthly Expenses
# =====================================================

print("\n===== Monthly Expenses =====")

expenses = [
    4500,
    2200,
    1800,
    3200
]

print("Expenses:", expenses)

print("Total Categories:", len(expenses))

# =====================================================
# 14. Best Practices
# =====================================================

# ✔ Use meaningful list names.
# ✔ Store related items together.
# ✔ Use indexing carefully.
# ✔ Use slicing for extracting data.
# ✔ Avoid unnecessary nested lists.

# =====================================================
# 15. Mini Practice
# =====================================================

# Try these on your own:
#
# 1. Create a list of your favourite books.
# 2. Print the first and last item.
# 3. Replace one element with another.
# 4. Reverse a list using slicing.
# 5. Create a nested list of student marks.
# 6. Check whether "Python" exists in a list.
# 7. Find the total number of elements.

# =====================================================
# End of Program
# =====================================================

print("\nCongratulations! You completed Lists in Python. 🎉")