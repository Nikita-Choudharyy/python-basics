"""
=========================================================
🎨 Decorators in Python
=========================================================

This file demonstrates:

1. Higher-Order Functions
2. Function Wrapping
3. Custom Decorators
4. @ Syntax
5. Decorators with Arguments
6. Multiple Decorators
7. Built-in Decorators
8. functools.wraps
9. Real-World Examples
10. Best Practices

=========================================================
"""

# =========================================================
# 1. Higher-Order Function
# =========================================================

print("=" * 60)
print("1. Higher-Order Function")
print("=" * 60)


def greet():

    print("Hello Python!")


def display(function):

    print("Before Function Call")

    function()

    print("After Function Call")


display(greet)


# =========================================================
# 2. Basic Decorator
# =========================================================

print("\n" + "=" * 60)
print("2. Basic Decorator")
print("=" * 60)


def decorator(function):

    def wrapper():

        print("Before Function Execution")

        function()

        print("After Function Execution")

    return wrapper


def message():

    print("Welcome to Python")


decorated_function = decorator(message)

decorated_function()


# =========================================================
# 3. Using @ Decorator Syntax
# =========================================================

print("\n" + "=" * 60)
print("3. @ Decorator Syntax")
print("=" * 60)


def decorator(function):

    def wrapper():

        print("Before Execution")

        function()

        print("After Execution")

    return wrapper


@decorator
def greet():

    print("Learning Decorators")


greet()


# =========================================================
# 4. Manual Decoration vs @ Syntax
# =========================================================

print("\n" + "=" * 60)
print("4. Manual Decoration vs @ Syntax")
print("=" * 60)


def logger(function):

    def wrapper():

        print("Logging Started")

        function()

        print("Logging Finished")

    return wrapper


def hello():

    print("Hello World!")


print("Manual Decoration")

manual = logger(hello)

manual()

print()

print("@ Syntax")


@logger
def welcome():

    print("Welcome!")


welcome()


# =========================================================
# 5. Decorator with Function Arguments
# =========================================================

print("\n" + "=" * 60)
print("5. Decorator with Function Arguments")
print("=" * 60)


def decorator(function):

    def wrapper(*args, **kwargs):

        print("Before Function")

        function(*args, **kwargs)

        print("After Function")

    return wrapper


@decorator
def introduce(name, age):

    print(f"Name : {name}")

    print(f"Age  : {age}")


introduce("Nikita", 20)


# =========================================================
# 6. Returning Values
# =========================================================

print("\n" + "=" * 60)
print("6. Returning Values")
print("=" * 60)


def decorator(function):

    def wrapper(*args, **kwargs):

        print("Calculating...")

        result = function(*args, **kwargs)

        print("Calculation Finished")

        return result

    return wrapper


@decorator
def add(a, b):

    return a + b


answer = add(15, 25)

print("Result :", answer)


# =========================================================
# 7. Logging Decorator
# =========================================================

print("\n" + "=" * 60)
print("7. Logging Decorator")
print("=" * 60)


def logger(function):

    def wrapper(*args, **kwargs):

        print(f"Calling Function : {function.__name__}")

        return function(*args, **kwargs)

    return wrapper


@logger
def multiply(a, b):

    return a * b


print("Answer :", multiply(10, 5))


# =========================================================
# 8. Key Points
# =========================================================

print("\n" + "=" * 60)
print("8. Key Points")
print("=" * 60)

print("""
✔ Decorators are Higher-Order Functions.
✔ Decorators wrap existing functions.
✔ The original function remains unchanged.
✔ @ syntax is a shortcut for applying Decorators.
✔ *args and **kwargs make Decorators reusable.
✔ Decorators improve code reusability.
""")

# =========================================================
# 9. Decorator with Arguments
# =========================================================

print("\n" + "=" * 60)
print("9. Decorator with Arguments")
print("=" * 60)


def repeat(times):

    def decorator(function):

        def wrapper(*args, **kwargs):

            for _ in range(times):

                function(*args, **kwargs)

        return wrapper

    return decorator


@repeat(3)
def greet():

    print("Hello Python!")


greet()


# =========================================================
# 10. Execution Flow of Decorator with Arguments
# =========================================================

print("\n" + "=" * 60)
print("10. Execution Flow")
print("=" * 60)

