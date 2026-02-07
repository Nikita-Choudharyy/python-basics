# ----------------------------------
# Python Custom Modules
# ----------------------------------
# A custom module is a user-defined Python file
# that contains functions, variables, or classes.
# It helps in code reuse and better organization.

# NOTE:
# Create a file named "math_utils.py" in the SAME folder
# and add the following code in it before running this file:
#
# def add(a, b):
#     return a + b
#
# def subtract(a, b):
#     return a - b
#
# PI = 3.14159

# -----------------------------
# Importing the custom module
# -----------------------------
import math_utils

print("Addition:", math_utils.add(10, 5))
print("Subtraction:", math_utils.subtract(10, 5))
print("Value of PI:", math_utils.PI)

# -----------------------------
# Import specific items
# -----------------------------
from math_utils import add, PI

print("Add using direct import:", add(3, 7))
print("PI value:", PI)

# -----------------------------
# Import with alias
# -----------------------------
import math_utils as mu

print("Addition using alias:", mu.add(20, 30))

# -----------------------------
# Using __name__ check (best practice)
# -----------------------------
if __name__ == "__main__":
    print("This file is executed directly")
