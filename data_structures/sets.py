# ----------------------------------
# Python Sets
# ----------------------------------
# A set is an unordered collection of unique elements.

# -----------------------------
# Creating sets
# -----------------------------
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print("Set 1:", set1)
print("Set 2:", set2)

# -----------------------------
# Adding elements
# -----------------------------
set1.add(10)        # add single element
print("After add():", set1)

set1.update([11, 12])   # add multiple elements
print("After update():", set1)

# -----------------------------
# Removing elements
# -----------------------------
set1.remove(2)      # removes element, error if not present
print("After remove():", set1)

set1.discard(100)   # removes element if present, no error
print("After discard():", set1)

popped_element = set1.pop()   # removes random element
print("Popped element:", popped_element)
print("After pop():", set1)

# -----------------------------
# Set operations (methods)
# -----------------------------
print("Union:", set1.union(set2))
print("Intersection:", set1.intersection(set2))
print("Difference:", set1.difference(set2))
print("Symmetric Difference:", set1.symmetric_difference(set2))

# -----------------------------
# Set operations (operators)
# -----------------------------
print("Union (|):", set1 | set2)
print("Intersection (&):", set1 & set2)
print("Difference (-):", set1 - set2)

# -----------------------------
# Other useful methods
# -----------------------------
print("Is set1 subset of set2?", set1.issubset(set2))
print("Is set1 superset of set2?", set1.issuperset(set2))

# -----------------------------
# Copy and clear
# -----------------------------
set_copy = set1.copy()
print("Copied set:", set_copy)

set_copy.clear()
print("After clear():", set_copy)

# -----------------------------
# Practice examples
# -----------------------------

# 1. Remove duplicate elements from a list
numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = set(numbers)
print("Unique numbers:", unique_numbers)

# 2. Find common elements between two lists
a = [1, 2, 3, 4]
b = [3, 4, 5, 6]
common_elements = set(a) & set(b)
print("Common elements:", common_elements)

# 3. Find elements present in first list but not in second
difference_elements = set(a) - set(b)
print("Difference elements:", difference_elements)
