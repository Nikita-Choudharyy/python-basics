"""
=====================================================
Topic: Regular Expressions (Regex) in Python
File : 04_Regular_Expressions.py

Description:
This file demonstrates:
1. Introduction to Regular Expressions
2. search() Function
3. match() Function
4. findall() Function
5. sub() Function
6. split() Function
7. compile() Function
8. Real-World Examples
9. Best Practices

Author : Nikita Choudhary
Repository : Python Basics
=====================================================
"""

import re

# =====================================================
# 1. What are Regular Expressions?
# =====================================================

# Regular Expressions (Regex) are patterns used
# to search, match, extract, and replace text.

print("===== Regular Expressions =====")

# =====================================================
# 2. re.search()
# =====================================================

print("\n===== re.search() =====")

text = "Learning Python is fun."

result = re.search("Python", text)

if result:
    print("Match Found:", result.group())

# =====================================================
# 3. re.match()
# =====================================================

print("\n===== re.match() =====")

text = "Python Programming"

result = re.match("Python", text)

if result:
    print("Starts With:", result.group())

# =====================================================
# 4. re.findall()
# =====================================================

print("\n===== re.findall() =====")

sentence = "AI ML AI Data AI"

matches = re.findall("AI", sentence)

print(matches)

# =====================================================
# 5. re.sub()
# =====================================================

print("\n===== re.sub() =====")

message = "I enjoy Java."

updated = re.sub("Java", "Python", message)

print(updated)

# =====================================================
# 6. re.split()
# =====================================================

print("\n===== re.split() =====")

skills = "Python,SQL,Git,Docker"

print(re.split(",", skills))

# =====================================================
# 7. re.compile()
# =====================================================

print("\n===== re.compile() =====")

pattern = re.compile(r"\d+")

text = "Order ID: 4589"

match = pattern.search(text)

print(match.group())

# =====================================================
# 8. Common Regex Patterns
# =====================================================

print("\n===== Common Patterns =====")

sample = "User123 Email45"

print(re.findall(r"\d+", sample))      # Digits
print(re.findall(r"[A-Za-z]+", sample)) # Words

# =====================================================
# 9. Real-World Example - Email Validation
# =====================================================

print("\n===== Email Validation =====")

email = "nikita123@gmail.com"

pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"

if re.match(pattern, email):
    print("Valid Email")
else:
    print("Invalid Email")

# =====================================================
# 10. Real-World Example - Mobile Number
# =====================================================

print("\n===== Mobile Number =====")

mobile = "9876543210"

if re.fullmatch(r"\d{10}", mobile):
    print("Valid Mobile Number")
else:
    print("Invalid Mobile Number")

# =====================================================
# 11. Real-World Example - Password Check
# =====================================================

print("\n===== Password Check =====")

password = "Python@123"

if len(password) >= 8:
    print("Password Length is Valid")
else:
    print("Password Too Short")

# =====================================================
# 12. Real-World Example - Extract Numbers
# =====================================================

print("\n===== Extract Numbers =====")

invoice = "Item1 ₹2500 Item2 ₹1800"

numbers = re.findall(r"\d+", invoice)

print(numbers)

# =====================================================
# 13. Best Practices
# =====================================================

# ✔ Use raw strings (r"...") for regex patterns.
# ✔ Keep regex patterns simple and readable.
# ✔ Compile frequently used patterns.
# ✔ Test regex patterns carefully.
# ✔ Add comments for complex expressions.

# =====================================================
# 14. Mini Practice
# =====================================================

# Try these on your own:
#
# 1. Extract all numbers from a sentence.
# 2. Replace all spaces with underscores.
# 3. Split a sentence into words using regex.
# 4. Validate a PIN containing exactly 6 digits.
# 5. Extract all email addresses from a paragraph.
# 6. Find all uppercase words.
# 7. Count how many times "Python" appears in a string.

# =====================================================
# End of Program
# =====================================================

print("\nCongratulations! You completed Regular Expressions in Python. 🎉")