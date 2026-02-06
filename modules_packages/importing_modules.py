# ----------------------------------
# Python Importing Modules
# ----------------------------------
# Modules are files that contain Python code (functions, variables, classes)
# and help in organizing code efficiently.

# -----------------------------
# Importing a built-in module
# -----------------------------
import math

print("Square root of 16:", math.sqrt(16))
print("Value of pi:", math.pi)

# -----------------------------
# Importing specific functions
# -----------------------------
from math import pow, factorial

print("2 raised to power 3:", pow(2, 3))
print("Factorial of 5:", factorial(5))

# -----------------------------
# Importing with alias
# -----------------------------
import datetime as dt

current_date = dt.date.today()
print("Today's date:", current_date)

# -----------------------------
# Using random module
# -----------------------------
import random

print("Random number between 1 and 10:", random.randint(1, 10))

# -----------------------------
# Checking module attributes
# -----------------------------
print("Math module attributes:", dir(math))

# -----------------------------
# Practice examples
# -----------------------------

# 1. Generate a random float number
print("Random float:", random.random())

# 2. Calculate area of a circle
radius = 7
area = math.pi * math.pow(radius, 2)
print("Area of circle:", area)
