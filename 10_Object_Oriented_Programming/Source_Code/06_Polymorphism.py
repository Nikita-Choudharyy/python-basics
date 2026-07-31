"""
=========================================================
Topic : Polymorphism
File  : 06_Polymorphism.py

Description:
This file explains the concept of Polymorphism in Python.
You will learn how the same method can behave
differently for different objects, the types of
polymorphism, and real-world applications.

Topics Covered:
1. What is Polymorphism?
2. Why Do We Need Polymorphism?
3. Types of Polymorphism
4. Method Overriding
5. Method Overloading in Python
6. Duck Typing
7. Polymorphism with Inheritance
8. Polymorphism with Built-in Functions
9. Polymorphism with User-Defined Functions
10. Advantages of Polymorphism
11. Difference Between Overloading and Overriding
12. Real-World Example

Author : Nikita Choudhary
Repository : Python Basics
=========================================================
"""

# =====================================================
# Polymorphism
# =====================================================

print("=" * 60)
print("POLYMORPHISM")
print("=" * 60)

# =====================================================
# 1. What is Polymorphism?
# =====================================================

print("\n===== What is Polymorphism? =====")

print(
    "Polymorphism is one of the four main principles "
    "of Object-Oriented Programming (OOP)."
)

print(
    "\nThe word 'Polymorphism' comes from two Greek words:"
)

print("Poly = Many")
print("Morph = Forms")

print(
    "\nPolymorphism means 'One Interface, Many Forms'."
)

print(
    "\nThe same method name can perform different "
    "actions depending on the object."
)

# =====================================================
# Visual Representation
# =====================================================

print("\n===== Visual Representation =====")

print("""
                Animal
                   │
        ┌──────────┼──────────┐
        │          │          │
       Dog        Cat        Cow
        │          │          │
    sound()    sound()    sound()
        │          │          │
      Bark!      Meow!      Moo!
""")

# =====================================================
# Syntax
# =====================================================

print("\nSyntax:\n")

print("""
class Parent:
    def method(self):
        pass

class Child(Parent):

    def method(self):
        pass
""")

# =====================================================
# Simple Example
# =====================================================


class Dog:

    def sound(self):
        print("Bark")


class Cat:

    def sound(self):
        print("Meow")


dog = Dog()
cat = Cat()

dog.sound()
cat.sound()

# Output:
# Bark
# Meow

# =====================================================
# Another Example
# =====================================================


class Circle:

    def draw(self):
        print("Drawing Circle")


class Rectangle:

    def draw(self):
        print("Drawing Rectangle")


circle = Circle()
rectangle = Rectangle()

circle.draw()
rectangle.draw()

# Output:
# Drawing Circle
# Drawing Rectangle

# =====================================================
# Real-World Example
# =====================================================

print("\n===== Real-World Example =====")

print(
    "Different vehicles have the same action 'start()',"
)

print(
    "but each vehicle starts differently."
)

print(
    "A Bike starts differently from a Car,"
)

print(
    "and an Electric Car starts differently from both."
)

# =====================================================
# Explanation
# =====================================================

print("\nExplanation")

print(
    "The method name remains the same,"
)

print(
    "but its behavior changes depending on the object."
)

# =====================================================
# Key Points
# =====================================================

print("\nKey Points")

print("✔ One Interface, Many Forms.")
print("✔ Same method name.")
print("✔ Different implementations.")
print("✔ Improves flexibility.")
print("✔ Makes code easier to extend.")

# =====================================================
# Important Note
# =====================================================

print("\nImportant Note")

print(
    "Polymorphism does NOT mean different method names."
)

print(
    "It means the SAME method behaves differently."
)

# =====================================================
# Remember
# =====================================================

print("\nRemember")

print("✔ Poly = Many")
print("✔ Morph = Forms")
print("✔ One Interface, Many Forms")

# =====================================================
# 2. Why Do We Need Polymorphism?
# =====================================================

