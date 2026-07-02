# ----------------------------------
# Python Exception Handling (try-except)
# ----------------------------------
# Exception handling is used to handle runtime errors
# so that the program does not crash.

# -----------------------------
# Basic try-except
# -----------------------------
try:
    a = 10
    b = 0
    result = a / b
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Cannot divide by zero")

# -----------------------------
# Handling multiple exceptions
# -----------------------------
try:
    x = int("abc")
except ValueError:
    print("Error: Invalid type conversion")
except Exception as e:
    print("Unexpected error:", e)

# -----------------------------
# try-except-else
# -----------------------------
try:
    num1 = 10
    num2 = 5
    result = num1 / num2
except ZeroDivisionError:
    print("Division by zero error")
else:
    print("Division successful, result:", result)

# -----------------------------
# try-except-finally
# -----------------------------
try:
    file = open("sample.txt", "r")
    print(file.read())
except FileNotFoundError:
    print("File not found")
finally:
    print("Execution completed")

# -----------------------------
# Practice examples
# -----------------------------

# 1. Handle invalid user input
try:
    number = int(input("Enter a number: "))
    print("You entered:", number)
except ValueError:
    print("Please enter a valid integer")

# 2. Handle index error
numbers = [1, 2, 3]
try:
    print(numbers[5])
except IndexError:
    print("Index out of range")
