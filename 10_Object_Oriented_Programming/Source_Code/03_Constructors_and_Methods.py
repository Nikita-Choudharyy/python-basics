"""
=========================================================
Topic : Constructors and Methods
File  : 03_Constructors_and_Methods.py

Description:
This file explains Constructors and Methods in Python.
You will learn how constructors work, why they are used,
how object initialization happens, and different types
of methods used in Object-Oriented Programming.

Topics Covered:
1. What is a Constructor?
2. Why Do We Need Constructors?
3. __init__() Method
4. Default Constructor
5. Parameterized Constructor
6. self Keyword
7. Instance Variables
8. Instance Methods
9. Class Variables
10. Class Methods
11. Static Methods
12. Difference Between Methods
13. Real-World Example

Author : Nikita Choudhary
Repository : Python Basics
=========================================================
"""

# =====================================================
# Constructors and Methods
# =====================================================

print("=" * 60)
print("CONSTRUCTORS AND METHODS")
print("=" * 60)

# =====================================================
# 1. What is a Constructor?
# =====================================================

print("\n===== What is a Constructor? =====")

print(
    "A Constructor is a special method that is "
    "automatically called whenever an object is created."
)

print(
    "\nIt is mainly used to initialize the object's data."
)

# =====================================================
# Syntax
# =====================================================

print("\nSyntax:\n")

print("""
class ClassName:

    def __init__(self):
        pass
""")

# =====================================================
# Simple Example
# =====================================================

print("\n===== Simple Example =====")


class Student:

    def __init__(self):
        print("Constructor Called!")


student1 = Student()

# =====================================================
# Expected Output
# =====================================================

print("\nExpected Output")

print("""
Constructor Called!
""")

# =====================================================
# Explanation
# =====================================================

print("Explanation:")

print(
    "As soon as the Student object is created, "
    "__init__() is called automatically."
)

# =====================================================
# Another Example
# =====================================================

print("\n===== Another Example =====")


class Car:

    def __init__(self):
        print("New Car Object Created!")


car1 = Car()

# =====================================================
# Real-World Example
# =====================================================

print("\n===== Real-World Example =====")

print(
    "Imagine you buy a new mobile phone."
)

print(
    "When you switch it on for the first time, "
    "basic setup happens automatically."
)

print(
    "Similarly, a constructor automatically performs "
    "initialization whenever an object is created."
)

# =====================================================
# Key Points
# =====================================================

print("\nKey Points")

print("✔ Constructor is a special method.")
print("✔ It runs automatically.")
print("✔ It is called when an object is created.")
print("✔ It helps initialize object data.")

# =====================================================
# Remember
# =====================================================

print("\nRemember")

print("✔ Every class can have a constructor.")
print("✔ Constructor name is always __init__().")
print("✔ You never call it directly in normal cases.")

# =====================================================
# 2. Why Do We Need Constructors?
# =====================================================

print("\n===== Why Do We Need Constructors? =====")

print(
    "Constructors help initialize objects automatically "
    "without writing extra code every time."
)

# =====================================================
# Example Without Constructor
# =====================================================

print("\n===== Without Constructor =====")


class Employee:
    pass


employee1 = Employee()

employee1.name = "Nikita"
employee1.department = "AI"

print(employee1.name)
print(employee1.department)

print(
    "\nHere we manually created every attribute after "
    "creating the object."
)

# =====================================================
# Example With Constructor
# =====================================================

print("\n===== With Constructor =====")


class EmployeeData:

    def __init__(self):
        self.name = "Nikita"
        self.department = "AI"


employee2 = EmployeeData()

print(employee2.name)
print(employee2.department)

print(
    "\nThe constructor automatically initialized "
    "the object."
)

# =====================================================
# Key Points
# =====================================================

print("\nKey Points")

print("✔ Saves time.")
print("✔ Reduces repeated code.")
print("✔ Automatically initializes objects.")
print("✔ Makes code clean and readable.")

# =====================================================
# Remember
# =====================================================

print("\nRemember")

print(
    "Without constructors, we would need to assign "
    "values manually after creating every object."
)

# =====================================================
# 3. __init__() Method
# =====================================================

print("\n===== __init__() Method =====")

