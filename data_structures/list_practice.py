# --------------------------------------------
# Focus: understanding list behavior through small examples
# This is part of my daily Python practice
# --------------------------------------------

# Creating lists
numbers = [10, 20, 30, 40]
mixed_list = [1, "python", 3.5, True]

# Printing lists
print(numbers)
print(mixed_list)

# --------------------------------------------
# Accessing elements using indexing
# --------------------------------------------

# Access first element
print(numbers[0])

# Access last element
print(numbers[-1])

# --------------------------------------------
# Slicing a list
# --------------------------------------------

# Elements from index 1 to 2 (excluding 3)
print(numbers[1:3])

# First two elements
print(numbers[:2])

# Elements from index 2 till end
print(numbers[2:])

# --------------------------------------------
# Modifying list elements (Lists are mutable)
# --------------------------------------------

# Changing value at index 1
numbers[1] = 25
print(numbers)

# --------------------------------------------
# Looping through a list
# --------------------------------------------

# Printing each element using for loop
for num in numbers:
    print(num)

# --------------------------------------------
# Checking if an element exists in list
# --------------------------------------------

print(30 in numbers)   # True
print(100 in numbers)  # False

# --------------------------------------------
# Finding length of list
# --------------------------------------------

print(len(numbers))

# --------------------------------------------
# Adding elements to a list
# --------------------------------------------

# Add element at the end
numbers.append(50)
print(numbers)

# Insert element at specific index
numbers.insert(2, 22)
print(numbers)

# Add multiple elements
numbers.extend([60, 70])
print(numbers)

# --------------------------------------------
# Removing elements from a list
# --------------------------------------------

# Remove specific value
numbers.remove(25)
print(numbers)

# Remove last element
numbers.pop()
print(numbers)

# Remove element at specific index
numbers.pop(0)
print(numbers)

# --------------------------------------------
# Sorting and reversing a list
# --------------------------------------------

# Sort list in ascending order
numbers.sort()
print(numbers)

# Reverse the list
numbers.reverse()
print(numbers)

# --------------------------------------------
# Count and index methods
# --------------------------------------------

# Count occurrences of an element
print(numbers.count(30))

# Find index of an element
print(numbers.index(30))

# --------------------------------------------
# Copying a list
# --------------------------------------------

# Creating a shallow copy
copy_numbers = numbers.copy()
print(copy_numbers)

# --------------------------------------------
# Clearing a list
# --------------------------------------------

# Remove all elements from list
numbers.clear()
print(numbers)
