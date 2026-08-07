"""
=========================================================
🔒 Closures in Python
=========================================================

This file demonstrates:

1. Nested Functions
2. Closures
3. Free Variables
4. Lexical Scoping
5. Function Factory
6. State Preservation
7. nonlocal Keyword
8. Real-World Examples
9. Best Practices
10. Practice Questions

=========================================================
"""

# =========================================================
# 1. Nested Function
# =========================================================

print("=" * 60)
print("1. Nested Function")
print("=" * 60)


def outer():

    print("Outer Function")

    def inner():

        print("Inner Function")

    inner()


outer()


# =========================================================
# 2. Scope of Nested Function
# =========================================================

print("\n" + "=" * 60)
print("2. Scope of Nested Function")
print("=" * 60)


def outer():

    def inner():

        print("Hello from Inner Function")

    inner()


outer()

# inner()   # Uncommenting this line will raise NameError


# =========================================================
# 3. First Closure Example
# =========================================================

print("\n" + "=" * 60)
print("3. First Closure Example")
print("=" * 60)


def outer():

    message = "Hello Python"

    def inner():

        print(message)

    return inner


closure = outer()

closure()


# =========================================================
# 4. Another Closure Example
# =========================================================

print("\n" + "=" * 60)
print("4. Another Closure Example")
print("=" * 60)


def outer():

    language = "Python"

    def inner():

        print(f"My favorite language is {language}")

    return inner


closure = outer()

closure()


# =========================================================
# 5. Free Variable
# =========================================================

print("\n" + "=" * 60)
print("5. Free Variable")
print("=" * 60)


def outer():

    course = "Advanced Python"

    def inner():

        print(course)

    return inner


closure = outer()

closure()


# =========================================================
# 6. Inspecting Closure
# =========================================================

print("\n" + "=" * 60)
print("6. Inspecting Closure")
print("=" * 60)


def outer():

    value = 100

    def inner():

        print(value)

    return inner


closure = outer()

print("Closure Object:", closure.__closure__)

print("Free Variables:", closure.__code__.co_freevars)


# =========================================================
# 7. Closure is a Function
# =========================================================

print("\n" + "=" * 60)
print("7. Closure is a Function")
print("=" * 60)


def outer():

    text = "Closures are Powerful!"

    def inner():

        print(text)

    return inner


closure = outer()

print(type(closure))

closure()


# =========================================================
# 8. Key Points
# =========================================================

print("\n" + "=" * 60)
print("8. Key Points")
print("=" * 60)

print("""
✔ Closure is a Nested Function.
✔ It remembers variables from the outer function.
✔ The outer function finishes execution.
✔ The inner function still remembers the data.
✔ Closures preserve state.
✔ Closures are the foundation of Decorators.
""")

# =========================================================
# 9. Function Factory
# =========================================================

print("\n" + "=" * 60)
print("9. Function Factory")
print("=" * 60)


def multiplier(factor):

    def multiply(number):

        return number * factor

    return multiply


double = multiplier(2)

triple = multiplier(3)

print("Double of 10 :", double(10))

print("Triple of 10 :", triple(10))


# =========================================================
# 10. Creating Multiple Closures
# =========================================================

print("\n" + "=" * 60)
print("10. Creating Multiple Closures")
print("=" * 60)


square = multiplier(2)

cube = multiplier(3)

print(square(5))

print(cube(5))


# =========================================================
# 11. State Preservation
# =========================================================

print("\n" + "=" * 60)
print("11. State Preservation")
print("=" * 60)


def greeting(message):

    def greet(name):

        print(f"{message}, {name}")

    return greet


english = greeting("Hello")

hindi = greeting("Namaste")

english("Nikita")

hindi("Nikita")


# =========================================================
# 12. Using nonlocal
# =========================================================

print("\n" + "=" * 60)
print("12. Using nonlocal")
print("=" * 60)


def counter():

    count = 0

    def increment():

        nonlocal count

        count += 1

        return count

    return increment


counter1 = counter()

print(counter1())

print(counter1())

print(counter1())


# =========================================================
# 13. Independent Closure Objects
# =========================================================

print("\n" + "=" * 60)
print("13. Independent Closure Objects")
print("=" * 60)


counter1 = counter()

counter2 = counter()

print("Counter 1")

print(counter1())

print(counter1())

print()

print("Counter 2")

print(counter2())

print(counter2())


# =========================================================
# 14. Without nonlocal (Common Mistake)
# =========================================================

print("\n" + "=" * 60)
print("14. Without nonlocal")
print("=" * 60)


def demo():

    value = 10

    def increase():

        # value += 1
        # Uncommenting the above line will raise
        # UnboundLocalError

        print(value)

    return increase


closure = demo()

closure()

print("\nUsing 'nonlocal' is required when modifying")
print("variables from the enclosing scope.")


# =========================================================
# 15. Nested Function vs Closure
# =========================================================

print("\n" + "=" * 60)
print("15. Nested Function vs Closure")
print("=" * 60)


