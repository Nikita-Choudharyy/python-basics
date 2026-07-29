"""
=========================================================
Topic : Custom Exceptions
File  : 05_Custom_Exceptions.py

Description:
This file demonstrates how to create and use custom
exceptions in Python for handling application-specific
errors.

Topics Covered:
1. Creating a Custom Exception
2. Raising a Custom Exception
3. Multiple Custom Exceptions
4. Real-World Examples
5. Best Practices

Author : Nikita Choudhary
Repository : Python Basics
=========================================================
"""

# =====================================================
# Custom Exceptions
# =====================================================

print("=" * 60)
print("CUSTOM EXCEPTIONS")
print("=" * 60)

# =====================================================
# 1. Creating a Custom Exception
# =====================================================

print("\n===== Creating a Custom Exception =====")


class AgeError(Exception):
    """Raised when age is less than 18."""
    pass


try:

    age = 15

    if age < 18:
        raise AgeError("Age must be at least 18.")

    print("Eligible")

except AgeError as error:

    print(error)

# =====================================================
# 2. Bank Balance Exception
# =====================================================

print("\n===== Bank Balance Exception =====")


class InsufficientBalanceError(Exception):
    """Raised when balance is insufficient."""
    pass


balance = 5000
withdraw_amount = 7000

try:

    if withdraw_amount > balance:
        raise InsufficientBalanceError(
            "Insufficient balance."
        )

    print("Withdrawal Successful.")

except InsufficientBalanceError as error:

    print(error)

# =====================================================
# 3. Password Exception
# =====================================================

print("\n===== Password Exception =====")


class PasswordError(Exception):
    """Raised when password is too short."""
    pass


password = "abc123"

try:

    if len(password) < 8:

        raise PasswordError(
            "Password must contain at least 8 characters."
        )

    print("Password Accepted.")

except PasswordError as error:

    print(error)

# =====================================================
# 4. Marks Validation
# =====================================================

print("\n===== Marks Validation =====")


class MarksError(Exception):
    """Raised when marks are invalid."""
    pass


marks = 110

try:

    if marks < 0 or marks > 100:

        raise MarksError(
            "Marks should be between 0 and 100."
        )

    print("Marks Recorded.")

except MarksError as error:

    print(error)

# =====================================================
# 5. Email Validation
# =====================================================

print("\n===== Email Validation =====")


class EmailError(Exception):
    """Raised for invalid email."""
    pass


email = "nikitagmail.com"

try:

    if "@" not in email:

        raise EmailError(
            "Invalid email address."
        )

    print("Email Verified.")

except EmailError as error:

    print(error)

# =====================================================
# 6. Login Validation
# =====================================================

print("\n===== Login Validation =====")


class LoginError(Exception):
    """Raised when username is empty."""
    pass


username = ""

try:

    if username == "":

        raise LoginError(
            "Username cannot be empty."
        )

    print("Login Successful.")

except LoginError as error:

    print(error)

# =====================================================
# 7. Product Stock Validation
# =====================================================

print("\n===== Product Stock Validation =====")


class OutOfStockError(Exception):
    """Raised when product is unavailable."""
    pass


stock = 0

try:

    if stock == 0:

        raise OutOfStockError(
            "Product is out of stock."
        )

    print("Order Confirmed.")

except OutOfStockError as error:

    print(error)

# =====================================================
# 8. Voting Eligibility
# =====================================================

print("\n===== Voting Eligibility =====")


class VotingEligibilityError(Exception):
    """Raised when user is not eligible to vote."""
    pass


age = 16

try:

    if age < 18:

        raise VotingEligibilityError(
            "You are not eligible to vote."
        )

    print("Eligible to Vote.")

except VotingEligibilityError as error:

    print(error)

# =====================================================
# 9. Real-World Example - ATM PIN
# =====================================================

print("\n===== ATM PIN Validation =====")


class InvalidPINError(Exception):
    """Raised for incorrect PIN."""
    pass


entered_pin = "1234"
correct_pin = "5678"

try:

    if entered_pin != correct_pin:

        raise InvalidPINError(
            "Incorrect ATM PIN."
        )

    print("PIN Verified.")

except InvalidPINError as error:

    print(error)

# =====================================================
# 10. Real-World Example - Online Shopping
# =====================================================

print("\n===== Online Shopping =====")


class PaymentError(Exception):
    """Raised when payment fails."""
    pass


payment_success = False

try:

    if not payment_success:

        raise PaymentError(
            "Payment could not be processed."
        )

    print("Order Placed Successfully.")

except PaymentError as error:

    print(error)

# =====================================================
# 11. Best Practices
# =====================================================

# ✔ Create custom exceptions for application-specific errors.
# ✔ Use meaningful exception class names.
# ✔ Inherit custom exceptions from Exception.
# ✔ Keep error messages simple and descriptive.
# ✔ Raise exceptions only when required.
# ✔ Avoid creating unnecessary custom exceptions.

# =====================================================
# 12. Mini Practice
# =====================================================

# Try these yourself:
#
# 1. Create an InvalidAgeError class.
# 2. Create a SalaryError class.
# 3. Create a MobileNumberError class.
# 4. Create a UsernameError class.
# 5. Create a GPAError class.
# 6. Create a ProductPriceError class.
# 7. Create a TemperatureError class.
# 8. Create a BookNotAvailableError class.
# 9. Create a FlightBookingError class.
# 10. Create your own custom exception for any real-world problem.

# =====================================================
# End of Program
# =====================================================

print("\nCongratulations! You completed Custom Exceptions. 🎉")