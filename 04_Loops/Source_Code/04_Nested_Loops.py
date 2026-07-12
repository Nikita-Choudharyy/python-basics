"""
=====================================================
Topic: Nested Loops in Python
File : 04_Nested_Loops.py

Description:
This file demonstrates:
1. Introduction to Nested Loops
2. Nested for Loops
3. Nested while Loops
4. Combining for and while Loops
5. Real-World Examples
6. Best Practices

Author : Nikita Choudhary
Repository : Python Basics
=====================================================
"""

# =====================================================
# 1. What are Nested Loops?
# =====================================================

# A nested loop is a loop inside another loop.
# The inner loop executes completely for every
# iteration of the outer loop.

print("Nested Loop Examples")

# =====================================================
# 2. Basic Nested for Loop
# =====================================================

print("\n===== Basic Nested for Loop =====")

for row in range(1, 4):

    for column in range(1, 4):
        print(f"({row}, {column})", end=" ")

    print()

# =====================================================
# 3. Multiplication Table
# =====================================================

print("\n===== Multiplication Table =====")

for i in range(1, 4):

    for j in range(1, 6):
        print(f"{i} × {j} = {i * j}")

    print()

# =====================================================
# 4. Basic Nested while Loop
# =====================================================

print("\n===== Basic Nested while Loop =====")

row = 1

while row <= 3:

    column = 1

    while column <= 3:
        print(f"({row}, {column})", end=" ")
        column += 1

    print()

    row += 1

# =====================================================
# 5. Combining for and while Loops
# =====================================================

print("\n===== for + while Loop =====")

for table in range(2, 4):

    multiplier = 1

    while multiplier <= 5:
        print(f"{table} × {multiplier} = {table * multiplier}")
        multiplier += 1

    print()

# =====================================================
# 6. Real-World Example - Classroom Seating
# =====================================================

print("\n===== Classroom Seating =====")

rows = 3
columns = 4

for row in range(1, rows + 1):

    for column in range(1, columns + 1):
        print(f"Seat-{row}{column}", end="  ")

    print()

# =====================================================
# 7. Real-World Example - Weekly Schedule
# =====================================================

print("\n===== Weekly Schedule =====")

days = ["Monday", "Tuesday", "Wednesday"]

subjects = ["Python", "SQL", "Statistics"]

for day in days:

    print(f"\n{day}")

    for subject in subjects:
        print("-", subject)

# =====================================================
# 8. Real-World Example - Shopping System
# =====================================================

print("\n===== Customer Orders =====")

customers = ["Rahul", "Anjali"]

orders = ["Laptop", "Mouse", "Keyboard"]

for customer in customers:

    print(f"\nCustomer: {customer}")

    for order in orders:
        print("Purchased:", order)

# =====================================================
# 9. Real-World Example - Employee Attendance
# =====================================================

print("\n===== Employee Attendance =====")

departments = ["HR", "IT"]

employees = ["Employee-1", "Employee-2"]

for department in departments:

    print(f"\nDepartment: {department}")

    for employee in employees:
        print(employee, "- Present")

# =====================================================
# 10. Star Pattern
# =====================================================

print("\n===== Star Pattern =====")

for row in range(5):

    for column in range(row + 1):
        print("*", end=" ")

    print()

# =====================================================
# 11. Number Pattern
# =====================================================

print("\n===== Number Pattern =====")

for row in range(1, 6):

    for number in range(1, row + 1):
        print(number, end=" ")

    print()

# =====================================================
# 12. Best Practices
# =====================================================

# ✔ Keep nesting levels as low as possible.
# ✔ Use meaningful variable names.
# ✔ Avoid deeply nested loops for better readability.
# ✔ Use nested loops only when required.

# =====================================================
# 13. Mini Practice
# =====================================================

# Try these on your own:
#
# 1. Print a square star pattern.
# 2. Print an inverted triangle pattern.
# 3. Print a multiplication table from 1 to 10.
# 4. Create a classroom seating arrangement.
# 5. Create a restaurant menu with categories and items.
# 6. Display employee attendance department-wise.
# 7. Create a calendar-like grid using nested loops.

# =====================================================
# End of Program
# =====================================================

print("\nCongratulations! You completed Nested Loops in Python. 🎉")