print("\n===== Why Do We Need Polymorphism? =====")

print(
    "Polymorphism allows us to write flexible "
    "and reusable code."
)

print(
    "Instead of writing separate logic for every object,"
)

print(
    "we can use one common interface."
)

# =====================================================
# Example Without Polymorphism
# =====================================================

print("\n===== Without Polymorphism =====")


class Dog:

    def bark(self):
        print("Bark")


class Cat:

    def meow(self):
        print("Meow")


dog = Dog()
cat = Cat()

dog.bark()
cat.meow()

# Output:
# Bark
# Meow

# =====================================================
# Example With Polymorphism
# =====================================================

print("\n===== With Polymorphism =====")


class Dog:

    def sound(self):
        print("Bark")


class Cat:

    def sound(self):
        print("Meow")


dog = Dog()
cat = Cat()

dog.sound()
cat.sound()

# Output:
# Bark
# Meow

# =====================================================
# Explanation
# =====================================================

print("\nExplanation")

print(
    "Both objects use the same method name."
)

print(
    "Only the behavior changes."
)

# =====================================================
# Real-World Example
# =====================================================

print("\n===== Real-World Example =====")

print(
    "Every payment application has a pay() function."
)

print(
    "Credit Card, UPI, and Net Banking"
)

print(
    "all perform payment differently."
)

print(
    "The method is the same,"
)

print(
    "but the implementation changes."
)

# =====================================================
# Key Points
# =====================================================

print("\nKey Points")

print("✔ Reduces complex conditions.")
print("✔ Improves code readability.")
print("✔ Makes programs easier to extend.")
print("✔ Supports reusable design.")

# =====================================================
# Remember
# =====================================================

print("\nRemember")

print("✔ One method, multiple behaviors.")

# =====================================================
# 3. Types of Polymorphism
# =====================================================

print("\n===== Types of Polymorphism =====")

print("1. Compile-Time Polymorphism")
print("2. Run-Time Polymorphism")

# =====================================================
# Compile-Time Polymorphism
# =====================================================

print("\n===== Compile-Time Polymorphism =====")

print(
    "Compile-Time Polymorphism is achieved through "
    "Method Overloading in many programming languages."
)

print(
    "Examples include C++, Java (compile-time overloading),"
)

print(
    "where multiple methods can have the same name "
    "but different parameter lists."
)

print(
    "Python does not support true Method Overloading "
    "like C++ or Java."
)

# =====================================================
# Example
# =====================================================

print("\nExample:")

print("""
# C++ / Java Style

add(5, 10)

add(5, 10, 20)

add(5.5, 6.5)
""")

# =====================================================
# Important Note
# =====================================================

print("\nImportant Note")

print(
    "Python handles this differently using"
)

print(
    "default arguments, *args, and keyword arguments."
)

print(
    "We will learn this in the next section."
)

# =====================================================
# Run-Time Polymorphism
# =====================================================

print("\n===== Run-Time Polymorphism =====")

print(
    "Run-Time Polymorphism is achieved through "
    "Method Overriding."
)

print(
    "The method that executes is decided "
    "while the program is running."
)

# =====================================================
# Visual Representation
# =====================================================

print("\n===== Visual Representation =====")

print("""
            Animal
               │
      ┌────────┴────────┐
      │                 │
     Dog               Cat
      │                 │
   sound()          sound()
      │                 │
    Bark            Meow
""")

# =====================================================
# Example
# =====================================================


class Animal:

    def sound(self):
        print("Some Animal Sound")


class Dog(Animal):

    def sound(self):
        print("Bark")


class Cat(Animal):

    def sound(self):
        print("Meow")


dog = Dog()
cat = Cat()

dog.sound()
cat.sound()

# Output:
# Bark
# Meow

# =====================================================
# Explanation
# =====================================================

print("\nExplanation")

