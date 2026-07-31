"""
=========================================================
Topic : Encapsulation
File  : 04_Encapsulation.py

Description:
This file explains the concept of Encapsulation in
Python Object-Oriented Programming. You will learn
how data and methods are combined into a single unit,
different access levels, and how encapsulation helps
protect object data.

Topics Covered:
1. What is Encapsulation?
2. Why Do We Need Encapsulation?
3. Public Members
4. Protected Members
5. Private Members
6. Name Mangling
7. Getters and Setters
8. Benefits of Encapsulation
9. Difference Between Public, Protected and Private
10. Real-World Example

Author : Nikita Choudhary
Repository : Python Basics
=========================================================
"""

# =====================================================
# Encapsulation
# =====================================================

print("=" * 60)
print("ENCAPSULATION")
print("=" * 60)

# =====================================================
# 1. What is Encapsulation?
# =====================================================

print("\n===== What is Encapsulation? =====")

print(
    "Encapsulation is one of the four main principles "
    "of Object-Oriented Programming (OOP)."
)

print(
    "\nIt is the process of combining data (variables) "
    "and methods (functions) into a single unit called a class."
)

print(
    "\nEncapsulation also helps control how object data "
    "is accessed and modified."
)

# =====================================================
# Syntax
# =====================================================

print("\nSyntax:\n")

print("""
class ClassName:

    def __init__(self):
        self.variable = value

    def method_name(self):
        pass
""")

# =====================================================
# Simple Example
# =====================================================


class Student:

    def __init__(self):
        self.name = "Nikita"

    def display(self):
        print("Student Name :", self.name)


student1 = Student()

student1.display()

# Output:
# Student Name : Nikita

# =====================================================
# Another Example
# =====================================================


class Car:

    def __init__(self):
        self.brand = "Toyota"

    def show_brand(self):
        print("Brand :", self.brand)


car1 = Car()

car1.show_brand()

# Output:
# Brand : Toyota

# =====================================================
# Real-World Example
# =====================================================

print("\n===== Real-World Example =====")

print(
    "Think about a mobile phone."
)

print(
    "A mobile phone stores data such as contacts, "
    "photos, and messages."
)

print(
    "It also provides features like calling, messaging, "
    "and taking photos."
)

print(
    "\nThe data and the features are packaged together "
    "inside one device."
)

print(
    "Similarly, a class stores both variables and "
    "methods together. This is called Encapsulation."
)

# =====================================================
# Explanation
# =====================================================

print("\nExplanation")

print(
    "In the Student class, 'name' is the data and "
    "'display()' is the method."
)

print(
    "Both are placed inside the same class."
)

print(
    "This is the basic idea of Encapsulation."
)

# =====================================================
# Key Points
# =====================================================

print("\nKey Points")

print("✔ Encapsulation combines data and methods.")
print("✔ A class acts as a single unit.")
print("✔ It improves code organization.")
print("✔ It helps protect object data.")

# =====================================================
# Important Note
# =====================================================

print("\nImportant Note")

print(
    "Encapsulation is not only about hiding data."
)

print(
    "It also means keeping related data and methods "
    "together inside one class."
)

# =====================================================
# Remember
# =====================================================

print("\nRemember")

print("✔ Encapsulation = Data + Methods.")
print("✔ Everything is organized inside a class.")

# =====================================================
# 2. Why Do We Need Encapsulation?
# =====================================================

print("\n===== Why Do We Need Encapsulation? =====")

print(
    "Encapsulation helps make programs secure, "
    "organized, and easier to maintain."
)

# =====================================================
# Benefits
# =====================================================

benefits = [
    "Protect important data",
    "Improve code readability",
    "Reduce accidental modification",
    "Increase code reusability",
    "Make maintenance easier",
    "Improve data management"
]

print("\nBenefits:")

for benefit in benefits:
    print(f"✔ {benefit}")

# =====================================================
# Real-World Example
# =====================================================

