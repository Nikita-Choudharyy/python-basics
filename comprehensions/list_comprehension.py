# ----------------------------------
# Python List Comprehension
# ----------------------------------
# List comprehension provides a concise way
# to create lists using a single line of code.

# -----------------------------
# Basic list comprehension
# -----------------------------
numbers = [1, 2, 3, 4, 5]

squares = [x * x for x in numbers]
print("Squares:", squares)

# -----------------------------
# List comprehension with condition
# -----------------------------
even_numbers = [x for x in numbers if x % 2 == 0]
print("Even numbers:", even_numbers)

# -----------------------------
# List comprehension with if-else
# -----------------------------
labels = ["Even" if x % 2 == 0 else "Odd" for x in numbers]
print("Even/Odd labels:", labels)

# -----------------------------
# Using list comprehension with strings
# -----------------------------
words = ["python", "data", "science", "ai"]

capital_words = [word.upper() for word in words]
print("Capitalized words:", capital_words)

# -----------------------------
# Nested list comprehension
# -----------------------------
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

flattened = [num for row in matrix for num in row]
print("Flattened matrix:", flattened)

# -----------------------------
# Practice examples
# -----------------------------

# 1. Create a list of cubes for numbers from 1 to 5
cubes = [x ** 3 for x in range(1, 6)]
print("Cubes:", cubes)

# 2. Extract vowels from a string
text = "comprehension"
vowels = [ch for ch in text if ch in "aeiou"]
print("Vowels:", vowels)

# 3. Create a list of numbers greater than 10
nums = [5, 12, 18, 7, 25]
greater_than_10 = [x for x in nums if x > 10]
print("Numbers greater than 10:", greater_than_10)