print(
    "The same method sound() behaves differently "
    "for Dog and Cat."
)

print(
    "This is Run-Time Polymorphism."
)

# =====================================================
# Key Points
# =====================================================

print("\nKey Points")

print("✔ Most common type in Python.")
print("✔ Achieved using Method Overriding.")
print("✔ Depends on the object created.")

# =====================================================
# Remember
# =====================================================

print("\nRemember")

print("✔ Compile-Time → Method Overloading (Not True in Python)")
print("✔ Run-Time → Method Overriding")

# =====================================================
# 4. Method Overriding
# =====================================================

print("\n===== Method Overriding =====")

print(
    "Method Overriding occurs when a Child Class "
    "provides its own implementation of a method "
    "that already exists in the Parent Class."
)

# =====================================================
# Visual Representation
# =====================================================

print("\n===== Visual Representation =====")

print("""
               Animal
                  │
         ┌────────┼────────┐
         │        │        │
        Dog      Cat      Cow
         │        │        │
     sound()  sound()  sound()
         │        │        │
       Bark    Meow      Moo
""")

# =====================================================
# Syntax
# =====================================================

print("\nSyntax:\n")

print("""
class Parent:

    def method(self):
        pass


class Child(Parent):

    def method(self):
        pass
""")

# =====================================================
# Simple Example
# =====================================================


class Animal:

    def sound(self):
        print("Some Animal Sound")


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


class Animal:

    def sound(self):
        print("Some Animal Sound")


class Cat(Animal):

    def sound(self):
        print("Meow")


cat = Cat()

cat.sound()

# Output:
# Meow

# =====================================================
# Real-World Example
# =====================================================


class Animal:

    def move(self):
        print("Animals can move.")


class Bird(Animal):

    def move(self):
        print("Birds fly in the sky.")


class Fish(Animal):

    def move(self):
        print("Fish swim in water.")


bird = Bird()
fish = Fish()

bird.move()
fish.move()

# Output:
# Birds fly in the sky.
# Fish swim in water.

# =====================================================
# Explanation
# =====================================================

print("\nExplanation")

print(
    "The Parent Class defines the original method."
)

print(
    "Each Child Class replaces that method "
    "with its own implementation."
)

print(
    "This process is called Method Overriding."
)

# =====================================================
# Key Points
# =====================================================

print("\nKey Points")

print("✔ Child Class replaces Parent method.")
print("✔ Method name remains the same.")
print("✔ Parameters are usually the same.")
print("✔ Achieves Run-Time Polymorphism.")

# =====================================================
# Important Note
# =====================================================

print("\nImportant Note")

print(
    "If the Child Class does not override the method,"
)

print(
    "the Parent Class method will be used."
)

# =====================================================
# Remember
# =====================================================

print("\nRemember")

print("✔ Same Method Name")
print("✔ Different Implementation")
print("✔ Run-Time Polymorphism")

# =====================================================
# 5. Method Overloading in Python
# =====================================================

print("\n===== Method Overloading in Python =====")

print(
    "Method Overloading means creating multiple "
    "methods with the same name but different parameters."
)

print()

print(
    "Languages like Java and C++ support true "
    "Method Overloading."
)

print()

print(
    "Python DOES NOT support true Method Overloading."
)

# =====================================================
# Example (Why It Doesn't Work)
# =====================================================

print("\n===== Example (True Overloading Does Not Work) =====")

print("""
class Calculator:

    def add(self, a, b):
        return a + b

    def add(self, a, b, c):
        return a + b + c
""")

print("\nExplanation")

print(
    "Python keeps only the LAST method definition."
)

print(
    "The first add() method is overwritten."
)

# =====================================================
# Correct Way in Python
# =====================================================

print("\n===== Correct Way Using Default Arguments =====")


class Calculator:

    def add(self, a, b, c=0):
        return a + b + c


calc = Calculator()

print(calc.add(10, 20))
print(calc.add(10, 20, 30))