print("\n===== Real-World Example =====")

print(
    "Imagine an ATM machine."
)

print(
    "You can withdraw money, check your balance, "
    "and deposit money."
)

print(
    "However, you cannot directly change the bank's "
    "database from the ATM."
)

print(
    "The ATM allows only specific operations."
)

print(
    "This is a simple example of Encapsulation."
)

# =====================================================
# Explanation
# =====================================================

print("\nExplanation")

print(
    "Encapsulation controls how data is accessed."
)

print(
    "Users interact through methods instead of "
    "changing important data directly."
)

# =====================================================
# Key Points
# =====================================================

print("\nKey Points")

print("✔ Improves security.")
print("✔ Prevents accidental changes.")
print("✔ Makes programs easier to maintain.")
print("✔ Keeps related code together.")

# =====================================================
# Remember
# =====================================================

print("\nRemember")

print(
    "Encapsulation controls access to object data "
    "while keeping the code organized."
)

# =====================================================
# 3. Public Members
# =====================================================

print("\n===== Public Members =====")

print(
    "Public Members are variables and methods that "
    "can be accessed from anywhere."
)

print(
    "By default, every variable and method in Python "
    "is public."
)

# =====================================================
# Syntax
# =====================================================

print("\nSyntax:\n")

print("""
class ClassName:

    def __init__(self):
        self.variable = value
""")

# =====================================================
# Simple Example
# =====================================================


class Student:

    def __init__(self, name):
        self.name = name

    def display(self):
        print("Student Name :", self.name)


student1 = Student("Nikita")

student1.display()

print(student1.name)

# Output:
# Student Name : Nikita
# Nikita

# =====================================================
# Another Example
# =====================================================


class Book:

    def __init__(self, title):
        self.title = title

    def show_title(self):
        print("Book :", self.title)


book1 = Book("Python Basics")

book1.show_title()

print(book1.title)

# Output:
# Book : Python Basics
# Python Basics

# =====================================================
# Explanation
# =====================================================

print("\nExplanation")

print(
    "The 'name' and 'title' variables are public."
)

print(
    "They can be accessed directly using the object."
)

# =====================================================
# Key Points
# =====================================================

print("\nKey Points")

print("✔ Accessible from anywhere.")
print("✔ No special symbol is used.")
print("✔ Default access level in Python.")
print("✔ Easy to use.")

# =====================================================
# Important Note
# =====================================================

print("\nImportant Note")

print(
    "Python does not have strict public access modifiers."
)

print(
    "If no underscore (_) is used, the member is considered public."
)

# =====================================================
# Remember
# =====================================================

print("\nRemember")

print("✔ Public Members can be accessed directly.")
print("✔ They are suitable for information that does not need protection.")

# =====================================================
# 4. Protected Members
# =====================================================

print("\n===== Protected Members =====")

print(
    "Protected Members are intended to be used within "
    "the class and its subclasses."
)

print(
    "In Python, a Protected Member is created using "
    "a single underscore (_)."
)

print(
    "It is a naming convention that tells programmers "
    "that the member should not be accessed directly "
    "from outside the class."
)

# =====================================================
# Syntax
# =====================================================

print("\nSyntax:\n")

print("""
class ClassName:

    def __init__(self):
        self._variable = value
""")

# =====================================================
# Simple Example
# =====================================================


class BankAccount:

    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self._balance = balance

    def display_balance(self):
        print("Balance :", self._balance)


account1 = BankAccount("Nikita", 50000)

account1.display_balance()

print(account1._balance)

# Output:
# Balance : 50000
# 50000

# =====================================================
# Another Example
# =====================================================


class Employee:

    def __init__(self, name, salary):
        self.name = name
        self._salary = salary

    def display_salary(self):
        print("Salary :", self._salary)


employee1 = Employee("Rahul", 60000)

employee1.display_salary()

print(employee1._salary)

# Output:
# Salary : 60000
# 60000

