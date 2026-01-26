# -----------------------------
# Python Lambda Functions
# -----------------------------
# Lambda functions are small anonymous functions
# written in a single line using the lambda keyword.

# -----------------------------
# Basic lambda function
# -----------------------------
square = lambda x: x * x
print("Square of 5:", square(5))

# -----------------------------
# Lambda with multiple arguments
# -----------------------------
add = lambda a, b: a + b
print("Addition:", add(10, 20))

# -----------------------------
# Lambda used inside another function
# -----------------------------
def multiply_by(n):
    return lambda x: x * n

double = multiply_by(2)
triple = multiply_by(3)

print("Double of 5:", double(5))
print("Triple of 5:", triple(5))

# -----------------------------
# Lambda with conditional expression
# -----------------------------
check_even_odd = lambda x: "Even" if x % 2 == 0 else "Odd"

print("7 is:", check_even_odd(7))
print("10 is:", check_even_odd(10))

# -----------------------------
# Lambda with list
# -----------------------------
numbers = [1, 2, 3, 4, 5]

squares = list(map(lambda x: x * x, numbers))
print("Squares:", squares)

# -----------------------------
# Practice examples
# -----------------------------

# 1. Lambda to find maximum of two numbers
max_num = lambda a, b: a if a > b else b
print("Maximum:", max_num(15, 20))

# 2. Lambda to calculate cube
cube = lambda x: x ** 3
print("Cube of 3:", cube(3))
