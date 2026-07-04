"""
=========================================================
Python Strings
=========================================================

Repository : python-basics
File       : 06_Strings.py
Author     : Nikita Choudhary

Description:
------------
This file demonstrates string creation, indexing, slicing,
concatenation, commonly used string methods, string
formatting, and practical examples.

This repository documents my Python learning journey.
The examples are written for revision and to help other
beginners understand Python concepts.

Learning Objectives:
--------------------
✔ Create strings
✔ Access characters using indexing
✔ Extract text using slicing
✔ Use common string methods
✔ Format strings
✔ Solve basic string problems

=========================================================
"""

# =========================================================
# 1. CREATING STRINGS
# =========================================================

# Strings are sequences of characters enclosed in
# single or double quotes.

name = "Python"
message = "Learning Strings"

print("\nCreating Strings")
print("-" * 30)

print(name)
print(message)

# Expected Output:
#
# Python
# Learning Strings


# =========================================================
# 2. STRING INDEXING AND SLICING
# =========================================================

# Indexing is used to access individual characters.
# Slicing extracts a portion of a string.

text = "Hello World"

print("\nString Indexing and Slicing")
print("-" * 30)

print("First Character :", text[0])
print("Last Character  :", text[-1])
print("Slice (0:5)     :", text[0:5])
print("Reverse String  :", text[::-1])

# Expected Output:
#
# First Character : H
# Last Character  : d
# Slice (0:5)     : Hello
# Reverse String  : dlroW olleH


# =========================================================
# 3. STRING CONCATENATION
# =========================================================

# Concatenation joins two or more strings.

first = "Hello"
second = "Python"

print("\nString Concatenation")
print("-" * 30)

print(first + " " + second)

# Expected Output:
#
# Hello Python


# =========================================================
# 4. STRING METHODS
# =========================================================

# Python provides many built-in string methods.

sample = "  python programming  "

print("\nCommon String Methods")
print("-" * 30)

print("Upper      :", sample.upper())
print("Lower      :", sample.lower())
print("Title      :", sample.title())
print("Strip      :", sample.strip())
print("Replace    :", sample.replace("python", "java"))
print("Find       :", sample.find("programming"))
print("Count 'p'  :", sample.count("p"))

# Expected Output:
#
# Upper      :   PYTHON PROGRAMMING
# Lower      :   python programming
# Title      :   Python Programming
# Strip      : python programming
# Replace    :   java programming
# Find       : 9
# Count 'p'  : 2


# =========================================================
# 5. STRING PROPERTY METHODS
# =========================================================

# These methods return True or False.

print("\nString Property Methods")
print("-" * 30)

print("Is Alpha        :", "Python".isalpha())
print("Is Digit        :", "123".isdigit())
print("Is Alphanumeric :", "Python3".isalnum())

# Expected Output:
#
# Is Alpha        : True
# Is Digit        : True
# Is Alphanumeric : True


# =========================================================
# 6. STRING FORMATTING
# =========================================================

# f-strings provide a clean way to format strings.

language = "Python"
version = 3

print("\nString Formatting")
print("-" * 30)

print(f"{language} version is {version}")

# Expected Output:
#
# Python version is 3


# =========================================================
# 7. PRACTICAL EXAMPLE - COUNT VOWELS
# =========================================================

word = "education"
vowels = "aeiou"
count = 0

for ch in word:
    if ch in vowels:
        count += 1

print("\nCount Vowels")
print("-" * 30)

print("Word        :", word)
print("Vowel Count :", count)

# Expected Output:
#
# Word        : education
# Vowel Count : 5


# =========================================================
# 8. PRACTICAL EXAMPLE - PALINDROME
# =========================================================

text = "madam"

print("\nPalindrome Check")
print("-" * 30)

if text == text[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

# Expected Output:
#
# Palindrome


# =========================================================
# BEST PRACTICES
# =========================================================

# ✔ Use meaningful variable names.
# ✔ Prefer f-strings for formatting.
# ✔ Use strip() to remove unwanted spaces.
# ✔ Use built-in string methods instead of manual logic
#   whenever possible.
# ✔ Keep string operations readable.


# =========================================================
# COMMON BEGINNER MISTAKES
# =========================================================

# ❌ Wrong

# text[20]

# Raises IndexError because the index does not exist.

# ✅ Correct

# Check the string length before accessing indexes.

# Another common mistake:

# "Python" + 3

# Raises TypeError.

# Correct:

# "Python " + str(3)


# =========================================================
# PRACTICE QUESTIONS
# =========================================================

# Q1. Print the first and last character of a string.
#
# Q2. Reverse a string using slicing.
#
# Q3. Convert a string to uppercase and lowercase.
#
# Q4. Replace one word with another in a sentence.
#
# Q5. Count the number of vowels in a string.
#
# Q6. Check whether a string is a palindrome.
#
# Q7. Print the length of a string using len().
#
# Q8. Take a string as input and print it using an f-string.


# =========================================================
# KEY TAKEAWAYS
# =========================================================

"""
Today You Learned:

✔ Creating Strings
✔ Indexing
✔ Slicing
✔ String Concatenation
✔ String Methods
✔ String Property Methods
✔ String Formatting
✔ Palindrome Check
✔ Vowel Counting

Happy Coding! 🚀
"""

# =========================================================
# End of File
# =========================================================
