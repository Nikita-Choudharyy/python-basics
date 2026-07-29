"""
=========================================================
Topic : Else, Finally and Raise
File  : 03_Else_Finally_and_Raise.py

Description:
This file demonstrates how to use else, finally, and
raise statements with exception handling in Python.

Topics Covered:
1. else Block
2. finally Block
3. raise Statement
4. User-defined Exception Raising
5. Real-World Examples
6. Best Practices

Author : Nikita Choudhary
Repository : Python Basics
=========================================================
"""

# =====================================================
# Else, Finally and Raise
# =====================================================

print("=" * 60)
print("ELSE, FINALLY AND RAISE")
print("=" * 60)

# =====================================================
# 1. else Block
# =====================================================

print("\n===== else Block =====")

try:

    number = 20
    result = number / 2

except ZeroDivisionError:

    print("Cannot divide by zero.")

else:

    print("Division Successful.")
    print("Result :", result)

# =====================================================
# 2. else Block Example
# =====================================================

print("\n===== else Example =====")

try:

    marks = int("95")

except ValueError:

    print("Invalid Marks.")

else:

    print("Student Marks :", marks)

# =====================================================
# 3. finally Block
# =====================================================

print("\n===== finally Block =====")

try:

    value = 100 / 5

    print(value)

except ZeroDivisionError:

    print("Division Error")

finally:

    print("Program Finished.")

# =====================================================
# 4. finally with Exception
# =====================================================

print("\n===== finally with Exception =====")

try:

    print(10 / 0)

except ZeroDivisionError:

    print("Cannot divide by zero.")

finally:

    print("This block always executes.")

# =====================================================
# 5. raise Statement
# =====================================================

print("\n===== raise Statement =====")

age = -5

try:

    if age < 0:

        raise ValueError("Age cannot be negative.")

    print(age)

except ValueError as error:

    print(error)

# =====================================================
# 6. raise with Custom Validation
# =====================================================

print("\n===== Password Validation =====")

password = "abc123"

try:

    if len(password) < 8:

        raise ValueError(
            "Password must contain at least 8 characters."
        )

    print("Password Accepted.")

except ValueError as error:

    print(error)

# =====================================================
# 7. Real-World Example - Bank Withdrawal
# =====================================================

print("\n===== Bank Withdrawal =====")

balance = 5000
withdraw_amount = 7000

try:

    if withdraw_amount > balance:

        raise ValueError("Insufficient Balance.")

    print("Withdrawal Successful.")

except ValueError as error:

    print(error)

finally:

    print("Transaction Completed.")

# =====================================================
# 8. Real-World Example - Student Marks
# =====================================================

print("\n===== Student Marks Validation =====")

marks = 120

try:

    if marks > 100:

        raise ValueError(
            "Marks cannot be greater than 100."
        )

    print("Marks Recorded.")

except ValueError as error:

    print(error)

# =====================================================
# 9. Real-World Example - Login System
# =====================================================

print("\n===== Login Validation =====")

username = ""

try:

    if username == "":

        raise ValueError(
            "Username cannot be empty."
        )

    print("Login Successful.")

except ValueError as error:

    print(error)

finally:

    print("Login Process Finished.")

# =====================================================
# 10. Best Practices
# =====================================================

# ✔ Use else for code that should run only if no exception occurs.
# ✔ Use finally for cleanup tasks.
# ✔ finally always executes.
# ✔ Use raise to create meaningful exceptions.
# ✔ Raise exceptions only when necessary.
# ✔ Keep validation messages clear and informative.

# =====================================================
# 11. Mini Practice
# =====================================================

# Try these yourself:
#
# 1. Use else after successful division.
# 2. Use finally after reading a file.
# 3. Raise ValueError for negative salary.
# 4. Raise ValueError if age is below 18.
# 5. Raise ValueError for empty email.
# 6. Validate mobile number length.
# 7. Validate PIN length.
# 8. Create a bank withdrawal example.
# 9. Create a login validation example.
# 10. Combine else and finally in one program.

# =====================================================
# End of Program
# =====================================================

print("\nCongratulations! You completed Else, Finally and Raise. 🎉")