# =====================================================
# Real-World Example
# =====================================================

print("\n===== Real-World Example =====")

print(
    "Imagine an office."
)

print(
    "Employees can view some internal information,"
)

print(
    "but outsiders are expected not to access it."
)

print(
    "Similarly, Protected Members are intended "
    "for internal use."
)

# =====================================================
# Explanation
# =====================================================

print("\nExplanation")

print(
    "The variable '_balance' starts with a single underscore."
)

print(
    "This is only a convention."
)

print(
    "Python still allows direct access to the variable."
)

# =====================================================
# Key Points
# =====================================================

print("\nKey Points")

print("✔ Starts with a single underscore (_).")
print("✔ Intended for internal use.")
print("✔ Can still be accessed from outside.")
print("✔ Follows Python naming conventions.")

# =====================================================
# Important Note
# =====================================================

print("\nImportant Note")

print(
    "Protected Members are NOT truly protected."
)

print(
    "The single underscore only tells other developers:"
)

print('"Please do not access this member directly."')

# =====================================================
# Remember
# =====================================================

print("\nRemember")

print("✔ Protected = Convention, not restriction.")
print("✔ Python trusts the programmer.")

# =====================================================
# 5. Private Members
# =====================================================

print("\n===== Private Members =====")

print(
    "Private Members are created using double underscores (__)."
)

print(
    "Python uses Name Mangling to make these members "
    "harder to access directly."
)

print(
    "Private Members are mainly used to prevent "
    "accidental access from outside the class."
)

# =====================================================
# Syntax
# =====================================================

print("\nSyntax:\n")

print("""
class ClassName:

    def __init__(self):
        self.__variable = value
""")

# =====================================================
# Simple Example
# =====================================================


class BankAccount:

    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.__balance = balance

    def display_balance(self):
        print("Balance :", self.__balance)


account1 = BankAccount("Nikita", 50000)

account1.display_balance()

# Output:
# Balance : 50000

# =====================================================
# Accessing Private Member Directly
# =====================================================

print("\n===== Accessing Private Member Directly =====")

print("""
print(account1.__balance)
""")

print(
    "\nThis code will raise an error because "
    "__balance cannot be accessed directly."
)

print("\nExpected Error")

print("""
AttributeError:
'BankAccount' object has no attribute '__balance'
""")

# =====================================================
# Another Example
# =====================================================


class Student:

    def __init__(self):
        self.__roll_number = 101

    def show_roll_number(self):
        print("Roll Number :", self.__roll_number)


student1 = Student()

student1.show_roll_number()

# Output:
# Roll Number : 101

# =====================================================
# Real-World Example
# =====================================================

print("\n===== Real-World Example =====")

print(
    "Think about your ATM PIN."
)

print(
    "You can use your PIN to withdraw money,"
)

print(
    "but the banking system does not allow everyone "
    "to view your PIN directly."
)

print(
    "Private Members work in a similar way."
)

# =====================================================
# Explanation
# =====================================================

print("\nExplanation")

print(
    "Private Members use double underscores (__)."
)

print(
    "Python internally changes their names using "
    "Name Mangling."
)

print(
    "This reduces accidental direct access."
)

# =====================================================
# Key Points
# =====================================================

print("\nKey Points")

print("✔ Starts with double underscores (__).")
print("✔ Uses Name Mangling.")
print("✔ Reduces accidental access.")
print("✔ Access is usually provided through methods.")

# =====================================================
# Important Note
# =====================================================

print("\nImportant Note")

print(
    "Private does NOT mean completely inaccessible."
)

print(
    "Python changes the variable name internally."
)

print(
    "In the next section, we will learn how "
    "Name Mangling actually works."
)

# =====================================================
# Remember
# =====================================================

print("\nRemember")

print("✔ _variable  → Protected (Convention)")
print("✔ __variable → Private (Name Mangling)")

# =====================================================
# 6. Name Mangling
# =====================================================

