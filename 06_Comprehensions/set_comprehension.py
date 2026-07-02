# ----------------------------------
# Python Set Comprehension
# ----------------------------------
# Set comprehension is used to create sets
# using a compact one-line syntax.

# -----------------------------
# Basic set comprehension
# -----------------------------
numbers = [1, 2, 2, 3, 4, 4, 5]

unique_squares = {x * x for x in numbers}
print("Unique squares:", unique_squares)

# -----------------------------
# Set comprehension with condition
# -----------------------------
even_numbers = {x for x in numbers if x % 2 == 0}
print("Even numbers:", even_numbers)

# -----------------------------
# Using set comprehension with strings
# -----------------------------
word = "comprehension"

unique_chars = {ch for ch in word}
print("Unique characters:", unique_chars)

# -----------------------------
# Removing duplicates using set comprehension
# -----------------------------
names = ["raj", "amit", "raj", "neha", "amit"]

unique_names = {name for name in names}
print("Unique names:", unique_names)

# -----------------------------
# Set comprehension with transformation
# -----------------------------
lowercase = ["PYTHON", "DaTa", "AI"]

converted = {x.lower() for x in lowercase}
print("Converted to lowercase:", converted)

# -----------------------------
# Practice examples
# -----------------------------

# 1. Create a set of cubes for numbers 1–5
cubes = {x ** 3 for x in range(1, 6)}
print("Cubes:", cubes)

# 2. Extract only vowels from a string
text = "information"
vowels = {ch for ch in text if ch in "aeiou"}
print("Vowels:", vowels)

# 3. Get unique lengths of words
words = ["python", "data", "ai", "science"]
lengths = {len(w) for w in words}
print("Word lengths:", lengths)
