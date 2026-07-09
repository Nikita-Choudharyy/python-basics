"""
=====================================================
Topic: Bitwise Operators in Python
File : 05_Bitwise_Operators.py

Description:
This file demonstrates:
1. Bitwise AND (&)
2. Bitwise OR (|)
3. Bitwise XOR (^)
4. Bitwise NOT (~)
5. Left Shift (<<)
6. Right Shift (>>)
7. Real-World Examples
8. Best Practices

Author : Nikita Choudhary
Repository : Python Basics
=====================================================
"""

# =====================================================
# 1. Creating Variables
# =====================================================

a = 10      # Binary: 1010
b = 6       # Binary: 0110

print("Value of a:", a)
print("Value of b:", b)

# =====================================================
# 2. Bitwise AND (&)
# =====================================================

print("\n===== Bitwise AND (&) =====")

result = a & b

print(f"{a} & {b} = {result}")

# =====================================================
# 3. Bitwise OR (|)
# =====================================================

print("\n===== Bitwise OR (|) =====")

result = a | b

print(f"{a} | {b} = {result}")

# =====================================================
# 4. Bitwise XOR (^)
# =====================================================

print("\n===== Bitwise XOR (^) =====")

result = a ^ b

print(f"{a} ^ {b} = {result}")

# =====================================================
# 5. Bitwise NOT (~)
# =====================================================

print("\n===== Bitwise NOT (~) =====")

result = ~a

print(f"~{a} = {result}")

# =====================================================
# 6. Left Shift (<<)
# =====================================================

print("\n===== Left Shift (<<) =====")

result = a << 1

print(f"{a} << 1 = {result}")

# =====================================================
# 7. Right Shift (>>) 
# =====================================================

print("\n===== Right Shift (>>) =====")

result = a >> 1

print(f"{a} >> 1 = {result}")

# =====================================================
# 8. Binary Representation
# =====================================================

print("\n===== Binary Representation =====")

print(f"Binary of {a}: {bin(a)}")
print(f"Binary of {b}: {bin(b)}")

# =====================================================
# 9. Real-World Example
# =====================================================

print("\n===== Permission System =====")

READ = 1      # 001
WRITE = 2     # 010
EXECUTE = 4   # 100

user_permission = READ | WRITE

print("User Permission Value:", user_permission)

print("Can Read?    ", bool(user_permission & READ))
print("Can Write?   ", bool(user_permission & WRITE))
print("Can Execute? ", bool(user_permission & EXECUTE))

# =====================================================
# 10. Best Practices
# =====================================================

# ✔ Learn binary representation before using bitwise operators.
# ✔ Use bitwise operators only when needed.
# ✔ Bitwise operators are commonly used in:
#    - Permissions
#    - Flags
#    - Embedded Systems
#    - Networking
#    - Performance Optimization

# =====================================================
# 11. Mini Practice
# =====================================================

# Try these on your own:
#
# 1. Perform all bitwise operations on 12 and 5.
# 2. Print the binary representation of a number.
# 3. Perform left shift on 8.
# 4. Perform right shift on 32.
# 5. Create a simple permission system using bitwise operators.

# =====================================================
# End of Program
# =====================================================

print("\nCongratulations! You completed Bitwise Operators in Python. 🎉")