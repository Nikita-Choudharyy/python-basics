"""
=========================================================
Python Lists
=========================================================

Repository : python-basics
File       : 01_Lists.py
Author     : Nikita Choudhary

Description:
------------
This file demonstrates Python lists, including list
creation, indexing, slicing, updating elements, list
methods, and common operations.

This repository documents my Python learning journey.
The examples are written for revision and to help other
beginners understand Python concepts.

Learning Objectives:
--------------------
✔ Create lists
✔ Access list elements
✔ Use indexing and slicing
✔ Modify lists
✔ Add and remove elements
✔ Sort and reverse lists
✔ Use common list methods

=========================================================
"""

# =========================================================
# 1. CREATING LISTS
# =========================================================

# A list is an ordered and mutable collection.

numbers = [10, 20, 30, 40]
mixed_list = [1, "Python", 3.5, True]

print("\nCreating Lists")
print("-" * 30)

print("Numbers   :", numbers)
print("Mixed List:", mixed_list)

# Expected Output:
#
# Numbers   : [10, 20, 30, 40]
# Mixed List: [1, 'Python', 3.5, True]


# =========================================================
# 2. INDEXING
# =========================================================

print("\nList Indexing")
print("-" * 30)

print("First Element :", numbers[0])
print("Last Element  :", numbers[-1])

# Expected Output:
#
# First Element : 10
# Last Element  : 40


# =========================================================
# 3. SLICING
# =========================================================

print("\nList Slicing")
print("-" * 30)

print("numbers[1:3] :", numbers[1:3])
print("numbers[:2]  :", numbers[:2])
print("numbers[2:]  :", numbers[2:])

# Expected Output:
#
# [20, 30]
# [10, 20]
# [30, 40]


# =========================================================
# 4. MODIFYING LIST ELEMENTS
# =========================================================

numbers[1] = 25

print("\nModifying Elements")
print("-" * 30)

print(numbers)

# Expected Output:
#
# [10, 25, 30, 40]


# =========================================================
# 5. LOOPING THROUGH A LIST
# =========================================================

print("\nLoop Through a List")
print("-" * 30)

for num in numbers:
    print(num)

# Expected Output:
#
# 10
# 25
# 30
# 40


# =========================================================
# 6. MEMBERSHIP TEST
# =========================================================

print("\nMembership Test")
print("-" * 30)

print("30 in numbers  :", 30 in numbers)
print("100 in numbers :", 100 in numbers)

# Expected Output:
#
# True
# False


# =========================================================
# 7. LIST LENGTH
# =========================================================

print("\nList Length")
print("-" * 30)

print("Length :", len(numbers))

# Expected Output:
#
# Length : 4


# =========================================================
# 8. ADDING ELEMENTS
# =========================================================

numbers.append(50)
numbers.insert(2, 22)
numbers.extend([60, 70])

print("\nAdding Elements")
print("-" * 30)

print(numbers)

# Expected Output:
#
# [10, 25, 22, 30, 40, 50, 60, 70]


# =========================================================
# 9. REMOVING ELEMENTS
# =========================================================

numbers.remove(25)
numbers.pop()
numbers.pop(0)

print("\nRemoving Elements")
print("-" * 30)

print(numbers)

# Expected Output:
#
# [22, 30, 40, 50, 60]


# =========================================================
# 10. SORTING AND REVERSING
# =========================================================

numbers.sort()

print("\nSorting")
print("-" * 30)

print(numbers)

numbers.reverse()

print("\nReversing")
print("-" * 30)

print(numbers)

# Expected Output:
#
# Sorted   : [22, 30, 40, 50, 60]
# Reversed : [60, 50, 40, 30, 22]


# =========================================================
# 11. COUNT AND INDEX
# =========================================================

print("\nCount and Index")
print("-" * 30)

print("Count of 30 :", numbers.count(30))
print("Index of 30 :", numbers.index(30))

# Expected Output:
#
# Count of 30 : 1
# Index of 30 : 3


# =========================================================
# 12. COPYING A LIST
# =========================================================

copy_numbers = numbers.copy()

print("\nCopy List")
print("-" * 30)

print(copy_numbers)

# Expected Output:
#
# [60, 50, 40, 30, 22]


# =========================================================
# 13. CLEARING A LIST
# =========================================================

numbers.clear()

print("\nClear List")
print("-" * 30)

print(numbers)

# Expected Output:
#
# []


# =========================================================
# BEST PRACTICES
# =========================================================

# ✔ Use meaningful list names.
# ✔ Use append() for single elements.
# ✔ Use extend() for multiple elements.
# ✔ Check if an element exists before removing it.
# ✔ Use copy() instead of assigning one list to another.


# =========================================================
# COMMON BEGINNER MISTAKES
# =========================================================

# ❌ Wrong

# list2 = list1

# Both variables refer to the same list.

# ✅ Correct

# list2 = list1.copy()


# Another common mistake:

# numbers[10]

# Raises IndexError because the index does not exist.


# =========================================================
# PRACTICE QUESTIONS
# =========================================================

# Q1. Create a list of five fruits.
#
# Q2. Print the first and last element.
#
# Q3. Add three new elements.
#
# Q4. Remove one element.
#
# Q5. Sort the list.
#
# Q6. Reverse the list.
#
# Q7. Count how many times an element appears.
#
# Q8. Copy the list and print both lists.


# =========================================================
# KEY TAKEAWAYS
# =========================================================

"""
Today You Learned:

✔ Creating Lists
✔ Indexing
✔ Slicing
✔ Updating Elements
✔ Adding Elements
✔ Removing Elements
✔ Sorting
✔ Reversing
✔ Copying Lists
✔ Clearing Lists

Happy Coding! 🚀
"""

# =========================================================
# End of File
# =========================================================