# Output:
# 30
# 60

# =====================================================
# Another Way Using *args
# =====================================================

print("\n===== Using *args =====")


class Calculator:

    def add(self, *numbers):
        return sum(numbers)


calc = Calculator()

print(calc.add(10, 20))
print(calc.add(10, 20, 30))
print(calc.add(10, 20, 30, 40))

# Output:
# 30
# 60
# 100

# =====================================================
# Real-World Example
# =====================================================


class ShoppingCart:

    def total_price(self, *prices):
        return sum(prices)


cart = ShoppingCart()

print(cart.total_price(500))
print(cart.total_price(500, 200))
print(cart.total_price(500, 200, 100))

# Output:
# 500
# 700
# 800

# =====================================================
# Explanation
# =====================================================

print("\nExplanation")

print(
    "Python achieves overloading-like behavior "
    "using default arguments and *args."
)

print(
    "This provides flexibility without creating "
    "multiple methods with the same name."
)

# =====================================================
# Difference
# =====================================================

print("\n===== Method Overriding vs Method Overloading =====")

print(f"{'Method Overriding':<35}Method Overloading")
print("-" * 70)

print(f"{'Parent & Child Class':<35}Same Class")
print(f"{'Same Method Name':<35}Same Method Name")
print(f"{'Different Implementation':<35}Different Parameters")
print(f"{'Supported in Python':<35}Not True Overloading")

# =====================================================
# Key Points
# =====================================================

print("\nKey Points")

print("✔ Python does not support true Method Overloading.")
print("✔ Use default arguments.")
print("✔ Use *args for flexibility.")
print("✔ Method Overriding is fully supported.")

# =====================================================
# Remember
# =====================================================

print("\nRemember")

print("✔ Overriding → Child changes Parent method.")
print("✔ Overloading → Same method, different parameters.")
print("✔ Python uses *args and default values.")

# =====================================================
# 6. Duck Typing
# =====================================================

print("\n===== Duck Typing =====")

print(
    "Duck Typing is a Python feature where the type "
    "of an object is less important than its behavior."
)

print()

print(
    "If an object behaves like the expected object,"
)

print(
    "Python allows it to be used."
)

# =====================================================
# Famous Duck Typing Rule
# =====================================================

print("\nDuck Typing Rule")

print(
    '"If it walks like a duck and quacks like a duck, '
    'it is treated as a duck."'
)

# =====================================================
# Simple Example
# =====================================================


class Dog:

    def speak(self):
        print("Bark")


class Cat:

    def speak(self):
        print("Meow")


def make_sound(animal):
    animal.speak()


dog = Dog()
cat = Cat()

make_sound(dog)
make_sound(cat)

# Output:
# Bark
# Meow

# =====================================================
# Another Example
# =====================================================


class Student:

    def introduction(self):
        print("I am a Student.")


class Teacher:

    def introduction(self):
        print("I am a Teacher.")


def introduce(person):
    person.introduction()


student = Student()
teacher = Teacher()

introduce(student)
introduce(teacher)

# Output:
# I am a Student.
# I am a Teacher.

# =====================================================
# Real-World Example
# =====================================================

print("\n===== Real-World Example =====")

print(
    "A USB keyboard and a Bluetooth keyboard "
    "work differently."
)

print(
    "But both can type."
)

print(
    "The computer simply calls the typing functionality."
)

# =====================================================
# Explanation
# =====================================================

print("\nExplanation")

print(
    "Duck Typing focuses on what an object can do,"
)

print(
    "not on what type of object it is."
)

# =====================================================
# Key Points
# =====================================================

print("\nKey Points")

print("✔ Python checks behavior.")
print("✔ Type checking is less important.")
print("✔ Makes code flexible.")
print("✔ Commonly used in Python libraries.")

# =====================================================
# Remember
# =====================================================

print("\nRemember")

