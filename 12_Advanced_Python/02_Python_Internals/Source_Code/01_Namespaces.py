"""
=========================================================
🧠 Namespaces in Python
=========================================================

This file demonstrates:

1. What is a Namespace?
2. Name → Object Relationship
3. Global Namespace
4. Local Namespace
5. Enclosing Namespace
6. Built-in Namespace
7. Module Namespace
8. globals()
9. locals()
10. Name Shadowing
11. Closures and Namespaces
12. __globals__
13. __closure__
14. Common Mistakes
15. Best Practices
16. Practice Questions

=========================================================
"""


# =========================================================
# 1. What is a Namespace?
# =========================================================

print("=" * 60)
print("1. What is a Namespace?")
print("=" * 60)


name = "Nikita"
age = 20

print(name)
print(age)


# Conceptually:
#
# name → "Nikita"
# age  → 20


# =========================================================
# 2. Name → Object Relationship
# =========================================================

print("\n" + "=" * 60)
print("2. Name → Object Relationship")
print("=" * 60)


name = "Nikita"
age = 20

print("Name :", name)
print("Age  :", age)

print("\nConceptually:")
print("name →", name)
print("age  →", age)


# =========================================================
# 3. Global Namespace
# =========================================================

print("\n" + "=" * 60)
print("3. Global Namespace")
print("=" * 60)


student_name = "Nikita"
student_age = 20


def greet():

    print("Hello Python")


print("Student Name:", globals()["student_name"])
print("Student Age :", globals()["student_age"])
print("Function    :", globals()["greet"])


# =========================================================
# 4. Inspecting Global Namespace
# =========================================================

print("\n" + "=" * 60)
print("4. Inspecting Global Namespace")
print("=" * 60)


course = "Advanced Python"
level = "Intermediate"

global_namespace = globals()

print("Course:", global_namespace["course"])
print("Level :", global_namespace["level"])


# Check whether a name exists

print("\nChecking Names:")

print("'course' in globals():", "course" in globals())

print("'language' in globals():", "language" in globals())


# =========================================================
# 5. Local Namespace
# =========================================================

print("\n" + "=" * 60)
print("5. Local Namespace")
print("=" * 60)


def student():

    name = "Nikita"
    age = 20
    course = "Python"

    print("Local Namespace:")
    print(locals())


student()


# =========================================================
# 6. Accessing Local Namespace
# =========================================================

print("\n" + "=" * 60)
print("6. Accessing Local Namespace")
print("=" * 60)


def calculate():

    x = 10
    y = 20

    namespace = locals()

    print("x =", namespace["x"])
    print("y =", namespace["y"])


calculate()


# =========================================================
# 7. Enclosing Namespace
# =========================================================

print("\n" + "=" * 60)
print("7. Enclosing Namespace")
print("=" * 60)


def outer():

    message = "Hello from Outer"

    def inner():

        print(message)

    inner()


outer()


# =========================================================
# 8. Built-in Namespace
# =========================================================

print("\n" + "=" * 60)
print("8. Built-in Namespace")
print("=" * 60)


print(len("Python"))

print(sum([10, 20, 30]))

print(max([10, 50, 20]))

print(min([10, 50, 20]))

print(type(100))


# =========================================================
# 9. Module Namespace
# =========================================================

print("\n" + "=" * 60)
print("9. Module Namespace")
print("=" * 60)


PI = 3.14159


def add(a, b):

    return a + b


print("PI:", PI)

print("add(10, 20):", add(10, 20))


# =========================================================
# 10. globals() vs locals()
# =========================================================

print("\n" + "=" * 60)
print("10. globals() vs locals()")
print("=" * 60)


language = "Python"


def show():

    topic = "Namespaces"

    print("Global Language:", globals()["language"])

    print("Local Topic:", locals()["topic"])


show()


# =========================================================
# 11. Name Shadowing
# =========================================================

print("\n" + "=" * 60)
print("11. Name Shadowing")
print("=" * 60)


name = "Global"


def show_name():

    name = "Local"

    print("Inside Function :", name)


show_name()

print("Outside Function:", name)


# =========================================================
# 12. Same Name in Different Namespaces
# =========================================================

print("\n" + "=" * 60)
print("12. Same Name in Different Namespaces")
print("=" * 60)


value = "Global"


