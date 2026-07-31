"""
=========================================================
Topic : Inheritance
File  : 05_Inheritance.py

Description:
This file explains the concept of Inheritance in Python.
You will learn how one class can inherit the properties
and methods of another class, different types of
inheritance, and their real-world applications.

Topics Covered:
1. What is Inheritance?
2. Why Do We Need Inheritance?
3. Parent Class (Base Class)
4. Child Class (Derived Class)
5. Creating Your First Inherited Class
6. Types of Inheritance
7. isinstance()
8. issubclass()
9. Advantages of Inheritance
10. Difference Between Parent and Child Class
11. Real-World Example

Author : Nikita Choudhary
Repository : Python Basics
=========================================================
"""

# =====================================================
# Inheritance
# =====================================================

print("=" * 60)
print("INHERITANCE")
print("=" * 60)

# =====================================================
# 1. What is Inheritance?
# =====================================================

print("\n===== What is Inheritance? =====")

print(
    "Inheritance is one of the four main principles "
    "of Object-Oriented Programming (OOP)."
)

print(
    "\nInheritance allows one class to acquire the "
    "properties and methods of another class."
)

print(
    "\nThe existing class is called the Parent Class "
    "and the new class is called the Child Class."
)

# =====================================================
# Syntax
# =====================================================

print("\nSyntax:\n")

print("""
class ParentClass:
    pass

class ChildClass(ParentClass):
    pass
""")

# =====================================================
# Simple Example
# =====================================================


class Animal:
    pass


class Dog(Animal):
    pass


print("Dog class successfully inherited Animal class.")

# Output:
# Dog class successfully inherited Animal class.

# =====================================================
# Another Example
# =====================================================


class Vehicle:
    pass


class Car(Vehicle):
    pass


print("Car class successfully inherited Vehicle class.")

# Output:
# Car class successfully inherited Vehicle class.

# =====================================================
# Visual Representation
# =====================================================

print("\n===== Visual Representation =====")

print("""
          Animal
             │
             │
            Dog
""")

# =====================================================
# Real-World Example
# =====================================================

print("\n===== Real-World Example =====")

print(
    "A Dog is an Animal."
)

print(
    "A Dog has all the basic characteristics of an Animal,"
)

print(
    "but it can also have its own unique characteristics."
)

print(
    "Similarly, a Child Class inherits the features "
    "of a Parent Class."
)

# =====================================================
# Explanation
# =====================================================

print("\nExplanation")

print(
    "The Dog class automatically inherits from "
    "the Animal class."
)

print(
    "This allows Dog to reuse the code written "
    "inside Animal."
)

# =====================================================
# Key Points
# =====================================================

print("\nKey Points")

print("✔ Inheritance promotes code reuse.")
print("✔ Child Class inherits Parent Class.")
print("✔ Reduces duplicate code.")
print("✔ Makes programs easier to maintain.")

# =====================================================
# Important Note
# =====================================================

print("\nImportant Note")

print(
    "Inheritance creates an 'is-a' relationship."
)

print(
    "Example:"
)

print("Dog is an Animal.")
print("Car is a Vehicle.")
print("Student is a Person.")

# =====================================================
# Remember
# =====================================================

print("\nRemember")

print("✔ Parent Class = Base Class")
print("✔ Child Class = Derived Class")

# =====================================================
# 2. Why Do We Need Inheritance?
# =====================================================

print("\n===== Why Do We Need Inheritance? =====")

print(
    "Inheritance helps us reuse existing code instead "
    "of writing the same code again."
)

# =====================================================
# Example Without Inheritance
# =====================================================

print("\n===== Without Inheritance =====")


class Dog:

    def eat(self):
        print("Dog is eating.")

    def sleep(self):
        print("Dog is sleeping.")


class Cat:

    def eat(self):
        print("Cat is eating.")

    def sleep(self):
        print("Cat is sleeping.")


print(
    "Both classes contain similar methods."
)

print(
    "This creates duplicate code."
)

# =====================================================
# Example With Inheritance
# =====================================================

print("\n===== With Inheritance =====")


class Animal:

    def eat(self):
        print("Animal is eating.")

    def sleep(self):
        print("Animal is sleeping.")


class Dog(Animal):
    pass


