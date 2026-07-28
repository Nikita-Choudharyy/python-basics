"""
=====================================================
Topic: Reading and Writing Files in Python
File : 02_Reading_and_Writing_Files.py

Description:
This file demonstrates:
1. Reading an Entire File
2. Reading One Line
3. Reading All Lines
4. Reading File Line by Line
5. Writing to a File
6. Appending to a File
7. Writing Multiple Lines
8. File Cursor
9. tell() Method
10. seek() Method
11. Real-World Examples
12. Best Practices

Author : Nikita Choudhary
Repository : Python Basics
=====================================================
"""
# =====================================================
# Dataset Folder Path
# =====================================================

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATASET = BASE_DIR.parent / "Datasets"

# =====================================================
# 1. Reading an Entire File
# =====================================================

print("===== read() Method =====")

# Make sure Datasets/sample.txt exists.

with open(DATASET/"sample.txt", "r") as file:
    content = file.read()

print(content)

# =====================================================
# 2. Reading One Line
# =====================================================

print("\n===== readline() Method =====")

with open(DATASET/"sample.txt", "r") as file:
    first_line = file.readline()

print(first_line)

# =====================================================
# 3. Reading All Lines
# =====================================================

print("\n===== readlines() Method =====")

with open(DATASET/"sample.txt", "r") as file:
    lines = file.readlines()

print(lines)

# =====================================================
# 4. Reading Line by Line
# =====================================================

print("\n===== Reading File Line by Line =====")

with open(DATASET/"sample.txt", "r") as file:

    for line in file:
        print(line.strip())

# =====================================================
# 5. Writing to a File
# =====================================================

print("\n===== write() Method =====")

with open(DATASET/"output.txt", "w") as file:

    file.write("Welcome to Python.\n")
    file.write("Learning File Handling.\n")
    file.write("This file was created using write().")

print("Data written successfully.")

# =====================================================
# 6. Appending to a File
# =====================================================

print("\n===== Append Mode =====")

with open(DATASET/"output.txt", "a") as file:

    file.write("\nThis line was added using append mode.")

print("Data appended successfully.")

# =====================================================
# 7. Writing Multiple Lines
# =====================================================

print("\n===== writelines() Method =====")

students = [
    "Rahul\n",
    "Neha\n",
    "Aman\n",
    "Nikita\n"
]

with open(DATASET/"students.txt", "w") as file:

    file.writelines(students)

print("Student records saved successfully.")

# =====================================================
# 8. File Cursor
# =====================================================

print("\n===== File Cursor =====")

with open(DATASET/"sample.txt", "r") as file:

    print(file.read(7))

    print(file.read(10))

# =====================================================
# 9. tell() Method
# =====================================================

print("\n===== tell() Method =====")

with open(DATASET/"sample.txt", "r") as file:

    print(file.read(8))

    cursor_position = file.tell()

    print("Cursor Position:", cursor_position)

# =====================================================
# 10. seek() Method
# =====================================================

print("\n===== seek() Method =====")

with open(DATASET/"sample.txt", "r") as file:

    print(file.read(10))

    file.seek(0)

    print(file.read(10))

# =====================================================
# 11. Real-World Example - Daily Journal
# =====================================================

print("\n===== Daily Journal =====")

journal_entry = "Today I practiced Python File Handling."

with open(DATASET/"journal.txt", "a") as file:

    file.write(journal_entry + "\n")

print("Journal updated successfully.")

# =====================================================
# 12. Real-World Example - Attendance Record
# =====================================================

print("\n===== Attendance Record =====")

attendance = [
    "Nikita - Present\n",
    "Rahul - Present\n",
    "Neha - Absent\n",
    "Aman - Present\n"
]

with open(DATASET/"attendance.txt", "w") as file:

    file.writelines(attendance)

print("Attendance saved successfully.")

# =====================================================
# 13. Real-World Example - Reading Configuration File
# =====================================================

print("\n===== Configuration File =====")

with open(DATASET/"config.txt", "r") as file:

    config = file.read()

print(config)

# =====================================================
# 14. Real-World Example - Application Log
# =====================================================

print("\n===== Application Log =====")

with open(DATASET/"application.log", "a") as file:

    file.write("Application Started Successfully.\n")

print("Log updated successfully.")

# =====================================================
# 15. Best Practices
# =====================================================

# ✔ Always use 'with open()' to handle files.
# ✔ Store practice files inside the datasets folder.
# ✔ Use read() for complete file content.
# ✔ Use readline() to read one line.
# ✔ Use readlines() when a list of lines is required.
# ✔ Use write() to overwrite file content.
# ✔ Use append mode ('a') to preserve existing data.
# ✔ Use seek() and tell() to control the file cursor.

# =====================================================
# 16. Mini Practice
# =====================================================

# Try these on your own:
#
# 1. Read the complete contents of sample.txt.
# 2. Read only the first line from sample.txt.
# 3. Read all lines into a list.
# 4. Create a file named notes.txt and write your name.
# 5. Append today's date to notes.txt.
# 6. Store five city names in cities.txt using writelines().
# 7. Print the cursor position after reading 15 characters.
# 8. Move the cursor back to the beginning using seek().
# 9. Create a journal.txt file and add three entries.
# 10. Create a log file and append execution details.

# =====================================================
# End of Program
# =====================================================

print("\nCongratulations! You completed Reading and Writing Files in Python. 🎉")
