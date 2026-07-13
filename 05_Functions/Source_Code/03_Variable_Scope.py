"""
=====================================================
Topic: Variable Scope in Python
File : 03_Variable_Scope.py

Description:
This file demonstrates:
1. Local Variables
2. Global Variables
3. Accessing Global Variables
4. Modifying Global Variables
5. Variable Shadowing
6. Local vs Global Scope
7. Real-World Examples
8. Best Practices

Author : Nikita Choudhary
Repository : Python Basics
=====================================================
"""

# =====================================================
# 1. Local Variables
# =====================================================

print("===== Local Variables =====")

def display_city():
    city = "Jaipur"
    print("Inside Function:", city)

display_city()

# print(city)   # Error: city is local to the function

# =====================================================
# 2. Global Variables
# =====================================================

print("\n===== Global Variables =====")

country = "India"

def show_country():
    print("Inside Function:", country)

show_country()

print("Outside Function:", country)

# =====================================================
# 3. Modifying Global Variables
# =====================================================

print("\n===== Modifying Global Variables =====")

visitors = 100

def update_visitors():
    global visitors
    visitors += 25

update_visitors()

print("Total Visitors:", visitors)

# =====================================================
# 4. Variable Shadowing
# =====================================================

print("\n===== Variable Shadowing =====")

company = "OpenAI"

def company_name():
    company = "Google"
    print("Inside Function:", company)

company_name()

print("Outside Function:", company)

# =====================================================
# 5. Local vs Global Scope
# =====================================================

print("\n===== Local vs Global Scope =====")

language = "Python"

def learn():

    language = "Machine Learning"

    print("Learning:", language)

learn()

print("Current Language:", language)

# =====================================================
# 6. Real-World Example - Website Visitors
# =====================================================

print("\n===== Website Visitors =====")

total_visitors = 0

def new_visitor():

    global total_visitors

    total_visitors += 1

new_visitor()
new_visitor()
new_visitor()

print("Visitors Today:", total_visitors)

# =====================================================
# 7. Real-World Example - Bank Balance
# =====================================================

print("\n===== Bank Balance =====")

balance = 5000

def deposit(amount):

    global balance

    balance += amount

deposit(1500)

print("Updated Balance: ₹", balance)

# =====================================================
# 8. Real-World Example - Exam Hall
# =====================================================

print("\n===== Exam Hall =====")

room_number = 205

def student():

    student_name = "Aarav"

    print(student_name, "is in Room", room_number)

student()

# =====================================================
# 9. Best Practices
# =====================================================

# ✔ Prefer local variables whenever possible.
# ✔ Avoid modifying global variables frequently.
# ✔ Use meaningful variable names.
# ✔ Minimize the use of the global keyword.
# ✔ Keep functions independent and reusable.

# =====================================================
# 10. Mini Practice
# =====================================================

# Try these on your own:
#
# 1. Create a local variable inside a function.
# 2. Create a global variable and access it.
# 3. Update a global counter using global.
# 4. Demonstrate variable shadowing.
# 5. Create a simple page view counter.

# =====================================================
# End of Program
# =====================================================

print("\nCongratulations! You completed Variable Scope in Python. 🎉")