dog1 = Dog()

dog1.eat()
dog1.sleep()

# Output:
# Animal is eating.
# Animal is sleeping.

# =====================================================
# Explanation
# =====================================================

print("\nExplanation")

print(
    "Dog automatically gets eat() and sleep() "
    "from the Animal class."
)

print(
    "No need to write the same methods again."
)

# =====================================================
# Real-World Example
# =====================================================

print("\n===== Real-World Example =====")

print(
    "Imagine a company with hundreds of employees."
)

print(
    "Every employee has common details like "
    "name, employee ID, and department."
)

print(
    "Instead of writing the same code for "
    "Manager, Developer, and Designer separately,"
)

print(
    "we can create one Employee class and let "
    "other classes inherit from it."
)

# =====================================================
# Key Points
# =====================================================

print("\nKey Points")

print("✔ Reuses existing code.")
print("✔ Reduces duplication.")
print("✔ Improves maintainability.")
print("✔ Makes programs scalable.")

# =====================================================
# Remember
# =====================================================

print("\nRemember")

print(
    "Inheritance follows the DRY Principle."
)

print(
    "DRY = Don't Repeat Yourself."
)

# =====================================================
# 3. Parent Class (Base Class)
# =====================================================

print("\n===== Parent Class (Base Class) =====")

print(
    "A Parent Class is the class whose properties "
    "and methods are inherited by another class."
)

# =====================================================
# Syntax
# =====================================================

print("\nSyntax:\n")

print("""
class ParentClass:
    pass
""")

# =====================================================
# Simple Example
# =====================================================


class Animal:

    def sound(self):
        print("Animals make different sounds.")


animal1 = Animal()

animal1.sound()

# Output:
# Animals make different sounds.

# =====================================================
# Another Example
# =====================================================


class Vehicle:

    def start(self):
        print("Vehicle Started.")


vehicle1 = Vehicle()

vehicle1.start()

# Output:
# Vehicle Started.

# =====================================================
# Explanation
# =====================================================

print("\nExplanation")

print(
    "The Parent Class provides common features "
    "that can be shared with Child Classes."
)

# =====================================================
# Key Points
# =====================================================

print("\nKey Points")

print("✔ Also called Base Class.")
print("✔ Contains common functionality.")
print("✔ Can have multiple Child Classes.")

# =====================================================
# Remember
# =====================================================

print("\nRemember")

print("✔ Parent Class shares common code.")

# =====================================================
# 4. Child Class (Derived Class)
# =====================================================

print("\n===== Child Class (Derived Class) =====")

print(
    "A Child Class inherits the properties and "
    "methods of a Parent Class."
)

print(
    "It can also have its own additional methods "
    "and variables."
)

# =====================================================
# Syntax
# =====================================================

print("\nSyntax:\n")

print("""
class ChildClass(ParentClass):
    pass
""")

# =====================================================
# Simple Example
# =====================================================


class Animal:

    def eat(self):
        print("Animal is eating.")


class Dog(Animal):
    pass


dog1 = Dog()

dog1.eat()

# Output:
# Animal is eating.

# =====================================================
# Another Example
# =====================================================


class Person:

    def introduce(self):
        print("Hello!")


class Student(Person):
    pass


student1 = Student()

student1.introduce()

# Output:
# Hello!

# =====================================================
# Visual Representation
# =====================================================

print("\n===== Visual Representation =====")

print("""
             Person
                │
                │
            Student
""")

# =====================================================
# Explanation
# =====================================================

print("\nExplanation")

print(
    "Student automatically gets the introduce() "
    "method from Person."
)

print(
    "No additional code is required in Student."
)

# =====================================================
# Key Points
# =====================================================

print("\nKey Points")

print("✔ Also called Derived Class.")
print("✔ Reuses Parent Class features.")
print("✔ Can add new features.")
print("✔ Can modify inherited behavior.")

# =====================================================
# Important Note
# =====================================================

print("\nImportant Note")

print(
    "A Child Class does not copy the Parent Class."
)

print(
    "Instead, it gains access to the Parent Class "
    "through inheritance."
)

# =====================================================
# Remember
# =====================================================

print("\nRemember")

print("✔ Parent → Shares Features")
print("✔ Child → Inherits Features")

