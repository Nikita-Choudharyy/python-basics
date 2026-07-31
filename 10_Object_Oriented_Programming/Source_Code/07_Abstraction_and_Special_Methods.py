"""
=========================================================
Topic : Abstraction and Special Methods
File  : 07_Abstraction_and_Special_Methods.py

Description:
This file explains the concept of Abstraction and
Special (Magic/Dunder) Methods in Python.

You will learn how to hide implementation details,
create abstract classes, use abstract methods,
and understand Python's built-in special methods.

Topics Covered:

Part A : Abstraction

1. What is Abstraction?
2. Why Do We Need Abstraction?
3. Abstract Class
4. Abstract Method
5. abc Module
6. @abstractmethod Decorator
7. Creating Your First Abstract Class
8. Rules of Abstract Classes
9. Advantages of Abstraction
10. Difference Between Abstraction and Encapsulation

Part B : Special Methods

11. What are Special Methods?
12. __init__()
13. __str__()
14. __repr__()
15. __len__()
16. __add__()
17. __eq__()
18. Other Common Special Methods

Part C

19. Real-World Example
20. Common Mistakes
21. Interview Questions
22. Best Practices
23. Mini Practice
24. Coding Challenge
25. Output Prediction
26. Summary

Author : Nikita Choudhary
Repository : Python Basics
=========================================================
"""

from abc import ABC, abstractmethod

# =====================================================
# Abstraction
# =====================================================

print("=" * 60)
print("ABSTRACTION")
print("=" * 60)

# =====================================================
# 1. What is Abstraction?
# =====================================================

print("\n===== What is Abstraction? =====")

print(
    "Abstraction is one of the four main principles "
    "of Object-Oriented Programming (OOP)."
)

print()

print(
    "Abstraction means hiding unnecessary implementation "
    "details and showing only the essential features."
)

print()

print(
    "The user knows WHAT an object does,"
)

print(
    "but does not need to know HOW it does it."
)

# =====================================================
# Visual Representation
# =====================================================

print("\n===== Visual Representation =====")

print("""
        +----------------------+
        |      Car Driver      |
        +----------------------+
                   │
           Presses Start Button
                   │
                   ▼
        +----------------------+
        |      Car Engine      |
        +----------------------+

Driver knows:
✔ How to start the car

Driver does NOT know:
✘ Internal engine mechanism
""")

# =====================================================
# Syntax
# =====================================================

print("\nSyntax:\n")

print("""
from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass
""")

# =====================================================
# Simple Example
# =====================================================


class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass


print(
    "Animal is an Abstract Class."
)

print(
    "The sound() method must be implemented "
    "by every Child Class."
)

# =====================================================
# Another Example
# =====================================================


class Shape(ABC):

    @abstractmethod
    def area(self):
        pass


print(
    "Shape is an Abstract Class."
)

# =====================================================
# Real-World Example
# =====================================================

print("\n===== Real-World Example =====")

print(
    "When you use an ATM,"
)

print(
    "you only interact with buttons and the screen."
)

print()

print(
    "You don't know how the banking system "
    "works internally."
)

print()

print(
    "This is a perfect example of Abstraction."
)

# =====================================================
# Explanation
# =====================================================

print("\nExplanation")

print(
    "Abstraction hides complex implementation details."
)

print(
    "It provides only the necessary functionality "
    "to the user."
)

# =====================================================
# Key Points
# =====================================================

print("\nKey Points")

print("✔ Hides implementation details.")
print("✔ Shows only essential features.")
print("✔ Improves security.")
print("✔ Makes programs easier to use.")

# =====================================================
# Important Note
# =====================================================

print("\nImportant Note")

print(
    "Abstraction focuses on WHAT an object does."
)

print(
    "Encapsulation focuses on HOW data is protected."
)

# =====================================================
# Remember
# =====================================================

print("\nRemember")

print("✔ Hide Complexity")
print("✔ Show Essentials")

# =====================================================
# 2. Why Do We Need Abstraction?
# =====================================================

