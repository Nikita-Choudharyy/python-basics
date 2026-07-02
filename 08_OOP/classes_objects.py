# ----------------------------------
# Python OOP: Classes and Objects
# ----------------------------------
# Object-Oriented Programming (OOP) helps organize
# code using classes and objects.

# -----------------------------
# Creating a class
# -----------------------------
class Student:
    # Constructor
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    # Method to display details
    def display_info(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Course:", self.course)

# -----------------------------
# Creating objects
# -----------------------------
student1 = Student("Amit", 21, "BTech")
student2 = Student("Neha", 22, "BSc")

# -----------------------------
# Calling methods
# -----------------------------
print("Student 1 Details:")
student1.display_info()

print("\nStudent 2 Details:")
student2.display_info()

# -----------------------------
# Modifying object attributes
# -----------------------------
student1.age = 22
print("\nUpdated age of student1:", student1.age)

# -----------------------------
# Practice examples
# -----------------------------

# 1. Create a class for Employee
class Employee:
    def __init__(self, emp_id, salary):
        self.emp_id = emp_id
        self.salary = salary

    def show_details(self):
        print("Employee ID:", self.emp_id)
        print("Salary:", self.salary)

emp1 = Employee(101, 50000)
emp1.show_details()

# 2. Create multiple objects using a loop
employees = [
    Employee(102, 60000),
    Employee(103, 55000)
]

for emp in employees:
    emp.show_details()
