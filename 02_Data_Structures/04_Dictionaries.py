"""
=========================================================
Python Dictionaries
=========================================================

Repository : python-basics
File       : 04_Dictionaries.py
Author     : Nikita Choudhary

Description:
------------
This file demonstrates Python dictionaries, including
creating dictionaries, accessing values, adding and
updating data, dictionary methods, and practical examples.

This repository documents my Python learning journey.
The examples are written for revision and to help other
beginners understand Python concepts.

Learning Objectives:
--------------------
✔ Create dictionaries
✔ Access values
✔ Add and update key-value pairs
✔ Remove dictionary items
✔ Use common dictionary methods
✔ Loop through dictionaries

=========================================================
"""

# =========================================================
# 1. CREATING A DICTIONARY
# =========================================================

# A dictionary stores data as key-value pairs.

student = {
    "name": "Amit",
    "age": 20,
    "course": "BCA"
}

print("\nCreating Dictionary")
print("-" * 30)

print(student)

# Expected Output:
#
# {'name': 'Amit', 'age': 20, 'course': 'BCA'}


# =========================================================
# 2. ACCESSING VALUES
# =========================================================

print("\nAccessing Values")
print("-" * 30)

print("Name :", student["name"])
print("Age  :", student.get("age"))

# get() returns None if the key does not exist,
# instead of raising an error.

print("City :", student.get("city"))

# Expected Output:
#
# Name : Amit
# Age  : 20
# City : None


# =========================================================
# 3. ADDING AND UPDATING VALUES
# =========================================================

student["city"] = "Delhi"
student["age"] = 21

print("\nAdding and Updating")
print("-" * 30)

print(student)

# Expected Output:
#
# {'name': 'Amit', 'age': 21, 'course': 'BCA', 'city': 'Delhi'}


# =========================================================
# 4. REMOVING ITEMS
# =========================================================

student.pop("course")

print("\nAfter pop()")
print("-" * 30)

print(student)

removed_item = student.popitem()

print("\nAfter popitem()")
print("-" * 30)

print("Removed Item :", removed_item)
print(student)

# Note:
# In Python 3.7+, popitem() removes the last inserted item.


# =========================================================
# 5. DICTIONARY METHODS
# =========================================================

print("\nDictionary Methods")
print("-" * 30)

print("Keys   :", student.keys())
print("Values :", student.values())
print("Items  :", student.items())


# =========================================================
# 6. UPDATE METHOD
# =========================================================

extra_info = {
    "college": "ABC College",
    "year": 3
}

student.update(extra_info)

print("\nUpdate Method")
print("-" * 30)

print(student)


# =========================================================
# 7. COPY AND CLEAR
# =========================================================

student_copy = student.copy()

print("\nCopy Dictionary")
print("-" * 30)

print(student_copy)

student_copy.clear()

print("After clear():", student_copy)

# Expected Output:
#
# {}


# =========================================================
# 8. LOOP THROUGH A DICTIONARY
# =========================================================

print("\nLoop Through Dictionary")
print("-" * 30)

for key, value in student.items():
    print(key, ":", value)


# =========================================================
# 9. PRACTICAL EXAMPLES
# =========================================================

product = {
    "id": 101,
    "name": "Laptop",
    "price": 55000
}

print("\nProduct Dictionary")
print("-" * 30)

print(product)

product["price"] += 5000

print("Updated Price :", product["price"])

print("Is 'price' key present? :", "price" in product)

# Expected Output:
#
# Updated Price : 60000
# True


# =========================================================
# BEST PRACTICES
# =========================================================

# ✔ Use meaningful keys.
# ✔ Use get() when a key may not exist.
# ✔ Keep key names consistent.
# ✔ Store related information together.
# ✔ Use update() to merge dictionaries.


# =========================================================
# COMMON BEGINNER MISTAKES
# =========================================================

# ❌ Wrong

# student["city"]

# Raises KeyError if the key does not exist.

# ✅ Correct

# student.get("city")

# Another common mistake:

# Thinking dictionaries preserve insertion order
# in all Python versions.

# Python 3.7+ preserves insertion order.


# =========================================================
# PRACTICE QUESTIONS
# =========================================================

# Q1. Create a dictionary to store employee details.
#
# Q2. Add a new key-value pair.
#
# Q3. Update an existing value.
#
# Q4. Remove a key using pop().
#
# Q5. Print all keys, values, and items.
#
# Q6. Loop through the dictionary.
#
# Q7. Check whether a key exists.
#
# Q8. Copy and clear a dictionary.


# =========================================================
# KEY TAKEAWAYS
# =========================================================

"""
Today You Learned:

✔ Creating Dictionaries
✔ Accessing Values
✔ Adding and Updating Items
✔ Removing Items
✔ Dictionary Methods
✔ update()
✔ Looping Through Dictionaries

Happy Coding! 🚀
"""

# =========================================================
# End of File
# =========================================================
