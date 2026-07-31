"""
=========================================================
Topic : Classes and Objects
File  : 02_Classes_and_Objects.py

Description:
This file introduces the fundamental concepts of
Classes and Objects in Python. It explains how to
create classes, create objects, understand their
relationship, and build a strong foundation for OOP.

Topics Covered:
1. What is a Class?
2. What is an Object?
3. Why Do We Need Classes?
4. Creating a Class
5. Creating Objects
6. Multiple Objects
7. Class Attributes
8. Instance Attributes
9. Instance Methods
10. Class vs Object
11. Relationship Between Class and Object

Author : Nikita Choudhary
Repository : Python Basics
=========================================================
"""

# =====================================================
# Classes and Objects
# =====================================================

print("=" * 60)
print("CLASSES AND OBJECTS")
print("=" * 60)

# =====================================================
# 1. What is a Class?
# =====================================================

print("\n===== What is a Class? =====")

print(
    "A Class is a blueprint or template used to create "
    "objects. It defines the attributes (data) and "
    "methods (behavior) that objects will have."
)

print(
    "\nThink of a class as a design or blueprint of a "
    "real-world object."
)

# =====================================================
# Simple Example
# =====================================================

print("\n===== Simple Class Example =====")


class Student:
    pass


print("Student class created successfully.")

# =====================================================
# Another Example
# =====================================================


class Car:
    pass


print("Car class created successfully.")

# =====================================================
# Remember
# =====================================================

print("\nRemember")

print("✔ A class is only a blueprint.")
print("✔ A class does not represent a real object.")
print("✔ Objects are created using a class.")

# =====================================================
# 2. What is an Object?
# =====================================================

print("\n===== What is an Object? =====")

print(
    "An Object is an instance of a class."
)

print(
    "\nObjects contain actual data and can perform "
    "the behaviors defined inside the class."
)

# =====================================================
# Simple Example
# =====================================================

print("\n===== Object Example =====")

student1 = Student()

print("Object Created Successfully.")
print(student1)

# =====================================================
# Another Example
# =====================================================

car1 = Car()

print("\nAnother Object Created Successfully.")
print(car1)

# =====================================================
# Remember
# =====================================================

print("\nRemember")

print("✔ One class can create many objects.")
print("✔ Every object has its own identity.")
print("✔ Objects are created using the class name.")

# =====================================================
# 3. Why Do We Need Classes?
# =====================================================

print("\n===== Why Do We Need Classes? =====")

reasons = [
    "Organize code efficiently",
    "Represent real-world objects",
    "Reduce code duplication",
    "Improve code reusability",
    "Make programs easier to maintain",
    "Support Object-Oriented Programming"
]

for reason in reasons:
    print(f"✔ {reason}")

print(
    "\nWithout classes, managing large applications "
    "becomes difficult because related data and "
    "functions remain separate."
)

# =====================================================
# 4. Creating a Class
# =====================================================

print("\n===== Creating a Class =====")

print("Syntax:\n")

print("""
class ClassName:
    pass
""")

print("Example:\n")


class Book:
    pass


print("Book class created successfully.")

# =====================================================
# 5. Creating Objects
# =====================================================

print("\n===== Creating Objects =====")

print("Syntax:\n")

print("""
object_name = ClassName()
""")

book1 = Book()

print("Book object created successfully.")

print(book1)

print(
    "\nAn object is created by calling the class "
    "just like a function."
)

# =====================================================
# 6. Multiple Objects
# =====================================================

print("\n===== Multiple Objects =====")


class Mobile:
    pass


mobile1 = Mobile()
mobile2 = Mobile()
mobile3 = Mobile()

print("Three Mobile objects created.\n")

print("Object 1 :", mobile1)
print("Object 2 :", mobile2)
print("Object 3 :", mobile3)

print(
    "\nAlthough all three objects are created from "
    "the same class, each object has a different "
    "memory address and identity."
)

# =====================================================
# Visual Representation
# =====================================================

print("\n===== Visual Representation =====")

