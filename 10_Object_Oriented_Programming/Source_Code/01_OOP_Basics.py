"""
=========================================================
Topic : Object-Oriented Programming (OOP) Basics
File  : 01_OOP_Basics.py

Description:
This file introduces the fundamentals of Object-Oriented
Programming (OOP) in Python. It explains what OOP is,
why it is used, its core features, advantages,
disadvantages, and real-world applications.

Topics Covered:
1. What is OOP?
2. Why OOP?
3. Procedural Programming vs OOP
4. Features of OOP
5. Four Pillars of OOP
6. OOP in Python
7. Real-World Example
8. Applications of OOP
9. Advantages & Disadvantages

Author : Nikita Choudhary
Repository : Python Basics
=========================================================
"""

# =====================================================
# Object-Oriented Programming (OOP)
# =====================================================

print("=" * 60)
print("OBJECT-ORIENTED PROGRAMMING (OOP)")
print("=" * 60)

# =====================================================
# 1. What is Object-Oriented Programming?
# =====================================================

print("\n===== What is Object-Oriented Programming? =====")

print(
    "Object-Oriented Programming (OOP) is a programming "
    "paradigm that organizes programs using classes and "
    "objects instead of only functions."
)

print(
    "\nIn OOP, real-world entities such as Cars, Students, "
    "Bank Accounts, and Mobile Phones are represented as "
    "software objects."
)

print(
    "\nOOP makes code more organized, reusable, scalable, "
    "and easier to maintain."
)

# =====================================================
# Remember
# =====================================================

print("\nRemember")
print("✔ Class = Blueprint")
print("✔ Object = Real thing created from the blueprint")

# =====================================================
# 2. Why Do We Use OOP?
# =====================================================

print("\n===== Why Do We Use OOP? =====")

benefits = [
    "Code Reusability",
    "Better Code Organization",
    "Easy Maintenance",
    "Scalability",
    "Improved Security",
    "Real-World Modeling",
    "Team Collaboration",
    "Reduced Code Duplication"
]

for benefit in benefits:
    print(f"✔ {benefit}")

print(
    "\nOOP is widely used for developing large and complex "
    "applications because it keeps code modular and easy "
    "to understand."
)

# =====================================================
# 3. Procedural Programming vs OOP
# =====================================================

print("\n===== Procedural Programming vs OOP =====")

print("\nProcedural Programming")
print("- Focuses on functions.")
print("- Data and functions are separate.")
print("- Suitable for small projects.")
print("- Less reusable for large applications.")

print("\nObject-Oriented Programming")
print("- Focuses on objects.")
print("- Combines data and methods.")
print("- Suitable for medium and large projects.")
print("- Highly reusable and maintainable.")

# =====================================================
# Quick Comparison
# =====================================================

print("\n===== Quick Comparison =====")

comparison = [
    ("Focus", "Functions", "Objects"),
    ("Code Reuse", "Limited", "High"),
    ("Security", "Lower", "Better"),
    ("Maintenance", "Harder", "Easier"),
    ("Scalability", "Low", "High")
]

for feature, procedural, oop in comparison:
    print(f"{feature:<15}: {procedural:<12} | {oop}")

# =====================================================
# 4. Features of OOP
# =====================================================

print("\n===== Features of OOP =====")

features = [
    "Class",
    "Object",
    "Encapsulation",
    "Inheritance",
    "Polymorphism",
    "Abstraction"
]

for feature in features:
    print(f"★ {feature}")

print(
    "\nThese features help us write clean, reusable, "
    "and maintainable software."
)

# =====================================================
# 5. Four Pillars of OOP
# =====================================================

print("\n===== Four Pillars of OOP =====")

pillars = {
    "Encapsulation": "Protects data",
    "Inheritance": "Reuses existing code",
    "Polymorphism": "One interface, many forms",
    "Abstraction": "Hides unnecessary details"
}

for pillar, meaning in pillars.items():
    print(f"✔ {pillar:<15} → {meaning}")

print(
    "\nThese four concepts form the foundation of "
    "Object-Oriented Programming."
)

# =====================================================
# Visual Representation
# =====================================================