# Nested Function
def outer():

    def inner():

        print("I am just a Nested Function.")

    inner()


outer()


print()


# Closure
def outer():

    message = "I am a Closure."

    def inner():

        print(message)

    return inner


closure = outer()

closure()


# =========================================================
# 16. Checking Closure Variables
# =========================================================

print("\n" + "=" * 60)
print("16. Checking Closure Variables")
print("=" * 60)


def outer():

    language = "Python"

    version = "3.13"

    def inner():

        print(language, version)

    return inner


closure = outer()

print("Free Variables :", closure.__code__.co_freevars)

print("Closure Cells  :", closure.__closure__)


# =========================================================
# 17. Key Points
# =========================================================

print("\n" + "=" * 60)
print("17. Key Points")
print("=" * 60)

print("""
✔ Closures preserve state.
✔ Each Closure has its own memory.
✔ Function Factories use Closures.
✔ nonlocal modifies enclosing variables.
✔ Closures reduce the need for global variables.
✔ Decorators are built using Closures.
""")

# =========================================================
# 18. Real-World Example - Greeting Factory
# =========================================================

print("\n" + "=" * 60)
print("18. Greeting Factory")
print("=" * 60)


def greeting(language):

    def greet(name):

        print(f"{language}, {name}!")

    return greet


english = greeting("Hello")

hindi = greeting("Namaste")

japanese = greeting("Konnichiwa")

english("Nikita")

hindi("Nikita")

japanese("Nikita")


# =========================================================
# 19. Real-World Example - Discount Calculator
# =========================================================

print("\n" + "=" * 60)
print("19. Discount Calculator")
print("=" * 60)


def discount(discount_percent):

    def calculate(price):

        final_price = price - (price * discount_percent / 100)

        return final_price

    return calculate


student_discount = discount(20)

festival_discount = discount(40)

print(student_discount(5000))

print(festival_discount(5000))


# =========================================================
# 20. Real-World Example - Tax Calculator
# =========================================================

print("\n" + "=" * 60)
print("20. Tax Calculator")
print("=" * 60)


def tax(rate):

    def calculate(amount):

        return amount + (amount * rate / 100)

    return calculate


gst5 = tax(5)

gst18 = tax(18)

print(gst5(1000))

print(gst18(1000))


# =========================================================
# 21. Data Encapsulation using Closure
# =========================================================

print("\n" + "=" * 60)
print("21. Data Encapsulation")
print("=" * 60)


def bank_account(balance):

    def show_balance():

        print("Current Balance :", balance)

    return show_balance


account = bank_account(25000)

account()


# =========================================================
# 22. Callback Example
# =========================================================

print("\n" + "=" * 60)
print("22. Callback Example")
print("=" * 60)


def execute(callback):

    print("Executing...")

    callback()


def task():

    print("Task Completed!")


execute(task)


# =========================================================
# 23. Function Configuration
# =========================================================

print("\n" + "=" * 60)
print("23. Function Configuration")
print("=" * 60)


def formatter(prefix):

    def display(text):

        print(f"{prefix} {text}")

    return display


info = formatter("[INFO]")

warning = formatter("[WARNING]")

error = formatter("[ERROR]")

info("Program Started")

warning("Low Battery")

error("Connection Lost")


# =========================================================
# 24. Closure Returning Multiple Functions
# =========================================================

print("\n" + "=" * 60)
print("24. Multiple Closures")
print("=" * 60)


def calculator():

    value = 100

    def add(x):

        return value + x

    def subtract(x):

        return value - x

    return add, subtract


add, subtract = calculator()

print(add(50))

print(subtract(25))


# =========================================================
# 25. Closure with Lambda
# =========================================================

print("\n" + "=" * 60)
print("25. Closure with Lambda")
print("=" * 60)


def multiplier(factor):

    return lambda number: number * factor


double = multiplier(2)

triple = multiplier(3)

print(double(8))

print(triple(8))


# =========================================================
# 26. Professional Uses of Closures
# =========================================================

print("\n" + "=" * 60)
print("26. Professional Uses")
print("=" * 60)

print("""
✔ Function Factories

✔ Decorators

✔ Callback Functions

✔ Event Handling

✔ Logging Systems

✔ Data Encapsulation

✔ Stateful Functions

✔ Configuration Functions

✔ Web Frameworks

✔ Machine Learning Pipelines
""")


# =========================================================
# 27. Key Points
# =========================================================

print("\n" + "=" * 60)
print("27. Key Points")
print("=" * 60)

print("""
✔ Closures remember variables.

✔ Every Closure has its own state.

✔ Closures can create customized functions.

✔ Closures improve code reusability.

✔ Closures help avoid global variables.

✔ Decorators internally use Closures.
""")

# =========================================================
# 28. Key Takeaways
# =========================================================

print("\n" + "=" * 60)
print("28. Key Takeaways")
print("=" * 60)