print("""
                  Mobile (Class)
                       │
        ┌──────────────┼──────────────┐
        │              │              │
     mobile1       mobile2       mobile3
      Object         Object         Object
""")

# =====================================================
# 7. Class Attributes
# =====================================================

print("\n===== Class Attributes =====")

print(
    "A Class Attribute is shared by all objects of a class."
)

print(
    "It is defined directly inside the class and outside "
    "any method."
)

print("\nSyntax:\n")

print("""
class ClassName:
    class_attribute = value
""")

# =====================================================
# Example 1
# =====================================================


class Student:

    school_name = "ABC Public School"


print("School Name :", Student.school_name)

# =====================================================
# Example 2
# =====================================================

student1 = Student()
student2 = Student()

print("\nAccessing using Objects")

print(student1.school_name)
print(student2.school_name)

print(
    "\nBoth objects share the same class attribute."
)

# =====================================================
# Modifying Class Attribute
# =====================================================

print("\n===== Modifying Class Attribute =====")

print("Before Modification")

print(student1.school_name)
print(student2.school_name)

Student.school_name = "XYZ Public School"

print("\nAfter Modification")

print(student1.school_name)
print(student2.school_name)

print(
    "\nChanging the class attribute affects all objects."
)

# =====================================================
# Remember
# =====================================================

print("\nRemember")

print("✔ Shared by all objects.")
print("✔ Defined inside the class.")
print("✔ Access using ClassName.attribute")

# =====================================================
# 8. Instance Attributes
# =====================================================

print("\n===== Instance Attributes =====")

print(
    "Instance Attributes belong to individual objects."
)

print(
    "Each object can store different values."
)

print(
    "\nNOTE:"
)

print(
    "For now, we are creating attributes outside the class "
    "only to understand the concept."
)

print(
    "In real projects, instance attributes are usually "
    "created inside the constructor (__init__)."
)

# =====================================================
# Example 1
# =====================================================


class Employee:
    pass


employee1 = Employee()

employee1.name = "Nikita"
employee1.department = "AI"

print("\nEmployee 1")

print("Name       :", employee1.name)
print("Department :", employee1.department)

# =====================================================
# Example 2
# =====================================================

employee2 = Employee()

employee2.name = "Rahul"
employee2.department = "HR"

print("\nEmployee 2")

print("Name       :", employee2.name)
print("Department :", employee2.department)

print(
    "\nEach object stores its own instance attributes."
)

# =====================================================
# Modifying Instance Attribute
# =====================================================

print("\n===== Modifying Instance Attribute =====")

print("Before Modification")

print(employee1.name)

employee1.name = "Anjali"

print("\nAfter Modification")

print(employee1.name)

print("\nEmployee 2 Name")

print(employee2.name)

print(
    "\nChanging one object's attribute does not affect "
    "other objects."
)

# =====================================================
# Remember
# =====================================================

print("\nRemember")

print("✔ Every object has its own data.")
print("✔ Instance attributes are not shared.")
print("✔ Changing one object does not change others.")

# =====================================================
# 9. Class Attribute vs Instance Attribute
# =====================================================

print("\n===== Class Attribute vs Instance Attribute =====")

comparison = [
    ("Shared", "Yes", "No"),
    ("Belongs To", "Class", "Object"),
    ("Copy", "One", "Each Object"),
    ("Access", "Class/Object", "Object"),
]

print(f"{'Feature':<18}{'Class':<15}{'Instance'}")
print("-" * 48)

for feature, class_attr, instance_attr in comparison:
    print(f"{feature:<18}{class_attr:<15}{instance_attr}")

# =====================================================
# Practical Example
# =====================================================

print("\n===== Practical Example =====")


class Laptop:

    company = "Dell"


laptop1 = Laptop()
laptop2 = Laptop()

laptop1.model = "Inspiron 15"
laptop2.model = "XPS 13"

print("Company :", laptop1.company)
print("Model   :", laptop1.model)

print()

print("Company :", laptop2.company)
print("Model   :", laptop2.model)

print(
    "\nCompany is a Class Attribute because it is shared."
)

