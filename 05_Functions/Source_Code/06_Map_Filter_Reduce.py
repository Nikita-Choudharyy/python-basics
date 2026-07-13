"""
=====================================================
Topic: map(), filter(), and reduce() in Python
File : 06_Map_Filter_Reduce.py

Description:
This file demonstrates:
1. map() Function
2. filter() Function
3. reduce() Function
4. Practical Examples
5. Best Practices

Author : Nikita Choudhary
Repository : Python Basics
=====================================================
"""

from functools import reduce

# =====================================================
# 1. map() Function
# =====================================================

print("===== map() Function =====")

numbers = [2, 4, 6, 8, 10]

squares = list(map(lambda number: number ** 2, numbers))

print("Original Numbers :", numbers)
print("Squared Numbers  :", squares)

# =====================================================
# 2. map() with String Data
# =====================================================

print("\n===== map() with Strings =====")

names = ["nikita", "rahul", "priya"]

capitalized_names = list(map(str.title, names))

print(capitalized_names)

# =====================================================
# 3. filter() Function
# =====================================================

print("\n===== filter() Function =====")

numbers = [5, 12, 19, 25, 30, 41]

even_numbers = list(filter(lambda number: number % 2 == 0, numbers))

print("Even Numbers:", even_numbers)

# =====================================================
# 4. filter() with Strings
# =====================================================

print("\n===== filter() with Strings =====")

languages = [
    "Python",
    "Java",
    "C",
    "JavaScript",
    "Go"
]

long_names = list(
    filter(lambda language: len(language) > 4, languages)
)

print(long_names)

# =====================================================
# 5. reduce() Function
# =====================================================

print("\n===== reduce() Function =====")

numbers = [2, 3, 4, 5]

product = reduce(
    lambda x, y: x * y,
    numbers
)

print("Product:", product)

# =====================================================
# 6. reduce() for Maximum Value
# =====================================================

print("\n===== reduce() for Maximum =====")

scores = [72, 91, 84, 99, 88]

highest_score = reduce(
    lambda x, y: x if x > y else y,
    scores
)

print("Highest Score:", highest_score)

# =====================================================
# 7. Real-World Example - Student Bonus Marks
# =====================================================

print("\n===== Student Bonus Marks =====")

marks = [65, 72, 81, 90]

updated_marks = list(
    map(lambda mark: mark + 5, marks)
)

print(updated_marks)

# =====================================================
# 8. Real-World Example - Eligible Employees
# =====================================================

print("\n===== Eligible Employees =====")

experience = [1, 5, 7, 2, 10, 4]

eligible = list(
    filter(lambda year: year >= 5, experience)
)

print(eligible)

# =====================================================
# 9. Real-World Example - Total Revenue
# =====================================================

print("\n===== Total Revenue =====")

monthly_revenue = [
    120000,
    135000,
    128000,
    142000
]

total_revenue = reduce(
    lambda x, y: x + y,
    monthly_revenue
)

print("Total Revenue: ₹", total_revenue)

# =====================================================
# 10. Best Practices
# =====================================================

# ✔ Use map() for transforming data.
# ✔ Use filter() for selecting data.
# ✔ Use reduce() for combining data into one result.
# ✔ Prefer readability over writing overly complex lambdas.
# ✔ Import reduce() from functools before using it.

# =====================================================
# 11. Mini Practice
# =====================================================

# Try these on your own:
#
# 1. Double every number using map().
# 2. Convert all names to uppercase using map().
# 3. Filter numbers greater than 50.
# 4. Filter all negative numbers.
# 5. Find the sum of numbers using reduce().
# 6. Find the minimum value using reduce().
# 7. Calculate the total price of products using reduce().

# =====================================================
# End of Program
# =====================================================

print("\nCongratulations! You completed map(), filter(), and reduce() in Python. 🎉")