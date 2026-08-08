"""
=========================================================
🎯 Scope in Python
=========================================================

This file demonstrates:

1. What is Scope?
2. Local Scope
3. Global Scope
4. Enclosing Scope
5. Built-in Scope
6. Scope vs Namespace
7. Variable Assignment and Scope
8. global Keyword
9. nonlocal Keyword
10. Nested Function Scope
11. Name Shadowing
12. Scope inside if / for / while
13. Function Parameters and Scope
14. Mutable Objects vs Rebinding
15. Closures and Scope
16. Function Factories
17. UnboundLocalError
18. Common Mistakes
19. Best Practices
20. Interview Questions
21. Debugging Practice
22. Practice Questions
23. Real-World Coding Task
24. Key Takeaways

=========================================================
"""


# =========================================================
# 1. What is Scope?
# =========================================================

print("=" * 60)
print("1. What is Scope?")
print("=" * 60)


print("""
Scope determines the region of a program
where a particular name can be accessed.

Important scopes:

Local
Enclosing
Global
Built-in

These are commonly remembered as:

L → Local
E → Enclosing
G → Global
B → Built-in
""")


# =========================================================
# 2. Local Scope
# =========================================================

print("\n" + "=" * 60)
print("2. Local Scope")
print("=" * 60)


def greet():

    message = "Hello Python"

    print("Inside Function:", message)


greet()


# message is local to greet().
# It cannot be directly accessed outside the function.


# =========================================================
# 3. Local Variable Outside Function
# =========================================================

print("\n" + "=" * 60)
print("3. Local Variable Outside Function")
print("=" * 60)


def show_message():

    message = "Hello from Function"

    print(message)


show_message()

# Uncomment to observe NameError:
#
# print(message)


# =========================================================
# 4. Global Scope
# =========================================================

print("\n" + "=" * 60)
print("4. Global Scope")
print("=" * 60)


course = "Python"


def show_course():

    print("Course:", course)


show_course()

print("Outside Function:", course)


# =========================================================
# 5. Local vs Global Scope
# =========================================================

print("\n" + "=" * 60)
print("5. Local vs Global Scope")
print("=" * 60)


course = "Python"


def show():

    topic = "Scope"

    print("Global variable:", course)
    print("Local variable :", topic)


show()


# =========================================================
# 6. Enclosing Scope
# =========================================================

print("\n" + "=" * 60)
print("6. Enclosing Scope")
print("=" * 60)


def outer():

    message = "Hello from Outer"

    def inner():

        print("Inner:", message)

    inner()


outer()


# message belongs to outer()
# and acts as an enclosing variable for inner().


# =========================================================
# 7. Built-in Scope
# =========================================================

print("\n" + "=" * 60)
print("7. Built-in Scope")
print("=" * 60)


numbers = [10, 20, 30]

print("Length:", len(numbers))
print("Sum   :", sum(numbers))
print("Maximum:", max(numbers))
print("Minimum:", min(numbers))
print("Type  :", type(numbers))


# len(), sum(), max(), min(), and type()
# are examples of built-in names.


# =========================================================
# 8. Scope vs Namespace
# =========================================================

print("\n" + "=" * 60)
print("8. Scope vs Namespace")
print("=" * 60)


print("""
Namespace:
Stores names and their associated objects.

Scope:
Determines where those names can be accessed.

Conceptually:

Namespace → Name → Object

Scope → Name Accessibility
""")


# =========================================================
# 9. Variable Assignment and Scope
# =========================================================

print("\n" + "=" * 60)
print("9. Variable Assignment and Scope")
print("=" * 60)


x = 10


def change():

    x = 20

    print("Inside Function:", x)


change()

print("Outside Function:", x)


# x = 20 creates a local binding.
# It does not modify the global x.


# =========================================================
# 10. Understanding Local Assignment
# =========================================================

print("\n" + "=" * 60)
print("10. Understanding Local Assignment")
print("=" * 60)


number = 100


def update():

    number = 500

    print("Local number :", number)


update()

print("Global number:", number)


# =========================================================
# 11. global Keyword
# =========================================================

print("\n" + "=" * 60)
print("11. global Keyword")
print("=" * 60)


counter = 0


def increment():

    global counter

    counter += 1

    print("Counter:", counter)


increment()
increment()
increment()

print("Final Counter:", counter)


# =========================================================
# 12. Why global is Needed
# =========================================================

print("\n" + "=" * 60)
print("12. Why global is Needed")
print("=" * 60)