print("""
✔ A Closure is a Nested Function.
✔ Every Closure remembers variables from its enclosing scope.
✔ Free Variables are captured automatically.
✔ Closures preserve state after the outer function finishes.
✔ Every Closure has its own independent memory.
✔ The 'nonlocal' keyword modifies variables in the enclosing scope.
✔ Closures are widely used in Function Factories and Decorators.
✔ Closures reduce the need for global variables.
✔ Decorators are built using Closures.
""")


# =========================================================
# 29. Common Mistakes
# =========================================================

print("\n" + "=" * 60)
print("29. Common Mistakes")
print("=" * 60)

print("""
1. Thinking every Nested Function is a Closure.

2. Forgetting to return the Inner Function.

3. Forgetting to use 'nonlocal' when modifying
   enclosing variables.

4. Using global variables instead of Closures.

5. Expecting the outer function to remain active.

6. Confusing Local Variables with Free Variables.
""")


# =========================================================
# 30. Best Practices
# =========================================================

print("\n" + "=" * 60)
print("30. Best Practices")
print("=" * 60)

print("""
✔ Keep Closures small and focused.

✔ Use meaningful function names.

✔ Prefer Closures over global variables.

✔ Use 'nonlocal' only when required.

✔ Use Closures for Function Factories.

✔ Use Closures for maintaining state.

✔ Keep the outer function simple.

✔ Write reusable Closure functions.
""")


# =========================================================
# 31. Interview Questions
# =========================================================

print("\n" + "=" * 60)
print("31. Interview Questions")
print("=" * 60)

print("""
Basic Questions

1. What is a Nested Function?

2. What is a Closure?

3. What is a Free Variable?

4. What is Lexical Scoping?

5. What is the purpose of Closures?

----------------------------------------

Intermediate Questions

6. How does a Closure preserve state?

7. Explain the 'nonlocal' keyword.

8. Difference between Nested Function and Closure.

9. What is a Function Factory?

10. Explain Free Variables with an example.

----------------------------------------

Advanced Questions

11. Explain how Closures work internally.

12. How are Decorators related to Closures?

13. Why are Closures preferred over global variables?

14. What does __closure__ return?

15. Give real-world applications of Closures.
""")


# =========================================================
# 32. Debugging Practice
# =========================================================

print("\n" + "=" * 60)
print("32. Debugging Practice")
print("=" * 60)

print("""
Question 1

Why is this not a Closure?

def outer():

    message = "Hello"

    def inner():

        print(message)

    inner()

----------------------------------------

Question 2

Which keyword is missing?

def counter():

    count = 0

    def increment():

        count += 1

        return count

----------------------------------------

Question 3

Identify the Free Variable.

def outer():

    language = "Python"

    def inner():

        print(language)

    return inner

----------------------------------------

Question 4

Why are these counters independent?

counter1 = counter()

counter2 = counter()

----------------------------------------

Question 5

Why are Closures considered better than using
global variables?
""")


# =========================================================
# 33. Practice Questions
# =========================================================

print("\n" + "=" * 60)
print("33. Practice Questions")
print("=" * 60)

print("""
Easy

1. Create a Closure that remembers your name.

2. Print the remembered value.

----------------------------------------

Medium

1. Create a greeting function using a Closure.

2. Create a multiplication Function Factory.

----------------------------------------

Hard

1. Build a counter using Closures.

2. Create a tax calculator using Closures.

----------------------------------------

Challenge

Create a bank account Closure.

Requirements:

• Initial Balance
• Deposit
• Withdraw
• Show Balance

Use Closures instead of Classes.
""")


# =========================================================
# 34. Real-World Coding Task
# =========================================================

print("\n" + "=" * 60)
print("34. Real-World Coding Task")
print("=" * 60)

print("""
Task

An e-commerce website wants to create
different discount calculators.

Example

Student Discount = 20%

Festival Discount = 40%

VIP Discount = 50%

Create a Function Factory using Closures
that generates customized discount functions.
""")


# =========================================================
# 35. Summary
# =========================================================

print("\n" + "=" * 60)
print("35. Summary")
print("=" * 60)

print("""
In this file, you learned:

✔ Nested Functions
✔ Closures
✔ Free Variables
✔ Lexical Scoping
✔ Function Factories
✔ State Preservation
✔ nonlocal Keyword
✔ Data Encapsulation
✔ Real-world Applications
✔ Best Practices

Closures allow functions to remember variables
from their enclosing scope, making Python code
more modular, reusable, and stateful.

They are one of the most important concepts in
Functional Programming and form the foundation
of Python Decorators.
""")


# =========================================================
# 36. What's Next?
# =========================================================

print("\n" + "=" * 60)
print("36. What's Next?")
print("=" * 60)

print("""
Next Topic

🎨 Decorators in Python

We'll learn:

✔ Function Wrapping
✔ Creating Decorators
✔ @ Syntax
✔ Decorators with Arguments
✔ Multiple Decorators
✔ Built-in Decorators
✔ functools.wraps

Decorators are one of the most widely used
features in professional Python development.
""")


# =========================================================
# End
# =========================================================

print("\n" + "=" * 60)
print("🎉 Closures Completed Successfully!")
print("=" * 60)