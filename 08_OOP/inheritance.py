# ----------------------------------
# Python OOP: Inheritance
# ----------------------------------
# Inheritance allows one class (child)
# to acquire properties and methods of another class (parent).

# -----------------------------
# Parent class
# -----------------------------
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_info(self):
        print("Name:", self.name)
        print("Age:", self.age)

# -----------------------------
# Child class inheriting Person
# -----------------------------
class Student(Person):
    def __init__(self, name, age, course):
        # Call parent constructor
        super().__init__(name, age)
        self.course = course

    def show_info(self):
        # Overriding parent method
        super().show_info()
        print("Course:", self.course)

# -----------------------------
# Creating object of child class
# -----------------------------
student1 = Student("Amit", 21, "BTech")

print("Student Details:")
student1.show_info()

# -----------------------------
# Another child class
# -----------------------------
class Employee(Person):
    def __init__(self, name, age, emp_id, salary):
        super().__init__(name, age)
        self.emp_id = emp_id
        self.salary = salary

    def show_details(self):
        print("Employee ID:", self.emp_id)
        print("Salary:", self.salary)

# -----------------------------
# Creating object of Employee
# -----------------------------
emp1 = Employee("Neha", 28, 101, 50000)

print("\nEmployee Details:")
emp1.show_info()
emp1.show_details()

# -----------------------------
# Practice examples
# -----------------------------

# 1. Create another student
student2 = Student("Rahul", 22, "BSc")
student2.show_info()

# 2. Check isinstance
print("\nIs student1 a Student?", isinstance(student1, Student))
print("Is student1 a Person?", isinstance(student1, Person))