print("\n===== Visual Representation =====")

print("""
                 Class
          (Blueprint / Template)
                   │
        ┌──────────┴──────────┐
        │                     │
     Object 1             Object 2
        │                     │
   Attributes           Attributes
     Methods              Methods
""")

print(
    "A class acts like a blueprint, and objects are the "
    "real instances created from that blueprint."
)

# =====================================================
# 6. OOP in Python
# =====================================================

print("\n===== OOP in Python =====")

print(
    "Python is a fully object-oriented programming language. "
    "Almost everything in Python is treated as an object."
)

print(
    "\nPython provides built-in support for creating classes, "
    "objects, inheritance, polymorphism, encapsulation, "
    "and abstraction."
)

print(
    "\nUsing OOP in Python helps developers write "
    "clean, reusable, and maintainable code."
)

# =====================================================
# Simple Example
# =====================================================

print("\n===== Simple OOP Example =====")


class Student:
    pass


student1 = Student()
student2 = Student()

print("Two Student objects created successfully.")

print("Object 1 :", student1)
print("Object 2 :", student2)

print(
    "\nAlthough both objects are created from the same "
    "class, they are different objects in memory."
)

# =====================================================
# Remember
# =====================================================

print("\nRemember")

print("✔ Everything in Python is an object.")
print("✔ One class can create multiple objects.")
print("✔ Every object has its own identity.")

# =====================================================
# 7. Real-World Example
# =====================================================

print("\n===== Real-World Example =====")

print(
    "Imagine a Car Manufacturing Company."
)

print(
    "\nThe company first creates a blueprint of a car."
)

print(
    "This blueprint contains information like:"
)

properties = [
    "Brand",
    "Color",
    "Model",
    "Engine",
    "Price"
]

for item in properties:
    print(f"• {item}")

print(
    "\nUsing the same blueprint, the company can manufacture "
    "thousands of different cars."
)

print(
    "\nSimilarly,"
)

print("✔ Class   → Blueprint")
print("✔ Object  → Real Car")

print(
    "\nEvery car has its own color, model, and owner "
    "but all are created from the same blueprint."
)

# =====================================================
# Another Real-World Example
# =====================================================

print("\n===== Student Example =====")


class Student:

    school = "ABC Public School"

    def introduce(self):

        print("School :", self.school)
        print("Name   :", self.name)
        print("Grade  :", self.grade)


student1 = Student()
student1.name = "Nikita"
student1.grade = "A"

student2 = Student()
student2.name = "Rahul"
student2.grade = "B"

print("\nStudent 1")

student1.introduce()

print("\nStudent 2")

student2.introduce()

print(
    "\nNotice that both objects belong to the same class "
    "but store different information."
)

# =====================================================
# Visual Representation
# =====================================================

print("\n===== Class to Object Representation =====")

print("""
           Student Class
      +---------------------+
      | Name                |
      | Grade               |
      | introduce()         |
      +---------------------+
             /      \\
            /        \\
           /          \\
      Student1     Student2
      --------     --------
      Name=A       Name=B
      Grade=A      Grade=B
""")

# =====================================================
# 8. Applications of OOP
# =====================================================

print("\n===== Applications of OOP =====")

applications = [
    "Desktop Applications",
    "Web Development",
    "Mobile App Development",
    "Game Development",
    "Banking Systems",
    "Hospital Management Systems",
    "E-Commerce Platforms",
    "School Management Systems",
    "Machine Learning",
    "Artificial Intelligence",
    "Data Science",
    "Cloud Computing"
]

for application in applications:
    print(f"✔ {application}")

print(
    "\nMost modern software applications are built using "
    "Object-Oriented Programming."
)

# =====================================================
# 9. Advantages of OOP
# =====================================================

print("\n===== Advantages of OOP =====")

advantages = [
    "Code Reusability",
    "Better Code Organization",
    "Easy Maintenance",
    "Improved Security",
    "Scalable Applications",
    "Reduced Code Duplication",
    "Modular Development",
    "Easy Testing and Debugging"
]

for advantage in advantages:
    print(f"✔ {advantage}")