print(
    "__init__() is the constructor method in Python."
)

print(
    "Python automatically calls this method whenever "
    "a new object is created."
)

# =====================================================
# Syntax
# =====================================================

print("\nSyntax:\n")

print("""
class ClassName:

    def __init__(self):
        # Initialization Code
        pass
""")

# =====================================================
# Example 1
# =====================================================


class Laptop:

    def __init__(self):
        print("Laptop Object Created")


laptop1 = Laptop()

# =====================================================
# Example 2
# =====================================================


class Book:

    def __init__(self):
        print("Book Object Created")


book1 = Book()

# =====================================================
# Explanation
# =====================================================

print("\nExplanation")

print(
    "__init__() executes automatically for every new object."
)

print(
    "Each object gets initialized independently."
)

# =====================================================
# Common Beginner Mistake
# =====================================================

print("\nCommon Beginner Mistake")

print("❌ Calling __init__() directly.")

print(
    "Instead, simply create an object."
)

print("Correct Example")

print("""
student = Student()
""")

# =====================================================
# Remember
# =====================================================

print("\nRemember")

print("✔ __init__() is not a normal method.")
print("✔ It runs automatically.")
print("✔ It initializes every new object.")

# =====================================================
# 4. Default Constructor
# =====================================================

print("\n===== Default Constructor =====")

print(
    "A Default Constructor is a constructor that "
    "does not take any extra arguments except self."
)

# =====================================================
# Syntax
# =====================================================

print("\nSyntax:\n")

print("""
class ClassName:

    def __init__(self):
        pass
""")

# =====================================================
# Example 1
# =====================================================


class Mobile:

    def __init__(self):
        print("Mobile Created Successfully")


mobile1 = Mobile()

# =====================================================
# Example 2
# =====================================================


class ATM:

    def __init__(self):
        print("ATM Object Created")


atm1 = ATM()
atm2 = ATM()

# =====================================================
# Expected Output
# =====================================================

print("\nExpected Output")

print("""
Mobile Created Successfully
ATM Object Created
ATM Object Created
""")

# =====================================================
# Explanation
# =====================================================

print("Explanation")

print(
    "The constructor is executed once for every object."
)

print(
    "Since two ATM objects are created, the constructor "
    "runs two times."
)

# =====================================================
# Key Points
# =====================================================

print("\nKey Points")

print("✔ Accepts only self.")
print("✔ Runs automatically.")
print("✔ Executes once per object.")
print("✔ Used for default initialization.")

# =====================================================
# Remember
# =====================================================

print("\nRemember")

print("✔ Default constructors are simple and easy to use.")
print("✔ They are useful when every object starts with the same initial setup.")

# =====================================================
# 5. Parameterized Constructor
# =====================================================

print("\n===== Parameterized Constructor =====")

print(
    "A Parameterized Constructor accepts additional "
    "arguments along with self."
)

print(
    "It allows us to initialize each object with "
    "different values."
)

# =====================================================
# Syntax
# =====================================================

print("\nSyntax:\n")

print("""
class ClassName:

    def __init__(self, parameter1, parameter2):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
""")

# =====================================================
# Simple Example
# =====================================================

print("\n===== Simple Example =====")


class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age


student1 = Student("Nikita", 20)

print("Name :", student1.name)
print("Age  :", student1.age)

# =====================================================
# Another Example
# =====================================================


class Car:

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model


car1 = Car("Toyota", "Fortuner")
car2 = Car("Hyundai", "Creta")

print("\nCar 1")
print("Brand :", car1.brand)
print("Model :", car1.model)

print("\nCar 2")
print("Brand :", car2.brand)
print("Model :", car2.model)

# =====================================================
# Real-World Example
# =====================================================

print("\n===== Real-World Example =====")

print(
    "Imagine a school where every student has a "
    "different name and age."
)

print(
    "A Parameterized Constructor allows us to provide "
    "different information while creating each object."
)

# =====================================================
# Expected Output
# =====================================================

print("\nExpected Output")

print("""
Name : Nikita
Age  : 20

Car 1
Brand : Toyota
Model : Fortuner

Car 2
Brand : Hyundai
Model : Creta
""")

