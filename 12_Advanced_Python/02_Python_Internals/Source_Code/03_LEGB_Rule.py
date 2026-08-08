"""
=========================================================
🔍 LEGB Rule in Python
=========================================================

LEGB stands for:

L → Local
E → Enclosing
G → Global
B → Built-in

This file demonstrates:

1. What is Name Resolution?
2. LEGB Rule
3. Local Scope
4. Enclosing Scope
5. Global Scope
6. Built-in Scope
7. Step-by-Step LEGB Lookup
8. Name Shadowing
9. Built-in Shadowing
10. builtins Module
11. Function Names and LEGB
12. Lambda Functions and LEGB
13. Comprehension Scope
14. Closures and LEGB
15. Free Variables
16. Closure Cells
17. global
18. nonlocal
19. NameError
20. UnboundLocalError
21. del and Name Binding
22. Common Mistakes
23. Best Practices
24. Interview Questions
25. Debugging Practice
26. Practice Questions
27. Real-World Coding Task
28. Key Takeaways

=========================================================
"""


# =========================================================
# 1. What is Name Resolution?
# =========================================================

print("=" * 60)
print("1. What is Name Resolution?")
print("=" * 60)


name = "Nikita"

print(name)


print("""
Name Resolution is the process Python uses
to determine which object a name refers to.

Python uses the LEGB Rule for name lookup.
""")


# =========================================================
# 2. LEGB Rule
# =========================================================

print("\n" + "=" * 60)
print("2. LEGB Rule")
print("=" * 60)


print("""
LEGB:

L → Local
E → Enclosing
G → Global
B → Built-in

Lookup order:

Local
   ↓
Enclosing
   ↓
Global
   ↓
Built-in

Python stops searching as soon as
it finds the requested name.
""")


# =========================================================
# 3. Local Scope
# =========================================================

print("\n" + "=" * 60)
print("3. Local Scope")
print("=" * 60)


name = "Global"


def greet():

    name = "Local"

    print("Selected:", name)


greet()


# Local name is found first.


# =========================================================
# 4. Enclosing Scope
# =========================================================

print("\n" + "=" * 60)
print("4. Enclosing Scope")
print("=" * 60)


def outer():

    name = "Outer"

    def inner():

        print("Selected:", name)

    inner()


outer()


# inner() has no local name.
# Python finds name in the Enclosing Scope.


# =========================================================
# 5. Global Scope
# =========================================================

print("\n" + "=" * 60)
print("5. Global Scope")
print("=" * 60)


name = "Global"


def show_name():

    print("Selected:", name)


show_name()


# Local → not found
# Enclosing → not found
# Global → found


# =========================================================
# 6. Built-in Scope
# =========================================================

print("\n" + "=" * 60)
print("6. Built-in Scope")
print("=" * 60)


numbers = [10, 20, 30]

print("Length:", len(numbers))
print("Sum   :", sum(numbers))
print("Max   :", max(numbers))
print("Min   :", min(numbers))


# len(), sum(), max(), min()
# are built-in names.


# =========================================================
# 7. Complete LEGB Example
# =========================================================

print("\n" + "=" * 60)
print("7. Complete LEGB Example")
print("=" * 60)


x = "Global"


def outer():

    x = "Enclosing"

    def inner():

        x = "Local"

        print("Selected:", x)

    inner()


outer()


# Lookup:
#
# Local → Found
# Enclosing → Not needed
# Global → Not needed
# Built-in → Not needed


# =========================================================
# 8. Removing Local Binding
# =========================================================

print("\n" + "=" * 60)
print("8. Removing Local Binding")
print("=" * 60)


x = "Global"


def outer():

    x = "Enclosing"

    def inner():

        print("Selected:", x)

    inner()


outer()


# Local → Not found
# Enclosing → Found


# =========================================================
# 9. Removing Enclosing Binding
# =========================================================

print("\n" + "=" * 60)
print("9. Removing Enclosing Binding")
print("=" * 60)


x = "Global"


def outer():

    def inner():

        print("Selected:", x)

    inner()


outer()


# Local → Not found
# Enclosing → Not found
# Global → Found


# =========================================================
# 10. Built-in Lookup
# =========================================================

print("\n" + "=" * 60)
print("10. Built-in Lookup")
print("=" * 60)


def calculate_length():

    values = [1, 2, 3, 4]

    print("Length:", len(values))


calculate_length()


# Local → len not found
# Enclosing → len not found
# Global → len not found
# Built-in → len found


