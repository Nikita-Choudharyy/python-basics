"""
=====================================================
Topic: Sets in Python
File : 03_Sets.py

Description:
This file demonstrates:
1. Introduction to Sets
2. Creating Sets
3. Unique Elements
4. Accessing Set Elements
5. Membership Operators
6. Adding Elements
7. Removing Elements
8. Set Length
9. Real-World Examples
10. Best Practices

Author : Nikita Choudhary
Repository : Python Basics
=====================================================
"""

# =====================================================
# 1. What is a Set?
# =====================================================

# A set is an unordered, mutable collection
# that stores only unique elements.

print("===== Python Sets =====")

# =====================================================
# 2. Creating Sets
# =====================================================

print("\n===== Creating Sets =====")

fruits = {"Apple", "Banana", "Mango"}

numbers = {10, 20, 30, 40}

mixed_data = {"Python", 3.13, True, 95}

print(fruits)
print(numbers)
print(mixed_data)

# =====================================================
# 3. Unique Elements
# =====================================================

print("\n===== Unique Elements =====")

colors = {"Red", "Blue", "Green", "Blue", "Red"}

print(colors)

# Duplicate values are automatically removed.

# =====================================================
# 4. Empty Set
# =====================================================

print("\n===== Empty Set =====")

empty_set = set()

print(empty_set)

# {} creates an empty dictionary, not a set.

# =====================================================
# 5. Accessing Set Elements
# =====================================================

print("\n===== Accessing Elements =====")

languages = {"Python", "Java", "C++"}

# Sets are unordered.
# We cannot access elements using indexing.

print(languages)

# =====================================================
# 6. Membership Operators
# =====================================================

print("\n===== Membership Operators =====")

print("Python" in languages)

print("Go" in languages)

print("Rust" not in languages)

# =====================================================
# 7. Adding Elements
# =====================================================

print("\n===== Adding Elements =====")

languages.add("SQL")

print(languages)

# =====================================================
# 8. Removing Elements
# =====================================================

print("\n===== Removing Elements =====")

languages.remove("Java")

print(languages)

# discard() does not raise an error
# if the element is not present.

languages.discard("Swift")

print(languages)

# =====================================================
# 9. Finding Length
# =====================================================

print("\n===== len() =====")

print("Total Elements:", len(languages))

# =====================================================
# 10. Real-World Example - Registered Users
# =====================================================

print("\n===== Registered Users =====")

users = {
    "Rahul",
    "Neha",
    "Aman",
    "Rahul"
}

print(users)

# Duplicate names are removed automatically.

# =====================================================
# 11. Real-World Example - Programming Skills
# =====================================================

print("\n===== Programming Skills =====")

skills = {
    "Python",
    "SQL",
    "Git"
}

skills.add("Machine Learning")

print(skills)

# =====================================================
# 12. Real-World Example - Available Courses
# =====================================================

print("\n===== Available Courses =====")

courses = {
    "Python",
    "Data Science",
    "Cloud Computing"
}

if "Python" in courses:
    print("Course Available")
else:
    print("Course Not Available")

# =====================================================
# 13. Real-World Example - Visited Cities
# =====================================================

print("\n===== Visited Cities =====")

cities = {
    "Jaipur",
    "Delhi",
    "Mumbai"
}

print("Visited Cities:")

for city in cities:
    print("-", city)

# =====================================================
# 14. Best Practices
# =====================================================

# ✔ Use sets when duplicate values are not allowed.
# ✔ Do not rely on the order of elements.
# ✔ Use add() to insert new elements.
# ✔ Use discard() when the element may not exist.
# ✔ Use meaningful variable names.

# =====================================================
# 15. Mini Practice
# =====================================================

# Try these on your own:
#
# 1. Create a set of your favourite fruits.
# 2. Add a new fruit to the set.
# 3. Remove an existing fruit.
# 4. Check whether "Python" exists in a set.
# 5. Create a set with duplicate values and observe the output.
# 6. Find the total number of elements.
# 7. Create an empty set.

# =====================================================
# End of Program
# =====================================================

print("\nCongratulations! You completed Sets in Python. 🎉")