print("""
repeat(3)
      │
      ▼
Decorator
      │
      ▼
Wrapper
      │
      ▼
Original Function
""")


# =========================================================
# 11. Multiple Decorators
# =========================================================

print("\n" + "=" * 60)
print("11. Multiple Decorators")
print("=" * 60)


def decorator_one(function):

    def wrapper():

        print("Decorator One - Before")

        function()

        print("Decorator One - After")

    return wrapper


def decorator_two(function):

    def wrapper():

        print("Decorator Two - Before")

        function()

        print("Decorator Two - After")

    return wrapper


@decorator_one
@decorator_two
def message():

    print("Welcome to Decorators!")


message()


# =========================================================
# 12. Order of Execution
# =========================================================

print("\n" + "=" * 60)
print("12. Order of Execution")
print("=" * 60)

print("""
Python converts

@decorator_one
@decorator_two

into

message = decorator_one(
            decorator_two(message)
          )
""")


# =========================================================
# 13. Using functools.wraps
# =========================================================

print("\n" + "=" * 60)
print("13. functools.wraps")
print("=" * 60)

from functools import wraps


def decorator(function):

    @wraps(function)
    def wrapper():

        print("Before Execution")

        function()

    return wrapper


@decorator
def welcome():
    """Welcome Function"""

    print("Hello!")


print("Function Name :", welcome.__name__)

print("Docstring :", welcome.__doc__)

welcome()


# =========================================================
# 14. Without functools.wraps
# =========================================================

print("\n" + "=" * 60)
print("14. Without functools.wraps")
print("=" * 60)


def decorator(function):

    def wrapper():

        function()

    return wrapper


@decorator
def demo():
    """Demo Function"""

    print("Demo")


print("Function Name :", demo.__name__)

print("Docstring :", demo.__doc__)


# =========================================================
# 15. Built-in Decorator - @staticmethod
# =========================================================

print("\n" + "=" * 60)
print("15. @staticmethod")
print("=" * 60)


class Student:

    @staticmethod
    def welcome():

        print("Welcome Students!")


Student.welcome()


# =========================================================
# 16. Built-in Decorator - @classmethod
# =========================================================

print("\n" + "=" * 60)
print("16. @classmethod")
print("=" * 60)


class Company:

    company = "OpenAI"

    @classmethod
    def show_company(cls):

        print(cls.company)


Company.show_company()


# =========================================================
# 17. Built-in Decorator - @property
# =========================================================

print("\n" + "=" * 60)
print("17. @property")
print("=" * 60)


class Circle:

    def __init__(self, radius):

        self.radius = radius

    @property
    def diameter(self):

        return self.radius * 2


circle = Circle(5)

print("Diameter :", circle.diameter)


# =========================================================
# 18. Key Points
# =========================================================

print("\n" + "=" * 60)
print("18. Key Points")
print("=" * 60)

print("""
✔ Decorators can accept arguments.
✔ Multiple Decorators can be stacked.
✔ Decorators execute in wrapping order.
✔ functools.wraps preserves metadata.
✔ @staticmethod belongs to the class.
✔ @classmethod receives the class as the first argument.
✔ @property allows methods to behave like attributes.
""")

# =========================================================
# 19. Timer Decorator
# =========================================================

print("\n" + "=" * 60)
print("19. Timer Decorator")
print("=" * 60)

import time


def timer(function):

    @wraps(function)
    def wrapper(*args, **kwargs):

        start_time = time.perf_counter()

        result = function(*args, **kwargs)

        end_time = time.perf_counter()

        print(f"Execution Time : {end_time - start_time:.6f} seconds")

        return result

    return wrapper


@timer
def calculate():

    total = 0

    for number in range(1_000_000):

        total += number

    return total


calculate()


# =========================================================
# 20. Logger Decorator
# =========================================================

print("\n" + "=" * 60)
print("20. Logger Decorator")
print("=" * 60)


def logger(function):

    @wraps(function)
    def wrapper(*args, **kwargs):

        print(f"Calling Function : {function.__name__}")

        result = function(*args, **kwargs)

        print(f"Finished Function : {function.__name__}")

        return result

    return wrapper


@logger
def greet(name):

    print(f"Hello {name}")


greet("Nikita")