print("\n===== Why Do We Need Abstraction? =====")

print(
    "Real-world systems can be very complex."
)

print()

print(
    "Users do not need to know every internal detail."
)

print()

print(
    "Abstraction hides unnecessary complexity "
    "and exposes only useful functionality."
)

# =====================================================
# Example
# =====================================================

print("\n===== Example =====")


class WashingMachine:

    def start(self):
        print("Washing Machine Started.")


machine = WashingMachine()

machine.start()

# Output:
# Washing Machine Started.

print()

print(
    "The user presses only one button."
)

print()

print(
    "The washing process happens internally."
)

# =====================================================
# Another Example
# =====================================================


class MobilePhone:

    def call(self):
        print("Calling...")

    def message(self):
        print("Sending Message...")


phone = MobilePhone()

phone.call()
phone.message()

# Output:
# Calling...
# Sending Message...

# =====================================================
# Explanation
# =====================================================

print("\nExplanation")

print(
    "The user only calls methods like "
    "call() or message()."
)

print()

print(
    "Internal communication remains hidden."
)

# =====================================================
# Key Points
# =====================================================

print("\nKey Points")

print("✔ Reduces complexity.")
print("✔ Improves readability.")
print("✔ Makes applications user-friendly.")
print("✔ Simplifies large software systems.")

# =====================================================
# Remember
# =====================================================

print("\nRemember")

print("✔ Users need features, not implementation.")

# =====================================================
# 3. Abstract Class
# =====================================================

print("\n===== Abstract Class =====")

print(
    "An Abstract Class is a class that cannot "
    "be instantiated directly."
)

print()

print(
    "It is used as a blueprint for other classes."
)

# =====================================================
# Syntax
# =====================================================

print("\nSyntax:\n")

print("""
from abc import ABC

class Animal(ABC):
    pass
""")

# =====================================================
# Simple Example
# =====================================================


class Animal(ABC):
    pass


print(
    "Animal is an Abstract Class."
)

# =====================================================
# Another Example
# =====================================================


class Vehicle(ABC):
    pass


print(
    "Vehicle is also an Abstract Class."
)

# =====================================================
# Real-World Example
# =====================================================

print("\n===== Real-World Example =====")

print(
    "Think of an architectural blueprint."
)

print()

print(
    "You cannot live inside the blueprint."
)

print()

print(
    "It is only used to build actual houses."
)

print()

print(
    "Similarly, an Abstract Class provides a template "
    "for Child Classes."
)

# =====================================================
# Explanation
# =====================================================

print("\nExplanation")

print(
    "Abstract Classes define common rules."
)

print()

print(
    "Child Classes provide actual implementations."
)

# =====================================================
# Key Points
# =====================================================

print("\nKey Points")

print("✔ Cannot be used to create objects.")
print("✔ Acts as a blueprint.")
print("✔ Parent for Child Classes.")

# =====================================================
# Important Note
# =====================================================

print("\nImportant Note")

print(
    "Python allows Abstract Classes using "
    "the abc module."
)

# =====================================================
# Remember
# =====================================================

print("\nRemember")

print("✔ Blueprint, not an actual object.")

# =====================================================
# 4. Abstract Method
# =====================================================

print("\n===== Abstract Method =====")

print(
    "An Abstract Method is a method declared "
    "inside an Abstract Class."
)

print()

print(
    "It has no implementation in the Parent Class."
)

print()

print(
    "Every Child Class MUST implement it."
)

# =====================================================
# Syntax
# =====================================================

print("\nSyntax:\n")

print("""
from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass
""")

# =====================================================
# Simple Example
# =====================================================


class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):

    def sound(self):
        print("Bark")


dog = Dog()

dog.sound()

# Output:
# Bark

# =====================================================
# Another Example
# =====================================================


class Shape(ABC):

    @abstractmethod
    def area(self):
        pass


class Square(Shape):

    def area(self):
        print("Area of Square")


square = Square()

square.area()

# Output:
# Area of Square

# =====================================================
# Real-World Example
# =====================================================

