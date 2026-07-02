# ----------------------------------
# Python map(), filter(), reduce()
# ----------------------------------
# These functions are used for functional-style programming.

from functools import reduce

# -----------------------------
# map()
# -----------------------------
# map() applies a function to each element of an iterable

numbers = [1, 2, 3, 4, 5]

squares = list(map(lambda x: x * x, numbers))
print("Squares using map:", squares)

# -----------------------------
# filter()
# -----------------------------
# filter() selects elements based on a condition

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers using filter:", even_numbers)

# -----------------------------
# reduce()
# -----------------------------
# reduce() reduces the iterable to a single value

sum_of_numbers = reduce(lambda a, b: a + b, numbers)
print("Sum using reduce:", sum_of_numbers)

# -----------------------------
# More examples
# -----------------------------

# Convert list of strings to integers using map
string_nums = ["1", "2", "3", "4"]
int_nums = list(map(int, string_nums))
print("Converted to integers:", int_nums)

# Filter numbers greater than 3
greater_than_three = list(filter(lambda x: x > 3, numbers))
print("Numbers greater than 3:", greater_than_three)

# Find product of all numbers
product = reduce(lambda a, b: a * b, numbers)
print("Product of numbers:", product)

# -----------------------------
# Practice examples
# -----------------------------

# 1. Double each number in list
doubled = list(map(lambda x: x * 2, numbers))
print("Doubled numbers:", doubled)

# 2. Filter odd numbers
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print("Odd numbers:", odd_numbers)

# 3. Find maximum number using reduce
max_num = reduce(lambda a, b: a if a > b else b, numbers)
print("Maximum number:", max_num)