# =========================================================
# 21. Authentication Decorator
# =========================================================

print("\n" + "=" * 60)
print("21. Authentication Decorator")
print("=" * 60)


def authenticate(function):

    @wraps(function)
    def wrapper(*args, **kwargs):

        authenticated = True

        if authenticated:

            return function(*args, **kwargs)

        print("Access Denied!")

    return wrapper


@authenticate
def dashboard():

    print("Welcome to Dashboard")


dashboard()


# =========================================================
# 22. Input Validation Decorator
# =========================================================

print("\n" + "=" * 60)
print("22. Input Validation Decorator")
print("=" * 60)


def positive_number(function):

    @wraps(function)
    def wrapper(number):

        if number < 0:

            print("Only Positive Numbers Allowed")

            return

        return function(number)

    return wrapper


@positive_number
def square(number):

    print(number ** 2)


square(5)

square(-5)


# =========================================================
# 23. Retry Decorator
# =========================================================

print("\n" + "=" * 60)
print("23. Retry Decorator")
print("=" * 60)


def retry(function):

    @wraps(function)
    def wrapper(*args, **kwargs):

        attempts = 3

        while attempts > 0:

            try:

                return function(*args, **kwargs)

            except Exception as error:

                print("Retrying...", error)

                attempts -= 1

        print("Operation Failed")

    return wrapper


@retry
def divide():

    return 10 / 0


divide()


# =========================================================
# 24. Simple Cache Decorator
# =========================================================

print("\n" + "=" * 60)
print("24. Simple Cache Decorator")
print("=" * 60)


def cache(function):

    memory = {}

    @wraps(function)
    def wrapper(number):

        if number not in memory:

            print("Calculating...")

            memory[number] = function(number)

        else:

            print("Using Cached Result")

        return memory[number]

    return wrapper


@cache
def square(number):

    return number ** 2


print(square(10))

print(square(10))


# =========================================================
# 25. Counting Function Calls
# =========================================================

print("\n" + "=" * 60)
print("25. Counting Function Calls")
print("=" * 60)


def count_calls(function):

    calls = 0

    @wraps(function)
    def wrapper(*args, **kwargs):

        nonlocal calls

        calls += 1

        print(f"Function Called : {calls} time(s)")

        return function(*args, **kwargs)

    return wrapper


@count_calls
def hello():

    print("Hello")


hello()

hello()

hello()


# =========================================================
# 26. Real-World Uses
# =========================================================

print("\n" + "=" * 60)
print("26. Real-World Uses")
print("=" * 60)

print("""
✔ Authentication Systems

✔ Logging

✔ Performance Monitoring

✔ API Rate Limiting

✔ Retry Mechanism

✔ Input Validation

✔ Caching

✔ Web Frameworks

✔ Machine Learning Pipelines

✔ Database Transactions
""")


# =========================================================
# 27. Key Points
# =========================================================

print("\n" + "=" * 60)
print("27. Key Points")
print("=" * 60)

print("""
✔ Decorators add reusable functionality.
✔ They help avoid duplicate code.
✔ They improve maintainability.
✔ They are heavily used in professional projects.
✔ Logging, Authentication, Timing and Caching
  are common real-world applications.
""")

# =========================================================
# 28. Key Takeaways
# =========================================================

print("\n" + "=" * 60)
print("28. Key Takeaways")
print("=" * 60)

print("""
✔ A Decorator is a function that wraps another function.
✔ Decorators extend functionality without modifying the original function.
✔ Decorators are built using Higher-Order Functions and Closures.
✔ The @ symbol is syntactic sugar for applying Decorators.
✔ *args and **kwargs make Decorators flexible.
✔ functools.wraps preserves function metadata.
✔ Multiple Decorators can be stacked together.
✔ Decorators are widely used in modern Python frameworks.
""")


# =========================================================
# 29. Common Mistakes
# =========================================================

print("\n" + "=" * 60)
print("29. Common Mistakes")
print("=" * 60)

print("""
1. Forgetting to return the wrapper function.

2. Forgetting to call the original function.

3. Not using *args and **kwargs.

4. Forgetting to return the function's result.

5. Not using functools.wraps.

6. Confusing Decorators with ordinary functions.

7. Decorating a function that has incompatible arguments.
""")