# =========================================================
# 11. Name Shadowing
# =========================================================

print("\n" + "=" * 60)
print("11. Name Shadowing")
print("=" * 60)


name = "Global"


def show():

    name = "Local"

    print("Inside :", name)


show()

print("Outside:", name)


# Local name shadows Global name.


# =========================================================
# 12. Shadowing Across Multiple Levels
# =========================================================

print("\n" + "=" * 60)
print("12. Shadowing Across Multiple Levels")
print("=" * 60)


value = "Global"


def outer():

    value = "Enclosing"

    def inner():

        value = "Local"

        print("Selected:", value)

    inner()


outer()


# Local wins because it is the closest scope.


# =========================================================
# 13. Function Parameters and LEGB
# =========================================================

print("\n" + "=" * 60)
print("13. Function Parameters and LEGB")
print("=" * 60)


x = "Global"


def show(x):

    print("Selected:", x)


show("Parameter")


# Function parameters are Local names.


# =========================================================
# 14. Built-in Shadowing
# =========================================================

print("\n" + "=" * 60)
print("14. Built-in Shadowing")
print("=" * 60)


len = 100

print("Shadowed len:", len)


# Uncomment to observe the problem:
#
# print(len([1, 2, 3]))


# Global len is found before Built-in len.


# =========================================================
# 15. Accessing Built-in Through builtins
# =========================================================

print("\n" + "=" * 60)
print("15. Accessing Built-in Through builtins")
print("=" * 60)


import builtins

print(
    "Built-in len:",
    builtins.len([10, 20, 30])
)


# =========================================================
# 16. Avoid Built-in Shadowing
# =========================================================

print("\n" + "=" * 60)
print("16. Avoid Built-in Shadowing")
print("=" * 60)


print("""
Avoid names such as:

list
dict
set
str
int
float
sum
max
min
len
type
id
input

Prefer descriptive names such as:

numbers
student_list
total
maximum_value
""")


# =========================================================
# 17. Function Name and LEGB
# =========================================================

print("\n" + "=" * 60)
print("17. Function Name and LEGB")
print("=" * 60)


def greet_user():

    print("Hello Python")


greet_user()


# The function name greet_user is
# available in the Global Namespace.


# =========================================================
# 18. Function Name Shadowing
# =========================================================

print("\n" + "=" * 60)
print("18. Function Name Shadowing")
print("=" * 60)


def welcome():

    print("Welcome")


welcome()


welcome = "Python"

print("Shadowed function name:", welcome)

# Uncomment to observe the problem:
#
# welcome()


# =========================================================
# 19. Lambda and LEGB
# =========================================================

print("\n" + "=" * 60)
print("19. Lambda and LEGB")
print("=" * 60)


x = 10

multiply = lambda number: number * x

print("Result:", multiply(5))


# Lambda does not define x locally.
# It can access the Global x.


# =========================================================
# 20. Lambda and Enclosing Scope
# =========================================================

print("\n" + "=" * 60)
print("20. Lambda and Enclosing Scope")
print("=" * 60)


x = 10


def calculate():

    x = 20

    multiply = lambda number: number * x

    return multiply


result = calculate()

print("Result:", result(5))


# The lambda accesses x
# from the Enclosing Scope.


# =========================================================
# 21. Comprehension Scope
# =========================================================

print("\n" + "=" * 60)
print("21. Comprehension Scope")
print("=" * 60)


numbers = [x * 2 for x in range(5)]

print("Numbers:", numbers)


# In Python 3, the comprehension's
# iteration variable does not leak
# into the surrounding scope.


# =========================================================
# 22. Normal for Loop Scope
# =========================================================

print("\n" + "=" * 60)
print("22. Normal for Loop Scope")
print("=" * 60)


for y in range(5):

    pass


print("Loop variable:", y)


# A normal for loop does not create
# a separate function-like scope.


# =========================================================
# 23. Closure and LEGB
# =========================================================

print("\n" + "=" * 60)
print("23. Closure and LEGB")
print("=" * 60)


def create_multiplier(factor):

    def multiply(number):

        return number * factor

    return multiply


double = create_multiplier(2)

print("Double:", double(10))


# factor is found in the Enclosing Scope.


# =========================================================
# 24. Inspecting Free Variables
# =========================================================

print("\n" + "=" * 60)
print("24. Inspecting Free Variables")
print("=" * 60)


print(
    "Free Variables:",
    double.__code__.co_freevars
)


# =========================================================
# 25. Inspecting Closure
# =========================================================