def outer_function():

    value = "Outer"

    def inner_function():

        value = "Inner"

        print("Inner Value:", value)

    inner_function()


outer_function()

print("Global Value:", value)


# =========================================================
# 13. Namespace Inspection
# =========================================================

print("\n" + "=" * 60)
print("13. Namespace Inspection")
print("=" * 60)


def inspect_student():

    name = "Nikita"
    age = 20
    course = "Advanced Python"

    namespace = locals()

    print("Name  :", namespace["name"])
    print("Age   :", namespace["age"])
    print("Course:", namespace["course"])


inspect_student()


# =========================================================
# 14. Adding Name Using globals()
# =========================================================

print("\n" + "=" * 60)
print("14. Adding Name Using globals()")
print("=" * 60)


globals()["language"] = "Python"

print("Language:", language)

print("From Namespace:", globals()["language"])


# Note:
# Directly modifying globals() is generally not recommended
# in normal application code.


# =========================================================
# 15. Removing Name Using globals()
# =========================================================

print("\n" + "=" * 60)
print("15. Removing Name Using globals()")
print("=" * 60)


globals()["temporary_value"] = 100

print("Before deletion:",temporary_value)

del globals()["temporary_value"]

print(
    "After deletion:",
    "temporary_value" in globals()
)


# =========================================================
# 16. Namespace and Closure
# =========================================================

print("\n" + "=" * 60)
print("16. Namespace and Closure")
print("=" * 60)


def create_message():

    message = "Hello Python"

    def display():

        return message

    return display


closure = create_message()

print("Closure Result:", closure())


# =========================================================
# 17. Inspecting Closure
# =========================================================

print("\n" + "=" * 60)
print("17. Inspecting Closure")
print("=" * 60)


def create_closure():

    value = 100

    def inner():

        return value

    return inner


closure = create_closure()

print("Result:", closure())

print(
    "Free Variables:",
    closure.__code__.co_freevars
)

print(
    "Closure:",
    closure.__closure__
)


# =========================================================
# 18. Inspecting Closure Cells
# =========================================================

print("\n" + "=" * 60)
print("18. Inspecting Closure Cells")
print("=" * 60)


def outer():

    message = "Hello from Closure"

    def inner():

        return message

    return inner


closure = outer()


if closure.__closure__:

    for cell in closure.__closure__:

        print("Stored Value:", cell.cell_contents)


# =========================================================
# 19. Function __globals__
# =========================================================

print("\n" + "=" * 60)
print("19. Function __globals__")
print("=" * 60)


course = "Advanced Python"


def show_course():

    print(course)


print(
    "Course from __globals__:",
    show_course.__globals__["course"]
)

show_course()


# =========================================================
# 20. Important Namespace Connection
# =========================================================

print("\n" + "=" * 60)
print("20. Important Namespace Connection")
print("=" * 60)


print("""
Namespace
    ↓
Stores names and objects

Scope
    ↓
Determines where names are accessible

LEGB Rule
    ↓
Determines name lookup order

Closures
    ↓
Allow inner functions to remember
enclosing variables
""")

# =========================================================
# 21. Common Namespace Mistakes
# =========================================================

print("\n" + "=" * 60)
print("21. Common Namespace Mistakes")
print("=" * 60)


print("""
Common Mistakes:

1. Confusing Namespace with Scope.

2. Assuming the same name always refers
   to the same variable.

3. Assuming a local variable automatically
   changes a global variable.

4. Using globals() unnecessarily.

5. Using too many global variables.

6. Confusing globals() with locals().

7. Forgetting that nested functions can have
   access to enclosing variables.
""")


# =========================================================
# 22. Local Variable Does Not Change Global Variable
# =========================================================

print("\n" + "=" * 60)
print("22. Local Variable vs Global Variable")
print("=" * 60)


number = 10


def update_number():

    number = 50

    print("Inside Function:", number)


update_number()

print("Outside Function:", number)


# =========================================================
# 23. Using Global Variable Explicitly
# =========================================================

print("\n" + "=" * 60)
print("23. Using Global Variable Explicitly")
print("=" * 60)


counter = 0


def increment():

    global counter

    counter += 1

    print("Counter:", counter)


increment()
increment()
increment()


# Important:
#
# The global keyword tells Python that
# we want to modify the existing global
# variable instead of creating a local one.


