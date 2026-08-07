"""
=========================================================
⚡ Generators in Python
=========================================================

This file demonstrates:

1. Generator Function
2. yield Keyword
3. Generator vs Normal Function
4. next()
5. for Loop with Generator
6. Generator Expression
7. Infinite Generator
8. Memory Efficiency
9. Real-World Examples
10. Best Practices
11. Practice Questions

=========================================================
"""

# =========================================================
# 1. Normal Function
# =========================================================

print("=" * 60)
print("1. Normal Function")
print("=" * 60)


def numbers():

    return [1, 2, 3, 4, 5]


result = numbers()

print(result)


# =========================================================
# 2. Generator Function
# =========================================================

print("\n" + "=" * 60)
print("2. Generator Function")
print("=" * 60)


def numbers():

    yield 1
    yield 2
    yield 3
    yield 4
    yield 5


generator = numbers()

print(generator)


# =========================================================
# 3. Accessing Generator Values
# =========================================================

print("\n" + "=" * 60)
print("3. Accessing Generator Values")
print("=" * 60)

generator = numbers()

print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))


# =========================================================
# 4. yield Keyword Demonstration
# =========================================================

print("\n" + "=" * 60)
print("4. yield Keyword Demonstration")
print("=" * 60)


def greet():

    print("Start")

    yield "Hello"

    print("Middle")

    yield "Python"

    print("End")


generator = greet()

print(next(generator))

print(next(generator))

try:
    next(generator)

except StopIteration:
    pass


# =========================================================
# 5. Generator vs Normal Function
# =========================================================

print("\n" + "=" * 60)
print("5. Generator vs Normal Function")
print("=" * 60)


def normal_function():
    return [10, 20, 30]


def generator_function():

    yield 10
    yield 20
    yield 30


print("Normal Function:")

print(normal_function())

print()

print("Generator Function:")

print(generator_function())


# =========================================================
# 6. Converting Generator into List
# =========================================================

print("\n" + "=" * 60)
print("6. Converting Generator into List")
print("=" * 60)


def colors():

    yield "Red"
    yield "Green"
    yield "Blue"


generator = colors()

print(list(generator))


# =========================================================
# 7. Checking Generator Type
# =========================================================

print("\n" + "=" * 60)
print("7. Generator Type")
print("=" * 60)


generator = numbers()

print(type(generator))


# =========================================================
# 8. Key Points
# =========================================================

print("\n" + "=" * 60)
print("8. Key Points")
print("=" * 60)

print("""
✔ Generator uses the 'yield' keyword.
✔ Generator returns one value at a time.
✔ Execution pauses after every yield.
✔ Execution resumes from the same position.
✔ Generator returns a Generator Object.
✔ Generators are memory-efficient.
""")

# =========================================================
# 9. Using next() with Generators
# =========================================================

print("\n" + "=" * 60)
print("9. Using next() with Generators")
print("=" * 60)


def numbers():

    yield 100
    yield 200
    yield 300


generator = numbers()

print(next(generator))
print(next(generator))
print(next(generator))


# =========================================================
# 10. StopIteration Exception
# =========================================================

print("\n" + "=" * 60)
print("10. StopIteration Exception")
print("=" * 60)


def colors():

    yield "Red"
    yield "Green"


generator = colors()

try:

    print(next(generator))
    print(next(generator))
    print(next(generator))

except StopIteration:

    print("Generator Exhausted!")


# =========================================================
# 11. Using for Loop with Generator
# =========================================================

print("\n" + "=" * 60)
print("11. Using for Loop with Generator")
print("=" * 60)


def fruits():

    yield "Apple"
    yield "Banana"
    yield "Mango"


for fruit in fruits():

    print(fruit)


# =========================================================
# 12. Generator Execution State
# =========================================================

print("\n" + "=" * 60)
print("12. Generator Execution State")
print("=" * 60)


def demo():

    print("Step 1")

    yield 1

    print("Step 2")

    yield 2

    print("Step 3")

    yield 3

    print("Finished")


generator = demo()

print(next(generator))

print(next(generator))

print(next(generator))

try:

    next(generator)

except StopIteration:

    print("Generator Completed")


# =========================================================
# 13. Generator Can Be Used Only Once
# =========================================================

print("\n" + "=" * 60)
print("13. Generator Can Be Used Only Once")
print("=" * 60)


def numbers():

    for i in range(5):

        yield i


generator = numbers()

print("First Iteration")

for value in generator:

    print(value)

print()

print("Second Iteration")

for value in generator:

    print(value)

print("No Output! Generator is already exhausted.")


# =========================================================
# 14. Creating a New Generator
# =========================================================

print("\n" + "=" * 60)
print("14. Creating a New Generator")
print("=" * 60)


generator = numbers()

for value in generator:

    print(value)

print()

print("Generator Created Again")

generator = numbers()

for value in generator:

    print(value)


# =========================================================
# 15. Internal Working of Generator
# =========================================================

