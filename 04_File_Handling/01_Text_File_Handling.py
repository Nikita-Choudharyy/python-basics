"""
=========================================================
Python Text File Handling
=========================================================

Repository : python-basics
File       : 01_Text_File_Handling.py
Author     : Nikita Choudhary

Description:
------------
This file demonstrates text file handling in Python.
It covers both the traditional approach using
open() and close(), as well as the recommended
approach using the with statement.

This repository documents my Python learning journey.
The examples are written for revision and to help other
beginners understand Python concepts.

Learning Objectives:
--------------------
✔ Create text files
✔ Write data to files
✔ Read file contents
✔ Read files line by line
✔ Append data to files
✔ Understand open() and close()
✔ Learn the with statement

=========================================================
"""

# =========================================================
# 1. WRITING TO A FILE (Traditional Method)
# =========================================================

# open(filename, mode)
#
# "w" mode:
# - Creates a new file if it does not exist.
# - Overwrites the file if it already exists.

file = open("sample.txt", "w")

file.write("Hello, this is a sample text file.\n")
file.write("Learning Python File Handling.\n")

file.close()

print("\nWriting to File")
print("-" * 30)
print("Data written successfully.")

# Expected Output:
#
# Data written successfully.


# =========================================================
# 2. READING A FILE USING read()
# =========================================================

# "r" mode is used to read a file.

file = open("sample.txt", "r")

content = file.read()

file.close()

print("\nReading File using read()")
print("-" * 30)

print(content)

# Expected Output:
#
# Hello, this is a sample text file.
# Learning Python File Handling.


# =========================================================
# 3. READING A SINGLE LINE USING readline()
# =========================================================

file = open("sample.txt", "r")

first_line = file.readline()
second_line = file.readline()

file.close()

print("\nReading using readline()")
print("-" * 30)

print("First Line :", first_line.strip())
print("Second Line:", second_line.strip())

# Expected Output:
#
# First Line : Hello, this is a sample text file.
# Second Line: Learning Python File Handling.


# =========================================================
# 4. READING ALL LINES USING readlines()
# =========================================================

file = open("sample.txt", "r")

lines = file.readlines()

file.close()

print("\nReading using readlines()")
print("-" * 30)

print(lines)

# Expected Output:
#
# ['Hello, this is a sample text file.\n',
#  'Learning Python File Handling.\n']


# =========================================================
# 5. READING FILE LINE BY LINE
# =========================================================

file = open("sample.txt", "r")

print("\nReading Line by Line")
print("-" * 30)

for line in file:
    print(line.strip())

file.close()

# Expected Output:
#
# Hello, this is a sample text file.
# Learning Python File Handling.


# =========================================================
# 6. APPENDING DATA TO A FILE
# =========================================================

# "a" mode adds new content without removing
# existing data.

file = open("sample.txt", "a")

file.write("This line is appended.\n")

file.close()

print("\nAppending Data")
print("-" * 30)

print("Data appended successfully.")

# Expected Output:
#
# Data appended successfully.


# =========================================================
# 7. VERIFY APPENDED DATA
# =========================================================

file = open("sample.txt", "r")

print("\nUpdated File Content")
print("-" * 30)

print(file.read())

file.close()

# Expected Output:
#
# Hello, this is a sample text file.
# Learning Python File Handling.
# This line is appended.

# =========================================================
# 8. USING THE with STATEMENT (Recommended)
# =========================================================

# Instead of manually closing the file,
# Python provides the "with" statement.
#
# It automatically closes the file after use.

print("\nUsing with Statement")
print("-" * 30)

with open("sample.txt", "r") as file:
    print(file.read())

# Expected Output:
#
# Hello, this is a sample text file.
# Learning Python File Handling.
# This line is appended.


# =========================================================
# 9. PRACTICAL EXAMPLE - COUNT LINES
# =========================================================

with open("sample.txt", "r") as file:
    lines = file.readlines()

print("\nCount Lines")
print("-" * 30)

print("Number of Lines :", len(lines))

# Expected Output:
#
# Number of Lines : 3


# =========================================================
# 10. PRACTICAL EXAMPLE - COUNT WORDS
# =========================================================

with open("sample.txt", "r") as file:
    text = file.read()

words = text.split()

print("\nCount Words")
print("-" * 30)

print("Number of Words :", len(words))

# Expected Output:
#
# Number of Words : 13
#
# (The count depends on the file content.)


# =========================================================
# 11. PRACTICAL EXAMPLE - COUNT CHARACTERS
# =========================================================

with open("sample.txt", "r") as file:
    text = file.read()

print("\nCount Characters")
print("-" * 30)

print("Number of Characters :", len(text))

# Expected Output:
#
# The output depends on the file content.


# =========================================================
# BEST PRACTICES
# =========================================================

# ✔ Learn both methods:
#     1. open() + close()
#     2. with open()
#
# ✔ Prefer using "with open()" in real-world projects.
#
# ✔ Always specify the correct file mode:
#     "r" -> Read
#     "w" -> Write (Overwrites existing content)
#     "a" -> Append
#
# ✔ Use meaningful file names.
#
# ✔ Handle exceptions when working with files.
#
# ✔ Close files properly if you are not using
#     the with statement.


# =========================================================
# COMMON BEGINNER MISTAKES
# =========================================================

# ❌ Opening a file that does not exist.

# open("abc.txt", "r")

# Raises:
# FileNotFoundError


# ❌ Forgetting to close a file.

# file = open("sample.txt", "r")
# print(file.read())

# File remains open.


# ✅ Correct

# file.close()

# OR

# with open("sample.txt", "r") as file:
#     print(file.read())


# ❌ Accidentally using "w" mode.

# "w" deletes all previous content before writing.

# Use "a" mode if you want to keep existing data.


# =========================================================
# PRACTICE QUESTIONS
# =========================================================

# Q1. Create a text file and write your name.
#
# Q2. Read the complete file using read().
#
# Q3. Read the first line using readline().
#
# Q4. Read all lines using readlines().
#
# Q5. Append a new line to an existing file.
#
# Q6. Count the number of lines.
#
# Q7. Count the number of words.
#
# Q8. Count the number of characters.
#
# Q9. Rewrite the above programs using
#     the with statement.


# =========================================================
# KEY TAKEAWAYS
# =========================================================

"""
Today You Learned:

✔ open()
✔ close()
✔ read()
✔ readline()
✔ readlines()
✔ write()
✔ append()
✔ with open()
✔ Counting Lines
✔ Counting Words
✔ Counting Characters

Happy Coding! 🚀
"""

# =========================================================
# End of File
# =========================================================
