# ----------------------------------
# Python File Handling (CSV Files)
# ----------------------------------
# This file covers basic operations on CSV files:
# write, read using csv module

import csv

# -----------------------------
# Writing to a CSV file
# -----------------------------
with open("students.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    
    # Writing header
    writer.writerow(["Name", "Age", "Marks"])
    
    # Writing rows
    writer.writerow(["Amit", 20, 85])
    writer.writerow(["Neha", 22, 90])
    writer.writerow(["Rahul", 21, 78])

print("Data written to students.csv")

# -----------------------------
# Reading from a CSV file
# -----------------------------
with open("students.csv", mode="r") as file:
    reader = csv.reader(file)
    
    print("CSV file content:")
    for row in reader:
        print(row)

# -----------------------------
# Reading CSV as dictionary
# -----------------------------
with open("students.csv", mode="r") as file:
    dict_reader = csv.DictReader(file)
    
    print("Reading CSV using DictReader:")
    for row in dict_reader:
        print(row)

# -----------------------------
# Practice examples
# -----------------------------

# 1. Count number of rows (excluding header)
count = 0
with open("students.csv", mode="r") as file:
    reader = csv.reader(file)
    next(reader)  # skip header
    for _ in reader:
        count += 1

print("Number of student records:", count)
