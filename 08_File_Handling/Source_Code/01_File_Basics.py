"""
=====================================================
Topic: File Basics in Python
File : 01_File_Basics.py

Description:
This file demonstrates:
1. Introduction to Files
2. Types of Files
3. File Paths
4. Opening Files
5. File Modes
6. Closing Files
7. with Statement
8. Real-World Examples
9. Best Practices

Author : Nikita Choudhary
Repository : Python Basics
=====================================================
"""

# =====================================================
# 1. What is a File?
# =====================================================

# A file is a collection of data stored on a storage
# device such as a hard disk or SSD.
#
# Files help us store data permanently so that it
# can be accessed even after the program ends.

print("===== File Basics =====")

# =====================================================
# 2. Types of Files
# =====================================================

print("\n===== Types of Files =====")

# Text Files
# Examples:
# .txt
# .csv
# .json
# .py

# Binary Files
# Examples:
# .jpg
# .png
# .mp3
# .pdf
# .exe

print("Text File Example  : notes.txt")
print("Binary File Example: image.jpg")

# =====================================================
# 3. File Paths
# =====================================================

print("\n===== File Paths =====")

# Relative Path
relative_path = "sample.txt"

# Absolute Path
absolute_path = r"C:\Users\Nikita\Documents\sample.txt"

print("Relative Path :", relative_path)
print("Absolute Path :", absolute_path)

# =====================================================
# 4. Opening a File
# =====================================================

print("\n===== Opening a File =====")

# Syntax:
#
# file = open("filename", "mode")

print('Example: open("sample.txt", "r")')

# =====================================================
# 5. File Modes
# =====================================================

print("\n===== File Modes =====")

print("r  -> Read")
print("w  -> Write")
print("a  -> Append")
print("x  -> Create")
print("t  -> Text Mode")
print("b  -> Binary Mode")
print("r+ -> Read & Write")
print("w+ -> Write & Read")
print("a+ -> Append & Read")

# =====================================================
# 6. Closing a File
# =====================================================

print("\n===== Closing a File =====")

# file = open("sample.txt", "r")
#
# file.close()

print("Always close files after use.")

# =====================================================
# 7. Using with Statement
# =====================================================

print("\n===== with Statement =====")

# Recommended approach

"""
with open("sample.txt", "r") as file:
    data = file.read()

print(data)
"""

print("The file is automatically closed.")

# =====================================================
# 8. Real-World Example - Reading Notes
# =====================================================

print("\n===== Reading Notes =====")

print("""
with open("notes.txt", "r") as file:
    notes = file.read()

print(notes)
""")

# =====================================================
# 9. Real-World Example - Writing Logs
# =====================================================

print("\n===== Writing Logs =====")

print("""
with open("log.txt", "w") as file:
    file.write("Application Started")
""")

# =====================================================
# 10. Real-World Example - Saving Student Data
# =====================================================

print("\n===== Saving Student Data =====")

print("""
with open("students.txt", "w") as file:
    file.write("Nikita\\n")
    file.write("Rahul\\n")
    file.write("Neha\\n")
""")

# =====================================================
# 11. Why Use with?
# =====================================================

print("\n===== Why Use with? =====")

# Advantages:
#
# ✔ Automatically closes the file.
# ✔ Cleaner code.
# ✔ Prevents resource leaks.
# ✔ Recommended by Python.

# =====================================================
# 12. Best Practices
# =====================================================

# ✔ Prefer using with open().
# ✔ Close files if not using with.
# ✔ Use meaningful file names.
# ✔ Choose the correct file mode.
# ✔ Store related files in dedicated folders.

# =====================================================
# 13. Mini Practice
# =====================================================

# Try these on your own:
#
# 1. Open a text file in read mode.
# 2. Open a file in write mode.
# 3. Create a new file using x mode.
# 4. Identify the difference between relative
#    and absolute paths.
# 5. List three text files and three binary files.
# 6. Explain why with is preferred over open().
# 7. Write the syntax of open().

# =====================================================
# End of Program
# =====================================================

print("\nCongratulations! You completed File Basics in Python. 🎉")