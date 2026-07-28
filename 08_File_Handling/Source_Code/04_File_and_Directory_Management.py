"""
=========================================================
Topic : File and Directory Management
File  : 04_File_and_Directory_Management.py

Description:
This file demonstrates how to manage files and
directories using pathlib and shutil.

Topics Covered:
1. Path Objects
2. Current Working Directory
3. Current File Path
4. Create Directories
5. Check File and Folder Existence
6. Rename Files
7. Rename Directories

Author : Nikita Choudhary
Repository : Python Basics
=========================================================
"""

from pathlib import Path
import shutil

# =====================================================
# Dataset Folder Path
# =====================================================

BASE_DIR = Path(__file__).resolve().parent
DATASETS_DIR = BASE_DIR.parent / "Datasets"

print("=" * 60)
print("FILE AND DIRECTORY MANAGEMENT")
print("=" * 60)

# =====================================================
# 1. Current Working Directory
# =====================================================

print("\n===== Current Working Directory =====")

print(Path.cwd())

# =====================================================
# 2. Current Python File
# =====================================================

print("\n===== Current Python File =====")

print(Path(__file__))

# =====================================================
# 3. Parent Directory
# =====================================================

print("\n===== Parent Directory =====")

print(Path(__file__).parent)

# =====================================================
# 4. Absolute Path
# =====================================================

print("\n===== Absolute Path =====")

print(Path(__file__).resolve())

# =====================================================
# 5. Creating a Directory
# =====================================================

print("\n===== Creating Directory =====")

backup_folder = DATASETS_DIR / "backup"

backup_folder.mkdir(exist_ok=True)

print("backup folder created.")

# =====================================================
# 6. Creating Nested Directories
# =====================================================

print("\n===== Creating Nested Directories =====")

reports_folder = DATASETS_DIR / "reports" / "2026"

reports_folder.mkdir(
    parents=True,
    exist_ok=True
)

print("Nested folders created.")

# =====================================================
# 7. Checking Folder Exists
# =====================================================

print("\n===== Folder Exists =====")

print(backup_folder.exists())

print(reports_folder.exists())

# =====================================================
# 8. Checking File Exists
# =====================================================

print("\n===== File Exists =====")

sample_file = DATASETS_DIR / "sample.txt"

print(sample_file.exists())

# =====================================================
# 9. Rename File
# =====================================================

print("\n===== Rename File =====")

old_file = DATASETS_DIR / "sample.txt"

new_file = DATASETS_DIR / "sample_backup.txt"

if old_file.exists():

    old_file.rename(new_file)

    print("File renamed successfully.")

# =====================================================
# 10. Rename Back
# =====================================================

print("\n===== Restore Original File Name =====")

if new_file.exists():

    new_file.rename(old_file)

    print("Original filename restored.")

# =====================================================
# 11. Copying a File
# =====================================================

print("\n===== Copy File =====")

source_file = DATASETS_DIR / "sample.txt"
destination_file = DATASETS_DIR / "sample_copy.txt"

shutil.copy(source_file, destination_file)

print("File copied successfully.")

# =====================================================
# 12. Copying File with Metadata
# =====================================================

print("\n===== Copy File with Metadata =====")

metadata_file = DATASETS_DIR / "sample_metadata.txt"

shutil.copy2(source_file, metadata_file)

print("File copied with metadata.")

# =====================================================
# 13. Moving a File
# =====================================================

print("\n===== Move File =====")

move_destination = backup_folder / "sample_copy.txt"

shutil.move(destination_file, move_destination)

print("File moved successfully.")

# =====================================================
# 14. Copying an Entire Directory
# =====================================================

print("\n===== Copy Directory =====")

reports_source = DATASETS_DIR / "reports"
reports_backup = DATASETS_DIR / "reports_backup"

if reports_backup.exists():
    shutil.rmtree(reports_backup)

shutil.copytree(reports_source, reports_backup)

print("Directory copied successfully.")

# =====================================================
# 15. Listing Files and Folders
# =====================================================

print("\n===== Directory Contents =====")

for item in DATASETS_DIR.iterdir():

    print(item.name)

# =====================================================
# 16. Searching Files using glob()
# =====================================================

print("\n===== TXT Files =====")

for file in DATASETS_DIR.glob("*.txt"):

    print(file.name)

# =====================================================
# 17. Recursive Search using rglob()
# =====================================================

print("\n===== All CSV Files =====")

for file in DATASETS_DIR.rglob("*.csv"):

    print(file)

# =====================================================
# 18. Removing a File
# =====================================================

print("\n===== Delete File =====")

delete_file = DATASETS_DIR / "sample_metadata.txt"

if delete_file.exists():

    delete_file.unlink()

    print("File deleted successfully.")

# =====================================================
# 19. Removing an Empty Directory
# =====================================================

print("\n===== Remove Empty Directory =====")

empty_folder = DATASETS_DIR / "Temp"

empty_folder.mkdir(exist_ok=True)

empty_folder.rmdir()

print("Empty directory removed.")

# =====================================================
# 20. Removing an Entire Directory
# =====================================================

print("\n===== Remove Directory Tree =====")

if reports_backup.exists():

    shutil.rmtree(reports_backup)

    print("reports_backup removed.")

# =====================================================
# 21. Real-World Example - Backup Folder
# =====================================================

print("\n===== Backup Example =====")

backup_file = backup_folder / "employees_backup.csv"

employees_file = DATASETS_DIR / "employees.csv"

shutil.copy(employees_file, backup_file)

print("Employee backup created.")

# =====================================================
# 22. Real-World Example - Archive Folder
# =====================================================

print("\n===== Archive Example =====")

archive_folder = DATASETS_DIR / "archive"

archive_folder.mkdir(exist_ok=True)

archive_file = archive_folder / "student.json"

student_json = DATASETS_DIR / "student.json"

shutil.copy(student_json, archive_file)

print("JSON archived successfully.")

# =====================================================
# 23. Best Practices
# =====================================================

# ✔ Use pathlib.Path instead of string paths.
# ✔ Use exist_ok=True when creating directories.
# ✔ Use parents=True for nested folders.
# ✔ Check exists() before renaming or deleting.
# ✔ Use shutil.copy() for normal file copies.
# ✔ Use shutil.copy2() to preserve metadata.
# ✔ Use shutil.move() to move files.
# ✔ Use shutil.copytree() to copy directories.
# ✔ Use shutil.rmtree() carefully because it permanently removes directories.
# ✔ Use glob() and rglob() to search files efficiently.

# =====================================================
# 24. Mini Practice
# =====================================================

# Try these on your own:
#
# 1. Create a Projects folder.
# 2. Create Projects/Python/Assignments.
# 3. Check whether sample.txt exists.
# 4. Rename employees.csv to employees_backup.csv.
# 5. Restore the original filename.
# 6. Copy student.json into the backup folder.
# 7. Move employees_backup.csv into archive.
# 8. List all files inside Datasets.
# 9. Display all JSON files using glob().
# 10. Display all TXT files recursively using rglob().
# 11. Create an empty Test folder and delete it.
# 12. Copy the reports folder and then remove the copied folder.

# =====================================================
# End of Program
# =====================================================

print("\nCongratulations! You completed File and Directory Management in Python. 🎉")