# =====================================================
# 5. Creating Your First Inherited Class
# =====================================================

print("\n===== Creating Your First Inherited Class =====")

print(
    "Let's create our first Parent Class and Child Class."
)

# =====================================================
# Visual Representation
# =====================================================

print("\n===== Visual Representation =====")

print("""
            Animal
               │
               │
              Dog
""")

# =====================================================
# Syntax
# =====================================================

print("\nSyntax:\n")

print("""
class Animal:
    pass

class Dog(Animal):
    pass
""")

# =====================================================
# Simple Example
# =====================================================


class Animal:

    def eat(self):
        print("Animal is eating.")


class Dog(Animal):
    pass


dog1 = Dog()

dog1.eat()

# Output:
# Animal is eating.

# =====================================================
# Another Example
# =====================================================


class Vehicle:

    def start(self):
        print("Vehicle Started.")


class Car(Vehicle):
    pass


car1 = Car()

car1.start()

# Output:
# Vehicle Started.

# =====================================================
# Real-World Example
# =====================================================

print("\n===== Real-World Example =====")

print(
    "A Car is a Vehicle."
)

print(
    "Every Car can use the common features of a Vehicle,"
)

print(
    "such as starting and stopping."
)

print(
    "Instead of writing those features again,"
)

print(
    "Car simply inherits them from Vehicle."
)

# =====================================================
# Explanation
# =====================================================

print("\nExplanation")

print(
    "The Dog object can call eat() even though "
    "the method is not written inside the Dog class."
)

print(
    "The method is inherited from the Animal class."
)

# =====================================================
# Key Points
# =====================================================

print("\nKey Points")

print("✔ Child Class inherits Parent Class.")
print("✔ Parent methods are directly available.")
print("✔ No duplicate code is required.")
print("✔ Improves code reusability.")

# =====================================================
# Remember
# =====================================================

print("\nRemember")

print("✔ Dog inherits Animal.")
print("✔ Car inherits Vehicle.")

# =====================================================
# 6. Single Inheritance
# =====================================================

print("\n===== Single Inheritance =====")

print(
    "Single Inheritance means one Child Class "
    "inherits from one Parent Class."
)

# =====================================================
# Visual Representation
# =====================================================

print("\n===== Visual Representation =====")

print("""
          Animal
             │
             │
            Dog
""")

# =====================================================
# Syntax
# =====================================================

print("\nSyntax:\n")

print("""
class Parent:
    pass

class Child(Parent):
    pass
""")

# =====================================================
# Simple Example
# =====================================================


class Animal:

    def sound(self):
        print("Animals make different sounds.")


class Dog(Animal):

    def bark(self):
        print("Dog barks.")


dog1 = Dog()

dog1.sound()
dog1.bark()

# Output:
# Animals make different sounds.
# Dog barks.

# =====================================================
# Another Example
# =====================================================


class Person:

    def introduce(self):
        print("Hello! I am a Person.")


class Student(Person):

    def study(self):
        print("Student is studying.")


student1 = Student()

student1.introduce()
student1.study()

# Output:
# Hello! I am a Person.
# Student is studying.

# =====================================================
# Real-World Example
# =====================================================

print("\n===== Real-World Example =====")

print(
    "A Student is a Person."
)

print(
    "A Student automatically has the basic "
    "features of a Person."
)

print(
    "Additionally, the Student class can have "
    "its own unique features."
)

# =====================================================
# Explanation
# =====================================================

print("\nExplanation")

print(
    "Student inherits introduce() from Person."
)

print(
    "Student also defines its own study() method."
)

# =====================================================
# Key Points
# =====================================================

print("\nKey Points")

print("✔ One Parent Class.")
print("✔ One Child Class.")
print("✔ Simplest type of Inheritance.")
print("✔ Most commonly used.")

# =====================================================
# Remember
# =====================================================

print("\nRemember")

print("✔ One Parent → One Child")

# =====================================================
# 7. Multiple Inheritance
# =====================================================

print("\n===== Multiple Inheritance =====")

print(
    "Multiple Inheritance means one Child Class "
    "inherits from more than one Parent Class."
)

# =====================================================
# Visual Representation
# =====================================================

print("\n===== Visual Representation =====")