print("\n" + "=" * 60)
print("25. Inspecting Closure")
print("=" * 60)


print(
    "Closure:",
    double.__closure__
)


if double.__closure__:

    for cell in double.__closure__:

        print(
            "Captured Value:",
            cell.cell_contents
        )


# =========================================================
# 26. global and LEGB
# =========================================================

print("\n" + "=" * 60)
print("26. global and LEGB")
print("=" * 60)


score = 10


def update_score():

    global score

    score = 50


print("Before:", score)

update_score()

print("After :", score)


# global makes the assignment target
# the Global binding.


# =========================================================
# 27. nonlocal and LEGB
# =========================================================

print("\n" + "=" * 60)
print("27. nonlocal and LEGB")
print("=" * 60)


def outer_score():

    score = 10

    def update():

        nonlocal score

        score = 50

    update()

    print("Enclosing score:", score)


outer_score()


# nonlocal targets an existing
# Enclosing Function binding.


# =========================================================
# 28. Multiple Nested Functions
# =========================================================

print("\n" + "=" * 60)
print("28. Multiple Nested Functions")
print("=" * 60)


x = "Global"


def outer():

    x = "Outer"

    def middle():

        x = "Middle"

        def inner():

            print("Selected:", x)

        inner()

    middle()


outer()


# Lookup inside inner():
#
# Local → Not found
# Middle → Found


# =========================================================
# 29. Detailed LEGB Trace
# =========================================================

print("\n" + "=" * 60)
print("29. Detailed LEGB Trace")
print("=" * 60)


print("""
Example:

x = "Global"

def outer():

    x = "Outer"

    def inner():

        print(x)

Lookup:

1. Local      → Not found
2. Enclosing  → Found
3. Global     → Not needed
4. Built-in   → Not needed

Result:

Outer
""")


# =========================================================
# 30. NameError
# =========================================================

print("\n" + "=" * 60)
print("30. NameError")
print("=" * 60)


print("""
NameError occurs when Python cannot
resolve a requested name.

Example:

print(student_name)

If student_name does not exist in the
relevant lookup chain, Python raises NameError.

The following example is intentionally
commented out.
""")


# Uncomment to observe NameError:
#
# print(student_name)


# =========================================================
# 31. UnboundLocalError
# =========================================================

print("\n" + "=" * 60)
print("31. UnboundLocalError")
print("=" * 60)


x = 10


def test():

    # Uncomment both lines to observe:
    #
    # print(x)
    # x = 20

    print("Example prepared.")


test()


# Assignment makes x a Local binding
# within the function.


# =========================================================
# 32. Reading vs Assignment
# =========================================================

print("\n" + "=" * 60)
print("32. Reading vs Assignment")
print("=" * 60)


x = 100


def read_value():

    print("Read Global x:", x)


def local_value():

    x = 200

    print("Local x:", x)


read_value()

local_value()

print("Global x:", x)


# =========================================================
# 33. del and Name Binding
# =========================================================

print("\n" + "=" * 60)
print("33. del and Name Binding")
print("=" * 60)


temporary_value = 100

print("Before deletion:", temporary_value)

del temporary_value

print("""
The binding of temporary_value
has now been removed.

Trying to access it again would
produce NameError.
""")


# Uncomment:
#
# print(temporary_value)


# =========================================================
# 34. Closure Value Lookup
# =========================================================

print("\n" + "=" * 60)
print("34. Closure Value Lookup")
print("=" * 60)


def outer_value():

    value = 10

    def inner():

        return value

    value = 20

    return inner


function = outer_value()

print("Closure Result:", function())


# The inner function retains access
# to the enclosing binding.


# =========================================================
# 35. Closure with nonlocal
# =========================================================

print("\n" + "=" * 60)
print("35. Closure with nonlocal")
print("=" * 60)


def create_counter():

    count = 0

    def increment():

        nonlocal count

        count += 1

        return count

    return increment


counter = create_counter()

print(counter())
print(counter())
print(counter())


# =========================================================
# 36. Closure State Inspection
# =========================================================

print("\n" + "=" * 60)
print("36. Closure State Inspection")
print("=" * 60)


print(
    "Free Variables:",
    counter.__code__.co_freevars
)

print(
    "Closure:",
    counter.__closure__
)

if counter.__closure__:

    for cell in counter.__closure__:

        print(
            "Captured Value:",
            cell.cell_contents
        )


# =========================================================
# 37. Advanced LEGB Challenge
# =========================================================

print("\n" + "=" * 60)
print("37. Advanced LEGB Challenge")
print("=" * 60)