print("\n" + "=" * 60)
print("15. Internal Working of Generator")
print("=" * 60)


def countdown():

    print("3")

    yield

    print("2")

    yield

    print("1")

    yield

    print("Done")


generator = countdown()

next(generator)

next(generator)

next(generator)

try:

    next(generator)

except StopIteration:

    pass


# =========================================================
# 16. Generator is an Iterator
# =========================================================

print("\n" + "=" * 60)
print("16. Generator is an Iterator")
print("=" * 60)


def values():

    yield 10

    yield 20


generator = values()

print(hasattr(generator, "__iter__"))

print(hasattr(generator, "__next__"))

print(iter(generator) is generator)


# =========================================================
# 17. Important Notes
# =========================================================

print("\n" + "=" * 60)
print("17. Important Notes")
print("=" * 60)

print("""
✔ next() starts executing the Generator.
✔ Execution pauses at every yield.
✔ next() resumes execution from the previous yield.
✔ After the last yield, StopIteration is raised.
✔ A Generator can be consumed only once.
✔ Create a new Generator object to iterate again.
""")

# =========================================================
# 18. Generator Expression
# =========================================================

print("\n" + "=" * 60)
print("18. Generator Expression")
print("=" * 60)

generator = (x for x in range(5))

print(generator)

print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))


# =========================================================
# 19. List Comprehension vs Generator Expression
# =========================================================

print("\n" + "=" * 60)
print("19. List vs Generator")
print("=" * 60)

numbers_list = [x for x in range(5)]

numbers_generator = (x for x in range(5))

print("List:", numbers_list)

print("Generator:", numbers_generator)


# =========================================================
# 20. Generator Expression with for Loop
# =========================================================

print("\n" + "=" * 60)
print("20. Generator Expression with for Loop")
print("=" * 60)

generator = (x * x for x in range(6))

for value in generator:

    print(value)


# =========================================================
# 21. Memory Efficient Processing
# =========================================================

print("\n" + "=" * 60)
print("21. Memory Efficient Processing")
print("=" * 60)


def square_numbers(limit):

    for number in range(limit):

        yield number ** 2


generator = square_numbers(10)

for value in generator:

    print(value)


# =========================================================
# 22. Infinite Generator
# =========================================================

print("\n" + "=" * 60)
print("22. Infinite Generator")
print("=" * 60)


def infinite_numbers():

    number = 1

    while True:

        yield number

        number += 1


generator = infinite_numbers()

for _ in range(10):

    print(next(generator))


# =========================================================
# 23. Generator for Even Numbers
# =========================================================

print("\n" + "=" * 60)
print("23. Even Number Generator")
print("=" * 60)


def even_numbers(limit):

    for number in range(2, limit + 1, 2):

        yield number


for value in even_numbers(20):

    print(value)


# =========================================================
# 24. Reading Large Data (Simulation)
# =========================================================

print("\n" + "=" * 60)
print("24. Processing Large Data")
print("=" * 60)


def process_records():

    for record in range(1, 6):

        yield f"Processing Record {record}"


for record in process_records():

    print(record)


# =========================================================
# 25. Generator Pipeline Example
# =========================================================

print("\n" + "=" * 60)
print("25. Generator Pipeline")
print("=" * 60)


def numbers():

    for i in range(1, 6):

        yield i


def square(generator):

    for number in generator:

        yield number ** 2


result = square(numbers())

for value in result:

    print(value)


# =========================================================
# 26. Generator with enumerate()
# =========================================================

print("\n" + "=" * 60)
print("26. Generator with enumerate()")
print("=" * 60)

generator = (letter for letter in "Python")

for index, value in enumerate(generator):

    print(index, value)


# =========================================================
# 27. Generator with sum()
# =========================================================

print("\n" + "=" * 60)
print("27. Generator with sum()")
print("=" * 60)

generator = (x for x in range(11))

print(sum(generator))


# =========================================================
# 28. Generator with max() and min()
# =========================================================

print("\n" + "=" * 60)
print("28. Generator with max() and min()")
print("=" * 60)

generator = (x * 10 for x in range(1, 6))

values = list(generator)

print("Maximum:", max(values))

print("Minimum:", min(values))


# =========================================================
# 29. Real-World Applications
# =========================================================

print("\n" + "=" * 60)
print("29. Real-World Applications")
print("=" * 60)

print("""
✔ Reading Large Files
✔ Streaming API Responses
✔ Database Record Processing
✔ Machine Learning Data Pipelines
✔ Sensor Data Processing
✔ Infinite Data Streams
✔ Log File Analysis
✔ Batch Data Processing
""")


# =========================================================
# 30. Key Points
# =========================================================

print("\n" + "=" * 60)
print("30. Key Points")
print("=" * 60)

print("""
✔ Generator Expressions use ().
✔ Lists use [].
✔ Generators generate values lazily.
✔ Memory usage remains low.
✔ Generators can create infinite sequences.
✔ A Generator is consumed only once.
✔ Generators are ideal for processing large datasets.
""")

