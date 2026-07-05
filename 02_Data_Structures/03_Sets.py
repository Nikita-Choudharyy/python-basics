"""
=========================================================
Python Sets
=========================================================

Repository : python-basics
File       : 03_Sets.py
Author     : Nikita Choudhary

Description:
------------
This file demonstrates Python sets, including creating
sets, adding and removing elements, set operations,
common methods, and practical examples.

This repository documents my Python learning journey.
The examples are written for revision and to help other
beginners understand Python concepts.

Learning Objectives:
--------------------
✔ Create sets
✔ Add and remove elements
✔ Perform set operations
✔ Learn useful set methods
✔ Solve practical problems using sets

=========================================================
"""

# =========================================================
# 1. CREATING SETS
# =========================================================

# A set is an unordered collection of unique elements.

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print("\nCreating Sets")
print("-" * 30)

print("Set 1 :", set1)
print("Set 2 :", set2)


# =========================================================
# 2. ADDING ELEMENTS
# =========================================================

set1.add(10)
set1.update([11, 12])

print("\nAdding Elements")
print("-" * 30)

print(set1)

# Expected Output:
#
# Elements are added successfully.
# (The order may vary because sets are unordered.)


# =========================================================
# 3. REMOVING ELEMENTS
# =========================================================

set1.remove(2)
set1.discard(100)

print("\nRemoving Elements")
print("-" * 30)

print(set1)

# pop() removes an arbitrary element because
# sets do not maintain order.

removed_element = set1.pop()

print("Removed Element :", removed_element)
print("Updated Set     :", set1)

# Expected Output:
#
# The removed element may be different each time
# because sets are unordered.


# =========================================================
# 4. SET OPERATIONS (METHODS)
# =========================================================

print("\nSet Operations (Methods)")
print("-" * 30)

print("Union                 :", set1.union(set2))
print("Intersection          :", set1.intersection(set2))
print("Difference            :", set1.difference(set2))
print("Symmetric Difference  :", set1.symmetric_difference(set2))


# =========================================================
# 5. SET OPERATIONS (OPERATORS)
# =========================================================

print("\nSet Operations (Operators)")
print("-" * 30)

print("Union (|)         :", set1 | set2)
print("Intersection (&)  :", set1 & set2)
print("Difference (-)    :", set1 - set2)


# =========================================================
# 6. SUBSET AND SUPERSET
# =========================================================

print("\nSubset and Superset")
print("-" * 30)

print("Subset   :", set1.issubset(set2))
print("Superset :", set1.issuperset(set2))


# =========================================================
# 7. COPY AND CLEAR
# =========================================================

set_copy = set1.copy()

print("\nCopy Set")
print("-" * 30)

print(set_copy)

set_copy.clear()

print("After clear():", set_copy)

# Expected Output:
#
# set()
#


# =========================================================
# 8. PRACTICAL EXAMPLES
# =========================================================

# Remove duplicate elements

numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = set(numbers)

print("\nRemove Duplicates")
print("-" * 30)

print(unique_numbers)

# Find common elements

list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

common = set(list1) & set(list2)

print("\nCommon Elements")
print("-" * 30)

print(common)

# Find difference

difference = set(list1) - set(list2)

print("\nDifference")
print("-" * 30)

print(difference)


# =========================================================
# BEST PRACTICES
# =========================================================

# ✔ Use sets when duplicate values are not required.
# ✔ Use sets for fast membership testing.
# ✔ Remember that sets are unordered.
# ✔ Avoid relying on the order of elements.


# =========================================================
# COMMON BEGINNER MISTAKES
# =========================================================

# ❌ Wrong

# my_set[0]

# Sets do not support indexing.

# ❌ Wrong

# set1.pop()

# Never expect pop() to remove a specific element.

# ✅ Correct

# Use remove() when you know the element.
# Use discard() if the element may not exist.


# =========================================================
# PRACTICE QUESTIONS
# =========================================================

# Q1. Create two sets and print their union.
#
# Q2. Find the intersection of two sets.
#
# Q3. Remove duplicate values from a list.
#
# Q4. Find elements present in one set but not another.
#
# Q5. Check whether one set is a subset of another.
#
# Q6. Copy a set and clear it.
#
# Q7. Experiment with pop() and observe the output.


# =========================================================
# KEY TAKEAWAYS
# =========================================================

"""
Today You Learned:

✔ Creating Sets
✔ Adding Elements
✔ Removing Elements
✔ Union
✔ Intersection
✔ Difference
✔ Symmetric Difference
✔ Subset and Superset
✔ Copying and Clearing Sets

Happy Coding! 🚀
"""

# =========================================================
# End of File
# =========================================================
