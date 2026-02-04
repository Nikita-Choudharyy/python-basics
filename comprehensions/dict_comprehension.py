# ----------------------------------
# Python Dictionary Comprehension
# ----------------------------------
# Dictionary comprehension is used to create dictionaries
# in a concise and readable way.

# -----------------------------
# Basic dictionary comprehension
# -----------------------------
numbers = [1, 2, 3, 4, 5]

squares = {x: x * x for x in numbers}
print("Squares dictionary:", squares)

# -----------------------------
# Dictionary comprehension with condition
# -----------------------------
even_squares = {x: x * x for x in numbers if x % 2 == 0}
print("Even squares dictionary:", even_squares)

# -----------------------------
# Dictionary comprehension with if-else
# -----------------------------
number_type = {x: "Even" if x % 2 == 0 else "Odd" for x in numbers}
print("Even/Odd dictionary:", number_type)

# -----------------------------
# Using dictionary comprehension with strings
# -----------------------------
words = ["python", "data", "science", "ai"]

word_length = {word: len(word) for word in words}
print("Word length dictionary:", word_length)

# -----------------------------
# Transforming an existing dictionary
# -----------------------------
prices = {"apple": 100, "banana": 40, "orange": 60}

# Increase price by 10
updated_prices = {item: price + 10 for item, price in prices.items()}
print("Updated prices:", updated_prices)

# -----------------------------
# Practice examples
# -----------------------------

# 1. Create dictionary of cubes
cubes = {x: x ** 3 for x in range(1, 6)}
print("Cubes dictionary:", cubes)

# 2. Filter items with value greater than 50
filtered_prices = {k: v for k, v in prices.items() if v > 50}
print("Filtered prices:", filtered_prices)

# 3. Create dictionary from two lists
keys = ["a", "b", "c"]
values = [10, 20, 30]

combined = {k: v for k, v in zip(keys, values)}
print("Combined dictionary:", combined)
