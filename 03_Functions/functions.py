# ----------------------------------
# Python Functions
# ----------------------------------
# Functions are blocks of reusable code
# that perform a specific task.

# -----------------------------
# 1. Defining a function
# -----------------------------
def greet():
    print("Hello, welcome to Python functions!")

greet()

# -----------------------------
# 2. Function with parameters
# -----------------------------
def add(a, b):
    return a + b

result = add(5, 3)
print("Addition result:", result)

# -----------------------------
# 3. Function with default parameter
# -----------------------------
def greet_user(name="User"):
    print("Hello", name)

greet_user()
greet_user("Nikita")

# -----------------------------
# 4. Function returning multiple values
# -----------------------------
def calculate(a, b):
    sum_val = a + b
    diff_val = a - b
    return sum_val, diff_val

s, d = calculate(10, 5)
print("Sum:", s)
print("Difference:", d)

# -----------------------------
# 5. Function inside loop
# -----------------------------
def square(num):
    return num * num

for i in range(1, 6):
    print("Square of", i, "is", square(i))

# -----------------------------
# Practice examples
# -----------------------------

# 1. Function to check even or odd
def check_even_odd(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"

print(check_even_odd(10))
print(check_even_odd(7))

# 2. Function to find maximum of two numbers
def find_max(a, b):
    if a > b:
        return a
    else:
        return b

print("Maximum value:", find_max(15, 20))
