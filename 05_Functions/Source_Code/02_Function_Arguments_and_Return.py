"""
=====================================================
Topic: Function Arguments and Return Statement
File : 02_Function_Arguments_and_Return.py

Description:
This file demonstrates:
1. Positional Arguments
2. Keyword Arguments
3. Default Arguments
4. Variable-Length Arguments (*args)
5. Keyword Variable-Length Arguments (**kwargs)
6. Return Statement
7. Returning Multiple Values
8. Real-World Examples
9. Best Practices

Author : Nikita Choudhary
Repository : Python Basics
=====================================================
"""

# =====================================================
# 1. Positional Arguments
# =====================================================

print("===== Positional Arguments =====")

def rectangle_area(length, width):
    area = length * width
    print("Area:", area)

rectangle_area(10, 5)

# =====================================================
# 2. Keyword Arguments
# =====================================================

print("\n===== Keyword Arguments =====")

def employee(name, department):
    print(f"Employee  : {name}")
    print(f"Department: {department}")

employee(department="AI Team", name="Anjali")

# =====================================================
# 3. Default Arguments
# =====================================================

print("\n===== Default Arguments =====")

def send_email(receiver, subject="No Subject"):
    print("Receiver :", receiver)
    print("Subject  :", subject)

send_email("nikita@gmail.com")
send_email("hr@company.com", "Interview Invitation")

# =====================================================
# 4. Variable-Length Arguments (*args)
# =====================================================

print("\n===== *args =====")

def highest_score(*scores):
    print("Highest Score:", max(scores))

highest_score(78, 82, 95, 89)

# =====================================================
# 5. Keyword Variable-Length Arguments (**kwargs)
# =====================================================

print("\n===== **kwargs =====")

def laptop_details(**details):

    for key, value in details.items():
        print(f"{key}: {value}")

laptop_details(
    Brand="Lenovo",
    RAM="16 GB",
    Processor="Ryzen 7"
)

# =====================================================
# 6. Return Statement
# =====================================================

print("\n===== Return Statement =====")

def cube(number):
    return number ** 3

result = cube(4)

print("Cube:", result)

# =====================================================
# 7. Returning Multiple Values
# =====================================================

print("\n===== Returning Multiple Values =====")

def circle(radius):

    area = 3.14 * radius ** 2
    circumference = 2 * 3.14 * radius

    return area, circumference

area, circumference = circle(7)

print("Area          :", area)
print("Circumference :", circumference)

# =====================================================
# 8. Real-World Example - Temperature Converter
# =====================================================

print("\n===== Temperature Converter =====")

def celsius_to_fahrenheit(celsius):

    fahrenheit = (celsius * 9/5) + 32

    return fahrenheit

temperature = celsius_to_fahrenheit(25)

print("Temperature:", temperature, "°F")

# =====================================================
# 9. Real-World Example - Movie Ticket Price
# =====================================================

print("\n===== Movie Ticket =====")

def ticket_price(price, seats):

    return price * seats

total = ticket_price(250, 4)

print("Total Ticket Price: ₹", total)

# =====================================================
# 10. Best Practices
# =====================================================

# ✔ Keep functions short and focused.
# ✔ Use descriptive parameter names.
# ✔ Prefer returning values over printing them.
# ✔ Use default arguments only when appropriate.
# ✔ Avoid unnecessary global variables.

# =====================================================
# 11. Mini Practice
# =====================================================

# Try these on your own:
#
# 1. Create a function to calculate BMI.
# 2. Create a function to convert rupees into dollars.
# 3. Create a function that returns the smallest of three numbers.
# 4. Create a function using *args to multiply numbers.
# 5. Create a function using **kwargs to display mobile specifications.
# 6. Create a function that returns quotient and remainder.
# 7. Create a function to calculate electricity bill.

# =====================================================
# End of Program
# =====================================================

print("\nCongratulations! You completed Function Arguments and Return Statement. 🎉")