print(
    "Model is an Instance Attribute because each laptop "
    "has a different model."
)

# =====================================================
# 10. Instance Methods
# =====================================================

print("\n===== Instance Methods =====")

print(
    "An Instance Method is a method that belongs to "
    "an object. It works with the data of that object."
)

print(
    "\nInstance methods always use 'self' as their "
    "first parameter."
)

print("\nSyntax:\n")

print("""
class ClassName:

    def method_name(self):
        pass
""")

# =====================================================
# Example 1
# =====================================================


class Student:

    def introduce(self):

        print("Hello, Welcome to Python OOP.")


student1 = Student()

student1.introduce()

# =====================================================
# Example 2
# =====================================================


class Car:

    def start(self):

        print("Car Started Successfully.")


car1 = Car()

car1.start()

# =====================================================
# Example 3
# =====================================================


class Mobile:

    def call(self):

        print("Calling...")


mobile1 = Mobile()

mobile1.call()

print(
    "\nDifferent classes can have different methods "
    "based on their behavior."
)

# =====================================================
# Remember
# =====================================================

print("\nRemember")

print("✔ Instance methods belong to objects.")
print("✔ They always use 'self'.")
print("✔ They define the behavior of objects.")

# =====================================================
# 11. Class vs Object
# =====================================================

print("\n===== Class vs Object =====")

comparison = [
    ("Meaning", "Blueprint", "Real Instance"),
    ("Memory", "No", "Yes"),
    ("Creation", "Defined Once", "Created Many Times"),
    ("Purpose", "Template", "Use the Template"),
]

print(f"{'Feature':<15}{'Class':<18}{'Object'}")
print("-" * 50)

for feature, class_value, object_value in comparison:
    print(f"{feature:<15}{class_value:<18}{object_value}")

# =====================================================
# Practical Example
# =====================================================

print("\n===== Practical Example =====")


class Book:
    pass


book1 = Book()
book2 = Book()

print("Class  :", Book)

print("\nObjects")

print(book1)
print(book2)

print(
    "\nBook is the Class."
)

print(
    "book1 and book2 are Objects created from the Book class."
)

# =====================================================
# 12. Relationship Between Class and Object
# =====================================================

print("\n===== Relationship Between Class and Object =====")

print("""
                Class
                  │
      Blueprint / Template
                  │
      ┌───────────┼───────────┐
      │           │           │
   Object1     Object2     Object3
""")

print(
    "One class can create multiple objects."
)

print(
    "Every object is an independent instance "
    "of the same class."
)

# =====================================================
# Another Example
# =====================================================


class Employee:
    pass


employee1 = Employee()
employee2 = Employee()
employee3 = Employee()

print("\nThree Employee objects created successfully.")

print(employee1)
print(employee2)
print(employee3)

# =====================================================
# 13. Real-World Example
# =====================================================

print("\n===== Real-World Example =====")

print("Example 1 : Student")

print(
    "\nA School first defines what information every "
    "student should have."
)

print(
    "Examples:"
)

student_properties = [
    "Name",
    "Age",
    "Roll Number",
    "Grade"
]

for item in student_properties:
    print(f"• {item}")

print(
    "\nEvery student in the school is an object "
    "created from the Student class."
)

print("\nExample 2 : Bank Account")

print(
    "\nA Bank creates thousands of accounts using "
    "the same structure."
)

print(
    "Every account has:"
)

bank_properties = [
    "Account Number",
    "Account Holder",
    "Balance",
    "IFSC Code"
]

for item in bank_properties:
    print(f"• {item}")

print(
    "\nEach account stores different values, "
    "but all follow the same blueprint."
)

# =====================================================
# Visual Representation
# =====================================================

print("\n===== Visual Representation =====")

print("""
                Student Class
          +-----------------------+
          | Name                  |
          | Age                   |
          | introduce()           |
          +-----------------------+
                /          \\
               /            \\
              /              \\
        student1         student2

      Name = Nikita     Name = Rahul
      Age  = 20         Age  = 21
""")

print(
    "The Student class is created only once, "
    "but many Student objects can be created."
)