print("""
Without global:

count = 0

def increment():

    count += 1

Python treats count as a local name
because of the assignment.

This can result in:

UnboundLocalError

When we intentionally want to modify
the global binding, we use:

global count
""")


# =========================================================
# 13. Function Parameters and Scope
# =========================================================

print("\n" + "=" * 60)
print("13. Function Parameters and Scope")
print("=" * 60)


def introduce(name, age):

    print("Name:", name)
    print("Age :", age)


introduce("Nikita", 20)


# Function parameters are local names.


# =========================================================
# 14. Inspecting Function Parameters
# =========================================================

print("\n" + "=" * 60)
print("14. Inspecting Function Parameters")
print("=" * 60)


def student(name, age, course):

    print("Local Namespace:", locals())


student("Nikita", 20, "Python")


# =========================================================
# 15. Nested Function Scope
# =========================================================

print("\n" + "=" * 60)
print("15. Nested Function Scope")
print("=" * 60)


def outer_function():

    outer_value = "Outer"

    def middle_function():

        middle_value = "Middle"

        def inner_function():

            inner_value = "Inner"

            print("Inner  :", inner_value)
            print("Middle :", middle_value)
            print("Outer  :", outer_value)

        inner_function()

    middle_function()


outer_function()


# =========================================================
# 16. Name Shadowing
# =========================================================

print("\n" + "=" * 60)
print("16. Name Shadowing")
print("=" * 60)


message = "Global"


def outer_message():

    message = "Outer"

    def inner_message():

        message = "Inner"

        print("Inner:", message)

    inner_message()

    print("Outer:", message)


outer_message()

print("Global:", message)


# =========================================================
# 17. global vs nonlocal
# =========================================================

print("\n" + "=" * 60)
print("17. global vs nonlocal")
print("=" * 60)


score = 10


def update_global():

    global score

    score = 50


update_global()

print("Global score:", score)


def update_enclosing():

    score = 10

    def change():

        nonlocal score

        score = 50

    change()

    print("Enclosing score:", score)


update_enclosing()


# =========================================================
# 18. nonlocal Keyword
# =========================================================

print("\n" + "=" * 60)
print("18. nonlocal Keyword")
print("=" * 60)


def outer_counter():

    count = 0

    def increment():

        nonlocal count

        count += 1

        print("Count:", count)

    increment()
    increment()
    increment()


outer_counter()


# =========================================================
# 19. Closure and Scope
# =========================================================

print("\n" + "=" * 60)
print("19. Closure and Scope")
print("=" * 60)


def create_multiplier(factor):

    def multiply(number):

        return number * factor

    return multiply


double = create_multiplier(2)
triple = create_multiplier(3)

print("Double:", double(10))
print("Triple:", triple(10))


# factor belongs to the enclosing scope
# of multiply().


# =========================================================
# 20. Inspecting Closure
# =========================================================

print("\n" + "=" * 60)
print("20. Inspecting Closure")
print("=" * 60)


print("Double Closure:", double.__closure__)

print(
    "Free Variables:",
    double.__code__.co_freevars
)


# =========================================================
# 21. Function Factory
# =========================================================

print("\n" + "=" * 60)
print("21. Function Factory")
print("=" * 60)


def power_factory(exponent):

    def power(number):

        return number ** exponent

    return power


square = power_factory(2)
cube = power_factory(3)

print("Square:", square(5))
print("Cube  :", cube(5))


# =========================================================
# 22. Scope Inside if
# =========================================================

print("\n" + "=" * 60)
print("22. Scope Inside if")
print("=" * 60)


if True:

    message = "Hello from if block"


print(message)


# if does not create a separate function-like scope.


# =========================================================
# 23. Scope Inside for Loop
# =========================================================

print("\n" + "=" * 60)
print("23. Scope Inside for Loop")
print("=" * 60)


for number in range(3):

    value = number


print("Last value:", value)


# for does not create a separate function-like scope.


# =========================================================
# 24. Mutable Objects and Scope
# =========================================================

print("\n" + "=" * 60)
print("24. Mutable Objects and Scope")
print("=" * 60)


numbers = [1, 2, 3]


def add_number():

    numbers.append(4)


add_number()

print("Numbers:", numbers)


# The list is mutated.
# The global name is not rebound.


# =========================================================
# 25. Mutation vs Rebinding
# =========================================================

print("\n" + "=" * 60)
print("25. Mutation vs Rebinding")
print("=" * 60)


numbers = [1, 2, 3]


def mutate():

    numbers.append(4)


mutate()

print("After Mutation:", numbers)


numbers = [1, 2, 3]