print("✔ Behavior matters more than object type.")

# =====================================================
# 7. Polymorphism with Inheritance
# =====================================================

print("\n===== Polymorphism with Inheritance =====")

print(
    "Method Overriding is the most common example "
    "of Polymorphism with Inheritance."
)

# =====================================================
# Visual Representation
# =====================================================

print("\n===== Visual Representation =====")

print("""
                Animal
                   │
       ┌───────────┼───────────┐
       │           │           │
      Dog         Cat         Cow
       │           │           │
   sound()     sound()     sound()
       │           │           │
     Bark       Meow        Moo
""")

# =====================================================
# Example
# =====================================================


class Animal:

    def sound(self):
        print("Some Animal Sound")


class Dog(Animal):

    def sound(self):
        print("Bark")


class Cat(Animal):

    def sound(self):
        print("Meow")


class Cow(Animal):

    def sound(self):
        print("Moo")


animals = [Dog(), Cat(), Cow()]

for animal in animals:
    animal.sound()

# Output:
# Bark
# Meow
# Moo

# =====================================================
# Explanation
# =====================================================

print("\nExplanation")

print(
    "The same sound() method behaves differently "
    "for each object."
)

print(
    "This is Run-Time Polymorphism."
)

# =====================================================
# Key Points
# =====================================================

print("\nKey Points")

print("✔ Uses Inheritance.")
print("✔ Uses Method Overriding.")
print("✔ Same method, different behavior.")

# =====================================================
# Remember
# =====================================================

print("\nRemember")

print("✔ Inheritance + Overriding = Polymorphism")

# =====================================================
# 8. Polymorphism with Built-in Functions
# =====================================================

print("\n===== Polymorphism with Built-in Functions =====")

print(
    "Many Python built-in functions are polymorphic."
)

# =====================================================
# len()
# =====================================================

print("\nExample : len()")

print(len("Python"))
print(len([10, 20, 30]))
print(len((1, 2, 3, 4)))
print(len({"A": 1, "B": 2}))

# Output:
# 6
# 3
# 4
# 2

# =====================================================
# abs()
# =====================================================

print("\nExample : abs()")

print(abs(-25))
print(abs(-12.8))

# Output:
# 25
# 12.8

# =====================================================
# type()
# =====================================================

print("\nExample : type()")

print(type(10))
print(type("Hello"))
print(type([1, 2, 3]))

# Output:
# <class 'int'>
# <class 'str'>
# <class 'list'>

# =====================================================
# Explanation
# =====================================================

print("\nExplanation")

print(
    "The same built-in function works with "
    "different object types."
)

# =====================================================
# Key Points
# =====================================================

print("\nKey Points")

print("✔ Same function.")
print("✔ Different data types.")
print("✔ Different behavior.")

# =====================================================
# Remember
# =====================================================

print("\nRemember")

print("✔ Built-in functions are also polymorphic.")

# =====================================================
# 9. Polymorphism with User-Defined Functions
# =====================================================

print("\n===== Polymorphism with User-Defined Functions =====")

print(
    "A single user-defined function can work "
    "with different object types."
)

# =====================================================
# Example
# =====================================================


class Dog:

    def sound(self):
        print("Bark")


class Cat:

    def sound(self):
        print("Meow")


class Cow:

    def sound(self):
        print("Moo")


def animal_sound(animal):
    animal.sound()


dog = Dog()
cat = Cat()
cow = Cow()

animal_sound(dog)
animal_sound(cat)
animal_sound(cow)

# Output:
# Bark
# Meow
# Moo

# =====================================================
# Another Example
# =====================================================


class Circle:

    def draw(self):
        print("Drawing Circle")


class Rectangle:

    def draw(self):
        print("Drawing Rectangle")


class Triangle:

    def draw(self):
        print("Drawing Triangle")


def draw_shape(shape):
    shape.draw()


