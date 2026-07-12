"""
=====================================================
Topic: Loop Control Statements in Python
File : 03_Loop_Control_Statements.py

Description:
This file demonstrates:
1. break Statement
2. continue Statement
3. pass Statement
4. Real-World Examples
5. Best Practices

Author : Nikita Choudhary
Repository : Python Basics
=====================================================
"""

# =====================================================
# 1. What are Loop Control Statements?
# =====================================================

# Loop control statements change the normal execution
# of a loop.

print("Loop Control Statements in Python")

# =====================================================
# 2. break Statement
# =====================================================

print("\n===== break Statement =====")

for number in range(1, 11):

    if number == 6:
        break

    print(number)

# =====================================================
# 3. continue Statement
# =====================================================

print("\n===== continue Statement =====")

for number in range(1, 11):

    if number == 5:
        continue

    print(number)

# =====================================================
# 4. pass Statement
# =====================================================

print("\n===== pass Statement =====")

for number in range(1, 6):

    if number == 3:
        pass

    print(number)

# =====================================================
# 5. break with while Loop
# =====================================================

print("\n===== break with while Loop =====")

count = 1

while True:

    print(count)

    if count == 5:
        break

    count += 1

# =====================================================
# 6. continue with while Loop
# =====================================================

print("\n===== continue with while Loop =====")

count = 0

while count < 10:

    count += 1

    if count == 5:
        continue

    print(count)

# =====================================================
# 7. Real-World Example - ATM PIN Verification
# =====================================================

print("\n===== ATM PIN Verification =====")

correct_pin = "1234"

attempts = 3

while attempts > 0:

    pin = input("Enter ATM PIN: ")

    if pin == correct_pin:
        print("Access Granted")
        break

    attempts -= 1
    print("Incorrect PIN")

if attempts == 0:
    print("Your account has been temporarily locked.")

# =====================================================
# 8. Real-World Example - Skip Out of Stock Products
# =====================================================

print("\n===== Shopping Cart =====")

products = [
    "Laptop",
    "Mouse",
    "Out of Stock",
    "Keyboard",
    "Monitor"
]

for product in products:

    if product == "Out of Stock":
        continue

    print("Purchased:", product)

# =====================================================
# 9. Real-World Example - Placeholder
# =====================================================

print("\n===== pass Example =====")

feature_completed = False

if feature_completed:
    print("Feature Ready")
else:
    pass

print("Development Continues...")

# =====================================================
# 10. Best Practices
# =====================================================

# ✔ Use break to exit a loop immediately.
# ✔ Use continue to skip only the current iteration.
# ✔ Use pass as a placeholder while writing code.
# ✔ Avoid excessive use of break and continue.
# ✔ Keep loop logic simple and readable.

# =====================================================
# 11. Mini Practice
# =====================================================

# Try these on your own:
#
# 1. Stop a loop when a number becomes greater than 20.
# 2. Skip all even numbers using continue.
# 3. Create a password checker using break.
# 4. Create a menu-driven program using while True.
# 5. Use pass while designing an unfinished function.

# =====================================================
# End of Program
# =====================================================

print("\nCongratulations! You completed Loop Control Statements in Python. 🎉")