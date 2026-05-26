# =====================================================================
# Topic: Object-Oriented Programming - Encapsulation
# Purpose: Restricting direct access to methods and variables (Data Hiding).
# =====================================================================

print("--- 1. UNDERSTANDING ACCESS MODIFIERS IN PYTHON ---")
# Encapsulation binds data (variables) and code (methods) together into a single unit.
# Python achieves data hiding using specific naming conventions:
# - Public attributes: Accessible from anywhere (No underscore).
# - Protected attributes: Hinted for internal/subclass use (Single underscore '_').
# - Private attributes: Strictly hidden from outside access (Double underscore '__').

class Employee:
    def __init__(self, name, department, salary):
        self.name = name                 # Public Variable
        self._department = department    # Protected Variable
        self.__salary = salary           # Private Variable

    # Public method to access private data safely
    def display_employee_details(self):
        print(f"Employee: {self.name} | Dept: {self._department} | Salary: ${self.__salary}")

# Testing access modifiers
emp = Employee("Nikita", "Data Science", 95000)

print(f"Accessing Public Name: {emp.name}")
print(f"Accessing Protected Department: {emp._department}")  # Works, but discouraged by convention

# print(emp.__salary) 
# AttributeError! Direct access to a private variable '__salary' is completely blocked.

print("\nExecuting public method to view protected data safely:")
emp.display_employee_details()


print("\n--- 2. REAL-WORLD DATA SCIENCE USE-CASE (Securing Model Hyperparameters) ---")
# Why do we need this in Data Science? Imagine a custom Machine Learning Model class.
# We don't want anyone to accidentally modify critical internal components like learning rate 
# or model weights directly from outside without proper checks.

class CustomLinearModel:
    def __init__(self, learning_rate):
        self.__learning_rate = learning_rate  # Private attribute to prevent accidental override
        self.weights = None                   # Public attribute

    # The @property decorator turns this method into a clean "Getter" for our private variable
    @property
    def learning_rate(self):
        return self.__learning_rate

    # The @.setter decorator acts as a validation layer before updating internal values
    @learning_rate.setter
    def learning_rate(self, value):
        if value <= 0 or value > 1:
            raise ValueError("Data Protection Alert: Learning rate must be strictly between 0 and 1!")
        self.__learning_rate = value

# Creating an ML model instance
model = CustomLinearModel(learning_rate=0.01)

# Reading the private variable cleanly using the getter property
print(f"Current Model Learning Rate: {model.learning_rate}")

# Attempting to change learning rate with a correct value
model.learning_rate = 0.05
print(f"Updated Model Learning Rate: {model.learning_rate}")

# Attempting to corrupt the learning rate with an invalid value
try:
    print("\nAttempting an invalid hyperparameter update...")
    model.learning_rate = -0.5  # This will trigger our setter validation layer
except ValueError as e:
    print(f"Captured Error Successfully: {e}")


# =====================================================================
# 📝 STUDENT REFLECTION & QUICK REVISION
# - Encapsulation keeps objects safe from accidental data corruption.
# - Double underscores '__' trigger 'Name Mangling' behind the scenes in Python.
# - Use '@property' and '@property_name.setter' to create highly secure, 
#   validated interfaces for critical variables.
# =====================================================================