x = "Global"


def outer():

    x = "Outer"

    def inner():

        print(x)

    x = "Updated Outer"

    return inner


function = outer()

print("Result:", function())


# inner() accesses the Enclosing binding.


# =========================================================
# 38. Common Mistakes
# =========================================================

print("\n" + "=" * 60)
print("38. Common Mistakes")
print("=" * 60)


print("""
❌ Memorizing LEGB without understanding lookup.

❌ Assuming Global is always selected.

❌ Forgetting Enclosing Scope.

❌ Shadowing built-in names.

❌ Confusing NameError with UnboundLocalError.

❌ Assuming nonlocal means Global.

❌ Forgetting that assignment affects local binding.

❌ Using too many Global variables.

❌ Creating unnecessary name shadowing.
""")


# =========================================================
# 39. Best Practices
# =========================================================

print("\n" + "=" * 60)
print("39. Best Practices")
print("=" * 60)


print("""
✔ Understand name lookup instead of only
  memorizing the LEGB acronym.

✔ Use meaningful variable names.

✔ Avoid unnecessary name shadowing.

✔ Never intentionally shadow built-ins
  without a very specific reason.

✔ Keep Global variables to a minimum.

✔ Use global only when genuinely required.

✔ Use nonlocal for appropriate Closure state.

✔ Keep nested functions focused.

✔ Understand reading vs assignment.

✔ Use debugging and tracing to understand
  unexpected name-resolution behavior.
""")


# =========================================================
# 40. Interview Questions
# =========================================================

print("\n" + "=" * 60)
print("40. Interview Questions")
print("=" * 60)


print("""
Basic:

1. What does LEGB stand for?

2. What is Name Resolution?

3. What is Local Scope?

4. What is Enclosing Scope?

5. What is Global Scope?

6. What is Built-in Scope?


Intermediate:

7. What is Name Shadowing?

8. Why does Local Scope have priority?

9. Why can built-in names be shadowed?

10. What is the purpose of the builtins module?

11. Why are function parameters Local names?

12. What happens when a name is not found?


Advanced:

13. Explain LEGB with nested functions.

14. Difference between NameError and
    UnboundLocalError?

15. How does global affect name binding?

16. How does nonlocal affect name binding?

17. How are Closures related to LEGB?

18. What are free variables?

19. What does __code__.co_freevars show?

20. What does __closure__ contain?

21. How does comprehension scope differ
    from a normal for loop?
""")


# =========================================================
# 41. Debugging Practice
# =========================================================

print("\n" + "=" * 60)
print("41. Debugging Practice")
print("=" * 60)


print("""
Question 1:

x = "Global"

def outer():

    x = "Outer"

    def inner():

        print(x)

    inner()

outer()

Which LEGB level finds x?


Question 2:

x = 10

def test():

    print(x)

    x = 20

Why can this produce UnboundLocalError?


Question 3:

x = "Global"

def outer():

    x = "Outer"

    def inner():

        x = "Inner"

        print(x)

Which binding is selected?


Question 4:

x = "Global"

def outer():

    x = "Outer"

    def inner():

        print(x)

    x = "Updated"

    return inner

Why does the returned function use Updated?


Question 5:

len = 100

print(len([1, 2, 3]))

Why does this fail?

How can builtins.len() be used?
""")


# =========================================================
# 42. Practice Questions
# =========================================================

print("\n" + "=" * 60)
print("42. Practice Questions")
print("=" * 60)


print("""
🟢 Easy

1. Create a Local variable and a Global
   variable with the same name.

2. Access a Global variable from a function.

3. Use len(), sum(), and max() and identify
   their LEGB source.


🟡 Medium

4. Create a nested function using
   an Enclosing variable.

5. Demonstrate name shadowing.

6. Shadow a built-in name and explain
   the problem.


🔴 Hard

7. Create a three-level nested function
   and trace LEGB manually.

8. Create a function that modifies a
   Global variable using global.

9. Create a Closure that modifies an
   Enclosing variable using nonlocal.


🔥 Challenge

Create:

create_calculator(operation)

The returned function should use an
Enclosing variable to determine the
operation.

Example:

add = create_calculator("add")

add(10, 20)

Expected:

30
""")


# =========================================================
# 43. Real-World Coding Task
# =========================================================

print("\n" + "=" * 60)
print("43. Real-World Coding Task")
print("=" * 60)


