"""
==================================================
🔄 Iterators and Iterables in Python
==================================================

This file demonstrates:

1. Iterables
2. Iterators
3. iter()
4. next()
5. StopIteration
6. Custom Iterator
7. Iterator Protocol

==================================================
"""

# ==================================================
# 1. Iterable Example
# ==================================================

print("=" * 60)
print("1. Iterable Example")
print("=" * 60)

numbers = [10, 20, 30, 40]

for num in numbers:
    print(num)


# ==================================================
# 2. Iterator Example
# ==================================================

print("\n" + "=" * 60)
print("2. Iterator Example")
print("=" * 60)

numbers = [10, 20, 30]

iterator = iter(numbers)

print(iterator)

print(next(iterator))
print(next(iterator))
print(next(iterator))


# ==================================================
# 3. String Iterator
# ==================================================

print("\n" + "=" * 60)
print("3. String Iterator")
print("=" * 60)

text = "Python"

char_iterator = iter(text)

print(next(char_iterator))
print(next(char_iterator))
print(next(char_iterator))
print(next(char_iterator))
print(next(char_iterator))
print(next(char_iterator))


# ==================================================
# 4. StopIteration Example
# ==================================================

print("\n" + "=" * 60)
print("4. StopIteration Example")
print("=" * 60)

numbers = [1, 2]

iterator = iter(numbers)

try:
    while True:
        print(next(iterator))

except StopIteration:
    print("Iteration Completed")


# ==================================================
# 5. iter() Function
# ==================================================

print("\n" + "=" * 60)
print("5. iter() Function")
print("=" * 60)

fruits = ["Apple", "Banana", "Mango"]

fruit_iterator = iter(fruits)

print(fruit_iterator)


# ==================================================
# 6. next() Function
# ==================================================

print("\n" + "=" * 60)
print("6. next() Function")
print("=" * 60)

numbers = [100, 200, 300]

iterator = iter(numbers)

print(next(iterator))
print(next(iterator))
print(next(iterator))


# ==================================================
# 7. Iterable vs Iterator
# ==================================================

print("\n" + "=" * 60)
print("7. Iterable vs Iterator")
print("=" * 60)

numbers = [10, 20, 30]

print(type(numbers))

iterator = iter(numbers)

print(type(iterator))


# ==================================================
# 8. Custom Iterator
# ==================================================

print("\n" + "=" * 60)
print("8. Custom Iterator")
print("=" * 60)


class CountUp:

    def __init__(self, limit):
        self.limit = limit
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):

        if self.current <= self.limit:
            number = self.current
            self.current += 1
            return number

        raise StopIteration


counter = CountUp(5)

for number in counter:
    print(number)


# ==================================================
# 9. Manual Iteration Using next()
# ==================================================

print("\n" + "=" * 60)
print("9. Manual Iteration")
print("=" * 60)

counter = CountUp(3)

print(next(counter))
print(next(counter))
print(next(counter))


# ==================================================
# 10. Every Iterator is Iterable
# ==================================================

print("\n" + "=" * 60)
print("10. Every Iterator is Iterable")
print("=" * 60)

iterator = iter([1, 2, 3])

print(iter(iterator) is iterator)


# ==================================================
# 11. Built-in Iterables
# ==================================================

print("\n" + "=" * 60)
print("11. Built-in Iterables")
print("=" * 60)

examples = [
    [1, 2, 3],
    (1, 2, 3),
    "Python",
    {"a": 1, "b": 2},
    {1, 2, 3},
    range(5),
]

for obj in examples:
    print(type(obj), "-> Iterable")


# ==================================================
# 12. for Loop Internally Uses Iterator
# ==================================================

print("\n" + "=" * 60)
print("12. Internal Working of for Loop")
print("=" * 60)

numbers = [10, 20, 30]

iterator = iter(numbers)

while True:
    try:
        value = next(iterator)
        print(value)

    except StopIteration:
        break


# ==================================================
# Common Mistakes
# ==================================================

print("\nCommon Mistakes")

print("""
1. Calling next() directly on a list.
2. Forgetting to use iter().
3. Ignoring StopIteration.
4. Forgetting __iter__().
5. Forgetting __next__().
""")

# ==================================================
# Best Practices
# ==================================================

print("\nBest Practices")

print("""
✔ Prefer for loops over manual next().
✔ Raise StopIteration correctly.
✔ Keep iterator logic simple.
✔ Use custom iterators for large datasets.
✔ Use generators when appropriate.
""")

# ==================================================
# Practice Questions
# ==================================================

print("""
Practice Questions

1. Convert a tuple into an iterator.

2. Print all characters of a string using next().

3. Create a custom iterator from 1–20.

4. Create an iterator for even numbers.

5. Explain the difference between Iterable and Iterator.
""")

# ==================================================
# Interview Questions
# ==================================================

print("""
Interview Questions

1. What is an Iterable?

2. What is an Iterator?

3. Explain iter().

4. Explain next().

5. What is StopIteration?

6. Explain the Iterator Protocol.

7. How does a for loop work internally?

8. What is the difference between Iterable and Iterator?
""")

# ==================================================
# Mini Challenge
# ==================================================

print("""
Mini Challenge

Create a custom iterator that prints

10
20
30
40
50

using __iter__() and __next__().
""")

# ==================================================
# What's Next?
# ==================================================

print("""
Next Topic

⚡ Generators

We'll learn:

✔ yield
✔ Generator Functions
✔ Generator Expressions
✔ Memory Optimization
✔ Infinite Generators
""")

# ==================================================
# End
# ==================================================

print("\n" + "=" * 60)
print("🎉 Iterators and Iterables Completed Successfully!")
print("=" * 60)