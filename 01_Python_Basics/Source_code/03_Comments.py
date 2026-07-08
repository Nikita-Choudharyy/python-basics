"""
=====================================================
Topic: Comments in Python
File : 03_Comments.py

Description:
This file demonstrates:
1. Single-line comments
2. Multi-line comments
3. Docstrings
4. Writing meaningful comments
5. Best practices for using comments

Author : Nikita Choudhary
Repository : Python Basics
=====================================================
"""

# =====================================================
# 1. Single-Line Comments
# =====================================================

# This is a single-line comment.
print("Hello, World!")

# =====================================================
# 2. Comment After Code
# =====================================================

print("Welcome to Python!")  # Prints a welcome message

# =====================================================
# 3. Multiple Single-Line Comments
# =====================================================

# Student Details
# Name : Nikita
# Course : Python Basics
# Topic : Comments

print("Learning Python Comments")

# =====================================================
# 4. Multi-Line Comments
# =====================================================

"""
Python does not have a dedicated multi-line comment syntax.

Instead, developers commonly use triple quotes (docstrings)
to write explanations or documentation spanning multiple lines.
"""

print("Multi-line documentation example")

# =====================================================
# 5. Docstrings
# =====================================================

def greet():
    """
    This function prints
    a welcome message.
    """
    print("Welcome to Python Programming!")

greet()

# Display the function documentation
print("\nFunction Documentation:")
print(greet.__doc__)

# =====================================================
# 6. Writing Meaningful Comments
# =====================================================

# Radius of the circle
radius = 7

# Calculate the area of the circle
area = 3.14 * radius ** 2

# Display the result
print("\nArea of Circle:", area)

# =====================================================
# 7. Best Practices
# =====================================================

# ✔ Write comments that explain WHY, not WHAT.
# ✔ Keep comments short and meaningful.
# ✔ Update comments whenever code changes.
# ✔ Avoid unnecessary comments for obvious code.

# Bad Example
# x = 10  # Store 10 in x

# Good Example
# Maximum number of login attempts allowed
max_login_attempts = 5

print("\nMaximum Login Attempts:", max_login_attempts)

# =====================================================
# 8. Mini Practice
# =====================================================

# Try these on your own:
#
# 1. Write a single-line comment.
# 2. Write a multi-line comment using triple quotes.
# 3. Create a function with a docstring.
# 4. Print the docstring using __doc__.
# 5. Add meaningful comments to a simple program.

# =====================================================
# End of Program
# =====================================================

print("\nCongratulations! You completed Comments in Python. 🎉")