# =====================================================
# 10. Disadvantages of OOP
# =====================================================

print("\n===== Disadvantages of OOP =====")

disadvantages = [
    "Steeper Learning Curve",
    "Consumes More Memory",
    "Slightly Slower Execution",
    "Not Suitable for Very Small Programs",
    "Requires Proper Design"
]

for disadvantage in disadvantages:
    print(f"✘ {disadvantage}")

# =====================================================
# 11. Common Mistakes
# =====================================================

print("\n===== Common Mistakes =====")

mistakes = [
    "Confusing a Class with an Object.",
    "Thinking every program should use OOP.",
    "Creating unnecessary classes.",
    "Using OOP for very small scripts.",
    "Ignoring meaningful class names."
]

for index, mistake in enumerate(mistakes, start=1):
    print(f"{index}. {mistake}")

# =====================================================
# 12. Interview Questions
# =====================================================

print("\n===== Interview Questions =====")

questions = [
    "What is Object-Oriented Programming?",
    "Why do we use OOP?",
    "What is the difference between a Class and an Object?",
    "What are the four pillars of OOP?",
    "What is the difference between Procedural Programming and OOP?",
    "Give some real-world examples of OOP.",
    "What are the advantages of OOP?",
    "What are the disadvantages of OOP?"
]

for index, question in enumerate(questions, start=1):
    print(f"{index}. {question}")

# =====================================================
# 13. Best Practices
# =====================================================

print("\n===== Best Practices =====")

best_practices = [
    "Choose meaningful class names.",
    "Keep one responsibility per class.",
    "Prefer code reusability.",
    "Avoid unnecessary complexity.",
    "Follow proper naming conventions.",
    "Write clean and readable code.",
    "Learn the four pillars before building projects."
]

for practice in best_practices:
    print(f"✔ {practice}")

# =====================================================
# 14. Mini Practice
# =====================================================

print("\n===== Mini Practice =====")

practice_questions = [
    "Define Object-Oriented Programming in your own words.",
    "List the four pillars of OOP.",
    "Differentiate between Class and Object.",
    "Write five advantages of OOP.",
    "Write three disadvantages of OOP.",
    "Compare Procedural Programming and OOP.",
    "Name five real-world applications of OOP.",
    "Identify five objects around you.",
    "Write their properties and behaviors.",
    "Research one software built using OOP."
]

for index, question in enumerate(practice_questions, start=1):
    print(f"{index}. {question}")

# =====================================================
# 15. Coding Challenge
# =====================================================

print("\n===== Coding Challenge =====")

print("Challenge 1")
print("- Create a Student class.")

print("\nChallenge 2")
print("- Create three Student objects.")

print("\nChallenge 3")
print("- Add name and age attributes.")

print("\nChallenge 4")
print("- Create a display() method.")

print("\nChallenge 5")
print("- Print details of all students.")

# =====================================================
# 16. Output Prediction
# =====================================================

print("\n===== Output Prediction =====")

print("Predict the output before running the code.\n")

print("""
class Student:
    pass

student = Student()

print(type(student))
""")

print("Expected Output")
print("<class '__main__.Student'>")

# =====================================================
# 17. Quick Recap
# =====================================================

print("\n===== Quick Recap =====")

recap = [
    "OOP organizes programs using Classes and Objects.",
    "Classes act as blueprints.",
    "Objects are created from classes.",
    "OOP improves code reusability.",
    "The four pillars form the foundation of OOP."
]

for point in recap:
    print(f"✔ {point}")

# =====================================================
# Summary
# =====================================================

print("\n===== Summary =====")

print("✔ OOP is a programming paradigm based on objects.")
print("✔ It helps write modular and reusable code.")
print("✔ OOP is widely used in modern software development.")
print("✔ Python provides excellent support for OOP.")
print("✔ The four pillars are:")
print("   • Encapsulation")
print("   • Inheritance")
print("   • Polymorphism")
print("   • Abstraction")

# =====================================================
# End of Program
# =====================================================

print("\nCongratulations! 🎉")
print("You have successfully completed")
print("Object-Oriented Programming (OOP) Basics.")
print("Keep practicing and move to the next chapter!")