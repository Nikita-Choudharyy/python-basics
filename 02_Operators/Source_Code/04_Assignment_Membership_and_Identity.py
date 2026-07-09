"""
=====================================================
Topic: Assignment, Membership and Identity Operators
File : 04_Assignment_Membership_and_Identity.py

Description:
This file demonstrates:
1. Assignment Operators
2. Membership Operators
3. Identity Operators
4. Real-World Examples
5. Best Practices

Author : Nikita Choudhary
Repository : Python Basics
=====================================================
"""

# =====================================================
# 1. Assignment Operators
# =====================================================

print("===== Assignment Operators =====")

x = 10

print("Initial Value:", x)

# +=
x += 5
print("After += 5 :", x)

# -=
x -= 3
print("After -= 3 :", x)

# *=
x *= 2
print("After *= 2 :", x)

# /=
x /= 4
print("After /= 4 :", x)

# //=
x //= 2
print("After //= 2 :", x)

# %=
x %= 3
print("After %= 3 :", x)

# **=
x **= 2
print("After **= 2 :", x)

# =====================================================
# 2. Membership Operators
# =====================================================

print("\n===== Membership Operators =====")

fruits = ["Apple", "Banana", "Mango"]

print("Fruits:", fruits)

print("\nUsing 'in'")
print("Apple" in fruits)
print("Orange" in fruits)

print("\nUsing 'not in'")
print("Orange" not in fruits)
print("Banana" not in fruits)

# =====================================================
# 3. Identity Operators
# =====================================================

print("\n===== Identity Operators =====")

list1 = [10, 20, 30]
list2 = list1
list3 = [10, 20, 30]

print("list1 is list2     :", list1 is list2)
print("list1 is list3     :", list1 is list3)

print("list1 is not list3 :", list1 is not list3)

# =====================================================
# 4. Difference Between == and is
# =====================================================

print("\n===== == vs is =====")

a = [1, 2, 3]
b = [1, 2, 3]

print("a == b :", a == b)
print("a is b :", a is b)

# =====================================================
# 5. Real-World Example
# =====================================================

print("\n===== Student Portal =====")

available_courses = [
    "Python",
    "SQL",
    "Machine Learning",
    "Data Visualization"
]

selected_course = "Python"

print("Selected Course :", selected_course)
print("Available        :", selected_course in available_courses)

# =====================================================
# 6. Real-World Example (Identity)
# =====================================================

print("\n===== Object Identity =====")

student_record = {
    "Name": "Nikita",
    "Marks": 95
}

backup_record = student_record

print(student_record is backup_record)

# =====================================================
# 7. Best Practices
# =====================================================

# ✔ Use assignment operators to simplify expressions.
# ✔ Use 'in' and 'not in' for checking membership.
# ✔ Use 'is' only for object identity.
# ✔ Use '==' when comparing values.
# ✔ Avoid using 'is' for numbers or strings.

# =====================================================
# 8. Mini Practice
# =====================================================

# Try these on your own:
#
# 1. Practice all assignment operators.
# 2. Check whether your favourite fruit exists in a list.
# 3. Create two lists and compare them using == and is.
# 4. Check whether a student's name exists in a list.
# 5. Experiment with 'is not'.

# =====================================================
# End of Program
# =====================================================

print("\nCongratulations! You completed Assignment, Membership and Identity Operators. 🎉")