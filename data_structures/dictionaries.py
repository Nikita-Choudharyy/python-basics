# ----------------------------------
# Python Dictionaries
# ----------------------------------
# Dictionary stores data in key-value pairs.

# -----------------------------
# Creating dictionaries
# -----------------------------
student = {
    "name": "Amit",
    "age": 20,
    "course": "BCA"
}

print("Student dictionary:", student)

# -----------------------------
# Accessing values
# -----------------------------
print("Name:", student["name"])
print("Age:", student.get("age"))

# -----------------------------
# Adding and updating elements
# -----------------------------
student["city"] = "Delhi"        # add new key
student["age"] = 21              # update existing key
print("After add/update:", student)

# -----------------------------
# Removing elements
# -----------------------------
student.pop("course")             # remove specific key
print("After pop():", student)

removed_item = student.popitem()  # remove last inserted item
print("Removed item:", removed_item)
print("After popitem():", student)

# -----------------------------
# Dictionary methods
# -----------------------------
print("Keys:", student.keys())
print("Values:", student.values())
print("Items:", student.items())

# -----------------------------
# Using update()
# -----------------------------
extra_info = {"college": "ABC College", "year": 3}
student.update(extra_info)
print("After update():", student)

# -----------------------------
# Copy and clear
# -----------------------------
student_copy = student.copy()
print("Copied dictionary:", student_copy)

student_copy.clear()
print("After clear():", student_copy)

# -----------------------------
# Looping through dictionary
# -----------------------------
for key, value in student.items():
    print(key, ":", value)

# -----------------------------
# Practice examples
# -----------------------------

# 1. Create a dictionary of a product
product = {
    "id": 101,
    "name": "Laptop",
    "price": 55000
}
print("Product:", product)

# 2. Increase price by 5000
product["price"] += 5000
print("Updated price:", product["price"])

# 3. Check if a key exists
print("Is 'price' key present?", "price" in product)