# =========================================================
# 24. Namespace and Function Parameters
# =========================================================

print("\n" + "=" * 60)
print("24. Namespace and Function Parameters")
print("=" * 60)


def introduce(name, age):

    print("Local Namespace:", locals())

    print(f"Name: {name}")
    print(f"Age : {age}")


introduce("Nikita", 20)


# Function parameters also become
# names in the function's Local Namespace.


# =========================================================
# 25. Namespace with Multiple Functions
# =========================================================

print("\n" + "=" * 60)
print("25. Namespace with Multiple Functions")
print("=" * 60)


def first():

    value = "First Function"

    print("First:", value)


def second():

    value = "Second Function"

    print("Second:", value)


first()

second()


# Each function has its own Local Namespace.


# =========================================================
# 26. Independent Local Namespaces
# =========================================================

print("\n" + "=" * 60)
print("26. Independent Local Namespaces")
print("=" * 60)


def function_one():

    message = "Hello from Function One"

    print(message)


def function_two():

    message = "Hello from Function Two"

    print(message)


function_one()

function_two()


# Both functions have a local name called "message",
# but the names belong to different Local Namespaces.


# =========================================================
# 27. Namespace and Nested Functions
# =========================================================

print("\n" + "=" * 60)
print("27. Namespace and Nested Functions")
print("=" * 60)


def outer():

    outer_value = "Outer Value"

    def inner():

        inner_value = "Inner Value"

        print("Inner Local:", inner_value)
        print("Enclosing :", outer_value)

    inner()


outer()


# =========================================================
# 28. Namespace Lookup Example
# =========================================================

print("\n" + "=" * 60)
print("28. Namespace Lookup Example")
print("=" * 60)


message = "Global Message"


def outer():

    message = "Outer Message"

    def inner():

        print(message)

    inner()


outer()


# The inner function finds "message"
# from its enclosing environment.


# =========================================================
# 29. Namespace Debugging Example
# =========================================================

print("\n" + "=" * 60)
print("29. Namespace Debugging Example")
print("=" * 60)


def debug_function():

    name = "Nikita"
    age = 20
    profession = "Student"

    print("\nLocal Namespace:")

    for key, value in locals().items():

        print(f"{key} → {value}")


debug_function()


# =========================================================
# 30. Inspecting Selected Global Names
# =========================================================

print("\n" + "=" * 60)
print("30. Inspecting Selected Global Names")
print("=" * 60)


python_version = "3.x"
learning = "Advanced Python"


global_namespace = globals()


print(
    "python_version:",
    global_namespace["python_version"]
)

print(
    "learning:",
    global_namespace["learning"]
)


# =========================================================
# 31. Namespace Best Practices
# =========================================================

print("\n" + "=" * 60)
print("31. Namespace Best Practices")
print("=" * 60)


print("""
Best Practices:

✔ Prefer local variables when possible.

✔ Avoid unnecessary global variables.

✔ Use meaningful variable names.

✔ Keep functions self-contained.

✔ Pass values through function parameters.

✔ Use globals() and locals() mainly for
  inspection and debugging.

✔ Avoid unnecessary modification of globals().

✔ Understand name shadowing.

✔ Keep namespaces clean and organized.
""")


# =========================================================
# 32. Interview Questions
# =========================================================

print("\n" + "=" * 60)
print("32. Interview Questions")
print("=" * 60)


print("""
Basic Questions:

1. What is a Namespace?

2. What is a Global Namespace?

3. What is a Local Namespace?

4. What is a Built-in Namespace?

5. What is an Enclosing Namespace?


Intermediate Questions:

6. What does globals() return?

7. What does locals() return?

8. What is name shadowing?

9. Can two namespaces contain the same name?

10. What is a Module Namespace?


Advanced Questions:

11. What is function.__globals__?

12. What is function.__closure__?

13. How are Namespaces related to Closures?

14. What is the difference between
    Namespace and Scope?

15. Why should unnecessary global variables
    be avoided?
""")


# =========================================================
# 33. Debugging Practice
# =========================================================

print("\n" + "=" * 60)
print("33. Debugging Practice")
print("=" * 60)


print("""
Question 1:

What will this code print?

x = 10

def test():

    x = 20

    print(x)

test()

print(x)


Question 2:

Why are these two values different?

name = "Global"

def show():

    name = "Local"

    print(name)


Question 3:

What does locals() return inside a function?

Question 4:

What does globals() return?

Question 5:

Why doesn't this modify the global variable?

value = 10

def update():

    value = 100

update()

print(value)
""")