# =========================================================
# 30. Best Practices
# =========================================================

print("\n" + "=" * 60)
print("30. Best Practices")
print("=" * 60)

print("""
✔ Keep each Decorator focused on one responsibility.

✔ Always use *args and **kwargs.

✔ Always return the original function's result.

✔ Use functools.wraps.

✔ Write reusable Decorators.

✔ Use meaningful Decorator names.

✔ Keep wrapper functions simple and readable.

✔ Document your Decorators properly.
""")


# =========================================================
# 31. Interview Questions
# =========================================================

print("\n" + "=" * 60)
print("31. Interview Questions")
print("=" * 60)

print("""
Basic Questions

1. What is a Decorator?

2. Why are Decorators used?

3. What is Function Wrapping?

4. What is a Higher-Order Function?

5. Explain the @ syntax.

----------------------------------------

Intermediate Questions

6. Why are *args and **kwargs used?

7. Explain functools.wraps.

8. What are Decorators with Arguments?

9. Explain Multiple Decorators.

10. Explain the execution flow of a Decorator.

----------------------------------------

Advanced Questions

11. Explain the relationship between Closures and Decorators.

12. How does Python internally apply @decorator?

13. Explain built-in Decorators.

14. What happens if functools.wraps is not used?

15. Give real-world applications of Decorators.
""")


# =========================================================
# 32. Debugging Practice
# =========================================================

print("\n" + "=" * 60)
print("32. Debugging Practice")
print("=" * 60)

print("""
Question 1

What is missing?

def decorator(function):

    def wrapper():

        function()

----------------------------------------

Question 2

Why will this fail?

def wrapper():

    function()

@decorator
def greet(name):

    print(name)

----------------------------------------

Question 3

Why is this incorrect?

def wrapper(*args, **kwargs):

    function(*args, **kwargs)

----------------------------------------

Question 4

Why does this print 'wrapper'?

print(greet.__name__)

----------------------------------------

Question 5

Why does the following execute twice?

@decorator_one
@decorator_two
def greet():

    print("Hello")
""")


# =========================================================
# 33. Practice Questions
# =========================================================

print("\n" + "=" * 60)
print("33. Practice Questions")
print("=" * 60)

print("""
Easy

1. Create a Decorator that prints:

   Before Execution
   After Execution

----------------------------------------

Medium

1. Create a Logger Decorator.

2. Create a Timer Decorator.

----------------------------------------

Hard

1. Create an Authentication Decorator.

2. Create an Input Validation Decorator.

----------------------------------------

Challenge

Create a Retry Decorator.

Requirements

• Retry 3 times.

• Handle Exceptions.

• Display Success or Failure.
""")


# =========================================================
# 34. Real-World Coding Task
# =========================================================

print("\n" + "=" * 60)
print("34. Real-World Coding Task")
print("=" * 60)

print("""
Task

An online shopping application wants to
measure the execution time of every payment.

Create a Timer Decorator that:

✔ Calculates execution time.

✔ Prints the function name.

✔ Returns the original result.

Bonus

Log every payment attempt before execution.
""")


# =========================================================
# 35. Summary
# =========================================================

print("\n" + "=" * 60)
print("35. Summary")
print("=" * 60)

print("""
In this file, you learned:

✔ Higher-Order Functions
✔ Function Wrapping
✔ Custom Decorators
✔ @ Syntax
✔ Decorators with Arguments
✔ Multiple Decorators
✔ Built-in Decorators
✔ functools.wraps
✔ Real-world Applications
✔ Best Practices

Decorators allow developers to extend the
behavior of existing functions without
modifying their source code.

They are one of Python's most powerful
features and are widely used in modern
frameworks and production applications.
""")


# =========================================================
# 36. What's Next?
# =========================================================

print("\n" + "=" * 60)
print("36. What's Next?")
print("=" * 60)

print("""
Next Section

🧠 Python Internals

Topics

✔ Namespaces
✔ Variable Scope
✔ LEGB Rule
✔ Shallow Copy
✔ Deep Copy

Understanding Python Internals will help you
write better, more efficient, and more
predictable Python code.
""")


# =========================================================
# End
# =========================================================

print("\n" + "=" * 60)
print("🎉 Decorators Completed Successfully!")
print("=" * 60)