# =====================================================
# Explanation
# =====================================================

print("Explanation")

print(
    "Every object receives its own values through the "
    "constructor parameters."
)

print(
    "This makes each object unique."
)

# =====================================================
# Key Points
# =====================================================

print("\nKey Points")

print("✔ Accepts additional parameters.")
print("✔ Initializes objects with different values.")
print("✔ Makes objects unique.")
print("✔ Commonly used in real-world applications.")

# =====================================================
# Remember
# =====================================================

print("\nRemember")

print("✔ self is not passed manually.")
print("✔ Only pass the required values while creating an object.")

# =====================================================
# 6. self Keyword
# =====================================================

print("\n===== self Keyword =====")

print(
    "The 'self' keyword represents the current object."
)

print(
    "It is used to access the attributes and methods "
    "of that object."
)

# =====================================================
# Syntax
# =====================================================

print("\nSyntax:\n")

print("""
class Student:

    def __init__(self, name):
        self.name = name
""")

# =====================================================
# Simple Example
# =====================================================


class Employee:

    def __init__(self, name):
        self.name = name


employee1 = Employee("Nikita")

print("Employee Name :", employee1.name)

# =====================================================
# Another Example
# =====================================================


class Mobile:

    def __init__(self, company):
        self.company = company


mobile1 = Mobile("Samsung")
mobile2 = Mobile("Apple")

print("\nMobile 1 :", mobile1.company)
print("Mobile 2 :", mobile2.company)

# =====================================================
# Visual Representation
# =====================================================

print("\n===== Visual Representation =====")

print("""
        Employee Object
        +------------------+
        | name = Nikita    |
        +------------------+
               ▲
               │
          self.name
""")

# =====================================================
# Explanation
# =====================================================

print("Explanation")

print(
    "'self.name' creates an attribute inside the current object."
)

print(
    "Every object has its own separate 'self'."
)

# =====================================================
# Common Beginner Mistake
# =====================================================

print("\nCommon Beginner Mistake")

print("❌ Forgetting to write self as the first parameter.")

print("\nWrong Example")

print("""
class Student:

    def __init__(name):
        pass
""")

print("✔ Correct Example")

print("""
class Student:

    def __init__(self, name):
        self.name = name
""")

# =====================================================
# Key Points
# =====================================================

print("\nKey Points")

print("✔ self refers to the current object.")
print("✔ self is the first parameter of instance methods.")
print("✔ It helps access object data.")
print("✔ Python passes self automatically.")

# =====================================================
# Remember
# =====================================================

print("\nRemember")

print("✔ Do not pass self manually while creating objects.")
print("✔ Python automatically sends the current object.")

# =====================================================
# 7. Instance Variables
# =====================================================

print("\n===== Instance Variables =====")

print(
    "Instance Variables belong to individual objects."
)

print(
    "Every object gets its own separate copy of "
    "instance variables."
)

# =====================================================
# Syntax
# =====================================================

print("\nSyntax:\n")

print("""
class Student:

    def __init__(self, name):
        self.name = name
""")

# =====================================================
# Simple Example
# =====================================================


class Book:

    def __init__(self, title):
        self.title = title


book1 = Book("Python Basics")
book2 = Book("Machine Learning")

print("Book 1 :", book1.title)
print("Book 2 :", book2.title)

# =====================================================
# Another Example
# =====================================================


class Laptop:

    def __init__(self, company, ram):
        self.company = company
        self.ram = ram


laptop1 = Laptop("Dell", "16 GB")
laptop2 = Laptop("HP", "8 GB")

print("\nLaptop 1")
print("Company :", laptop1.company)
print("RAM     :", laptop1.ram)

print("\nLaptop 2")
print("Company :", laptop2.company)
print("RAM     :", laptop2.ram)

# =====================================================
# Explanation
# =====================================================

print("\nExplanation")

print(
    "Although both objects belong to the same class,"
)

print(
    "their instance variables store different values."
)

# =====================================================
# Key Points
# =====================================================

print("\nKey Points")

print("✔ Belong to individual objects.")
print("✔ Created using self.")
print("✔ Store object-specific data.")
print("✔ Each object has its own copy.")