print("\n===== Real-World Example =====")

print(
    "Every payment method must provide "
    "its own payment process."
)

print()

print(
    "Credit Card, UPI, and Net Banking"
)

print(
    "all implement pay() differently."
)

# =====================================================
# Explanation
# =====================================================

print("\nExplanation")

print(
    "The Parent Class only declares the method."
)

print()

print(
    "The Child Class provides the implementation."
)

# =====================================================
# Key Points
# =====================================================

print("\nKey Points")

print("✔ Declared using @abstractmethod.")
print("✔ Must be implemented by Child Classes.")
print("✔ Defines a common interface.")

# =====================================================
# Important Note
# =====================================================

print("\nImportant Note")

print(
    "If a Child Class does not implement "
    "every Abstract Method,"
)

print(
    "Python will not allow its object to be created."
)

# =====================================================
# Remember
# =====================================================

print("\nRemember")

print("✔ Parent defines the rule.")
print("✔ Child provides the implementation.")

# =====================================================
# 5. abc Module
# =====================================================

print("\n===== abc Module =====")

print(
    "The abc module stands for "
    "'Abstract Base Classes'."
)

print()

print(
    "It allows us to create Abstract Classes "
    "and Abstract Methods in Python."
)

# =====================================================
# Import Statement
# =====================================================

print("\nImport Statement:\n")

print("""
from abc import ABC, abstractmethod
""")

# =====================================================
# Simple Example
# =====================================================

from abc import ABC, abstractmethod


class Animal(ABC):
    pass


print("Animal is now an Abstract Class.")

# Output:
# Animal is now an Abstract Class.

# =====================================================
# Another Example
# =====================================================


class Vehicle(ABC):
    pass


print("Vehicle is also an Abstract Class.")

# Output:
# Vehicle is also an Abstract Class.

# =====================================================
# Real-World Example
# =====================================================

print("\n===== Real-World Example =====")

print(
    "Think of ABC as a blueprint designer."
)

print()

print(
    "It provides rules for creating proper classes."
)

# =====================================================
# Explanation
# =====================================================

print("\nExplanation")

print(
    "Without the abc module,"
)

print()

print(
    "Python cannot create true Abstract Classes."
)

# =====================================================
# Key Points
# =====================================================

print("\nKey Points")

print("✔ abc = Abstract Base Classes")
print("✔ Used to create Abstract Classes.")
print("✔ Part of Python's standard library.")

# =====================================================
# Remember
# =====================================================

print("\nRemember")

print("✔ Import ABC before creating Abstract Classes.")

# =====================================================
# 6. @abstractmethod Decorator
# =====================================================

print("\n===== @abstractmethod Decorator =====")

print(
    "@abstractmethod is used to declare "
    "an Abstract Method."
)

print()

print(
    "Every Child Class must implement "
    "this method."
)

# =====================================================
# Syntax
# =====================================================

print("\nSyntax:\n")

print("""
from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass
""")

# =====================================================
# Simple Example
# =====================================================


class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass


print(
    "sound() is an Abstract Method."
)

# =====================================================
# Another Example
# =====================================================


class Shape(ABC):

    @abstractmethod
    def area(self):
        pass


print(
    "area() is an Abstract Method."
)

# =====================================================
# Real-World Example
# =====================================================

print("\n===== Real-World Example =====")

print(
    "Every payment system must implement "
    "the pay() method."
)

print()

print(
    "The implementation can be different,"
)

print(
    "but the method must exist."
)

# =====================================================
# Explanation
# =====================================================

print("\nExplanation")

print(
    "@abstractmethod forces Child Classes"
)

print(
    "to provide their own implementation."
)

# =====================================================
# Key Points
# =====================================================

print("\nKey Points")

print("✔ Declares Abstract Methods.")
print("✔ Forces implementation.")
print("✔ Works only inside Abstract Classes.")

# =====================================================
# Remember
# =====================================================

print("\nRemember")

print("✔ Rule first, implementation later.")

