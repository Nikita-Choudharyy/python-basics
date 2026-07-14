"""
=====================================================
Topic: String Methods in Python
File : 02_String_Methods.py

Description:
This file demonstrates:
1. Case Conversion Methods
2. Whitespace Methods
3. Search Methods
4. Replace Method
5. Split and Join Methods
6. Checking Methods
7. Counting Methods
8. Real-World Examples
9. Best Practices

Author : Nikita Choudhary
Repository : Python Basics
=====================================================
"""

# =====================================================
# 1. Case Conversion Methods
# =====================================================

print("===== Case Conversion Methods =====")

text = "python programming"

print("Original     :", text)
print("Upper        :", text.upper())
print("Lower        :", text.lower())
print("Title        :", text.title())
print("Capitalize   :", text.capitalize())
print("Swapcase     :", text.swapcase())

# =====================================================
# 2. Whitespace Methods
# =====================================================

print("\n===== Whitespace Methods =====")

message = "   Welcome to Python   "

print("Original :", repr(message))
print("strip()  :", repr(message.strip()))
print("lstrip() :", repr(message.lstrip()))
print("rstrip() :", repr(message.rstrip()))

# =====================================================
# 3. Search Methods
# =====================================================

print("\n===== Search Methods =====")

sentence = "Python is simple and powerful."

print("find('simple')  :", sentence.find("simple"))
print("index('Python') :", sentence.index("Python"))
print("startswith()    :", sentence.startswith("Python"))
print("endswith()      :", sentence.endswith("powerful."))

# =====================================================
# 4. Replace Method
# =====================================================

print("\n===== replace() =====")

statement = "I love Java."

updated_statement = statement.replace("Java", "Python")

print("Original :", statement)
print("Updated  :", updated_statement)

# =====================================================
# 5. split() Method
# =====================================================

print("\n===== split() =====")

skills = "Python,SQL,Machine Learning,Git"

skill_list = skills.split(",")

print(skill_list)

# =====================================================
# 6. join() Method
# =====================================================

print("\n===== join() =====")

words = ["Learn", "Python", "Step", "by", "Step"]

sentence = " ".join(words)

print(sentence)

# =====================================================
# 7. Count Method
# =====================================================

print("\n===== count() =====")

paragraph = "Python Python SQL Python"

print("Python appears:", paragraph.count("Python"))

# =====================================================
# 8. Checking Methods
# =====================================================

print("\n===== Checking Methods =====")

username = "nikita123"

print("isalnum() :", username.isalnum())
print("isalpha() :", username.isalpha())
print("isdigit() :", username.isdigit())

value = "2026"

print("isdigit() :", value.isdigit())

language = "Python"

print("isupper() :", language.isupper())
print("islower() :", language.islower())

# =====================================================
# 9. Real-World Example - Username Validation
# =====================================================

print("\n===== Username Validation =====")

username = "Nikita_2026"

if username.replace("_", "").isalnum():
    print("Valid Username")
else:
    print("Invalid Username")

# =====================================================
# 10. Real-World Example - File Extension
# =====================================================

print("\n===== File Extension =====")

filename = "project_report.pdf"

extension = filename.split(".")[-1]

print("Extension:", extension)

# =====================================================
# 11. Real-World Example - Tags
# =====================================================

print("\n===== Blog Tags =====")

tags = ["python", "machine-learning", "ai", "github"]

hashtags = ", ".join(tags)

print(hashtags)

# =====================================================
# 12. Real-World Example - Product Search
# =====================================================

print("\n===== Product Search =====")

products = "Laptop,Mouse,Keyboard,Monitor"

if "Mouse" in products.split(","):
    print("Product Available")
else:
    print("Product Not Available")

# =====================================================
# 13. Best Practices
# =====================================================

# ✔ Use strip() before processing user input.
# ✔ Use split() when converting text into lists.
# ✔ Use join() instead of repeated string concatenation.
# ✔ Use startswith() and endswith() for validation.
# ✔ Choose find() when a missing value is acceptable.
# ✔ Use index() only when the value is guaranteed to exist.

# =====================================================
# 14. Mini Practice
# =====================================================

# Try these on your own:
#
# 1. Convert your name to uppercase.
# 2. Count how many times "Python" appears in a sentence.
# 3. Replace one programming language with another.
# 4. Split a sentence into words.
# 5. Join a list of cities into a single string.
# 6. Validate whether a string contains only digits.
# 7. Check whether a filename ends with ".csv".

# =====================================================
# End of Program
# =====================================================

print("\nCongratulations! You completed String Methods in Python. 🎉")