print("""
        Father        Mother
            \\        /
             \\      /
              \\    /
               Child
""")

# =====================================================
# Syntax
# =====================================================

print("\nSyntax:\n")

print("""
class Parent1:
    pass

class Parent2:
    pass

class Child(Parent1, Parent2):
    pass
""")

# =====================================================
# Simple Example
# =====================================================


class Father:

    def skills_from_father(self):
        print("Cricket")


class Mother:

    def skills_from_mother(self):
        print("Painting")


class Child(Father, Mother):
    pass


child1 = Child()

child1.skills_from_father()
child1.skills_from_mother()

# Output:
# Cricket
# Painting

# =====================================================
# Another Example
# =====================================================


class Camera:

    def click_photo(self):
        print("Photo Clicked")


class MusicPlayer:

    def play_music(self):
        print("Playing Music")


class Smartphone(Camera, MusicPlayer):
    pass


phone1 = Smartphone()

phone1.click_photo()
phone1.play_music()

# Output:
# Photo Clicked
# Playing Music

# =====================================================
# Real-World Example
# =====================================================

print("\n===== Real-World Example =====")

print(
    "A Smartphone works as a Camera and also "
    "as a Music Player."
)

print(
    "Instead of rewriting both functionalities,"
)

print(
    "the Smartphone class inherits them."
)

# =====================================================
# Explanation
# =====================================================

print("\nExplanation")

print(
    "Child inherits features from multiple Parent Classes."
)

print(
    "This increases code reuse."
)

# =====================================================
# Key Points
# =====================================================

print("\nKey Points")

print("✔ Multiple Parent Classes.")
print("✔ One Child Class.")
print("✔ Reuses features from different classes.")
print("✔ Useful in complex applications.")

# =====================================================
# Important Note
# =====================================================

print("\nImportant Note")

print(
    "Multiple Inheritance can sometimes create ambiguity."
)

print(
    "Python resolves this using MRO (Method Resolution Order)."
)

print(
    "We will study MRO in detail in later chapters."
)

# =====================================================
# Remember
# =====================================================

print("\nRemember")

print("✔ Multiple Parents → One Child")
print("✔ Python uses MRO to resolve conflicts.")

# =====================================================
# 8. Multilevel Inheritance
# =====================================================

print("\n===== Multilevel Inheritance =====")

print(
    "Multilevel Inheritance occurs when one Child Class "
    "inherits another Child Class."
)

# =====================================================
# Visual Representation
# =====================================================

print("\n===== Visual Representation =====")

print("""
            Animal
               │
               │
            Mammal
               │
               │
              Dog
""")

# =====================================================
# Syntax
# =====================================================

print("\nSyntax:\n")

print("""
class A:
    pass

class B(A):
    pass

class C(B):
    pass
""")

# =====================================================
# Simple Example
# =====================================================


class Animal:

    def eat(self):
        print("Animal is eating.")


class Mammal(Animal):

    def walk(self):
        print("Mammal can walk.")


class Dog(Mammal):

    def bark(self):
        print("Dog barks.")


dog1 = Dog()

dog1.eat()
dog1.walk()
dog1.bark()

# Output:
# Animal is eating.
# Mammal can walk.
# Dog barks.

# =====================================================
# Another Example
# =====================================================


class LivingThing:

    def breathe(self):
        print("Breathing...")


class Person(LivingThing):

    def speak(self):
        print("Speaking...")


class Student(Person):

    def study(self):
        print("Studying...")


student1 = Student()

student1.breathe()
student1.speak()
student1.study()

# Output:
# Breathing...
# Speaking...
# Studying...

# =====================================================
# Real-World Example
# =====================================================

print("\n===== Real-World Example =====")

print("Animal → Mammal → Dog")

print(
    "A Dog has the characteristics of both "
    "Animal and Mammal."
)

# =====================================================
# Explanation
# =====================================================

print("\nExplanation")

print(
    "Dog inherits from Mammal."
)

print(
    "Mammal already inherits from Animal."
)

print(
    "Therefore, Dog can use methods from both classes."
)

# =====================================================
# Key Points
# =====================================================

print("\nKey Points")

print("✔ Parent → Child → Grandchild")
print("✔ Features are inherited step by step.")
print("✔ Promotes maximum code reuse.")