circle = Circle()
rectangle = Rectangle()
triangle = Triangle()

draw_shape(circle)
draw_shape(rectangle)
draw_shape(triangle)

# Output:
# Drawing Circle
# Drawing Rectangle
# Drawing Triangle

# =====================================================
# Explanation
# =====================================================

print("\nExplanation")

print(
    "The function does not care about the object's class."
)

print(
    "It only expects the required method to exist."
)

# =====================================================
# Key Points
# =====================================================

print("\nKey Points")

print("✔ One function.")
print("✔ Multiple object types.")
print("✔ Cleaner and reusable code.")

# =====================================================
# Important Note
# =====================================================

print("\nImportant Note")

print(
    "If the required method does not exist,"
)

print(
    "Python raises an AttributeError."
)

# =====================================================
# Remember
# =====================================================

print("\nRemember")

print("✔ Functions work with behavior, not specific classes.")

# =====================================================
# 10. Advantages of Polymorphism
# =====================================================

print("\n===== Advantages of Polymorphism =====")

advantages = [
    "Promotes code reusability.",
    "Improves code flexibility.",
    "Makes programs easier to extend.",
    "Reduces complex conditional statements.",
    "Supports clean and maintainable code.",
    "Improves scalability.",
    "Makes software easier to test.",
    "Works naturally with Inheritance."
]

for advantage in advantages:
    print(f"✔ {advantage}")

# =====================================================
# Explanation
# =====================================================

print("\nExplanation")

print(
    "Polymorphism allows one interface to work with "
    "many different objects."
)

print(
    "This makes applications easier to maintain "
    "and extend."
)

# =====================================================
# Remember
# =====================================================

print("\nRemember")

print("✔ One Interface → Many Implementations")

# =====================================================
# 11. Difference Between Method Overloading and
#     Method Overriding
# =====================================================

print("\n===== Method Overloading vs Method Overriding =====")

print(
    f"{'Feature':<25}"
    f"{'Method Overloading':<30}"
    f"{'Method Overriding'}"
)

print("-" * 90)

comparison = [
    (
        "Meaning",
        "Same method, different parameters",
        "Child replaces Parent method"
    ),
    (
        "Classes",
        "Usually Same Class",
        "Parent & Child Class"
    ),
    (
        "Python Support",
        "Not True Overloading",
        "Fully Supported"
    ),
    (
        "Polymorphism",
        "Compile-Time (Other Languages)",
        "Run-Time"
    ),
    (
        "Method Name",
        "Same",
        "Same"
    ),
    (
        "Parameters",
        "Different",
        "Usually Same"
    ),
]

for feature, overloading, overriding in comparison:
    print(
        f"{feature:<25}"
        f"{overloading:<30}"
        f"{overriding}"
    )

# =====================================================
# 12. Real-World Example
# =====================================================

print("\n===== Real-World Example =====")


class Payment:

    def pay(self):
        print("Processing Payment...")


class CreditCard(Payment):

    def pay(self):
        print("Payment completed using Credit Card.")


class UPI(Payment):

    def pay(self):
        print("Payment completed using UPI.")


class NetBanking(Payment):

    def pay(self):
        print("Payment completed using Net Banking.")


payments = [
    CreditCard(),
    UPI(),
    NetBanking()
]

for payment in payments:
    payment.pay()

# Output:
# Payment completed using Credit Card.
# Payment completed using UPI.
# Payment completed using Net Banking.

# =====================================================
# Explanation
# =====================================================

print("\nExplanation")

print(
    "Each payment method implements the same "
    "pay() function differently."
)

print(
    "This is a real-world example of Polymorphism."
)

# =====================================================
# 13. Common Mistakes
# =====================================================

print("\n===== Common Mistakes =====")

mistakes = [
    "Confusing Overloading with Overriding.",
    "Changing method names while overriding.",
    "Changing required parameters unnecessarily.",
    "Forgetting inheritance when overriding.",
    "Thinking Python supports true Method Overloading.",
    "Ignoring Duck Typing.",
    "Writing unnecessary if-else chains."
]

