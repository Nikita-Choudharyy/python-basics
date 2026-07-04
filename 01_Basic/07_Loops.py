"""
=========================================================
Python Loops
=========================================================

Repository : python-basics
File       : 07_Loops.py
Author     : Nikita Choudhary

Description:
------------
This file demonstrates loops in Python, including
for loops, while loops, break, continue, and
practical examples.

This repository documents my Python learning journey.
The examples are written for revision and to help other
beginners understand Python concepts.

Learning Objectives:
--------------------
✔ Understand for loops
✔ Learn while loops
✔ Use break and continue
✔ Solve simple problems using loops
✔ Improve logical thinking

=========================================================
"""

# =========================================================
# 1. FOR LOOP
# =========================================================

# A for loop is used to iterate over a sequence.

print("\nFor Loop")
print("-" * 30)

print("Numbers from 1 to 5:")

for i in range(1, 6):
    print(i)

# Expected Output:
#
# Numbers from 1 to 5:
# 1
# 2
# 3
# 4
# 5


# =========================================================
# 2. LOOP THROUGH A STRING
# =========================================================

# Iterate through each character of a string.

name = "Python"

print("\nLoop Through a String")
print("-" * 30)

for char in name:
    print(char)

# Expected Output:
#
# P
# y
# t
# h
# o
# n


# =========================================================
# 3. WHILE LOOP
# =========================================================

# A while loop runs as long as the condition is True.

count = 1

print("\nWhile Loop")
print("-" * 30)

while count <= 5:
    print(count)
    count += 1

# Expected Output:
#
# 1
# 2
# 3
# 4
# 5


# =========================================================
# 4. BREAK STATEMENT
# =========================================================

# break immediately stops the loop.

print("\nBreak Statement")
print("-" * 30)

for i in range(1, 6):
    if i == 3:
        break
    print(i)

# Expected Output:
#
# 1
# 2


# =========================================================
# 5. CONTINUE STATEMENT
# =========================================================

# continue skips the current iteration.

print("\nContinue Statement")
print("-" * 30)

for i in range(1, 6):
    if i == 3:
        continue
    print(i)

# Expected Output:
#
# 1
# 2
# 4
# 5


# =========================================================
# 6. PRACTICAL EXAMPLE - SUM OF NUMBERS
# =========================================================

# Calculate the sum of numbers from 1 to 5.

total = 0

for i in range(1, 6):
    total += i

print("\nSum of Numbers")
print("-" * 30)

print("Sum:", total)

# Expected Output:
#
# Sum: 15


# =========================================================
# 7. PRACTICAL EXAMPLE - EVEN NUMBERS
# =========================================================

print("\nEven Numbers from 1 to 10")
print("-" * 30)

for i in range(1, 11):
    if i % 2 == 0:
        print(i)

# Expected Output:
#
# 2
# 4
# 6
# 8
# 10


# =========================================================
# 8. PRACTICAL EXAMPLE - COUNTDOWN
# =========================================================

num = 5

print("\nCountdown")
print("-" * 30)

while num > 0:
    print(num)
    num -= 1

print("Blast Off! 🚀")

# Expected Output:
#
# 5
# 4
# 3
# 2
# 1
# Blast Off! 🚀


# =========================================================
# BEST PRACTICES
# =========================================================

# ✔ Use a for loop when the number of iterations is known.
# ✔ Use a while loop when the stopping condition is unknown.
# ✔ Avoid infinite loops.
# ✔ Use break only when necessary.
# ✔ Use continue carefully to avoid skipping important logic.


# =========================================================
# COMMON BEGINNER MISTAKES
# =========================================================

# ❌ Forgetting to update the loop variable in a while loop.
#
# count = 1
# while count <= 5:
#     print(count)
#
# This creates an infinite loop.

# ✅ Correct
#
# count += 1


# Another common mistake:
#
# Using break instead of continue (or vice versa).
#
# break    → Stops the loop completely.
# continue → Skips only the current iteration.


# =========================================================
# PRACTICE QUESTIONS
# =========================================================

# Q1. Print numbers from 1 to 20 using a for loop.
#
# Q2. Print the multiplication table of a given number.
#
# Q3. Print all odd numbers from 1 to 50.
#
# Q4. Find the sum of the first 10 natural numbers.
#
# Q5. Print the factorial of a number using a loop.
#
# Q6. Print each character of your name.
#
# Q7. Use break to stop a loop when a specific number is found.
#
# Q8. Use continue to skip all even numbers.


# =========================================================
# KEY TAKEAWAYS
# =========================================================

"""
Today You Learned:

✔ for Loop
✔ while Loop
✔ break Statement
✔ continue Statement
✔ Looping Through Strings
✔ Sum Using Loops
✔ Printing Even Numbers
✔ Countdown Using while Loop

Happy Coding! 🚀
"""

# =========================================================
# End of File
# =========================================================