def rebind():

    numbers = [10, 20, 30]

    print("Inside Function:", numbers)


rebind()

print("Outside Function:", numbers)


# =========================================================
# 26. Rebinding Global Name
# =========================================================

print("\n" + "=" * 60)
print("26. Rebinding Global Name")
print("=" * 60)


numbers = [1, 2, 3]


def update_numbers():

    global numbers

    numbers = numbers + [4]


update_numbers()

print("Numbers:", numbers)


# =========================================================
# 27. Mutable Object in Enclosing Scope
# =========================================================

print("\n" + "=" * 60)
print("27. Mutable Object in Enclosing Scope")
print("=" * 60)


def outer_list():

    numbers = [1, 2, 3]

    def inner():

        numbers.append(4)

    inner()

    print("Numbers:", numbers)


outer_list()


# =========================================================
# 28. Rebinding Enclosing Name with nonlocal
# =========================================================

print("\n" + "=" * 60)
print("28. Rebinding Enclosing Name with nonlocal")
print("=" * 60)


def outer_numbers():

    numbers = [1, 2, 3]

    def inner():

        nonlocal numbers

        numbers = numbers + [4]

    inner()

    print("Numbers:", numbers)


outer_numbers()


# =========================================================
# 29. UnboundLocalError Example
# =========================================================

print("\n" + "=" * 60)
print("29. UnboundLocalError Example")
print("=" * 60)


x = 10


def test():

    # Uncomment these lines to observe
    # UnboundLocalError:
    #
    # print(x)
    # x = 20

    print("Global x:", x)


test()


# Assignment inside a function can make
# a name local throughout that function.


# =========================================================
# 30. Scope Lookup Example
# =========================================================

print("\n" + "=" * 60)
print("30. Scope Lookup Example")
print("=" * 60)


x = 100


def outer():

    x = 200

    def inner():

        print("Selected x:", x)

    x = 300

    inner()


outer()


# inner() accesses the enclosing x.


# =========================================================
# 31. Common Scope Mistakes
# =========================================================

print("\n" + "=" * 60)
print("31. Common Scope Mistakes")
print("=" * 60)


print("""
❌ Using global unnecessarily.

❌ Using nonlocal without an enclosing binding.

❌ Confusing mutation with rebinding.

❌ Assuming if/for/while create function-like scope.

❌ Forgetting that assignment can make a name local.

❌ Using too many global variables.

❌ Creating confusing variable shadowing.
""")


# =========================================================
# 32. Best Practices
# =========================================================

print("\n" + "=" * 60)
print("32. Best Practices")
print("=" * 60)


print("""
✔ Prefer local variables when possible.

✔ Pass data through function parameters.

✔ Avoid unnecessary global state.

✔ Use global only when genuinely required.

✔ Use nonlocal for closure state when appropriate.

✔ Keep closures small and focused.

✔ Avoid unnecessary name shadowing.

✔ Understand mutation vs rebinding.

✔ Use meaningful variable names.

✔ Keep functions predictable and maintainable.
""")


# =========================================================
# 33. Interview Questions
# =========================================================

print("\n" + "=" * 60)
print("33. Interview Questions")
print("=" * 60)


print("""
Basic:

1. What is Scope in Python?

2. What is Local Scope?

3. What is Global Scope?

4. What is Enclosing Scope?

5. What is Built-in Scope?

6. Do if, for, and while create function-like scope?


Intermediate:

7. What is the difference between Namespace and Scope?

8. What does the global keyword do?

9. What does the nonlocal keyword do?

10. What is name shadowing?

11. Why are function parameters local names?

12. What is the difference between mutation
    and rebinding?


Advanced:

13. Why can reading a global variable work
    without using global?

14. Why can x = x + 1 produce UnboundLocalError?

15. Why can't nonlocal directly refer to
    a global variable?

16. How are Closures related to Enclosing Scope?

17. Explain global vs nonlocal.

18. How do function factories use Enclosing Scope?
""")


# =========================================================
# 34. Debugging Practice
# =========================================================

print("\n" + "=" * 60)
print("34. Debugging Practice")
print("=" * 60)


print("""
Question 1:

x = 10

def test():

    print(x)

    x = 20

test()

Why can this produce UnboundLocalError?


Question 2:

x = 10

def outer():

    x = 20

    def inner():

        print(x)

    inner()

Which x is used?


Question 3:

def outer():

    count = 0

    def inner():

        count += 1

What is wrong?

How can nonlocal fix it?


Question 4:

numbers = [1, 2, 3]

def update():

    numbers.append(4)

Why can this work without global?


Question 5:

What is the difference between:

numbers.append(4)

and:

numbers = numbers + [4]
""")


