"""
=====================================================
Topic: String Basics in Python
File : 01_String_Basics.py

Description:
This file demonstrates:
1. Introduction to Strings
2. Creating Strings
3. Accessing Characters
4. String Indexing
5. Negative Indexing
6. String Slicing
7. String Concatenation
8. String Repetition
9. Membership Operators
10. Real-World Examples
11. Best Practices

Author : Nikita Choudhary
Repository : Python Basics
=====================================================
"""

# =====================================================
# 1. What is a String?
# =====================================================

# A string is a sequence of characters enclosed
# within single quotes (' '), double quotes (" "),
# or triple quotes (''' ''' / """ """).

print("===== String Basics =====")

# =====================================================
# 2. Creating Strings
# =====================================================

print("\n===== Creating Strings =====")

language = "Python"
city = 'Jaipur'

message = """
Welcome to Python Programming!
"""

print(language)
print(city)
print(message)

# =====================================================
# 3. Accessing Characters
# =====================================================

print("\n===== Accessing Characters =====")

course = "Machine Learning"

print(course[0])
print(course[1])
print(course[5])

# =====================================================
# 4. Positive Indexing
# =====================================================

print("\n===== Positive Indexing =====")

text = "Developer"

print(text[0])
print(text[3])
print(text[8])

# =====================================================
# 5. Negative Indexing
# =====================================================

print("\n===== Negative Indexing =====")

print(text[-1])
print(text[-2])
print(text[-5])

# =====================================================
# 6. String Slicing
# =====================================================

print("\n===== String Slicing =====")

framework = "Data Science"

print(framework[0:4])
print(framework[5:])
print(framework[:4])
print(framework[::2])
print(framework[::-1])

# =====================================================
# 7. String Concatenation
# =====================================================

print("\n===== String Concatenation =====")

first_name = "Nikita"
last_name = "Choudhary"

full_name = first_name + " " + last_name

print(full_name)

# =====================================================
# 8. String Repetition
# =====================================================

print("\n===== String Repetition =====")

print("AI " * 3)

# =====================================================
# 9. Membership Operators
# =====================================================

print("\n===== Membership Operators =====")

sentence = "Python is easy to learn."

print("Python" in sentence)
print("Java" in sentence)

print("easy" not in sentence)
print("C++" not in sentence)

# =====================================================
# 10. String Immutability
# =====================================================

print("\n===== String Immutability =====")

language = "Python"

print(language)

# Strings are immutable.
# The following statement will raise an error.

# language[0] = "J"

language = "Jython"

print(language)

# =====================================================
# 11. Real-World Example - Email Address
# =====================================================

print("\n===== Email Example =====")

email = "nikita@gmail.com"

print("Email:", email)

print("Username:", email[:email.index("@")])

print("Domain:", email[email.index("@") + 1:])

# =====================================================
# 12. Real-World Example - Product Code
# =====================================================

print("\n===== Product Code =====")

product_code = "LAP-4589"

category = product_code[:3]

print("Category:", category)

print("Product Code:", product_code)

# =====================================================
# 13. Best Practices
# =====================================================

# ✔ Use meaningful variable names.
# ✔ Prefer double quotes for normal strings.
# ✔ Use triple quotes for multi-line strings.
# ✔ Use slicing instead of unnecessary loops.
# ✔ Remember that strings are immutable.

# =====================================================
# 14. Mini Practice
# =====================================================

# Try these on your own:
#
# 1. Create a string with your full name.
# 2. Print the first and last character.
# 3. Reverse a string using slicing.
# 4. Concatenate your city and country.
# 5. Check whether "Python" exists in a sentence.
# 6. Extract the username from an email.
# 7. Print every second character of a string.

# =====================================================
# End of Program
# =====================================================

print("\nCongratulations! You completed String Basics in Python. 🎉")