"""
=====================================================
Topic: Variables in Python
File : 04_Variables.py

Description:
This file demonstrates:
1. Creating variables
2. Naming variables
3. Multiple assignment
4. Assigning the same value
5. Reassigning variables
6. Dynamic typing
7. Using variables in expressions

Author : Nikita Choudhary
Repository : Python Basics
=====================================================
"""

# =====================================================
# 1. Creating Variables
# =====================================================

name = "Nikita"
age = 21
height = 5.4

print("Name   :", name)
print("Age    :", age)
print("Height :", height)

# =====================================================
# 2. Variable Naming Rules
# =====================================================

student_name = "Rahul"
employee_salary = 50000
is_logged_in = True

print("\nStudent Name    :", student_name)
print("Employee Salary :", employee_salary)
print("Logged In       :", is_logged_in)

# =====================================================
# 3. Multiple Variable Assignment
# =====================================================

city, state, country = "Jaipur", "Rajasthan", "India"

print("\nCity    :", city)
print("State   :", state)
print("Country :", country)

# =====================================================
# 4. Assigning the Same Value
# =====================================================

x = y = z = 100

print("\nValue of x:", x)
print("Value of y:", y)
print("Value of z:", z)

# =====================================================
# 5. Reassigning Variables
# =====================================================

course = "Python Basics"

print("\nCourse:", course)

course = "Advanced Python"

print("Updated Course:", course)

# =====================================================
# 6. Dynamic Typing
# =====================================================

value = 100
print("\nValue :", value)
print("Type  :", type(value))

value = 99.99
print("\nValue :", value)
print("Type  :", type(value))

value = "Python"
print("\nValue :", value)
print("Type  :", type(value))

value = True
print("\nValue :", value)
print("Type  :", type(value))

# =====================================================
# 7. Variables in Expressions
# =====================================================

price = 799
gst = 18

total_price = price + gst

print("\nProduct Price :", price)
print("GST           :", gst)
print("Total Price   :", total_price)

# =====================================================
# 8. Swapping Variables
# =====================================================

a = 10
b = 20

print("\nBefore Swapping")
print("a =", a)
print("b =", b)

a, b = b, a

print("\nAfter Swapping")
print("a =", a)
print("b =", b)

# =====================================================
# 9. Real-World Example
# =====================================================

student_name = "Aman"
python_marks = 92
statistics_marks = 88

total_marks = python_marks + statistics_marks

print("\n===== Student Report =====")
print("Student Name      :", student_name)
print("Python Marks      :", python_marks)
print("Statistics Marks  :", statistics_marks)
print("Total Marks       :", total_marks)

# =====================================================
# 10. Best Practices
# =====================================================

# ✔ Use meaningful variable names.
# ✔ Follow snake_case naming convention.
# ✔ Avoid using Python keywords as variable names.
# ✔ Keep variable names descriptive and readable.

# Good Examples
student_age = 20
account_balance = 15000
is_registered = True

# Bad Examples
# a = 20
# x = 100
# data = "ABC"   # Too generic

# =====================================================
# 11. Mini Practice
# =====================================================

# Try these on your own:
#
# 1. Create variables for your name, age, and city.
# 2. Swap two numbers without using a third variable.
# 3. Calculate the total price of three products.
# 4. Store your favourite programming language in a variable.
# 5. Print the data type of each variable.

# =====================================================
# End of Program
# =====================================================

print("\nCongratulations! You completed Variables in Python. 🎉")