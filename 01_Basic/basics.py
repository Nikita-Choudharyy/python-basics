# Day 1: Python Basics Practice

# Variables
name = "Nikita"
age = 21
is_student = True

print("Name:", name)
print("Age:", age)
print("Student:", is_student)

print("-" * 30)

# Operators
a = 10
b = 3

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)

print("-" * 30)

# Conditional Statement
number = 7

if number % 2 == 0:
    print(number, "is Even")
else:
    print(number, "is Odd")

print("-" * 30)

# Loop
print("Numbers from 1 to 5:")
for i in range(1, 6):
    print(i)

print("-" * 30)

# Function
def square(num):
    return num * num

print("Square of 4:", square(4))