print("\n===== Name Mangling =====")

print(
    "Name Mangling is a mechanism used by Python for "
    "Private Members."
)

print(
    "When a variable starts with double underscores (__), "
    "Python internally changes its name."
)

print(
    "This helps prevent accidental direct access "
    "to Private Members."
)

# =====================================================
# Syntax
# =====================================================

print("\nSyntax:\n")

print("""
class ClassName:

    def __init__(self):
        self.__variable = value
""")

# =====================================================
# Simple Example
# =====================================================


class Student:

    def __init__(self):
        self.__name = "Nikita"

    def display(self):
        print("Name :", self.__name)


student1 = Student()

student1.display()

# Output:
# Name : Nikita

# =====================================================
# Trying Direct Access
# =====================================================

print("\n===== Trying Direct Access =====")

print("""
print(student1.__name)
""")

print(
    "\nResult:"
)

print(
    "AttributeError because Python changes "
    "the variable name internally."
)

# =====================================================
# Accessing Name Mangled Variable
# =====================================================

print("\n===== Accessing Name Mangled Variable =====")


class Employee:

    def __init__(self):
        self.__salary = 50000


employee1 = Employee()

print(employee1._Employee__salary)

# Output:
# 50000

# =====================================================
# Explanation
# =====================================================

print("\nExplanation")

print(
    "Python internally converts:"
)

print("__salary")

print("\ninto")

print("_Employee__salary")

print(
    "\nThis process is called Name Mangling."
)

print(
    "Its main purpose is to reduce accidental access "
    "or accidental overriding."
)

# =====================================================
# Real-World Example
# =====================================================

print("\n===== Real-World Example =====")

print(
    "Imagine an office locker."
)

print(
    "The locker has a unique internal identification "
    "number that employees normally do not use."
)

print(
    "Similarly, Python internally changes the variable "
    "name to reduce accidental access."
)

# =====================================================
# Key Points
# =====================================================

print("\nKey Points")

print("✔ Works only for Private Members.")
print("✔ Uses double underscores (__).")
print("✔ Changes the variable name internally.")
print("✔ Prevents accidental access.")
print("✔ Prevents accidental overriding in subclasses.")

# =====================================================
# Important Note
# =====================================================

print("\nImportant Note")

print(
    "Name Mangling is NOT true security."
)

print(
    "It simply makes accidental access more difficult."
)

print(
    "The variable can still be accessed if you know "
    "its mangled name."
)

# =====================================================
# Remember
# =====================================================

print("\nRemember")

print("__name becomes _ClassName__name internally.")

# =====================================================
# 7. Getters and Setters
# =====================================================

print("\n===== Getters and Setters =====")

print(
    "Getters and Setters are methods used to "
    "access and modify Private Members safely."
)

print(
    "Instead of accessing a Private Variable directly,"
)

print(
    "we use methods to read or update its value."
)

# =====================================================
# Simple Example
# =====================================================


