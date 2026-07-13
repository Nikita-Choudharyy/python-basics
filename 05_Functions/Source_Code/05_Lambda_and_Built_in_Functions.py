"""
=====================================================
Topic: Lambda and Built-in Functions in Python
File : 05_Lambda_and_Built_in_Functions.py

Description:
This file demonstrates:
1. Lambda Functions
2. Built-in Functions
3. enumerate()
4. zip()
5. any() and all()
6. Real-World Examples
7. Best Practices

Author : Nikita Choudhary
Repository : Python Basics
=====================================================
"""

# =====================================================
# 1. Lambda Function
# =====================================================

print("===== Lambda Function =====")

square = lambda number: number ** 2

print("Square of 9:", square(9))

# =====================================================
# 2. Lambda with Multiple Arguments
# =====================================================

print("\n===== Lambda with Multiple Arguments =====")

rectangle_area = lambda length, width: length * width

print("Area:", rectangle_area(12, 8))

# =====================================================
# 3. len()
# =====================================================

print("\n===== len() =====")

languages = [
    "Python",
    "SQL",
    "Machine Learning"
]

print("Total Courses:", len(languages))

# =====================================================
# 4. sum()
# =====================================================

print("\n===== sum() =====")

monthly_sales = [12000, 18000, 16000, 14000]

print("Total Sales:", sum(monthly_sales))

# =====================================================
# 5. max() and min()
# =====================================================

print("\n===== max() and min() =====")

temperatures = [31, 28, 36, 25, 33]

print("Highest Temperature:", max(temperatures))
print("Lowest Temperature :", min(temperatures))

# =====================================================
# 6. sorted()
# =====================================================

print("\n===== sorted() =====")

cities = [
    "Delhi",
    "Mumbai",
    "Jaipur",
    "Bengaluru"
]

print(sorted(cities))

print(sorted(cities, reverse=True))

# =====================================================
# 7. abs()
# =====================================================

print("\n===== abs() =====")

print(abs(-150))
print(abs(85))

# =====================================================
# 8. round()
# =====================================================

print("\n===== round() =====")

pi = 3.14159265

print(round(pi, 2))
print(round(pi, 4))

# =====================================================
# 9. pow()
# =====================================================

print("\n===== pow() =====")

print(pow(5, 2))
print(pow(2, 8))

# =====================================================
# 10. divmod()
# =====================================================

print("\n===== divmod() =====")

quotient, remainder = divmod(25, 4)

print("Quotient :", quotient)
print("Remainder:", remainder)

# =====================================================
# 11. enumerate()
# =====================================================

print("\n===== enumerate() =====")

tasks = [
    "Study Python",
    "Practice SQL",
    "Revise Statistics"
]

for index, task in enumerate(tasks, start=1):
    print(index, task)

# =====================================================
# 12. zip()
# =====================================================

print("\n===== zip() =====")

products = ["Laptop", "Keyboard", "Mouse"]
prices = [65000, 2500, 800]

for product, price in zip(products, prices):
    print(product, "₹", price)

# =====================================================
# 13. any() and all()
# =====================================================

print("\n===== any() and all() =====")

attendance = [True, True, False, True]

print("Any Present :", any(attendance))
print("All Present :", all(attendance))

# =====================================================
# 14. Real-World Example - Exam Ranking
# =====================================================

print("\n===== Exam Ranking =====")

marks = [88, 72, 95, 67, 91]

print("Highest Marks :", max(marks))
print("Lowest Marks  :", min(marks))
print("Average Marks :", round(sum(marks) / len(marks), 2))

# =====================================================
# 15. Real-World Example - Product Catalog
# =====================================================

print("\n===== Product Catalog =====")

products = [
    "Tablet",
    "Monitor",
    "Printer",
    "Camera"
]

for number, product in enumerate(products, start=101):
    print(number, product)

# =====================================================
# 16. Best Practices
# =====================================================

# ✔ Use lambda only for short expressions.
# ✔ Prefer normal functions for complex logic.
# ✔ Learn commonly used built-in functions.
# ✔ Write readable code instead of clever code.
# ✔ Choose the right built-in function for the task.

# =====================================================
# 17. Mini Practice
# =====================================================

# Try these on your own:
#
# 1. Create a lambda function to calculate the area of a circle.
# 2. Find the longest word in a list.
# 3. Find the total of five numbers using sum().
# 4. Round a decimal number to three places.
# 5. Number a list of books using enumerate().
# 6. Combine employee names and IDs using zip().
# 7. Check whether all students passed using all().

# =====================================================
# End of Program
# =====================================================

print("\nCongratulations! You completed Lambda and Built-in Functions in Python. 🎉")