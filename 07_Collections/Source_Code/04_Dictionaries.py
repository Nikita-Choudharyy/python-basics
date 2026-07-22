"""
=====================================================
Topic: Dictionaries in Python
File : 04_Dictionaries.py

Description:
This file demonstrates:
1. Introduction to Dictionaries
2. Creating Dictionaries
3. Accessing Values
4. Adding Key-Value Pairs
5. Updating Values
6. Removing Key-Value Pairs
7. Membership Operators
8. Dictionary Length
9. Nested Dictionaries
10. Real-World Examples
11. Best Practices

Author : Nikita Choudhary
Repository : Python Basics
=====================================================
"""

# =====================================================
# 1. What is a Dictionary?
# =====================================================

# A dictionary is an unordered, mutable collection
# that stores data as key-value pairs.

print("===== Python Dictionaries =====")

# =====================================================
# 2. Creating Dictionaries
# =====================================================

print("\n===== Creating Dictionaries =====")

student = {
    "name": "Nikita",
    "age": 21,
    "course": "Computer Science"
}

print(student)

# =====================================================
# 3. Accessing Values
# =====================================================

print("\n===== Accessing Values =====")

print("Name   :", student["name"])
print("Age    :", student["age"])
print("Course :", student["course"])

# =====================================================
# 4. Adding Key-Value Pairs
# =====================================================

print("\n===== Adding New Data =====")

student["city"] = "Jaipur"

print(student)

# =====================================================
# 5. Updating Values
# =====================================================

print("\n===== Updating Values =====")

student["age"] = 22

print(student)

# =====================================================
# 6. Removing Key-Value Pairs
# =====================================================

print("\n===== Removing Data =====")

del student["city"]

print(student)

# =====================================================
# 7. Membership Operators
# =====================================================

print("\n===== Membership Operators =====")

print("name" in student)

print("salary" in student)

print("city" not in student)

# =====================================================
# 8. Finding Length
# =====================================================

print("\n===== len() =====")

print("Total Keys:", len(student))

# =====================================================
# 9. Nested Dictionaries
# =====================================================

print("\n===== Nested Dictionaries =====")

employees = {
    "EMP101": {
        "name": "Rahul",
        "department": "HR"
    },
    "EMP102": {
        "name": "Neha",
        "department": "Finance"
    }
}

print(employees)

print(employees["EMP101"]["name"])
print(employees["EMP102"]["department"])

# =====================================================
# 10. Real-World Example - Student Profile
# =====================================================

print("\n===== Student Profile =====")

profile = {
    "Name": "Ananya",
    "Branch": "Information Technology",
    "CGPA": 9.1
}

print(profile)

# =====================================================
# 11. Real-World Example - Product Information
# =====================================================

print("\n===== Product Information =====")

product = {
    "id": 101,
    "name": "Wireless Mouse",
    "price": 899,
    "stock": 25
}

print(product)

# =====================================================
# 12. Real-World Example - Employee Details
# =====================================================

print("\n===== Employee Details =====")

employee = {
    "Employee ID": "EMP501",
    "Name": "Amit",
    "Department": "AI Research",
    "Experience": 4
}

print(employee)

# =====================================================
# 13. Real-World Example - Book Record
# =====================================================

print("\n===== Book Record =====")

book = {
    "Title": "Python Crash Course",
    "Author": "Eric Matthes",
    "Year": 2023
}

print(book)

# =====================================================
# 14. Best Practices
# =====================================================

# ✔ Use meaningful key names.
# ✔ Keep keys unique.
# ✔ Use dictionaries for structured data.
# ✔ Update values using keys.
# ✔ Use nested dictionaries for hierarchical data.

# =====================================================
# 15. Mini Practice
# =====================================================

# Try these on your own:
#
# 1. Create a dictionary for your favourite movie.
# 2. Add a new key-value pair.
# 3. Update an existing value.
# 4. Delete a key from the dictionary.
# 5. Create a nested dictionary.
# 6. Check whether a key exists.
# 7. Find the total number of keys.

# =====================================================
# End of Program
# =====================================================

print("\nCongratulations! You completed Dictionaries in Python. 🎉")