# =====================================================
# 14. Common Mistakes
# =====================================================

print("\n===== Common Mistakes =====")

mistakes = [
    "Thinking a Class and an Object are the same.",
    "Creating unnecessary classes.",
    "Using meaningless class names.",
    "Forgetting to create an object before calling methods.",
    "Confusing Class Attributes with Instance Attributes.",
    "Writing all logic inside one class.",
    "Ignoring proper naming conventions."
]

for index, mistake in enumerate(mistakes, start=1):
    print(f"{index}. {mistake}")

# =====================================================
# 15. Interview Questions
# =====================================================

print("\n===== Interview Questions =====")

questions = [
    "What is a Class?",
    "What is an Object?",
    "What is the difference between a Class and an Object?",
    "Why do we use Classes?",
    "Can one Class create multiple Objects?",
    "What is a Class Attribute?",
    "What is an Instance Attribute?",
    "What is an Instance Method?",
    "What is the relationship between a Class and an Object?",
    "Give a real-world example of a Class and an Object."
]

for index, question in enumerate(questions, start=1):
    print(f"{index}. {question}")

# =====================================================
# 16. Best Practices
# =====================================================

print("\n===== Best Practices =====")

best_practices = [
    "Use meaningful class names.",
    "Follow PascalCase for class names.",
    "Keep one responsibility for each class.",
    "Use class attributes only for shared data.",
    "Use instance attributes for object-specific data.",
    "Keep methods small and readable.",
    "Write clean and well-formatted code."
]

for practice in best_practices:
    print(f"✔ {practice}")

# =====================================================
# 17. Mini Practice
# =====================================================

print("\n===== Mini Practice =====")

practice_questions = [
    "Create a Student class.",
    "Create three Student objects.",
    "Create a Car class.",
    "Create two Car objects.",
    "Create a Book class.",
    "Add title and author as instance attributes.",
    "Create a Mobile class.",
    "Create an instance method named call().",
    "Identify one Class Attribute and one Instance Attribute.",
    "Explain the relationship between a Class and an Object."
]

for index, question in enumerate(practice_questions, start=1):
    print(f"{index}. {question}")

# =====================================================
# 18. Coding Challenge
# =====================================================

print("\n===== Coding Challenge =====")

print("Challenge 1")
print("- Create an Employee class.")

print("\nChallenge 2")
print("- Create three Employee objects.")

print("\nChallenge 3")
print("- Add name and department as instance attributes.")

print("\nChallenge 4")
print("- Create an introduce() method.")

print("\nChallenge 5")
print("- Print details of all employees.")

# =====================================================
# 19. Output Prediction
# =====================================================

print("\n===== Output Prediction =====")

print("Predict the output before running the code.\n")

print("""
class Student:
    pass

student1 = Student()
student2 = Student()

print(student1 == student2)
""")

print("Think Carefully...")
print("Both objects are created from the same class.")
print("Will the output be True or False?")

print("\nExpected Output")
print("False")

print(
    "\nReason:"
)

print(
    "student1 and student2 are different objects stored "
    "at different memory locations."
)

# =====================================================
# Quick Revision
# =====================================================

print("\n===== Quick Revision =====")

revision = [
    "A Class is a blueprint.",
    "An Object is an instance of a class.",
    "One Class can create many Objects.",
    "Class Attributes are shared.",
    "Instance Attributes belong to individual objects.",
    "Instance Methods define object behavior."
]

for point in revision:
    print(f"✔ {point}")

# =====================================================
# Summary
# =====================================================

print("\n===== Summary =====")

print("✔ A Class is a blueprint used to create Objects.")
print("✔ Objects are real instances of a Class.")
print("✔ One Class can create multiple Objects.")
print("✔ Class Attributes are shared among all Objects.")
print("✔ Instance Attributes store individual Object data.")
print("✔ Instance Methods define the behavior of Objects.")
print("✔ Classes and Objects are the foundation of OOP.")

# =====================================================
# End of Program
# =====================================================

print("\nCongratulations! 🎉")
print("You have successfully completed")
print("Classes and Objects.")