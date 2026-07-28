"""
=========================================================
Topic : CSV and JSON Files
File  : 03_CSV_and_JSON_Files.py

Description:
This file demonstrates how to work with CSV and JSON
files using Python's built-in csv and json modules.

Topics Covered:
1. CSV Introduction
2. Writing CSV Files
3. Reading CSV Files
4. DictWriter
5. DictReader
6. JSON Introduction
7. json.dumps()
8. json.loads()
9. json.dump()
10. json.load()

Author : Nikita Choudhary
Repository : Python Basics
=========================================================
"""

import csv
import json
from pathlib import Path

# =====================================================
# Dataset Folder Path
# =====================================================

BASE_DIR = Path(__file__).resolve().parent
DATASETS_DIR = BASE_DIR.parent / "Datasets"

print("=" * 60)
print("CSV AND JSON FILES")
print("=" * 60)

# =====================================================
# 1. Writing CSV File
# =====================================================

print("\n===== Writing CSV File =====")

employees_file = DATASETS_DIR / "employees.csv"

with employees_file.open(
    "w",
    newline="",
    encoding="utf-8"
) as file:

    writer = csv.writer(file)

    # Header
    writer.writerow([
        "ID",
        "Name",
        "Department",
        "Salary"
    ])

    # Records
    writer.writerow([101, "Nikita", "AI", 50000])
    writer.writerow([102, "Rahul", "HR", 35000])
    writer.writerow([103, "Neha", "Finance", 45000])
    writer.writerow([104, "Aman", "Sales", 40000])

print("employees.csv created successfully.")

# =====================================================
# 2. Reading CSV File
# =====================================================

print("\n===== Reading CSV File =====")

with employees_file.open(
    "r",
    encoding="utf-8"
) as file:

    reader = csv.reader(file)

    for row in reader:
        print(row)

# =====================================================
# 3. Reading CSV with Line Numbers
# =====================================================

print("\n===== CSV with Line Numbers =====")

with employees_file.open(
    "r",
    encoding="utf-8"
) as file:

    reader = csv.reader(file)

    for line_number, row in enumerate(reader, start=1):

        print(f"{line_number} : {row}")

# =====================================================
# 4. CSV DictReader
# =====================================================

print("\n===== DictReader =====")

with employees_file.open(
    "r",
    encoding="utf-8"
) as file:

    reader = csv.DictReader(file)

    for row in reader:

        print(row)

# =====================================================
# 5. Accessing Individual Columns
# =====================================================

print("\n===== Employee Details =====")

with employees_file.open(
    "r",
    encoding="utf-8"
) as file:

    reader = csv.DictReader(file)

    for row in reader:

        print(f"Employee   : {row['Name']}")
        print(f"Department : {row['Department']}")
        print(f"Salary     : {row['Salary']}")
        print("-" * 35)

# =====================================================
# 6. Writing CSV using DictWriter
# =====================================================

print("\n===== DictWriter =====")

students_file = DATASETS_DIR / "students.csv"

field_names = [
    "Roll No",
    "Name",
    "Course",
    "Marks"
]

with students_file.open(
    "w",
    newline="",
    encoding="utf-8"
) as file:

    writer = csv.DictWriter(
        file,
        fieldnames=field_names
    )

    writer.writeheader()

    writer.writerow({
        "Roll No": 1,
        "Name": "Nikita",
        "Course": "Python",
        "Marks": 95
    })

    writer.writerow({
        "Roll No": 2,
        "Name": "Rahul",
        "Course": "Data Science",
        "Marks": 90
    })

    writer.writerow({
        "Roll No": 3,
        "Name": "Neha",
        "Course": "Machine Learning",
        "Marks": 92
    })

print("students.csv created successfully.")

# =====================================================
# 7. Reading CSV using DictReader
# =====================================================

print("\n===== Reading students.csv =====")

with students_file.open(
    "r",
    encoding="utf-8"
) as file:

    reader = csv.DictReader(file)

    for row in reader:

        print(row)

# =====================================================
# 8. JSON Introduction
# =====================================================

print("\n===== Python Dictionary =====")

student = {

    "id": 101,

    "name": "Nikita",

    "course": "Python",

    "marks": 95,

    "skills": [
        "Python",
        "NumPy",
        "Pandas",
        "SQL"
    ]
}

print(student)

# =====================================================
# 9. Python Object to JSON String
# =====================================================

print("\n===== json.dumps() =====")

json_string = json.dumps(student)

