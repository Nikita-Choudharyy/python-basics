"""
=========================================================
Python CSV File Handling
=========================================================

Repository : python-basics
File       : 02_CSV_File_Handling.py
Author     : Nikita Choudhary

Description:
------------
This file demonstrates CSV (Comma-Separated Values)
file handling in Python using the built-in csv module.

It covers writing, reading, DictReader, DictWriter,
and common CSV operations.

This repository documents my Python learning journey.
The examples are written for revision and to help other
beginners understand Python concepts.

Learning Objectives:
--------------------
✔ Create CSV files
✔ Write data to CSV files
✔ Read CSV files
✔ Use csv.reader()
✔ Use csv.writer()
✔ Use csv.DictReader()
✔ Use csv.DictWriter()

=========================================================
"""

import csv

# =========================================================
# 1. WRITING TO A CSV FILE
# =========================================================

# csv.writer() writes data row by row.

students = [
    ["Name", "Age", "Marks"],
    ["Amit", 20, 85],
    ["Neha", 22, 90],
    ["Rahul", 21, 78]
]

with open("students.csv", "w", newline="") as file:

    writer = csv.writer(file)

    writer.writerows(students)

print("\nWriting CSV File")
print("-" * 30)

print("Data written successfully.")

# Expected Output:
#
# Data written successfully.


# =========================================================
# 2. READING A CSV FILE
# =========================================================

print("\nReading CSV File")
print("-" * 30)

with open("students.csv", "r") as file:

    reader = csv.reader(file)

    for row in reader:
        print(row)

# Expected Output:
#
# ['Name', 'Age', 'Marks']
# ['Amit', '20', '85']
# ['Neha', '22', '90']
# ['Rahul', '21', '78']


# =========================================================
# 3. DISPLAYING CSV DATA
# =========================================================

print("\nFormatted Output")
print("-" * 30)

with open("students.csv", "r") as file:

    reader = csv.reader(file)

    next(reader)        # Skip Header

    for row in reader:

        print(
            f"Name: {row[0]}, "
            f"Age: {row[1]}, "
            f"Marks: {row[2]}"
        )

# Expected Output:
#
# Name: Amit, Age: 20, Marks: 85
# Name: Neha, Age: 22, Marks: 90
# Name: Rahul, Age: 21, Marks: 78


# =========================================================
# 4. WRITING CSV USING DictWriter
# =========================================================

print("\nWriting using DictWriter")
print("-" * 30)

with open("employees.csv", "w", newline="") as file:

    fieldnames = [
        "Name",
        "Department",
        "Salary"
    ]

    writer = csv.DictWriter(
        file,
        fieldnames=fieldnames
    )

    writer.writeheader()

    writer.writerow(
        {
            "Name": "Nikita",
            "Department": "AI",
            "Salary": 50000
        }
    )

    writer.writerow(
        {
            "Name": "Amit",
            "Department": "ML",
            "Salary": 45000
        }
    )

print("employees.csv created successfully.")

# Expected Output:
#
# employees.csv created successfully.


# =========================================================
# 5. READING CSV USING DictReader
# =========================================================

print("\nReading using DictReader")
print("-" * 30)

with open("employees.csv", "r") as file:

    reader = csv.DictReader(file)

    for row in reader:

        print(row)

# Expected Output:
#
# {'Name': 'Nikita', 'Department': 'AI', 'Salary': '50000'}
# {'Name': 'Amit', 'Department': 'ML', 'Salary': '45000'}

# =========================================================
# 6. COUNT NUMBER OF RECORDS
# =========================================================

print("\nCount Records")
print("-" * 30)

count = 0

with open("students.csv", "r") as file:

    reader = csv.reader(file)

    next(reader)      # Skip Header

    for _ in reader:
        count += 1

print("Number of Student Records :", count)

# Expected Output:
#
# Number of Student Records : 3


# =========================================================
# 7. COUNT NUMBER OF COLUMNS
# =========================================================

