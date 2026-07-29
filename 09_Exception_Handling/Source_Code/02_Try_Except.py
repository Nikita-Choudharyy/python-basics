"""
=========================================================
Topic : Try and Except
File  : 02_Try_Except.py

Description:
This file demonstrates how to use try and except blocks
to handle runtime exceptions gracefully.

Topics Covered:
1. Introduction to try-except
2. Basic try-except
3. Handling Different Exceptions
4. Multiple except Blocks
5. Catching Multiple Exceptions
6. Real-World Examples
7. Best Practices

Author : Nikita Choudhary
Repository : Python Basics
=========================================================
"""

# =====================================================
# Try and Except
# =====================================================

print("=" * 60)
print("TRY AND EXCEPT")
print("=" * 60)

# =====================================================
# 1. Basic try-except
# =====================================================

print("\n===== Basic try-except =====")

try:

    number = 10 / 0

    print(number)

except ZeroDivisionError:

    print("Cannot divide a number by zero.")

# =====================================================
# 2. Handling ValueError
# =====================================================

print("\n===== ValueError =====")

try:

    age = int("Twenty")

    print(age)

except ValueError:

    print("Invalid integer value.")

# =====================================================
# 3. Handling IndexError
# =====================================================

print("\n===== IndexError =====")

languages = [
    "Python",
    "Java",
    "C++"
]

try:

    print(languages[10])

except IndexError:

    print("List index is out of range.")

# =====================================================
# 4. Handling KeyError
# =====================================================

print("\n===== KeyError =====")

student = {

    "name": "Nikita",

    "course": "Python"

}

try:

    print(student["marks"])

except KeyError:

    print("Requested key does not exist.")

# =====================================================
# 5. Handling TypeError
# =====================================================

print("\n===== TypeError =====")

try:

    result = 100 + "50"

    print(result)

except TypeError:

    print("Cannot add integer and string.")

# =====================================================
# 6. Multiple except Blocks
# =====================================================

print("\n===== Multiple except Blocks =====")

try:

    number = int("Python")

    result = 10 / number

    print(result)

except ValueError:

    print("Invalid number.")

except ZeroDivisionError:

    print("Division by zero is not allowed.")

# =====================================================
# 7. Catching Multiple Exceptions Together
# =====================================================

print("\n===== Multiple Exceptions =====")

try:

    numbers = [10, 20]

    print(numbers[5])

except (IndexError, KeyError):

    print("IndexError or KeyError occurred.")

# =====================================================
# 8. Exception Object
# =====================================================

print("\n===== Exception Object =====")

try:

    number = int("Hello")

except ValueError as error:

    print("Exception Message :")

    print(error)

# =====================================================
# 9. Real-World Example - ATM Withdrawal
# =====================================================

print("\n===== ATM Withdrawal =====")

balance = 5000

try:

    withdrawal_amount = 6000

    if withdrawal_amount > balance:

        raise ValueError("Insufficient Balance")

    print("Transaction Successful")

except ValueError as error:

    print(error)

# =====================================================
# 10. Real-World Example - Student Marks
# =====================================================

print("\n===== Student Marks =====")

marks = {

    "Python": 95,

    "SQL": 90

}

try:

    print("Machine Learning :", marks["Machine Learning"])

except KeyError:

    print("Subject not found.")

# =====================================================
# 11. Best Practices
# =====================================================

# ✔ Keep try blocks as small as possible.
# ✔ Catch only expected exceptions.
# ✔ Use specific exception types.
# ✔ Display meaningful error messages.
# ✔ Avoid using bare except.

# =====================================================
# 12. Mini Practice
# =====================================================

# Try these yourself:
#
# 1. Handle ZeroDivisionError.
# 2. Handle ValueError.
# 3. Handle TypeError.
# 4. Handle IndexError.
# 5. Handle KeyError.
# 6. Use multiple except blocks.
# 7. Catch multiple exceptions together.
# 8. Print exception messages using "as".
# 9. Create your own student record example.
# 10. Create your own banking example.

# =====================================================
# End of Program
# =====================================================

print("\nCongratulations! You completed Try and Except. 🎉")