# =====================================================
# Remember
# =====================================================

print("\nRemember")

print("✔ Instance Variables are created inside the constructor.")
print("✔ They are accessed using the object name.")

# =====================================================
# 8. Instance Methods
# =====================================================

print("\n===== Instance Methods =====")

print(
    "An Instance Method is a method that works with "
    "the data of a particular object."
)

print(
    "Instance methods always use 'self' as their "
    "first parameter."
)

# =====================================================
# Syntax
# =====================================================

print("\nSyntax:\n")

print("""
class ClassName:

    def method_name(self):
        pass
""")

# =====================================================
# Simple Example
# =====================================================


class Student:

    def __init__(self, name):
        self.name = name

    def display_name(self):
        print("Student Name :", self.name)


student1 = Student("Nikita")

student1.display_name()

# =====================================================
# Another Example
# =====================================================


class Car:

    def __init__(self, brand):
        self.brand = brand

    def show_brand(self):
        print("Brand :", self.brand)


car1 = Car("Toyota")
car2 = Car("Hyundai")

car1.show_brand()
car2.show_brand()

# =====================================================
# Real-World Example
# =====================================================

print("\n===== Real-World Example =====")

print(
    "Every student has a different name."
)

print(
    "The display_name() method prints the information "
    "of the current student object."
)

# =====================================================
# Explanation
# =====================================================

print("\nExplanation")

print(
    "Inside display_name(), 'self.name' refers to the "
    "name of the object that calls the method."
)

print(
    "When student1.display_name() is executed,"
)

print(
    "'self' automatically refers to student1."
)

# =====================================================
# Key Points
# =====================================================

print("\nKey Points")

print("✔ Instance methods belong to objects.")
print("✔ They always use self.")
print("✔ They can access instance variables.")
print("✔ Different objects use the same method with different data.")

# =====================================================
# Remember
# =====================================================

print("\nRemember")

print("✔ Call instance methods using an object.")
print("✔ Python automatically passes self.")

# =====================================================
# 9. Class Variables
# =====================================================

print("\n===== Class Variables =====")

print(
    "A Class Variable is shared by all objects "
    "of the class."
)

# =====================================================
# Syntax
# =====================================================

print("\nSyntax:\n")

print("""
class ClassName:

    class_variable = value
""")

# =====================================================
# Simple Example
# =====================================================


class Student:

    school_name = "ABC Public School"

    def __init__(self, name):
        self.name = name


student1 = Student("Nikita")
student2 = Student("Rahul")

print("Student 1 School :", student1.school_name)
print("Student 2 School :", student2.school_name)

# =====================================================
# Modifying Class Variable
# =====================================================

print("\n===== Modifying Class Variable =====")

Student.school_name = "XYZ Public School"

print(student1.school_name)
print(student2.school_name)

# =====================================================
# Real-World Example
# =====================================================

print("\n===== Real-World Example =====")

print(
    "Every student belongs to the same school."
)

print(
    "Instead of storing the school name in every object,"
)

print(
    "we store it once as a Class Variable."
)

# =====================================================
# Key Points
# =====================================================

print("\nKey Points")

print("✔ Shared by every object.")
print("✔ Declared inside the class.")
print("✔ Saves memory.")
print("✔ Best for common data.")

# =====================================================
# Remember
# =====================================================

print("\nRemember")

print("✔ Use Class Variables only for shared information.")

# =====================================================
# 10. Class Methods
# =====================================================

print("\n===== Class Methods =====")

print(
    "A Class Method works with Class Variables "
    "instead of individual objects."
)

print(
    "It uses the @classmethod decorator."
)

print(
    "The first parameter is 'cls', which refers "
    "to the class."
)

# =====================================================
# Syntax
# =====================================================

print("\nSyntax:\n")

print("""
class ClassName:

    @classmethod
    def method_name(cls):
        pass
""")

# =====================================================
# Example
# =====================================================


class Student:

    school_name = "ABC Public School"

    @classmethod
    def display_school(cls):
        print("School :", cls.school_name)


Student.display_school()

# =====================================================
# Another Example
# =====================================================


class Company:

    company_name = "OpenAI"

    @classmethod
    def show_company(cls):
        print("Company :", cls.company_name)