# =====================================================
# 7. Creating Your First Abstract Class
# =====================================================

print("\n===== Creating Your First Abstract Class =====")

# =====================================================
# Visual Representation
# =====================================================

print("\n===== Visual Representation =====")

print("""
               Animal (Abstract)
                     │
         ┌───────────┼───────────┐
         │           │           │
       Dog         Cat         Cow
         │           │           │
      sound()     sound()     sound()
""")

# =====================================================
# Example
# =====================================================


class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):

    def sound(self):
        print("Bark")


class Cat(Animal):

    def sound(self):
        print("Meow")


class Cow(Animal):

    def sound(self):
        print("Moo")


dog = Dog()
cat = Cat()
cow = Cow()

dog.sound()
cat.sound()
cow.sound()

# Output:
# Bark
# Meow
# Moo

# =====================================================
# What Happens If We Create Animal Object?
# =====================================================

print("\n===== Incorrect Example =====")

print("""
animal = Animal()
""")

print("\nExpected Error:")

print("""
TypeError:
Can't instantiate abstract class Animal
with abstract method sound
""")

# =====================================================
# Explanation
# =====================================================

print("\nExplanation")

print(
    "Animal is an Abstract Class."
)

print()

print(
    "Python does not allow creating its object."
)

print()

print(
    "Only Child Classes that implement "
    "all Abstract Methods can create objects."
)

# =====================================================
# Key Points
# =====================================================

print("\nKey Points")

print("✔ Cannot create Abstract Class objects.")
print("✔ Child Classes must implement Abstract Methods.")
print("✔ Promotes a common interface.")

# =====================================================
# Remember
# =====================================================

print("\nRemember")

print("✔ Abstract Class = Blueprint")

# =====================================================
# 8. Rules of Abstract Classes
# =====================================================

print("\n===== Rules of Abstract Classes =====")

rules = [
    "Use the abc module.",
    "Inherit from ABC.",
    "Declare methods using @abstractmethod.",
    "Cannot create objects of an Abstract Class.",
    "Child Classes must implement all Abstract Methods.",
    "Abstract Classes can contain normal methods.",
    "Abstract Classes can contain constructors.",
    "Abstract Classes can contain attributes."
]

for index, rule in enumerate(rules, start=1):
    print(f"{index}. {rule}")

# =====================================================
# Example
# =====================================================


class Animal(ABC):

    def eat(self):
        print("Animal is eating.")

    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):

    def sound(self):
        print("Bark")


dog = Dog()

dog.eat()
dog.sound()

# Output:
# Animal is eating.
# Bark

# =====================================================
# Explanation
# =====================================================

print("\nExplanation")

print(
    "Abstract Classes can have both"
)

print(
    "normal methods and Abstract Methods."
)

print()

print(
    "Only Abstract Methods must be implemented."
)

# =====================================================
# Key Points
# =====================================================

print("\nKey Points")

print("✔ Normal methods are allowed.")
print("✔ Constructors are allowed.")
print("✔ Attributes are allowed.")
print("✔ Only Abstract Methods are compulsory.")

# =====================================================
# Important Note
# =====================================================

print("\nImportant Note")

print(
    "An Abstract Class does not have to contain"
)

print(
    "only Abstract Methods."
)

print()

print(
    "It can also include reusable code"
)

print(
    "for all Child Classes."
)

# =====================================================
# Remember
# =====================================================

print("\nRemember")

print("✔ Abstract Class = Rules + Shared Functionality")

# =====================================================
# 9. Advantages of Abstraction
# =====================================================

print("\n===== Advantages of Abstraction =====")

advantages = [
    "Hides unnecessary implementation details.",
    "Reduces program complexity.",
    "Improves code readability.",
    "Provides better security.",
    "Makes code easier to maintain.",
    "Promotes code reusability.",
    "Provides a common interface.",
    "Makes large applications easier to manage."
]

for advantage in advantages:
    print(f"✔ {advantage}")

# =====================================================
# Explanation
# =====================================================

print("\nExplanation")

