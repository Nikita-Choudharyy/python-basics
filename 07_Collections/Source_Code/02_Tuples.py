"""
=====================================================
Topic: Tuples in Python
File : 02_Tuples.py

Description:
This file demonstrates:
1. Introduction to Tuples
2. Creating Tuples
3. Accessing Tuple Elements
4. Indexing
5. Negative Indexing
6. Tuple Slicing
7. Tuple Packing & Unpacking
8. Nested Tuples
9. Membership Operators
10. Tuple Length
11. Real-World Examples
12. Best Practices

Author : Nikita Choudhary
Repository : Python Basics
=====================================================
"""

# =====================================================
# 1. What is a Tuple?
# =====================================================

# A tuple is an ordered and immutable collection.
# Once created, its elements cannot be changed.

print("===== Python Tuples =====")

# =====================================================
# 2. Creating Tuples
# =====================================================

print("\n===== Creating Tuples =====")

fruits = ("Apple", "Banana", "Mango")

numbers = (10, 20, 30, 40)

mixed_data = ("Python", 3.13, True, 95)

print(fruits)
print(numbers)
print(mixed_data)

# =====================================================
# 3. Accessing Tuple Elements
# =====================================================

print("\n===== Accessing Elements =====")

courses = (
    "Python",
    "SQL",
    "Machine Learning",
    "Git"
)

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
# 6. Tuple Slicing
# =====================================================

print("\n===== Tuple Slicing =====")

print(courses[0:2])

print(courses[1:])

print(courses[:3])

print(courses[::-1])

# =====================================================
# 7. Tuple Packing
# =====================================================

print("\n===== Tuple Packing =====")

student = "Nikita", 21, "AI Engineer"

print(student)

# =====================================================
# 8. Tuple Unpacking
# =====================================================

print("\n===== Tuple Unpacking =====")

name, age, profession = student

print(name)
print(age)
print(profession)

# =====================================================
# 9. Nested Tuples
# =====================================================

print("\n===== Nested Tuples =====")

employees = (
    ("Rahul", "Developer"),
    ("Aman", "Designer"),
    ("Neha", "Data Analyst")
)

print(employees)

print(employees[1])

print(employees[2][1])

# =====================================================
# 10. Membership Operators
# =====================================================

print("\n===== Membership Operators =====")

languages = (
    "Python",
    "Java",
    "C++"
)

print("Python" in languages)

print("Go" in languages)

print("Rust" not in languages)

# =====================================================
# 11. Finding Length
# =====================================================

print("\n===== len() =====")

months = (
    "January",
    "February",
    "March",
    "April"
)

print("Total Months:", len(months))

# =====================================================
# 12. Tuple Immutability
# =====================================================

print("\n===== Tuple Immutability =====")

colors = (
    "Red",
    "Green",
    "Blue"
)

print(colors)

# Tuples cannot be modified.
# Uncommenting the next line will raise an error.

# colors[0] = "Black"

# =====================================================
# 13. Real-World Example - RGB Color
# =====================================================

print("\n===== RGB Color =====")

rgb = (255, 165, 0)

print("Red   :", rgb[0])
print("Green :", rgb[1])
print("Blue  :", rgb[2])

# =====================================================
# 14. Real-World Example - GPS Coordinates
# =====================================================

print("\n===== GPS Coordinates =====")

location = (26.9124, 75.7873)

print("Latitude :", location[0])
print("Longitude:", location[1])

# =====================================================
# 15. Real-World Example - Student Record
# =====================================================

print("\n===== Student Record =====")

student_record = (
    "Nikita",
    "Computer Science",
    8.9
)

print("Name :", student_record[0])
print("Branch :", student_record[1])
print("CGPA :", student_record[2])

# =====================================================
# 16. Best Practices
# =====================================================

# ✔ Use tuples for fixed data.
# ✔ Store related values together.
# ✔ Use tuple unpacking for readability.
# ✔ Choose tuples when data should not change.
# ✔ Use meaningful variable names.

# =====================================================
# 17. Mini Practice
# =====================================================

# Try these on your own:
#
# 1. Create a tuple of five countries.
# 2. Print the first and last element.
# 3. Reverse a tuple using slicing.
# 4. Create a nested tuple.
# 5. Unpack a tuple into variables.
# 6. Check whether "Python" exists in a tuple.
# 7. Find the total number of elements.

# =====================================================
# End of Program
# =====================================================

print("\nCongratulations! You completed Tuples in Python. 🎉")