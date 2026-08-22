# ============================
# 🧮 Python Calculator
# ============================

def add(a,b):
    """Return the sum of two numbers."""
    return a + b

def subtract(a,b):
    """Return the difference of two numbers."""
    return a - b

def multiply(a,b):
    """Return the product of two numbers."""
    return a * b

def divide(a,b):
    """Return the division of two numbers."""
    return a / b

def modulus(a,b):
    """Return the remainder of two numbers."""
    return a % b

def display_menu():
    """Display the calculator menu."""

    print("\n" + "=" * 30)
    print("     PYTHON CALCULATOR  ")
    print("=" * 30)

    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Exit")
    print("=" * 30)

def main():
    """Run the calculator program."""

    while True:
        display_menu()

        choice = input("Enter your choice :")

        if choice == "6":
            print("\nThank you for using the calculator!")
            break

        if choice not in {"1","2","3","4","5"}:
            print("\n❌ Invalid choice. Please select a valid option.")
            continue

        try:

            num1 = float(input("Enter first number :"))
            num2 = float(input("Enter second number :"))

            if choice == "1":
                result = add(num1,num2)

            elif choice == "2":
                result = subtract(num1,num2)

            elif choice == "3":
                result = multiply(num1,num2)

            elif choice == "4":
                if num2 == 0:
                    print("\n❌ Error : Cannot divide by zero.")
                    continue

                result = divide(num1,num2)

            elif choice == "5":
                if num2 == 0:
                    print("\n❌ Error : Cannot perform modulus by zero.")
                    continue
                
                result = modulus(num1,num2)

            print(f"\n✅ Result: {result}")

        except ValueError:
            print("\n❌ Invalid input. Please enter numbers only.")

        except Exception as error:
            print(f"\n❌ An unexpected error occurred: {error}")


if __name__ == "__main__":
    main()