for index, mistake in enumerate(mistakes, start=1):
    print(f"{index}. {mistake}")

# =====================================================
# 14. Interview Questions
# =====================================================

print("\n===== Interview Questions =====")

questions = [
    "What is Polymorphism?",
    "Why is Polymorphism important?",
    "What is Method Overriding?",
    "What is Method Overloading?",
    "Does Python support Method Overloading?",
    "Explain Duck Typing.",
    "What is Run-Time Polymorphism?",
    "What is Compile-Time Polymorphism?",
    "Difference between Overloading and Overriding?",
    "Give a real-world example of Polymorphism."
]

for index, question in enumerate(questions, start=1):
    print(f"{index}. {question}")

# =====================================================
# 15. Best Practices
# =====================================================

print("\n===== Best Practices =====")

best_practices = [
    "Use meaningful method names.",
    "Override methods only when necessary.",
    "Prefer Polymorphism over long if-else chains.",
    "Follow the Liskov Substitution Principle.",
    "Keep Child implementations simple.",
    "Write reusable code.",
    "Use descriptive class names.",
    "Follow PEP 8 naming conventions."
]

for practice in best_practices:
    print(f"✔ {practice}")

# =====================================================
# 16. Mini Practice
# =====================================================

print("\n===== Mini Practice =====")

practice = [
    "Create an Animal Parent Class.",
    "Create Dog and Cat Child Classes.",
    "Override sound() in both classes.",
    "Create a Vehicle hierarchy.",
    "Override start() in Car and Bike.",
    "Create a Payment hierarchy.",
    "Override pay() in all Child Classes.",
    "Create a common function that calls all objects."
]

for index, item in enumerate(practice, start=1):
    print(f"{index}. {item}")

# =====================================================
# 17. Coding Challenge
# =====================================================

print("\n===== Coding Challenge =====")

print("Challenge 1")
print("- Create a Shape Parent Class.")

print("\nChallenge 2")
print("- Create Circle, Rectangle and Triangle classes.")

print("\nChallenge 3")
print("- Override draw() in each class.")

print("\nChallenge 4")
print("- Store all objects inside a list.")

print("\nChallenge 5")
print("- Use a loop to call draw().")

# =====================================================
# 18. Output Prediction
# =====================================================

print("\n===== Output Prediction =====")

print("Predict the output before running the code.\n")

print("""
class Animal:

    def sound(self):
        print("Animal Sound")


class Dog(Animal):

    def sound(self):
        print("Bark")


obj = Dog()

obj.sound()
""")

print("\nExpected Output")

print("""
Bark
""")

print("\nReason")

print(
    "Dog overrides the sound() method "
    "of the Animal class."
)

# =====================================================
# Quick Revision
# =====================================================

print("\n===== Quick Revision =====")

revision = [
    "Polymorphism means One Interface, Many Forms.",
    "Method Overriding provides Run-Time Polymorphism.",
    "Python does not support true Method Overloading.",
    "Duck Typing focuses on behavior.",
    "Built-in functions also show Polymorphism.",
    "One function can work with different objects."
]

for point in revision:
    print(f"✔ {point}")

# =====================================================
# Summary
# =====================================================

print("\n===== Summary =====")

print("✔ Polymorphism means One Interface, Many Forms.")
print("✔ Same method behaves differently for different objects.")
print("✔ Method Overriding is the most common form in Python.")
print("✔ Python uses Duck Typing.")
print("✔ Built-in and user-defined functions can be polymorphic.")
print("✔ Polymorphism improves flexibility and code reuse.")
print("✔ It works closely with Inheritance.")

# =====================================================
# End of Program
# =====================================================

print("\nCongratulations! 🎉")
print("You have successfully completed")
print("Polymorphism.")
