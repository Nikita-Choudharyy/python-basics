# ----------------------------------
# Python Custom Exceptions
# ----------------------------------
# Custom exceptions are user-defined exceptions
# created by extending the Exception class.

# -----------------------------
# Creating a custom exception
# -----------------------------
class AgeError(Exception):
    pass

# -----------------------------
# Using custom exception
# -----------------------------
def check_age(age):
    if age < 18:
        raise AgeError("Age must be 18 or above")
    else:
        print("Access granted")

try:
    check_age(16)
except AgeError as e:
    print("Custom Exception:", e)

# -----------------------------
# Another custom exception example
# -----------------------------
class BalanceError(Exception):
    pass

def withdraw(balance, amount):
    if amount > balance:
        raise BalanceError("Insufficient balance")
    return balance - amount

try:
    remaining = withdraw(5000, 7000)
    print("Remaining balance:", remaining)
except BalanceError as e:
    print("Transaction failed:", e)

# -----------------------------
# Practice examples
# -----------------------------

# 1. Custom exception for negative number
class NegativeNumberError(Exception):
    pass

def check_number(num):
    if num < 0:
        raise NegativeNumberError("Negative numbers are not allowed")
    return num

try:
    value = check_number(-5)
    print("Value:", value)
except NegativeNumberError as e:
    print("Error:", e)