# =========================================================
# 35. Practice Questions
# =========================================================

print("\n" + "=" * 60)
print("35. Practice Questions")
print("=" * 60)


print("""
🟢 Easy

1. Create a function with three local variables.

2. Create a global variable and access it
   from inside a function.

3. Create a function with parameters and
   inspect locals().


🟡 Medium

4. Create a global counter using global.

5. Create an outer function and inner function
   using an enclosing variable.

6. Create a Closure using nonlocal.


🔴 Hard

7. Create power_factory(exponent).

8. Create an example of UnboundLocalError
   and explain the reason.

9. Demonstrate mutation vs rebinding.


🔥 Challenge

Create a Student Profile Factory:

create_student(course)

The returned function should accept:

name
age

and display:

Student Name
Age
Course

The course must come from the Enclosing Scope.
""")


# =========================================================
# 36. Real-World Coding Task
# =========================================================

print("\n" + "=" * 60)
print("36. Real-World Coding Task")
print("=" * 60)


print("""
Build a reusable Counter System.

Create:

create_counter(start)

Example:

counter = create_counter(10)

counter()
counter()
counter()

Expected:

11
12
13

Requirements:

✔ Use a nested function.

✔ Use Enclosing Scope.

✔ Use nonlocal.

✔ Preserve state between function calls.

Bonus:

Inspect:

__closure__

and:

__code__.co_freevars
""")


def create_counter(start):

    count = start

    def increment():

        nonlocal count

        count += 1

        return count

    return increment


counter = create_counter(10)

print(counter())
print(counter())
print(counter())


# =========================================================
# 37. Mini Challenge
# =========================================================

print("\n" + "=" * 60)
print("37. Mini Challenge")
print("=" * 60)


print("""
Create a Discount Calculator Factory.

Function:

create_discount(percent)

Example:

discount_10 = create_discount(10)

discount_10(1000)

Expected:

900

Requirements:

✔ Use a nested function.

✔ Store percent in the enclosing scope.

✔ Return the inner function.

✔ Do not use a global discount variable.

Bonus:

Inspect the Closure.
""")


# =========================================================
# 38. Key Takeaways
# =========================================================

print("\n" + "=" * 60)
print("38. Key Takeaways")
print("=" * 60)


print("""
✔ Scope determines where a name can be accessed.

✔ Functions create Local Scope.

✔ Enclosing Scope exists around nested functions.

✔ Global Scope belongs to the module-level environment.

✔ Built-in Scope contains Python's built-in names.

✔ if, for, and while do not create function-like scope.

✔ Function parameters are local names.

✔ global targets a Global binding.

✔ nonlocal targets an Enclosing Function binding.

✔ Local variables can shadow outer variables.

✔ Mutation and rebinding are different operations.

✔ Closures use Enclosing Scope to preserve state.

✔ Understanding Scope helps explain
  UnboundLocalError.
""")


# =========================================================
# 39. Summary
# =========================================================

print("\n" + "=" * 60)
print("39. Summary")
print("=" * 60)


print("""
In this file, we learned:

✔ What is Scope?
✔ Local Scope
✔ Global Scope
✔ Enclosing Scope
✔ Built-in Scope
✔ Scope vs Namespace
✔ Variable Assignment
✔ global
✔ nonlocal
✔ Nested Functions
✔ Name Shadowing
✔ Function Parameters
✔ Scope in if/for/while
✔ Mutable Objects
✔ Mutation vs Rebinding
✔ Closures
✔ Function Factories
✔ UnboundLocalError
✔ Common Mistakes
✔ Best Practices
✔ Interview Questions
✔ Debugging Practice
✔ Practice Questions
✔ Real-World Coding Task

Understanding Scope is essential for
understanding Python's name resolution.
""")


# =========================================================
# 40. What's Next?
# =========================================================

print("\n" + "=" * 60)
print("40. What's Next?")
print("=" * 60)


print("""
🎯 Next Topic:

03_LEGB_Rule.py

Topics:

✔ Local
✔ Enclosing
✔ Global
✔ Built-in
✔ Name Lookup Order
✔ Variable Shadowing
✔ Tricky LEGB Examples
✔ Debugging
✔ Interview Questions
✔ Practice Questions
✔ Real-World Examples
""")


# =========================================================
# End of File
# =========================================================

print("\n" + "=" * 60)
print("🎉 Scope Completed Successfully!")
print("=" * 60)