# =====================================================
# Remember
# =====================================================

print("\nRemember")

print("✔ One inheritance chain with multiple levels.")

# =====================================================
# 9. Hierarchical Inheritance
# =====================================================

print("\n===== Hierarchical Inheritance =====")

print(
    "Hierarchical Inheritance occurs when multiple "
    "Child Classes inherit from one Parent Class."
)

# =====================================================
# Visual Representation
# =====================================================

print("\n===== Visual Representation =====")

print("""
                Animal
              /    |    \\
             /     |     \\
           Dog    Cat    Cow
""")

# =====================================================
# Syntax
# =====================================================

print("\nSyntax:\n")

print("""
class Parent:
    pass

class Child1(Parent):
    pass

class Child2(Parent):
    pass
""")

# =====================================================
# Example
# =====================================================


class Animal:

    def eat(self):
        print("Animal is eating.")


class Dog(Animal):

    def bark(self):
        print("Dog barks.")


class Cat(Animal):

    def meow(self):
        print("Cat meows.")


dog1 = Dog()
cat1 = Cat()

dog1.eat()
dog1.bark()

cat1.eat()
cat1.meow()

# Output:
# Animal is eating.
# Dog barks.
# Animal is eating.
# Cat meows.

# =====================================================
# Real-World Example
# =====================================================

print("\n===== Real-World Example =====")

print(
    "One Person class can have multiple child classes "
    "such as Student, Teacher, and Employee."
)

# =====================================================
# Explanation
# =====================================================

print("\nExplanation")

print(
    "Dog and Cat inherit the common features "
    "from Animal."
)

print(
    "Each child class can also have its own methods."
)

# =====================================================
# Key Points
# =====================================================

print("\nKey Points")

print("✔ One Parent Class.")
print("✔ Multiple Child Classes.")
print("✔ Common functionality is shared.")

# =====================================================
# Remember
# =====================================================

print("\nRemember")

print("✔ One Parent → Many Children")

# =====================================================
# 10. Hybrid Inheritance
# =====================================================

print("\n===== Hybrid Inheritance =====")

print(
    "Hybrid Inheritance is a combination of two or more "
    "types of inheritance."
)

print(
    "It usually combines Single, Multiple, "
    "Multilevel, or Hierarchical Inheritance."
)

# =====================================================
# Visual Representation
# =====================================================

print("\n===== Visual Representation =====")

print("""
             A
           /   \\
          B     C
           \\   /
             D
""")

# =====================================================
# Important Note
# =====================================================

print("\nImportant Note")

print(
    "Hybrid Inheritance often creates complexity."
)

print(
    "Python supports it, but developers should use it "
    "carefully."
)

print(
    "Method Resolution Order (MRO) helps Python decide "
    "which method should be called."
)

# =====================================================
# Example
# =====================================================


class A:

    def show_a(self):
        print("Class A")


class B(A):

    def show_b(self):
        print("Class B")


class C(A):

    def show_c(self):
        print("Class C")


class D(B, C):

    def show_d(self):
        print("Class D")


obj = D()

obj.show_a()
obj.show_b()
obj.show_c()
obj.show_d()

# Output:
# Class A
# Class B
# Class C
# Class D

# =====================================================
# Key Points
# =====================================================

print("\nKey Points")

print("✔ Combination of inheritance types.")
print("✔ Can become complex.")
print("✔ Python uses MRO to resolve ambiguity.")

# =====================================================
# Remember
# =====================================================

print("\nRemember")

print("✔ Hybrid = Combination of inheritance types.")

# =====================================================
# 11. isinstance() Function
# =====================================================

print("\n===== isinstance() Function =====")

print(
    "isinstance() checks whether an object belongs "
    "to a particular class."
)

print("\nSyntax:\n")

print("""
isinstance(object, ClassName)
""")

# =====================================================
# Example
# =====================================================


class Animal:
    pass


class Dog(Animal):
    pass


dog1 = Dog()

print(isinstance(dog1, Dog))
print(isinstance(dog1, Animal))

# Output:
# True
# True

# =====================================================
# Explanation
# =====================================================

print("\nExplanation")

print(
    "dog1 is an object of Dog."
)