print(json_string)

# =====================================================
# 10. Pretty Printing JSON
# =====================================================

print("\n===== Pretty JSON =====")

pretty_json = json.dumps(
    student,
    indent=4
)

print(pretty_json)

# =====================================================
# 11. JSON String to Python Object
# =====================================================

print("\n===== json.loads() =====")

json_data = """
{
    "id": 201,
    "name": "Aman",
    "course": "Data Science",
    "marks": 89
}
"""

python_object = json.loads(json_data)

print(python_object)
print(type(python_object))

# =====================================================
# 12. Writing JSON File
# =====================================================

print("\n===== json.dump() =====")

student_data = {
    "id": 101,
    "name": "Nikita",
    "course": "Python",
    "marks": 95,
    "skills": [
        "Python",
        "NumPy",
        "Pandas",
        "SQL"
    ]
}

student_json_file = DATASETS_DIR / "student.json"

with student_json_file.open(
    "w",
    encoding="utf-8"
) as file:

    json.dump(
        student_data,
        file,
        indent=4
    )

print("student.json created successfully.")

# =====================================================
# 13. Reading JSON File
# =====================================================

print("\n===== json.load() =====")

with student_json_file.open(
    "r",
    encoding="utf-8"
) as file:

    data = json.load(file)

print(data)

# =====================================================
# 14. Accessing JSON Values
# =====================================================

print("\n===== Student Details =====")

print(f"ID      : {data['id']}")
print(f"Name    : {data['name']}")
print(f"Course  : {data['course']}")
print(f"Marks   : {data['marks']}")
print(f"Skills  : {', '.join(data['skills'])}")

# =====================================================
# 15. Real-World Example - Employee Database
# =====================================================

print("\n===== Employee Database =====")

employees = [
    {
        "id": 101,
        "name": "Nikita",
        "department": "AI"
    },
    {
        "id": 102,
        "name": "Rahul",
        "department": "HR"
    },
    {
        "id": 103,
        "name": "Neha",
        "department": "Finance"
    }
]

employee_json_file = DATASETS_DIR / "employees.json"

with employee_json_file.open(
    "w",
    encoding="utf-8"
) as file:

    json.dump(
        employees,
        file,
        indent=4
    )

print("employees.json created successfully.")

# Display Employee Records

with employee_json_file.open(
    "r",
    encoding="utf-8"
) as file:

    employee_records = json.load(file)

for employee in employee_records:

    print(
        f"{employee['id']} | "
        f"{employee['name']} | "
        f"{employee['department']}"
    )

# =====================================================
# 16. Real-World Example - Configuration File
# =====================================================

print("\n===== Configuration File =====")

config = {
    "theme": "Dark",
    "language": "English",
    "font_size": 14,
    "auto_save": True
}

config_file = DATASETS_DIR / "config.json"

with config_file.open(
    "w",
    encoding="utf-8"
) as file:

    json.dump(
        config,
        file,
        indent=4
    )

print("config.json created successfully.")

with config_file.open(
    "r",
    encoding="utf-8"
) as file:

    settings = json.load(file)

print(settings)

# =====================================================
# 17. Best Practices
# =====================================================

# ✔ Use csv.reader() for reading CSV files.
# ✔ Use csv.writer() for writing CSV files.
# ✔ Use DictReader when working with column names.
# ✔ Use DictWriter to write dictionaries directly.
# ✔ Always use newline="" while writing CSV files.
# ✔ Use UTF-8 encoding for better compatibility.
# ✔ Use json.dumps() for converting Python objects to JSON strings.
# ✔ Use json.loads() for converting JSON strings to Python objects.
# ✔ Use json.dump() to write JSON data into a file.
# ✔ Use json.load() to read JSON data from a file.
# ✔ Use indent=4 to make JSON files human-readable.

# =====================================================
# 18. Mini Practice
# =====================================================

# Try these on your own:
#
# 1. Create a products.csv file.
# 2. Add five product records.
# 3. Read and display all products.
# 4. Create students.csv using DictWriter.
# 5. Read students.csv using DictReader.
# 6. Convert a Python dictionary into a JSON string.
# 7. Convert a JSON string back into a dictionary.
# 8. Save a dictionary into employee.json.
# 9. Read employee.json and display all values.
# 10. Create your own config.json file with at least five settings.

# =====================================================
# End of Program
# =====================================================

print("\nCongratulations! You completed CSV and JSON Files in Python. 🎉")