print(
    "Abstraction hides internal implementation and "
    "shows only the required functionality."
)

print(
    "This makes software easier to understand "
    "and maintain."
)

# =====================================================
# Remember
# =====================================================

print("\nRemember")

print("✔ Hide Complexity, Show Simplicity.")

# =====================================================
# 10. Difference Between Abstraction and Encapsulation
# =====================================================

print("\n===== Abstraction vs Encapsulation =====")

print(
    f"{'Feature':<22}"
    f"{'Abstraction':<32}"
    f"{'Encapsulation'}"
)

print("-" * 90)

comparison = [
    (
        "Focus",
        "Hiding Implementation",
        "Hiding Data"
    ),
    (
        "Purpose",
        "Shows Essential Features",
        "Protects Data"
    ),
    (
        "Achieved Using",
        "Abstract Classes",
        "Private Attributes"
    ),
    (
        "Keyword",
        "@abstractmethod",
        "Access Modifiers"
    ),
    (
        "Question",
        "What does it do?",
        "How is data protected?"
    ),
]

for feature, abstraction, encapsulation in comparison:
    print(
        f"{feature:<22}"
        f"{abstraction:<32}"
        f"{encapsulation}"
    )

# =====================================================
# Real-World Comparison
# =====================================================

print("\n===== Real-World Comparison =====")

print("Abstraction Example")

print(
    "A car driver only uses the steering,"
)

print(
    "accelerator, and brake."
)

print(
    "The engine's internal mechanism remains hidden."
)

print("\nEncapsulation Example")

print(
    "The engine's internal components are protected."
)

print(
    "Users cannot directly modify them."
)

# =====================================================
# Explanation
# =====================================================

print("\nExplanation")

print(
    "Abstraction hides HOW something works."
)

print()

print(
    "Encapsulation protects internal data "
    "from direct access."
)

# =====================================================
# Key Points
# =====================================================

print("\nKey Points")

print("✔ Abstraction hides implementation.")
print("✔ Encapsulation hides data.")
print("✔ Both improve software design.")

# =====================================================
# Remember
# =====================================================

print("\nRemember")

print("✔ Abstraction → What?")
print("✔ Encapsulation → How?")

# =====================================================
# Part B : Special (Magic / Dunder) Methods
# =====================================================

print("\n" + "=" * 60)
print("SPECIAL (MAGIC / DUNDER) METHODS")
print("=" * 60)

# =====================================================
# 11. What are Special Methods?
# =====================================================

print("\n===== What are Special Methods? =====")

print(
    "Special Methods are predefined methods "
    "provided by Python."
)

print()

print(
    "They always begin and end with "
    "double underscores (__)."
)

print()

print(
    "These methods are also called "
    "Magic Methods or Dunder Methods."
)

# =====================================================
# Examples
# =====================================================

print("\nCommon Special Methods")

methods = [
    "__init__()",
    "__str__()",
    "__repr__()",
    "__len__()",
    "__add__()",
    "__eq__()"
]

for method in methods:
    print(f"✔ {method}")

# =====================================================
# Real-World Example
# =====================================================

print("\n===== Real-World Example =====")

print(
    "When you use len(my_list),"
)

print(
    "Python internally calls:"
)

print()

print("my_list.__len__()")

# =====================================================
# Explanation
# =====================================================

print("\nExplanation")

print(
    "Special Methods allow Python objects "
    "to work naturally with built-in functions "
    "and operators."
)

# =====================================================
# Key Points
# =====================================================

print("\nKey Points")

print("✔ Built into Python.")
print("✔ Automatically called.")
print("✔ Make objects behave like built-in types.")

# =====================================================
# Remember
# =====================================================

print("\nRemember")

print("✔ __method__ = Special Method")

# =====================================================
# 12. __init__() Method
# =====================================================

print("\n===== __init__() Method =====")

print(
    "__init__() is a constructor."
)

print()

print(
    "It is automatically executed when "
    "an object is created."
)

# =====================================================
# Syntax
# =====================================================

print("\nSyntax:\n")