# =========================================================
# 34. Practice Questions
# =========================================================

print("\n" + "=" * 60)
print("34. Practice Questions")
print("=" * 60)


print("""
🟢 Easy

1. Create three global variables and inspect
   them using globals().

2. Create a function with three local variables
   and inspect them using locals().


🟡 Medium

3. Create two functions containing a variable
   with the same name.

   Explain why there is no conflict.

4. Create a nested function and identify:

   - Local Namespace
   - Enclosing Namespace
   - Global Namespace


🔴 Hard

5. Create a Closure that remembers a value.

   Then inspect:

   - __closure__
   - __code__.co_freevars


🔥 Challenge

Create a function factory that remembers
a student's course.

Example:

python_student = create_student("Python")

python_student("Nikita")

Expected Output:

Student: Nikita
Course: Python
""")


# =========================================================
# 35. Real-World Coding Task
# =========================================================

print("\n" + "=" * 60)
print("35. Real-World Coding Task")
print("=" * 60)


print("""
Task:

Create an Employee Configuration System.

Requirements:

1. Create a function:

       create_employee(department)

2. Store the department inside the
   enclosing function.

3. Create an inner function:

       show_employee(name)

4. Return the inner function.

5. Demonstrate that the inner function
   remembers the department.

6. Inspect the Closure.

Example:

engineering = create_employee("Engineering")

engineering("Nikita")

Expected Output:

Employee: Nikita
Department: Engineering
""")


# =========================================================
# 36. Mini Challenge
# =========================================================

print("\n" + "=" * 60)
print("36. Mini Challenge")
print("=" * 60)


print("""
Build a simple Student Profile Factory.

Function:

    create_student(course)

The returned function should accept:

    name
    age

and display:

    Student Name
    Age
    Course

The course should come from the
Enclosing Namespace.

Bonus:

Inspect the returned function using:

    __closure__

    __code__.co_freevars
""")


# =========================================================
# 37. Key Takeaways
# =========================================================

print("\n" + "=" * 60)
print("37. Key Takeaways")
print("=" * 60)


print("""
✔ A Namespace maps names to objects.

✔ Python uses multiple namespaces.

✔ Global Namespace contains module-level names.

✔ Local Namespace is created during function execution.

✔ Nested functions can access enclosing variables.

✔ Built-in Namespace contains Python's built-in names.

✔ globals() helps inspect the Global Namespace.

✔ locals() helps inspect the Local Namespace.

✔ Functions have a __globals__ attribute.

✔ Closures can preserve access to enclosing variables.

✔ The same name can exist in different namespaces.

✔ Local names can shadow global names.

✔ Namespace and Scope are related but different.

✔ LEGB defines Python's name lookup order.
""")


# =========================================================
# 38. Summary
# =========================================================

print("\n" + "=" * 60)
print("38. Summary")
print("=" * 60)


print("""
In this file, we learned how Python organizes
and manages names using Namespaces.

We covered:

✔ Global Namespace
✔ Local Namespace
✔ Enclosing Namespace
✔ Built-in Namespace
✔ Module Namespace
✔ globals()
✔ locals()
✔ Name Shadowing
✔ global keyword
✔ Nested Functions
✔ Closures
✔ __globals__
✔ __closure__
✔ Common Mistakes
✔ Best Practices
✔ Debugging
✔ Practice Questions

Namespaces are the foundation for understanding
Python's variable management and name resolution.

The next topic is Scope.
""")


# =========================================================
# 39. What's Next?
# =========================================================

print("\n" + "=" * 60)
print("39. What's Next?")
print("=" * 60)


print("""
🎯 Next Topic:

02_Scope.py

We will learn:

✔ What is Scope?

✔ Local Scope

✔ Global Scope

✔ Enclosing Scope

✔ Built-in Scope

✔ global keyword

✔ nonlocal keyword

✔ Nested Function Scope

✔ Scope-related Debugging

✔ Interview Questions

✔ Practice Questions
""")


# =========================================================
# End of File
# =========================================================

print("\n" + "=" * 60)
print("🎉 Namespaces Completed Successfully!")
print("=" * 60)