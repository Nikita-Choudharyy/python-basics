# -----------------------------
# Python Operators
# -----------------------------
# Operators are used to perform operations on values and variables.

# -----------------------------
# Arithmetic Operators
# -----------------------------
a = 10
b = 3

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Exponent:", a ** b)

# -----------------------------
# Comparison Operators
# -----------------------------
print("a == b:", a == b)
print("a != b:", a != b)
print("a > b:", a > b)
print("a < b:", a < b)
print("a >= b:", a >= b)
print("a <= b:", a <= b)

# -----------------------------
# Logical Operators
# -----------------------------
x = True
y = False

print("x and y:", x and y)
print("x or y:", x or y)
print("not x:", not x)

# -----------------------------
# Assignment Operators
# -----------------------------
num = 5
num += 3
print("After += :", num)

num -= 2
print("After -= :", num)

num *= 2
print("After *= :", num)

# -----------------------------
# Membership Operators
# -----------------------------
numbers = [1, 2, 3, 4, 5]

print("3 in numbers:", 3 in numbers)
print("10 not in numbers:", 10 not in numbers)

# -----------------------------
# Identity Operators
# -----------------------------
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print("a is b:", a is b)
print("a is c:", a is c)
print("a is not b:", a is not b)

# -----------------------------
# Practice examples
# -----------------------------

# Check if a number is positive and even
num = 8
print("Positive and even:", num > 0 and num % 2 == 0)
