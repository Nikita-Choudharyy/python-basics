# -----------------------------
# Python Type Casting
# -----------------------------
# Type casting is used to convert one data type into another.

# -----------------------------
# String to Integer
# -----------------------------
a = "10"
b = "20"

print("Before casting:")
print(type(a), type(b))

a = int(a)
b = int(b)

print("After casting:")
print(type(a), type(b))
print("Sum:", a + b)

# -----------------------------
# String to Float
# -----------------------------
x = "3.5"
y = "2.5"

x = float(x)
y = float(y)

print("Addition of floats:", x + y)

# -----------------------------
# Integer to String
# -----------------------------
num = 100
num_str = str(num)

print("Number:", num)
print("String value:", num_str)
print("Type after casting:", type(num_str))

# -----------------------------
# Boolean casting
# -----------------------------
print(bool(0))
print(bool(1))
print(bool(""))
print(bool("Python"))

# -----------------------------
# Practice examples
# -----------------------------

# Take input and convert into integer
num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))

print("Multiplication:", num1 * num2)