print("""
class Student:

    def __init__(self):
        pass
""")

# =====================================================
# Simple Example
# =====================================================


class Student:

    def __init__(self):
        print("Object Created")


student = Student()

# Output:
# Object Created

# =====================================================
# Another Example
# =====================================================


class Employee:

    def __init__(self, name):
        self.name = name


employee = Employee("Nikita")

print(employee.name)

# Output:
# Nikita

# =====================================================
# Real-World Example
# =====================================================


class Car:

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display(self):
        print(f"{self.brand} {self.model}")


car = Car("Toyota", "Fortuner")

car.display()

# Output:
# Toyota Fortuner

# =====================================================
# Explanation
# =====================================================

print("\nExplanation")

print(
    "__init__() initializes object attributes."
)

print()

print(
    "It runs automatically during object creation."
)

# =====================================================
# Key Points
# =====================================================

print("\nKey Points")

print("✔ Constructor.")
print("✔ Called automatically.")
print("✔ Initializes object data.")

# =====================================================
# Remember
# =====================================================

print("\nRemember")

print("✔ One object → One __init__() call")

# =====================================================
# 13. __str__() Method
# =====================================================

print("\n===== __str__() Method =====")

print(
    "__str__() returns a human-readable "
    "string representation of an object."
)

# =====================================================
# Syntax
# =====================================================

print("\nSyntax:\n")

print("""
class Student:

    def __str__(self):
        return "Student Object"
""")

# =====================================================
# Simple Example
# =====================================================


class Student:

    def __str__(self):
        return "Student Object"


student = Student()

print(student)

# Output:
# Student Object

# =====================================================
# Another Example
# =====================================================


class Employee:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Employee(Name={self.name})"


employee = Employee("Nikita")

print(employee)

# Output:
# Employee(Name=Nikita)

# =====================================================
# Real-World Example
# =====================================================


class Book:

    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return (
            f"Book: {self.title} "
            f"by {self.author}"
        )


book = Book("Python Basics", "Nikita")

print(book)

# Output:
# Book: Python Basics by Nikita

# =====================================================
# Explanation
# =====================================================

print("\nExplanation")

print(
    "__str__() controls what is displayed "
    "when print(object) is used."
)

# =====================================================
# Key Points
# =====================================================

print("\nKey Points")

print("✔ Used by print().")
print("✔ Returns a string.")
print("✔ Improves object readability.")

# =====================================================
# Important Note
# =====================================================

print("\nImportant Note")

print(
    "__str__() must always return a string."
)

# =====================================================
# Remember
# =====================================================

print("\nRemember")

print("✔ print(object) → object.__str__()")

# =====================================================
# 14. __repr__() Method
# =====================================================

print("\n===== __repr__() Method =====")

print(
    "__repr__() returns the official string "
    "representation of an object."
)

print()

print(
    "It is mainly used by developers for debugging."
)

# =====================================================
# Syntax
# =====================================================

print("\nSyntax:\n")

print("""
class Book:

    def __repr__(self):
        return "Book()"
""")

# =====================================================
# Simple Example
# =====================================================


class Book:

    def __repr__(self):
        return "Book()"


book = Book()

print(repr(book))

# Output:
# Book()

# =====================================================
# Another Example
# =====================================================


class Student:

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Student(name='{self.name}')"


student = Student("Nikita")

print(repr(student))

# Output:
# Student(name='Nikita')

# =====================================================
# Explanation
# =====================================================

print("\nExplanation")

print(
    "__repr__() provides an unambiguous representation "
    "of an object."
)

print(
    "It is mainly intended for developers."
)

# =====================================================
# Key Points
# =====================================================

print("\nKey Points")

print("✔ Used by repr().")
print("✔ Helpful for debugging.")
print("✔ Returns a string.")

# =====================================================
# Remember
# =====================================================

print("\nRemember")

print("✔ repr(object) → object.__repr__()")

# =====================================================
# 15. __len__() Method
# =====================================================

print("\n===== __len__() Method =====")