print(
    "Since Dog inherits Animal,"
)

print(
    "dog1 is also considered an Animal object."
)

# =====================================================
# Remember
# =====================================================

print("\nRemember")

print("✔ Returns True or False.")

# =====================================================
# 12. issubclass() Function
# =====================================================

print("\n===== issubclass() Function =====")

print(
    "issubclass() checks whether one class "
    "inherits another class."
)

print("\nSyntax:\n")

print("""
issubclass(ChildClass, ParentClass)
""")

# =====================================================
# Example
# =====================================================


class Animal:
    pass


class Dog(Animal):
    pass


print(issubclass(Dog, Animal))
print(issubclass(Animal, Dog))

# Output:
# True
# False

# =====================================================
# Explanation
# =====================================================

print("\nExplanation")

print(
    "Dog is derived from Animal."
)

print(
    "Animal is not derived from Dog."
)

# =====================================================
# Key Points
# =====================================================

print("\nKey Points")

print("✔ Works with classes.")
print("✔ Returns True or False.")
print("✔ Checks inheritance relationships.")

# =====================================================
# Remember
# =====================================================

print("\nRemember")

print("✔ isinstance() → Object")
print("✔ issubclass() → Class")

# =====================================================
# 13. Advantages of Inheritance
# =====================================================

print("\n===== Advantages of Inheritance =====")

advantages = [
    "Promotes code reusability.",
    "Reduces duplicate code.",
    "Improves code organization.",
    "Makes programs easier to maintain.",
    "Supports code extensibility.",
    "Makes large projects easier to manage.",
    "Represents real-world relationships naturally.",
    "Provides a strong foundation for Polymorphism."
]

for advantage in advantages:
    print(f"✔ {advantage}")

# =====================================================
# Explanation
# =====================================================

print("\nExplanation")

print(
    "Inheritance allows developers to reuse existing code "
    "instead of writing the same functionality again."
)

print(
    "This makes programs cleaner, shorter, and easier "
    "to maintain."
)

# =====================================================
# Remember
# =====================================================

print("\nRemember")

print("✔ Inheritance mainly focuses on code reuse.")

# =====================================================
# 14. Difference Between Parent Class and Child Class
# =====================================================

print("\n===== Difference Between Parent Class and Child Class =====")

comparison = [
    ("Meaning", "Base Class", "Derived Class"),
    ("Purpose", "Provides Common Features", "Uses and Extends Features"),
    ("Inheritance", "Cannot inherit itself", "Inherits Parent Class"),
    ("Methods", "Defines Common Methods", "Can Use and Add Methods"),
    ("Variables", "Defines Common Variables", "Can Add New Variables"),
]

print(
    f"{'Feature':<18}"
    f"{'Parent Class':<28}"
    f"{'Child Class'}"
)

print("-" * 80)

for feature, parent, child in comparison:
    print(
        f"{feature:<18}"
        f"{parent:<28}"
        f"{child}"
    )

# =====================================================
# 15. Real-World Example
# =====================================================

print("\n===== Real-World Example =====")


class Employee:

    def __init__(self, name):
        self.name = name

    def company(self):
        print(f"{self.name} works at ABC Technologies.")


class Developer(Employee):

    def coding(self):
        print(f"{self.name} writes Python code.")


class Manager(Employee):

    def manage_team(self):
        print(f"{self.name} manages the development team.")


developer1 = Developer("Nikita")
manager1 = Manager("Rahul")

developer1.company()
developer1.coding()

print()

manager1.company()
manager1.manage_team()

# Output:
# Nikita works at ABC Technologies.
# Nikita writes Python code.
#
# Rahul works at ABC Technologies.
# Rahul manages the development team.

# =====================================================
# Explanation
# =====================================================

print("\nExplanation")

print(
    "Developer and Manager inherit the common "
    "company() method from Employee."
)

print(
    "Each Child Class also has its own unique method."
)

# =====================================================
# 16. Common Mistakes
# =====================================================

print("\n===== Common Mistakes =====")

mistakes = [
    "Confusing Parent Class with Child Class.",
    "Creating inheritance where it is not required.",
    "Forgetting to inherit the Parent Class.",
    "Writing duplicate code instead of reusing Parent methods.",
    "Assuming Child Class copies Parent Class.",
    "Using Multiple Inheritance unnecessarily.",
    "Ignoring Method Resolution Order (MRO)."
]