print("\nCount Columns")
print("-" * 30)

with open("students.csv", "r") as file:

    reader = csv.reader(file)

    header = next(reader)

print("Number of Columns :", len(header))
print("Column Names      :", header)

# Expected Output:
#
# Number of Columns : 3
# Column Names      : ['Name', 'Age', 'Marks']


# =========================================================
# 8. READ A SPECIFIC COLUMN
# =========================================================

print("\nRead Specific Column")
print("-" * 30)

with open("students.csv", "r") as file:

    reader = csv.DictReader(file)

    print("Student Names:")

    for row in reader:
        print(row["Name"])

# Expected Output:
#
# Student Names:
# Amit
# Neha
# Rahul


# =========================================================
# 9. PRACTICAL EXAMPLES
# =========================================================

# Example 1 : Find students scoring 80 or more

print("\nStudents Scoring 80 or More")
print("-" * 30)

with open("students.csv", "r") as file:

    reader = csv.DictReader(file)

    for row in reader:

        if int(row["Marks"]) >= 80:

            print(
                f"{row['Name']} -> {row['Marks']}"
            )

# Expected Output:
#
# Amit -> 85
# Neha -> 90


# Example 2 : Calculate Total Marks

print("\nCalculate Total Marks")
print("-" * 30)

total_marks = 0

with open("students.csv", "r") as file:

    reader = csv.DictReader(file)

    for row in reader:

        total_marks += int(row["Marks"])

print("Total Marks :", total_marks)

# Expected Output:
#
# Total Marks : 253


# Example 3 : Calculate Average Marks

average_marks = total_marks / count

print("Average Marks :", average_marks)

# Expected Output:
#
# Average Marks : 84.33333333333333


# =========================================================
# BEST PRACTICES
# =========================================================

# ✔ Always use newline="" while writing CSV files.
#
# ✔ Prefer using DictReader() when working
#   with column names.
#
# ✔ Use DictWriter() for better readability.
#
# ✔ Convert numeric values using int() or float()
#   before performing calculations.
#
# ✔ Always use the with statement while
#   working with files.


# =========================================================
# COMMON BEGINNER MISTAKES
# =========================================================

# ❌ Forgetting newline=""
#
# open("students.csv", "w")
#
# This may create blank lines on some systems.
#
# ✅ Correct
#
# open("students.csv", "w", newline="")


# ❌ Forgetting to skip the header
#
# next(reader)
#
# Without this, the header may be processed
# as normal data.


# ❌ Performing calculations directly
#
# row["Marks"] + 10
#
# row["Marks"] is a string.
#
# ✅ Correct
#
# int(row["Marks"]) + 10


# =========================================================
# PRACTICE QUESTIONS
# =========================================================

# Q1. Create a CSV file containing employee details.
#
# Q2. Read all records from a CSV file.
#
# Q3. Read only one specific column.
#
# Q4. Count the total number of records.
#
# Q5. Count the total number of columns.
#
# Q6. Find students scoring above 75.
#
# Q7. Calculate the average marks.
#
# Q8. Write data using DictWriter().
#
# Q9. Read data using DictReader().


# =========================================================
# WHY LEARN CSV FILE HANDLING?
# =========================================================

"""
CSV files are one of the most commonly used formats
for storing datasets.

As you move into Machine Learning and AI, you'll
frequently work with CSV datasets before loading them
into libraries such as Pandas, NumPy, or Scikit-learn.

Understanding how CSV files work helps build a strong
foundation for data preprocessing and analysis.
"""


# =========================================================
# KEY TAKEAWAYS
# =========================================================

"""
Today You Learned:

✔ csv.writer()
✔ csv.reader()
✔ csv.DictWriter()
✔ csv.DictReader()
✔ Reading CSV Files
✔ Writing CSV Files
✔ Counting Records
✔ Reading Specific Columns
✔ Calculating Total & Average Values

Happy Coding! 🚀
"""

# =========================================================
# End of File
# =========================================================