print(
    "__len__() allows an object to work "
    "with the len() function."
)

# =====================================================
# Syntax
# =====================================================

print("\nSyntax:\n")

print("""
class Book:

    def __len__(self):
        return 0
""")

# =====================================================
# Example
# =====================================================


class Book:

    def __init__(self, pages):
        self.pages = pages

    def __len__(self):
        return self.pages


book = Book(350)

print(len(book))

# Output:
# 350

# =====================================================
# Explanation
# =====================================================

print("\nExplanation")

print(
    "Python internally calls __len__() "
    "when len(object) is used."
)

# =====================================================
# Key Points
# =====================================================

print("\nKey Points")

print("✔ Used by len().")
print("✔ Must return an integer.")

# =====================================================
# Remember
# =====================================================

print("\nRemember")

print("✔ len(object) → object.__len__()")

# =====================================================
# 16. __add__() Method
# =====================================================

print("\n===== __add__() Method =====")

print(
    "__add__() defines the behavior of "
    "the + operator."
)

# =====================================================
# Syntax
# =====================================================

print("\nSyntax:\n")

print("""
object1 + object2
""")

# =====================================================
# Example
# =====================================================


class Book:

    def __init__(self, pages):
        self.pages = pages

    def __add__(self, other):
        return self.pages + other.pages


book1 = Book(250)
book2 = Book(350)

print(book1 + book2)

# Output:
# 600

# =====================================================
# Explanation
# =====================================================

print("\nExplanation")

print(
    "Python internally calls __add__() "
    "when the + operator is used."
)

# =====================================================
# Key Points
# =====================================================

print("\nKey Points")

print("✔ Used with + operator.")
print("✔ Enables operator overloading.")

# =====================================================
# Remember
# =====================================================

print("\nRemember")

print("✔ object1 + object2 → object1.__add__(object2)")

# =====================================================
# 17. __eq__() Method
# =====================================================

print("\n===== __eq__() Method =====")

print(
    "__eq__() defines how two objects "
    "are compared using ==."
)

# =====================================================
# Example
# =====================================================


class Student:

    def __init__(self, roll_no):
        self.roll_no = roll_no

    def __eq__(self, other):
        return self.roll_no == other.roll_no


student1 = Student(101)
student2 = Student(101)
student3 = Student(102)

print(student1 == student2)
print(student1 == student3)

# Output:
# True
# False

# =====================================================
# Explanation
# =====================================================

print("\nExplanation")

print(
    "__eq__() allows custom comparison "
    "between objects."
)

# =====================================================
# Key Points
# =====================================================

print("\nKey Points")

print("✔ Used by == operator.")
print("✔ Returns True or False.")

# =====================================================
# Remember
# =====================================================

print("\nRemember")

print("✔ object1 == object2 → object1.__eq__(object2)")

# =====================================================
# 18. Other Common Special Methods
# =====================================================

print("\n===== Other Common Special Methods =====")

methods = [
    "__sub__()  -> - operator",
    "__mul__()  -> * operator",
    "__truediv__() -> / operator",
    "__lt__()   -> < operator",
    "__gt__()   -> > operator",
    "__contains__() -> in operator",
    "__getitem__() -> [] indexing",
    "__call__() -> Object as a function"
]

for method in methods:
    print(f"✔ {method}")

# =====================================================
# 19. Real-World Example
# =====================================================

print("\n===== Real-World Example =====")


class Book:

    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def __str__(self):
        return f"{self.title} ({self.pages} pages)"

    def __repr__(self):
        return (
            f"Book(title='{self.title}', "
            f"pages={self.pages})"
        )

    def __len__(self):
        return self.pages

    def __add__(self, other):
        return self.pages + other.pages

    def __eq__(self, other):
        return self.pages == other.pages


book1 = Book("Python", 350)
book2 = Book("Machine Learning", 450)
book3 = Book("Data Science", 350)

print(book1)
print(repr(book1))
print(len(book1))
print(book1 + book2)
print(book1 == book3)

# Output:
# Python (350 pages)
# Book(title='Python', pages=350)
# 350
# 800
# True

