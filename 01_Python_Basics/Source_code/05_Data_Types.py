"""
=====================================================
Topic: Data Types in Python
File : 05_Data_Types.py

Description:
This file demonstrates:
1. Numeric Data Types
2. Boolean Data Type
3. String Data Type
4. NoneType
5. Collection Data Types
6. Using type() function
7. Using isinstance() function
8. Mutable vs Immutable Data Types

Author : Nikita Choudhary
Repository : Python Basics
=====================================================
"""

# =====================================================
# 1. Integer (int)
# =====================================================

age = 21

print("Age:", age)
print("Type:", type(age))

# =====================================================
# 2. Float (float)
# =====================================================

price = 499.99

print("\nPrice:", price)
print("Type:", type(price))

# =====================================================
# 3. Complex (complex)
# =====================================================

complex_number = 3 + 4j

print("\nComplex Number:", complex_number)
print("Type:", type(complex_number))

# =====================================================
# 4. String (str)
# =====================================================

course = "Python Basics"

print("\nCourse:", course)
print("Type:", type(course))

# =====================================================
# 5. Boolean (bool)
# =====================================================

is_student = True

print("\nIs Student:", is_student)
print("Type:", type(is_student))

# =====================================================
# 6. NoneType
# =====================================================

result = None

print("\nResult:", result)
print("Type:", type(result))

# =====================================================
# 7. List (Mutable)
# =====================================================

fruits = ["Apple", "Banana", "Mango"]

print("\nFruits:", fruits)
print("Type:", type(fruits))

# =====================================================
# 8. Tuple (Immutable)
# =====================================================

colors = ("Red", "Green", "Blue")

print("\nColors:", colors)
print("Type:", type(colors))

# =====================================================
# 9. Set
# =====================================================

numbers = {10, 20, 30, 40}

print("\nNumbers:", numbers)
print("Type:", type(numbers))

# =====================================================
# 10. Dictionary
# =====================================================

student = {
    "name": "Nikita",
    "age": 21,
    "course": "Python Basics"
}

print("\nStudent:", student)
print("Type:", type(student))

# =====================================================
# 11. Using type()
# =====================================================

language = "Python"
marks = 95
cgpa = 8.8

print("\nUsing type()")
print(type(language))
print(type(marks))
print(type(cgpa))

# =====================================================
# 12. Using isinstance()
# =====================================================

print("\nUsing isinstance()")

print(isinstance(language, str))
print(isinstance(marks, int))
print(isinstance(cgpa, float))
print(isinstance(student, dict))

# =====================================================
# 13. Mutable Data Type Example
# =====================================================

fruits = ["Apple", "Banana"]

print("\nBefore:", fruits)

fruits.append("Orange")

print("After :", fruits)

# =====================================================
# 14. Immutable Data Type Example
# =====================================================

language = "Python"

print("\nOriginal:", language)

language = "Java"

print("Updated :", language)

# =====================================================
# 15. Real-World Example
# =====================================================

student_name = "Aman"
student_age = 20
student_marks = 91.5
is_passed = True

print("\n===== Student Details =====")

print("Name   :", student_name)
print("Age    :", student_age)
print("Marks  :", student_marks)
print("Passed :", is_passed)

print("\nData Types")
print(type(student_name))
print(type(student_age))
print(type(student_marks))
print(type(is_passed))

# =====================================================
# 16. Best Practices
# =====================================================

# ✔ Use the appropriate data type for your data.
# ✔ Use type() to identify an object's data type.
# ✔ Use isinstance() when checking an object's type.
# ✔ Understand which data types are mutable and immutable.

# Mutable:
# list, set, dictionary

# Immutable:
# int, float, bool, str, tuple, complex

# =====================================================
# 17. Mini Practice
# =====================================================

# Try these on your own:
#
# 1. Create variables of all basic data types.
# 2. Print the type of each variable.
# 3. Create a list and add a new item.
# 4. Create a dictionary to store student information.
# 5. Use isinstance() to check whether a variable is a string.

# =====================================================
# End of Program
# =====================================================

print("\nCongratulations! You completed Data Types in Python. 🎉")