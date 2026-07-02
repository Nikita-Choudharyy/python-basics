# ----------------------------------
# Python File Handling (Text Files)
# ----------------------------------
# This file covers basic operations on .txt files:
# write, read, append

# -----------------------------
# Writing to a file
# -----------------------------
file = open("sample.txt", "w")
file.write("Hello, this is a sample text file.\n")
file.write("Learning Python file handling.\n")
file.close()

print("Data written to file.")

# -----------------------------
# Reading from a file
# -----------------------------
file = open("sample.txt", "r")
content = file.read()
file.close()

print("File content:")
print(content)

# -----------------------------
# Reading line by line
# -----------------------------
file = open("sample.txt", "r")
for line in file:
    print(line.strip())
file.close()

# -----------------------------
# Appending to a file
# -----------------------------
file = open("sample.txt", "a")
file.write("This line is appended.\n")
file.close()

print("Data appended to file.")

# -----------------------------
# Using with statement
# -----------------------------
# Automatically closes the file
with open("sample.txt", "r") as file:
    print("Reading using with statement:")
    print(file.read())

# -----------------------------
# Practice examples
# -----------------------------

# 1. Count number of lines in file
with open("sample.txt", "r") as file:
    lines = file.readlines()
    print("Number of lines:", len(lines))

# 2. Count number of words in file
with open("sample.txt", "r") as file:
    text = file.read()
    words = text.split()
    print("Number of words:", len(words))
