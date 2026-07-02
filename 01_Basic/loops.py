"""
Loops in Python
This file covers:
1. for loop
2. while loop
3. break and continue
4. Common practice examples
"""

# -------------------------------
# 1. for loop
# -------------------------------

# Print numbers from 1 to 5
for i in range(1, 6):
    print(i)

# Loop through a string
name = "Python"
for char in name:
    print(char)


# -------------------------------
# 2. while loop
# -------------------------------

# Print numbers from 1 to 5 using while loop
count = 1
while count <= 5:
    print(count)
    count += 1


# -------------------------------
# 3. break statement
# -------------------------------

# Stop the loop when number is 3
for i in range(1, 6):
    if i == 3:
        break
    print(i)


# -------------------------------
# 4. continue statement
# -------------------------------

# Skip number 3
for i in range(1, 6):
    if i == 3:
        continue
    print(i)


# -------------------------------
# 5. Practice Examples
# -------------------------------

# Example 1: Sum of first 5 numbers
total = 0
for i in range(1, 6):
    total += i
print("Sum:", total)

# Example 2: Print even numbers from 1 to 10
for i in range(1, 11):
    if i % 2 == 0:
        print(i)

# Example 3: Count down using while loop
num = 5
while num > 0:
    print(num)
    num -= 1
