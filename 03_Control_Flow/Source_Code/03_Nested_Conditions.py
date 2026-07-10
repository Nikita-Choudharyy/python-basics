"""
=====================================================
Topic: Nested Conditions in Python
File : 03_Nested_Conditions.py

Description:
This file demonstrates:
1. Introduction to Nested Conditions
2. Basic Nested if Statement
3. Nested if-else Statement
4. Nested if-elif-else Statement
5. Real-World Examples
6. Best Practices

Author : Nikita Choudhary
Repository : Python Basics
=====================================================
"""

# =====================================================
# 1. What are Nested Conditions?
# =====================================================

# A nested condition means placing one conditional
# statement inside another conditional statement.

print("Nested conditions allow us to make multiple levels of decisions.")

# =====================================================
# 2. Basic Nested if Statement
# =====================================================

age = 22
has_id = True

print("\n===== Basic Nested if =====")

if age >= 18:
    print("Age requirement satisfied.")

    if has_id:
        print("Identity verified.")

# =====================================================
# 3. Nested if-else Statement
# =====================================================

marks = 75
attendance = 82

print("\n===== Nested if-else =====")

if attendance >= 75:
    if marks >= 40:
        print("Student Passed.")
    else:
        print("Failed due to low marks.")
else:
    print("Failed due to low attendance.")

# =====================================================
# 4. Nested if-elif-else Statement
# =====================================================

percentage = 87
attendance = 91

print("\n===== Nested if-elif-else =====")

if attendance >= 75:

    if percentage >= 90:
        print("Grade: A+")

    elif percentage >= 75:
        print("Grade: A")

    elif percentage >= 60:
        print("Grade: B")

    else:
        print("Grade: C")

else:
    print("Not Eligible for Grading")

# =====================================================
# 5. Real-World Example - ATM Withdrawal
# =====================================================

balance = 12000
withdraw_amount = 5000
pin_correct = True

print("\n===== ATM Withdrawal =====")

if pin_correct:

    if withdraw_amount <= balance:
        balance -= withdraw_amount

        print("Withdrawal Successful")
        print("Remaining Balance:", balance)

    else:
        print("Insufficient Balance")

else:
    print("Invalid PIN")

# =====================================================
# 6. Real-World Example - Online Shopping
# =====================================================

is_logged_in = True
cart_items = 3

print("\n===== Online Shopping =====")

if is_logged_in:

    if cart_items > 0:
        print("Proceed to Checkout")

    else:
        print("Your cart is empty.")

else:
    print("Please log in first.")

# =====================================================
# 7. Real-World Example - Driving Eligibility
# =====================================================

age = 20
has_license = True

print("\n===== Driving Eligibility =====")

if age >= 18:

    if has_license:
        print("You are allowed to drive.")

    else:
        print("Please obtain a driving license.")

else:
    print("You are underage.")

# =====================================================
# 8. Best Practices
# =====================================================

# ✔ Avoid excessive nesting.
# ✔ Keep nested blocks simple.
# ✔ Use meaningful variable names.
# ✔ Use nested conditions only when necessary.
# ✔ Consider using logical operators when they
#   make the code simpler.

# =====================================================
# 9. Mini Practice
# =====================================================

# Try these on your own:
#
# 1. Check voting eligibility with age and citizenship.
# 2. Create a login system with username and password.
# 3. Check college admission based on marks and age.
# 4. Create an ATM withdrawal program.
# 5. Check whether a student can appear in the final exam.

# =====================================================
# End of Program
# =====================================================

print("\nCongratulations! You completed Nested Conditions in Python. 🎉")