Company.show_company()

# =====================================================
# Explanation
# =====================================================

print("\nExplanation")

print(
    "'cls' refers to the class itself."
)

print(
    "A Class Method can directly access "
    "Class Variables."
)

# =====================================================
# Key Points
# =====================================================

print("\nKey Points")

print("✔ Uses @classmethod.")
print("✔ First parameter is cls.")
print("✔ Works with Class Variables.")
print("✔ Can be called using the class name.")

# =====================================================
# Remember
# =====================================================

print("\nRemember")

print("✔ Use Class Methods when working with class-level data.")

# =====================================================
# 11. Static Methods
# =====================================================

print("\n===== Static Methods =====")

print(
    "A Static Method does not work with object data "
    "or class data."
)

print(
    "It is placed inside the class only because "
    "it is logically related to the class."
)

# =====================================================
# Syntax
# =====================================================

print("\nSyntax:\n")

print("""
class ClassName:

    @staticmethod
    def method_name():
        pass
""")

# =====================================================
# Example 1
# =====================================================


class Calculator:

    @staticmethod
    def add(a, b):
        return a + b


print("Addition :", Calculator.add(10, 20))

# =====================================================
# Example 2
# =====================================================


class Temperature:

    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return (celsius * 9 / 5) + 32


print("37°C =", Temperature.celsius_to_fahrenheit(37), "°F")

# =====================================================
# Real-World Example
# =====================================================

print("\n===== Real-World Example =====")

print(
    "A calculator performs calculations."
)

print(
    "Addition does not depend on any specific object "
    "or class variable."
)

print(
    "Therefore, add() is a Static Method."
)

# =====================================================
# Key Points
# =====================================================

print("\nKey Points")

print("✔ Uses @staticmethod.")
print("✔ No self parameter.")
print("✔ No cls parameter.")
print("✔ Cannot directly access Instance Variables.")
print("✔ Cannot directly access Class Variables.")

# =====================================================
# Remember
# =====================================================

print("\nRemember")

print("✔ Use Static Methods for utility functions.")
print("✔ Static Methods improve code organization.")

# =====================================================
# 12. Difference Between Instance, Class and Static Methods
# =====================================================

print("\n===== Difference Between Methods =====")

comparison = [
    ("First Parameter", "self", "cls", "None"),
    ("Decorator", "None", "@classmethod", "@staticmethod"),
    ("Works With", "Object Data", "Class Data", "Independent Logic"),
    ("Access Instance Variables", "Yes", "No", "No"),
    ("Access Class Variables", "Yes", "Yes", "No (Directly)"),
    ("Called Using", "Object", "Class / Object", "Class / Object"),
    ("Main Purpose", "Object Behavior", "Class Behavior", "Utility Function")
]

print(
    f"{'Feature':<28}"
    f"{'Instance':<18}"
    f"{'Class':<18}"
    f"{'Static'}"
)

print("-" * 82)

for feature, instance, class_method, static in comparison:
    print(
        f"{feature:<28}"
        f"{instance:<18}"
        f"{class_method:<18}"
        f"{static}"
    )

# =====================================================
# 13. Real-World Example
# =====================================================

print("\n===== Real-World Example =====")


class BankAccount:

    bank_name = "ABC Bank"

    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def display_account(self):
        print("\nAccount Holder :", self.account_holder)
        print("Balance        :", self.balance)

    @classmethod
    def display_bank(cls):
        print("\nBank Name :", cls.bank_name)

    @staticmethod
    def bank_rules():
        print("\nMinimum balance should be maintained.")
        print("Carry a valid ID proof while visiting the bank.")


account1 = BankAccount("Nikita", 50000)

account1.display_account()

BankAccount.display_bank()

BankAccount.bank_rules()

print("\nExplanation")

print("display_account() works with object data.")
print("display_bank() works with class data.")
print("bank_rules() works independently.")

# =====================================================
# 14. Common Mistakes
# =====================================================

print("\n===== Common Mistakes =====")

mistakes = [
    "Forgetting to write self in Instance Methods.",
    "Forgetting to write cls in Class Methods.",
    "Using self inside Static Methods.",
    "Calling Instance Methods without creating an object.",
    "Confusing Class Variables with Instance Variables.",
    "Using Static Methods when object data is required.",
    "Creating unnecessary constructors."
]