class BankAccount:

    def __init__(self, balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def set_balance(self, balance):
        self.__balance = balance


account1 = BankAccount(50000)

print("Current Balance :", account1.get_balance())

account1.set_balance(75000)

print("Updated Balance :", account1.get_balance())

# Output:
# Current Balance : 50000
# Updated Balance : 75000

# =====================================================
# Another Example
# =====================================================


class Student:

    def __init__(self):
        self.__marks = 0

    def get_marks(self):
        return self.__marks

    def set_marks(self, marks):
        self.__marks = marks


student1 = Student()

student1.set_marks(95)

print("Marks :", student1.get_marks())

# Output:
# Marks : 95

# =====================================================
# Real-World Example
# =====================================================

print("\n===== Real-World Example =====")

print(
    "Think about an ATM."
)

print(
    "You cannot directly change your account balance."
)

print(
    "Instead, you use banking operations like deposit "
    "or withdraw."
)

print(
    "Similarly, Setters control how data is modified."
)

# =====================================================
# Explanation
# =====================================================

print("\nExplanation")

print(
    "Getter methods return Private Data."
)

print(
    "Setter methods update Private Data."
)

print(
    "This gives better control over object data."
)

# =====================================================
# Key Points
# =====================================================

print("\nKey Points")

print("✔ Getter reads Private Data.")
print("✔ Setter updates Private Data.")
print("✔ Improves data protection.")
print("✔ Gives controlled access.")

# =====================================================
# Important Note
# =====================================================

print("\nImportant Note")

print(
    "A Setter can also validate data before storing it."
)

print(
    "This helps prevent invalid values."
)

# =====================================================
# Remember
# =====================================================

print("\nRemember")

print("✔ Getter = Read Data")
print("✔ Setter = Update Data")

# =====================================================
# 8. Benefits of Encapsulation
# =====================================================

print("\n===== Benefits of Encapsulation =====")

benefits = [
    "Protects important data.",
    "Reduces accidental modification.",
    "Improves code organization.",
    "Makes programs easier to maintain.",
    "Improves code reusability.",
    "Provides controlled access to data.",
    "Makes debugging easier.",
    "Improves software reliability."
]

for benefit in benefits:
    print(f"✔ {benefit}")

# =====================================================
# Explanation
# =====================================================

print("\nExplanation")

print(
    "Encapsulation groups related data and methods "
    "inside a class."
)

print(
    "It also controls how important data is accessed "
    "or modified."
)

# =====================================================
# Remember
# =====================================================

print("\nRemember")

print("✔ Encapsulation improves both security and organization.")
print("✔ It is one of the most important principles of OOP.")

# =====================================================
# 9. Difference Between Public, Protected and Private
# =====================================================

print("\n===== Difference Between Public, Protected and Private =====")

comparison = [
    ("Prefix", "variable", "_variable", "__variable"),
    ("Access Level", "Anywhere", "Class & Subclass", "Inside Class"),
    ("Naming Convention", "None", "Single Underscore", "Double Underscore"),
    ("Direct Access", "Yes", "Yes (Not Recommended)", "No (Directly)"),
    ("Purpose", "General Access", "Internal Use", "Data Protection"),
]

print(
    f"{'Feature':<22}"
    f"{'Public':<22}"
    f"{'Protected':<24}"
    f"{'Private'}"
)

print("-" * 90)

for feature, public, protected, private in comparison:
    print(
        f"{feature:<22}"
        f"{public:<22}"
        f"{protected:<24}"
        f"{private}"
    )

# =====================================================
# 10. Real-World Example
# =====================================================

print("\n===== Real-World Example =====")


class BankAccount:

    bank_name = "ABC Bank"          # Public Class Variable

    def __init__(self, name, balance, pin):
        self.name = name            # Public Member
        self._balance = balance     # Protected Member
        self.__pin = pin            # Private Member

    def display_details(self):
        print("Account Holder :", self.name)
        print("Balance        :", self._balance)

    def verify_pin(self, pin):
        if pin == self.__pin:
            print("PIN Verified Successfully.")
        else:
            print("Incorrect PIN.")


account1 = BankAccount("Nikita", 50000, 1234)

account1.display_details()

account1.verify_pin(1234)

# Output:
# Account Holder : Nikita
# Balance        : 50000
# PIN Verified Successfully.

print("\nExplanation")

print("name          → Public Member")
print("_balance      → Protected Member")
print("__pin         → Private Member")

# =====================================================
# 11. Common Mistakes
# =====================================================

print("\n===== Common Mistakes =====")

mistakes = [
    "Thinking Protected Members are completely protected.",
    "Thinking Private Members cannot be accessed at all.",
    "Accessing Private Members directly.",
    "Using Public Members for sensitive information.",
    "Confusing Protected and Private Members.",
    "Ignoring Getters and Setters when validation is required.",
    "Using double underscores everywhere unnecessarily."
]

for index, mistake in enumerate(mistakes, start=1):
    print(f"{index}. {mistake}")

# =====================================================
# 12. Interview Questions
# =====================================================

print("\n===== Interview Questions =====")

questions = [
    "What is Encapsulation?",
    "Why is Encapsulation important?",
    "What are Public Members?",
    "What are Protected Members?",
    "What are Private Members?",
    "What is Name Mangling?",
    "Why does Python use Name Mangling?",
    "What are Getters and Setters?",
    "Difference between Public, Protected and Private Members?",
    "Does Python support true data hiding?"
]

for index, question in enumerate(questions, start=1):
    print(f"{index}. {question}")

# =====================================================
# 13. Best Practices
# =====================================================

print("\n===== Best Practices =====")

best_practices = [
    "Keep sensitive data private.",
    "Use Protected Members only for internal use.",
    "Use Public Members only when appropriate.",
    "Use Getters and Setters for controlled access.",
    "Validate data before updating it.",
    "Keep methods short and meaningful.",
    "Follow Python naming conventions.",
    "Write clean and readable code."
]

for practice in best_practices:
    print(f"✔ {practice}")

# =====================================================
# 14. Mini Practice
# =====================================================

print("\n===== Mini Practice =====")

practice_questions = [
    "Create a Student class with one Public Member.",
    "Create an Employee class with one Protected Member.",
    "Create a BankAccount class with one Private Member.",
    "Create a Getter Method.",
    "Create a Setter Method.",
    "Access a Public Member.",
    "Try accessing a Private Member directly.",
    "Explain the purpose of Name Mangling.",
    "Differentiate Public and Private Members.",
    "Differentiate Protected and Private Members."
]

for index, question in enumerate(practice_questions, start=1):
    print(f"{index}. {question}")

# =====================================================
# 15. Coding Challenge
# =====================================================

print("\n===== Coding Challenge =====")

print("Challenge 1")
print("- Create a BankAccount class.")

print("\nChallenge 2")
print("- Add account_holder as a Public Member.")

print("\nChallenge 3")
print("- Add balance as a Protected Member.")

print("\nChallenge 4")
print("- Add pin as a Private Member.")

print("\nChallenge 5")
print("- Create Getter and Setter methods for the PIN.")

print("\nChallenge 6")
print("- Verify the PIN before displaying account details.")

# =====================================================
# 16. Output Prediction
# =====================================================

print("\n===== Output Prediction =====")

print("Predict the output before running the code.\n")

print("""
class Student:

    def __init__(self):
        self.__name = "Nikita"

student = Student()

print(student.__name)
""")

print("\nExpected Result")

print("AttributeError")

print("\nReason")

print(
    "The variable '__name' is a Private Member."
)

print(
    "Python performs Name Mangling, so direct access "
    "using '__name' is not allowed."
)

# =====================================================
# Quick Revision
# =====================================================

print("\n===== Quick Revision =====")

revision = [
    "Encapsulation combines data and methods.",
    "Public Members are accessible everywhere.",
    "Protected Members use a single underscore (_).",
    "Private Members use double underscores (__).",
    "Private Members use Name Mangling.",
    "Getters read Private Data.",
    "Setters update Private Data.",
    "Encapsulation improves data protection."
]

for point in revision:
    print(f"✔ {point}")

# =====================================================
# Summary
# =====================================================

print("\n===== Summary =====")

print("✔ Encapsulation combines data and methods.")
print("✔ Public Members are accessible from anywhere.")
print("✔ Protected Members use a single underscore (_).")
print("✔ Private Members use double underscores (__).")
print("✔ Python uses Name Mangling for Private Members.")
print("✔ Getters and Setters provide controlled access.")
print("✔ Encapsulation improves code organization.")
print("✔ Encapsulation helps protect important data.")

# =====================================================
# End of Program
# =====================================================

print("\nCongratulations! 🎉")
print("You have successfully completed")
print("Encapsulation.")