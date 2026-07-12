"""
=====================================================
Topic: While Loop in Python
File : 02_While_Loop.py

Description:
This file demonstrates:
1. Introduction to while Loop
2. Basic while Loop
3. Infinite Loop (Example)
4. Counter-Controlled Loop
5. User-Controlled Loop
6. Real-World Examples
7. Best Practices

Author : Nikita Choudhary
Repository : Python Basics
=====================================================
"""

# =====================================================
# 1. What is a while Loop?
# =====================================================

# A while loop repeatedly executes a block of code
# as long as the given condition remains True.

print("Python While Loop Examples")

# =====================================================
# 2. Basic while Loop
# =====================================================

print("\n===== Basic while Loop =====")

count = 1

while count <= 5:
    print(count)
    count += 1

# =====================================================
# 3. Counter-Controlled Loop
# =====================================================

print("\n===== Counter-Controlled Loop =====")

number = 10

while number >= 1:
    print(number)
    number -= 1

# =====================================================
# 4. User-Controlled Loop
# =====================================================

print("\n===== User-Controlled Loop =====")

password = ""

while password != "python123":
    password = input("Enter password: ")

print("Access Granted!")

# =====================================================
# 5. Infinite Loop (Example)
# =====================================================

print("\n===== Infinite Loop Example =====")

print("Example (Do NOT Run):")

# while True:
#     print("This loop runs forever.")

# =====================================================
# 6. Real-World Example - ATM PIN Verification
# =====================================================

print("\n===== ATM PIN Verification =====")

correct_pin = "1234"
entered_pin = ""

while entered_pin != correct_pin:
    entered_pin = input("Enter your ATM PIN: ")

print("PIN Verified Successfully!")

# =====================================================
# 7. Real-World Example - Countdown Timer
# =====================================================

print("\n===== Countdown Timer =====")

timer = 5

while timer > 0:
    print(timer)
    timer -= 1

print("Time's Up!")

# =====================================================
# 8. Real-World Example - Shopping Cart
# =====================================================

print("\n===== Shopping Cart =====")

cart_items = 3

while cart_items > 0:
    print(f"Item Remaining: {cart_items}")
    cart_items -= 1

print("Your cart is now empty.")

# =====================================================
# 9. Real-World Example - Water Bottle Filling
# =====================================================

print("\n===== Water Bottle Filling =====")

water_level = 0

while water_level < 5:
    water_level += 1
    print(f"Water Level: {water_level} Litre")

print("Bottle is Full!")

# =====================================================
# 10. Best Practices
# =====================================================

# ✔ Always update the loop variable.
# ✔ Ensure the condition eventually becomes False.
# ✔ Avoid unnecessary infinite loops.
# ✔ Use while loops when the number of iterations
#   is unknown.

# =====================================================
# 11. Mini Practice
# =====================================================

# Try these on your own:
#
# 1. Print numbers from 1 to 20.
# 2. Print even numbers using a while loop.
# 3. Print odd numbers using a while loop.
# 4. Create a countdown timer from 10 to 1.
# 5. Ask the user to enter "yes" to stop the loop.
# 6. Create a simple login system.
# 7. Print the multiplication table of 7.
# 8. Calculate the sum of numbers from 1 to 100.

# =====================================================
# End of Program
# =====================================================

print("\nCongratulations! You completed While Loop in Python. 🎉")