for index, mistake in enumerate(mistakes, start=1):
    print(f"{index}. {mistake}")

# =====================================================
# 17. Interview Questions
# =====================================================

print("\n===== Interview Questions =====")

questions = [
    "What is Inheritance?",
    "Why do we use Inheritance?",
    "What is a Parent Class?",
    "What is a Child Class?",
    "What is Single Inheritance?",
    "What is Multiple Inheritance?",
    "What is Multilevel Inheritance?",
    "What is Hierarchical Inheritance?",
    "What is Hybrid Inheritance?",
    "What is isinstance()?",
    "What is issubclass()?",
    "What are the advantages of Inheritance?"
]

for index, question in enumerate(questions, start=1):
    print(f"{index}. {question}")

# =====================================================
# 18. Best Practices
# =====================================================

print("\n===== Best Practices =====")

best_practices = [
    "Use inheritance only when an 'is-a' relationship exists.",
    "Keep Parent Classes simple and reusable.",
    "Avoid unnecessary Multiple Inheritance.",
    "Reuse code instead of duplicating it.",
    "Use meaningful class names.",
    "Follow PEP 8 naming conventions.",
    "Design Child Classes with a single responsibility.",
    "Write clean and readable code."
]

for practice in best_practices:
    print(f"✔ {practice}")

# =====================================================
# 19. Mini Practice
# =====================================================

print("\n===== Mini Practice =====")

practice_questions = [
    "Create an Animal Parent Class.",
    "Create a Dog Child Class.",
    "Create a Vehicle Parent Class.",
    "Create a Bike Child Class.",
    "Create an Employee Parent Class.",
    "Create Manager and Developer Child Classes.",
    "Create a Multilevel Inheritance example.",
    "Create a Hierarchical Inheritance example.",
    "Use isinstance() in your program.",
    "Use issubclass() in your program."
]

for index, question in enumerate(practice_questions, start=1):
    print(f"{index}. {question}")

# =====================================================
# 20. Coding Challenge
# =====================================================

print("\n===== Coding Challenge =====")

print("Challenge 1")
print("- Create a Person class.")

print("\nChallenge 2")
print("- Create a Student class that inherits Person.")

print("\nChallenge 3")
print("- Create a Teacher class that inherits Person.")

print("\nChallenge 4")
print("- Add one common method inside Person.")

print("\nChallenge 5")
print("- Add one unique method inside Student.")

print("\nChallenge 6")
print("- Add one unique method inside Teacher.")

print("\nChallenge 7")
print("- Create objects and call all inherited methods.")

# =====================================================
# 21. Output Prediction
# =====================================================

print("\n===== Output Prediction =====")

print("Predict the output before running the code.\n")

print("""
class Animal:

    def eat(self):
        print("Eating...")

class Dog(Animal):
    pass

dog = Dog()

dog.eat()
""")

print("\nExpected Output")

print("""
Eating...
""")

print("\nReason")

print(
    "Dog inherits the eat() method from the Animal class."
)

# =====================================================
# Quick Revision
# =====================================================

print("\n===== Quick Revision =====")

revision = [
    "Inheritance promotes code reuse.",
    "Parent Class is also called Base Class.",
    "Child Class is also called Derived Class.",
    "Python supports five types of Inheritance.",
    "isinstance() works with objects.",
    "issubclass() works with classes.",
    "Inheritance creates an 'is-a' relationship."
]

for point in revision:
    print(f"✔ {point}")

# =====================================================
# Summary
# =====================================================

print("\n===== Summary =====")

print("✔ Inheritance allows one class to inherit another class.")
print("✔ Parent Class provides common features.")
print("✔ Child Class reuses and extends those features.")
print("✔ Inheritance reduces duplicate code.")
print("✔ Python supports five types of Inheritance.")
print("✔ isinstance() checks objects.")
print("✔ issubclass() checks classes.")
print("✔ Inheritance is the foundation of Polymorphism.")

# =====================================================
# End of Program
# =====================================================

print("\nCongratulations! 🎉")
print("You have successfully completed")
print("Inheritance.")