print("""
Build a Configuration Factory.

Create:

create_config(environment)

Return:

get_config(key)

Example:

production = create_config("production")

production("database")

Expected:

production_database_configuration

Requirements:

✔ Use nested functions.

✔ Store environment in Enclosing Scope.

✔ Return the inner function.

✔ Use Closure behavior.

✔ Do not use a Global variable
  for the environment.

Bonus:

Inspect:

__code__.co_freevars

__closure__
""")


def create_config(environment):

    def get_config(key):

        return f"{environment}_{key}_configuration"

    return get_config


production = create_config("production")

print(
    production("database")
)

print(
    production("debug")
)


# =========================================================
# 44. Mini Challenge
# =========================================================

print("\n" + "=" * 60)
print("44. Mini Challenge")
print("=" * 60)


print("""
Create a nested function structure:

Global
   ↓
outer()
   ↓
middle()
   ↓
inner()

Create the same variable:

value

at multiple levels.

Then:

1. Call inner().
2. Predict the selected value.
3. Trace LEGB manually.
4. Remove one binding at a time.
5. Observe how the result changes.
""")


# =========================================================
# 45. Final LEGB Visualization
# =========================================================

print("\n" + "=" * 60)
print("45. Final LEGB Visualization")
print("=" * 60)


print("""
                    NAME
                      │
                      ▼
              ┌─────────────┐
              │    LOCAL    │
              └──────┬──────┘
                     │
                  Not Found
                     ↓
              ┌─────────────┐
              │  ENCLOSING  │
              └──────┬──────┘
                     │
                  Not Found
                     ↓
              ┌─────────────┐
              │    GLOBAL   │
              └──────┬──────┘
                     │
                  Not Found
                     ↓
              ┌─────────────┐
              │   BUILT-IN  │
              └──────┬──────┘
                     │
                  Not Found
                     ↓
                 NameError
""")


# =========================================================
# 46. Key Takeaways
# =========================================================

print("\n" + "=" * 60)
print("46. Key Takeaways")
print("=" * 60)


print("""
✔ LEGB means Local, Enclosing, Global, Built-in.

✔ LEGB describes Python's name-resolution order.

✔ Local is checked first.

✔ Enclosing is checked next.

✔ Global is checked after Enclosing.

✔ Built-in is checked last.

✔ Python stops after finding the name.

✔ A closer binding shadows an outer binding.

✔ Function parameters are Local names.

✔ Built-in names can be shadowed.

✔ global targets a Global binding.

✔ nonlocal targets an Enclosing binding.

✔ Closures rely on Enclosing Scope.

✔ __code__.co_freevars shows free variables.

✔ __closure__ exposes closure cells.

✔ NameError occurs when a name cannot be resolved.

✔ UnboundLocalError commonly occurs when a
  Local binding is accessed before assignment.

✔ Understanding LEGB makes debugging
  variable-related problems easier.
""")


# =========================================================
# 47. Summary
# =========================================================

print("\n" + "=" * 60)
print("47. Summary")
print("=" * 60)


print("""
In this file, we learned:

✔ Name Resolution
✔ LEGB Rule
✔ Local Scope
✔ Enclosing Scope
✔ Global Scope
✔ Built-in Scope
✔ Step-by-Step Lookup
✔ Name Shadowing
✔ Built-in Shadowing
✔ builtins Module
✔ Function Names
✔ Lambda Functions
✔ Comprehension Scope
✔ Closures
✔ Free Variables
✔ Closure Cells
✔ global
✔ nonlocal
✔ NameError
✔ UnboundLocalError
✔ del
✔ Debugging
✔ Interview Questions
✔ Practice Questions
✔ Real-World Coding Task
✔ Common Mistakes
✔ Best Practices

The LEGB Rule connects:

Namespace
    +
Scope
    +
Name Resolution
""")


# =========================================================
# 48. What's Next?
# =========================================================

print("\n" + "=" * 60)
print("48. What's Next?")
print("=" * 60)


print("""
🎯 Next Topic:

04_Copy_vs_Deep_Copy.py

Topics:

✔ Object References
✔ Assignment vs Copying
✔ Object Identity
✔ id()
✔ Shallow Copy
✔ Deep Copy
✔ copy.copy()
✔ copy.deepcopy()
✔ Nested Mutable Objects
✔ Common Copying Mistakes
✔ Debugging
✔ Interview Questions
✔ Practice Questions
✔ Real-World Coding Task
""")


# =========================================================
# End of File
# =========================================================

print("\n" + "=" * 60)
print("🎉 LEGB Rule Completed Successfully!")
print("=" * 60)