for index, mistake in enumerate(mistakes, start=1):
    print(f"{index}. {mistake}")

# =====================================================
# 15. Interview Questions
# =====================================================

print("\n===== Interview Questions =====")

questions = [
    "What is a Constructor?",
    "Why is __init__() used?",
    "What is the purpose of self?",
    "What is the difference between self and cls?",
    "What are Instance Variables?",
    "What are Class Variables?",
    "What is an Instance Method?",
    "What is a Class Method?",
    "What is a Static Method?",
    "When should we use @classmethod?",
    "When should we use @staticmethod?",
    "Differentiate Instance, Class and Static Methods."
]

for index, question in enumerate(questions, start=1):
    print(f"{index}. {question}")

# =====================================================
# 16. Best Practices
# =====================================================

print("\n===== Best Practices =====")

best_practices = [
    "Use meaningful class names.",
    "Keep constructors simple.",
    "Initialize required data inside __init__().",
    "Use Instance Variables for object-specific data.",
    "Use Class Variables only for shared data.",
    "Use Class Methods for class-level operations.",
    "Use Static Methods for utility functions.",
    "Follow PEP 8 naming conventions.",
    "Write clean and readable methods."
]

for practice in best_practices:
    print(f"✔ {practice}")

# =====================================================
# 17. Mini Practice
# =====================================================

print("\n===== Mini Practice =====")

practice_questions = [
    "Create a Student class with a constructor.",
    "Create three Student objects.",
    "Create an Employee class with name and salary.",
    "Create an Instance Method to display employee details.",
    "Create a Class Variable named company.",
    "Create a Class Method to display the company name.",
    "Create a Static Method to calculate GST.",
    "Identify Instance Variables and Class Variables.",
    "Explain the role of self.",
    "Explain the role of cls."
]

for index, question in enumerate(practice_questions, start=1):
    print(f"{index}. {question}")

# =====================================================
# 18. Coding Challenge
# =====================================================

print("\n===== Coding Challenge =====")

print("Challenge 1")
print("- Create a BankAccount class.")

print("\nChallenge 2")
print("- Create a constructor with account holder and balance.")

print("\nChallenge 3")
print("- Create an Instance Method to display account details.")

print("\nChallenge 4")
print("- Create a Class Variable named bank_name.")

print("\nChallenge 5")
print("- Create a Class Method to display the bank name.")

print("\nChallenge 6")
print("- Create a Static Method to display bank rules.")

# =====================================================
# 19. Output Prediction
# =====================================================

print("\n===== Output Prediction =====")

print("Predict the output before running the code.\n")

print("""
class Student:

    def __init__(self):
        print("Constructor Called")

student1 = Student()
student2 = Student()
""")

print("Expected Output")

print("""
Constructor Called
Constructor Called
""")

print("Reason")

print(
    "The constructor is executed every time a new object "
    "is created."
)

# =====================================================
# Quick Revision
# =====================================================

print("\n===== Quick Revision =====")

revision = [
    "Constructor initializes objects.",
    "__init__() is called automatically.",
    "self represents the current object.",
    "Instance Variables belong to objects.",
    "Class Variables are shared.",
    "Instance Methods work with object data.",
    "Class Methods work with class data.",
    "Static Methods are utility methods."
]

for point in revision:
    print(f"✔ {point}")

# =====================================================
# Summary
# =====================================================

print("\n===== Summary =====")

print("✔ Constructors initialize objects automatically.")
print("✔ __init__() is Python's constructor.")
print("✔ self refers to the current object.")
print("✔ cls refers to the current class.")
print("✔ Instance Variables store object-specific data.")
print("✔ Class Variables store shared data.")
print("✔ Instance Methods work with objects.")
print("✔ Class Methods work with class-level data.")
print("✔ Static Methods perform utility tasks.")
print("✔ Constructors and Methods are the core of Python OOP.")

# =====================================================
# End of Program
# =====================================================

print("\nCongratulations! 🎉")
print("You have successfully completed")
print("Constructors and Methods.")