# =========================================================
# 31. Key Takeaways
# =========================================================

print("\n" + "=" * 60)
print("31. Key Takeaways")
print("=" * 60)

print("""
✔ A Generator is a special function that uses the 'yield' keyword.
✔ Every Generator is an Iterator.
✔ Generators produce values one at a time.
✔ Execution pauses after every yield.
✔ Execution resumes from the same position.
✔ Generators follow Lazy Evaluation.
✔ Generator Expressions use ().
✔ Generators are memory-efficient.
✔ A Generator can be consumed only once.
✔ Create a new Generator object to iterate again.
""")


# =========================================================
# 32. Common Mistakes
# =========================================================

print("\n" + "=" * 60)
print("32. Common Mistakes")
print("=" * 60)

print("""
1. Using return instead of yield.

2. Expecting a Generator to return a list.

3. Forgetting that a Generator is consumed only once.

4. Calling next() after the Generator is exhausted.

5. Using a Generator when multiple iterations are required.

6. Forgetting to create a new Generator object.
""")


# =========================================================
# 33. Best Practices
# =========================================================

print("\n" + "=" * 60)
print("33. Best Practices")
print("=" * 60)

print("""
✔ Use Generators for large datasets.
✔ Prefer for loops instead of repeatedly calling next().
✔ Use Generator Expressions for simple sequences.
✔ Create a new Generator when re-iteration is needed.
✔ Use Generators for streaming data.
✔ Keep Generator functions focused on one task.
✔ Use meaningful Generator function names.
""")


# =========================================================
# 34. Interview Questions
# =========================================================

print("\n" + "=" * 60)
print("34. Interview Questions")
print("=" * 60)

print("""
Basic Questions

1. What is a Generator?
2. What is the yield keyword?
3. Difference between return and yield?
4. What is Lazy Evaluation?
5. What is a Generator Expression?

Intermediate Questions

6. Why are Generators memory-efficient?
7. Can a Generator be reused?
8. Explain Generator Expressions.
9. How does next() work with a Generator?
10. Explain StopIteration in Generators.

Advanced Questions

11. Explain the Generator execution flow.
12. Difference between Iterators and Generators.
13. When should you use a Generator instead of a list?
14. Explain Infinite Generators.
15. Give some real-world applications of Generators.
""")


# =========================================================
# 35. Debugging Practice
# =========================================================

print("\n" + "=" * 60)
print("35. Debugging Practice")
print("=" * 60)

print("""
Question 1

Why is this not a Generator?

def numbers():
    return 1
    return 2

----------------------------------------

Question 2

Why does this print a Generator Object?

generator = (x for x in range(5))
print(generator)

----------------------------------------

Question 3

Why does the second loop produce no output?

generator = (x for x in range(3))

for value in generator:
    print(value)

for value in generator:
    print(value)

----------------------------------------

Question 4

What exception will this raise?

generator = (x for x in range(2))

print(next(generator))
print(next(generator))
print(next(generator))

----------------------------------------

Question 5

Why is this more memory-efficient?

(x for x in range(1000000))

than

[x for x in range(1000000)]
""")


# =========================================================
# 36. Practice Questions
# =========================================================

print("\n" + "=" * 60)
print("36. Practice Questions")
print("=" * 60)

print("""
Easy

1. Create a Generator that yields numbers from 1 to 5.

2. Print Generator values using next().

----------------------------------------

Medium

1. Create a Generator that yields squares of numbers.

2. Print all values using a for loop.

----------------------------------------

Hard

1. Create a Generator that yields only even numbers.

2. Create a Generator Expression for cubes.

----------------------------------------

Challenge

Create an Infinite Generator that generates multiples of 5.

Display only the first 10 values.
""")


# =========================================================
# 37. Summary
# =========================================================

print("\n" + "=" * 60)
print("37. Summary")
print("=" * 60)

print("""
In this file, you learned:

✔ Generator Functions
✔ yield Keyword
✔ next()
✔ Generator Expressions
✔ Lazy Evaluation
✔ Memory Efficiency
✔ Infinite Generators
✔ Real-world Applications
✔ Best Practices
✔ Interview Questions

Generators simplify the creation of iterators and allow Python
to process large amounts of data efficiently by generating values
only when they are needed.
""")


# =========================================================
# 38. What's Next?
# =========================================================

print("\n" + "=" * 60)
print("38. What's Next?")
print("=" * 60)

print("""
Next Topic

🔒 Closures in Python

We'll learn:

✔ Nested Functions
✔ Free Variables
✔ Lexical Scoping
✔ Closure Objects
✔ Remembering State
✔ Real-world Applications

Closures are an important Functional Programming concept
and form the foundation for understanding Decorators.
""")


# =========================================================
# End
# =========================================================

print("\n" + "=" * 60)
print("🎉 Generators Completed Successfully!")
print("=" * 60)