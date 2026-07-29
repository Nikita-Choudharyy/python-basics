"""
=========================================================
Topic : Built-in Exceptions
File  : 04_Built_in_Exceptions.py

Description:
This file demonstrates the most commonly used built-in
exceptions available in Python.

Topics Covered:
1. ZeroDivisionError
2. ValueError
3. TypeError
4. NameError
5. IndexError
6. KeyError
7. AttributeError
8. FileNotFoundError
9. ModuleNotFoundError
10. ImportError
11. Best Practices

Author : Nikita Choudhary
Repository : Python Basics
=========================================================
"""

# =====================================================
# Built-in Exceptions
# =====================================================

print("=" * 60)
print("BUILT-IN EXCEPTIONS")
print("=" * 60)

# =====================================================
# 1. ZeroDivisionError
# =====================================================

print("\n===== ZeroDivisionError =====")

try:

    result = 10 / 0

except ZeroDivisionError:

    print("Cannot divide by zero.")

# =====================================================
# 2. ValueError
# =====================================================

print("\n===== ValueError =====")

try:

    age = int("Twenty")

except ValueError:

    print("Invalid integer value.")

# =====================================================
# 3. TypeError
# =====================================================

print("\n===== TypeError =====")

try:

    result = 100 + "50"

except TypeError:

    print("Cannot add integer and string.")

# =====================================================
# 4. NameError
# =====================================================

print("\n===== NameError =====")

try:

    print(student_name)

except NameError:

    print("Variable is not defined.")

# =====================================================
# 5. IndexError
# =====================================================

print("\n===== IndexError =====")

languages = [
    "Python",
    "Java",
    "C++"
]

try:

    print(languages[10])

except IndexError:

    print("List index is out of range.")

# =====================================================
# 6. KeyError
# =====================================================

print("\n===== KeyError =====")

student = {

    "name": "Nikita",

    "course": "Python"

}

try:

    print(student["marks"])

except KeyError:

    print("Requested key does not exist.")

# =====================================================
# 7. AttributeError
# =====================================================

print("\n===== AttributeError =====")

message = "Python"

try:

    message.append(" Programming")

except AttributeError:

    print("String object has no append() method.")

# =====================================================
# 8. FileNotFoundError
# =====================================================

print("\n===== FileNotFoundError =====")

try:

    with open("missing_file.txt", "r") as file:

        print(file.read())

except FileNotFoundError:

    print("File does not exist.")

# =====================================================
# 9. ModuleNotFoundError
# =====================================================

print("\n===== ModuleNotFoundError =====")

try:

    import my_custom_module

except ModuleNotFoundError:

    print("Module not found.")

# =====================================================
# 10. ImportError
# =====================================================

print("\n===== ImportError =====")

try:

    from math import cube

except ImportError:

    print("Requested object cannot be imported.")

# =====================================================
# 11. Real-World Example - Student Record
# =====================================================

print("\n===== Student Record =====")

student = {

    "name": "Nikita",

    "marks": 95

}

try:

    print(student["grade"])

except KeyError:

    print("Grade information is not available.")

# =====================================================
# 12. Real-World Example - Employee Data
# =====================================================

print("\n===== Employee Data =====")

employees = [

    "Rahul",

    "Neha",

    "Aman"

]

try:

    print(employees[5])

except IndexError:

    print("Employee record not found.")

# =====================================================
# 13. Best Practices
# =====================================================

# ✔ Catch specific exceptions whenever possible.
# ✔ Read exception messages carefully.
# ✔ Avoid using bare except.
# ✔ Validate user input before processing.
# ✔ Write meaningful error messages.
# ✔ Handle expected exceptions gracefully.

# =====================================================
# 14. Mini Practice
# =====================================================

# Try these yourself:
#
# 1. Create a ZeroDivisionError.
# 2. Create a ValueError.
# 3. Create a TypeError.
# 4. Create a NameError.
# 5. Create an IndexError.
# 6. Create a KeyError.
# 7. Create an AttributeError.
# 8. Create a FileNotFoundError.
# 9. Create a ModuleNotFoundError.
# 10. Create an ImportError.

# =====================================================
# End of Program
# =====================================================

print("\nCongratulations! You completed Built-in Exceptions. 🎉")