# =====================================================
# 20. Common Mistakes
# =====================================================

print("\n===== Common Mistakes =====")

mistakes = [
    "__str__() not returning a string.",
    "Forgetting self parameter.",
    "Returning wrong data type.",
    "Confusing __repr__() and __str__().",
    "Ignoring Abstract Methods.",
    "Creating objects of Abstract Classes.",
    "Not overriding required methods."
]

for index, mistake in enumerate(mistakes, start=1):
    print(f"{index}. {mistake}")

# =====================================================
# 21. Interview Questions
# =====================================================

print("\n===== Interview Questions =====")

questions = [
    "What is Abstraction?",
    "What is an Abstract Class?",
    "What is an Abstract Method?",
    "Why do we use the abc module?",
    "Difference between Abstraction and Encapsulation?",
    "What are Magic Methods?",
    "Difference between __str__() and __repr__()?",
    "What is __len__()?",
    "What is __add__()?",
    "What is __eq__()?"
]

for index, question in enumerate(questions, start=1):
    print(f"{index}. {question}")

# =====================================================
# 22. Best Practices
# =====================================================

print("\n===== Best Practices =====")

best_practices = [
    "Use Abstract Classes for common interfaces.",
    "Implement all Abstract Methods.",
    "Use __str__() for users.",
    "Use __repr__() for developers.",
    "Keep Magic Methods simple.",
    "Return correct data types.",
    "Write readable and maintainable code.",
    "Follow PEP 8 naming conventions."
]

for practice in best_practices:
    print(f"✔ {practice}")

# =====================================================
# 23. Mini Practice
# =====================================================

print("\n===== Mini Practice =====")

practice = [
    "Create an Abstract Class.",
    "Implement an Abstract Method.",
    "Create Dog and Cat classes.",
    "Implement __str__().",
    "Implement __repr__().",
    "Implement __len__().",
    "Implement __add__().",
    "Implement __eq__()."
]

for index, item in enumerate(practice, start=1):
    print(f"{index}. {item}")

# =====================================================
# 24. Coding Challenge
# =====================================================

print("\n===== Coding Challenge =====")

print("Challenge 1")
print("- Create an abstract Vehicle class.")

print("\nChallenge 2")
print("- Create Car and Bike classes.")

print("\nChallenge 3")
print("- Override start().")

print("\nChallenge 4")
print("- Implement __str__().")

print("\nChallenge 5")
print("- Compare two objects using ==.")

# =====================================================
# 25. Output Prediction
# =====================================================

print("\n===== Output Prediction =====")

print("""
class Book:

    def __len__(self):
        return 500

book = Book()

print(len(book))
""")

print("\nExpected Output")

print("""
500
""")

print("\nReason")

print(
    "len(book) internally calls "
    "book.__len__()."
)

# =====================================================
# Quick Revision
# =====================================================

print("\n===== Quick Revision =====")

revision = [
    "Abstraction hides implementation details.",
    "ABC creates Abstract Classes.",
    "@abstractmethod defines rules.",
    "__init__() initializes objects.",
    "__str__() returns a readable string.",
    "__repr__() returns a developer-friendly string.",
    "__len__() works with len().",
    "__add__() overloads + operator.",
    "__eq__() overloads == operator."
]

for point in revision:
    print(f"✔ {point}")

# =====================================================
# Summary
# =====================================================

print("\n===== Summary =====")

print("✔ Abstraction hides implementation details.")
print("✔ Abstract Classes define common rules.")
print("✔ Child Classes implement Abstract Methods.")
print("✔ Special Methods customize object behavior.")
print("✔ __str__() is for users.")
print("✔ __repr__() is for developers.")
print("✔ __len__(), __add__(), and __eq__() integrate objects with Python operators.")
print("✔ Magic Methods make custom classes behave like built-in objects.")

# =====================================================
# End of Program
# =====================================================

print("\nCongratulations! 🎉")
print("You have successfully completed")
print("Abstraction and Special Methods.")