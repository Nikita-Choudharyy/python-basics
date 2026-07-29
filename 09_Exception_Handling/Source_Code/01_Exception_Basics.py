"""
=========================================================
Topic : Exception Basics
File  : 01_Exception_Basics.py

Description:
This file introduces the fundamentals of exceptions in
Python. It explains what exceptions are, why they occur,
and how they affect program execution.

Topics Covered:
1. What is an Exception?
2. Exception vs Syntax Error
3. Why Exceptions Occur
4. Common Exception Examples
5. Program Flow with Exceptions
6. Real-World Example
7. Best Practices

Author : Nikita Choudhary
Repository : Python Basics
=========================================================
"""

# =====================================================
# Exception Basics
# =====================================================

print("=" * 60)
print("EXCEPTION BASICS")
print("=" * 60)

# =====================================================
# 1. What is an Exception?
# =====================================================

print("\n===== What is an Exception? =====")

print(
    "An exception is an error that occurs during "
    "program execution and interrupts the normal "
    "flow of the program."
)

# =====================================================
# 2. Exception vs Syntax Error
# =====================================================

print("\n===== Exception vs Syntax Error =====")

print("Syntax Error : Happens before the program runs.")
print("Exception    : Happens while the program is running.")

# =====================================================
# 3. Example - ZeroDivisionError
# =====================================================

print("\n===== ZeroDivisionError Example =====")

number = 10

print("Number :", number)

print("The next statement will generate an exception.")

# Uncomment the line below to see the exception.

# print(number / 0)

# =====================================================
# 4. Example - NameError
# =====================================================

print("\n===== NameError Example =====")

print("Using an undefined variable causes NameError.")

# Uncomment the line below.

# print(student_name)

# =====================================================
# 5. Example - TypeError
# =====================================================

print("\n===== TypeError Example =====")

print("Adding integer and string causes TypeError.")

# Uncomment the line below.

# print(10 + "20")

# =====================================================
# 6. Example - IndexError
# =====================================================

print("\n===== IndexError Example =====")

languages = [
    "Python",
    "Java",
    "C++"
]

print("Languages :", languages)

print("Accessing an invalid index raises IndexError.")

# Uncomment the line below.

# print(languages[10])

# =====================================================
# 7. Example - KeyError
# =====================================================

print("\n===== KeyError Example =====")

student = {
    "name": "Nikita",
    "course": "Python"
}

print(student)

print("Accessing a missing key raises KeyError.")

# Uncomment the line below.

# print(student["marks"])

# =====================================================
# 8. Program Flow
# =====================================================

print("\n===== Program Flow =====")

print("Statement 1")

print("Statement 2")

print("If an exception occurs here,")

print("the remaining statements stop executing.")

print("Statement 3")

# =====================================================
# 9. Real-World Example
# =====================================================

print("\n===== Real-World Example =====")

print(
    "Imagine an ATM machine."
)

print(
    "If the network connection fails while "
    "withdrawing money, the ATM cannot continue "
    "processing the request."
)

print(
    "That runtime problem is similar to an exception."
)

# =====================================================
# 10. Why Learn Exception Handling?
# =====================================================

print("\n===== Why Exception Handling? =====")

print("- Prevents unexpected program crashes.")

print("- Improves user experience.")

print("- Makes programs reliable.")

print("- Helps in debugging.")

print("- Essential for real-world applications.")

# =====================================================
# 11. Best Practices
# =====================================================

# ✔ Learn common exceptions before handling them.
# ✔ Read error messages carefully.
# ✔ Understand why an exception occurred.
# ✔ Don't ignore runtime errors.
# ✔ Use exception handling only when needed.

# =====================================================
# 12. Mini Practice
# =====================================================

# Try these yourself:
#
# 1. Create a ZeroDivisionError.
# 2. Create a NameError.
# 3. Create a TypeError.
# 4. Create an IndexError.
# 5. Create a KeyError.
# 6. Read each error message carefully.
# 7. Identify which line generated the error.
# 8. Explain why the error occurred.
# 9. Fix each error without using try-except.
# 10. Observe how program execution stops after an exception.

# =====================================================
# End of Program
# =====================================================

print("\nCongratulations! You completed Exception Basics. 🎉")