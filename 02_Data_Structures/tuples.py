# ---------------------------------
# Tuples in Python
# ---------------------------------
# Tuples are ordered collections used to store multiple items.
# They are commonly used to group related data together.

# -----------------------------
# 1. Creating Tuples
# -----------------------------

# Empty tuple
empty_tuple = ()
print("Empty tuple:", empty_tuple)

# Tuple with elements
fruits = ("apple", "banana", "cherry")
print("Fruits tuple:", fruits)

# Tuple with single element (comma is required)
single_element = ("apple",)
print("Single element tuple:", single_element)

# Using tuple() constructor
numbers = tuple([1, 2, 3, 4])
print("Numbers tuple:", numbers)

# -----------------------------
# 2. Accessing Elements
# -----------------------------

print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])
print("Slice of fruits:", fruits[0:2])

# -----------------------------
# 3. Tuple Unpacking
# -----------------------------

a, b, c = fruits
print("Unpacked values:", a, b, c)

# -----------------------------
# 4. Tuple Methods
# -----------------------------

sample = (1, 2, 2, 3, 4, 2)

print("Count of 2:", sample.count(2))
print("Index of 3:", sample.index(3))

# -----------------------------
# 5. Nested Tuples
# -----------------------------

nested = (1, 2, ("a", "b"))
print("Nested tuple:", nested)
print("Access nested element:", nested[2][0])

# -----------------------------
# 6. Practice Problems
# -----------------------------

# Problem 1: Create a tuple of your favorite movies
movies = ("Inception", "Interstellar", "Matrix")
print("Movies tuple:", movies)

# Problem 2: Swap two variables using tuple unpacking
x = 5
y = 10
x, y = y, x
print("Swapped values:", x, y)

# Problem 3: Count occurrences of an element in a tuple
nums = (1, 2, 3, 2, 4, 2)
print("Occurrences of 2:", nums.count(2))
