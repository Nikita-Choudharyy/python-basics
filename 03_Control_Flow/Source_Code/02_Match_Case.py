"""
=====================================================
Topic: Match-Case Statement in Python
File : 02_Match_Case.py

Description:
This file demonstrates:
1. Introduction to match-case
2. Basic match-case Syntax
3. Using Multiple Cases
4. Default Case (_)
5. Real-World Examples
6. Best Practices

Note:
The match-case statement is available in Python 3.10 and later.

Author : Nikita Choudhary
Repository : Python Basics
=====================================================
"""

# =====================================================
# 1. What is Match-Case?
# =====================================================

# The match-case statement is used to compare
# a value against multiple possible cases.
# It is similar to the switch statement
# found in many other programming languages.

print("Match-Case helps simplify multiple conditional checks.")

# =====================================================
# 2. Basic match-case Statement
# =====================================================

day = 3

print("\n===== Basic Match-Case =====")

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")

# =====================================================
# 3. Using Multiple Cases
# =====================================================

day = "Saturday"

print("\n===== Multiple Cases =====")

match day:
    case "Saturday" | "Sunday":
        print("Weekend")
    case _:
        print("Weekday")

# =====================================================
# 4. Default Case (_)
# =====================================================

fruit = "Apple"

print("\n===== Default Case =====")

match fruit:
    case "Mango":
        print("Mango Selected")
    case "Banana":
        print("Banana Selected")
    case _:
        print("Fruit Not Available")

# =====================================================
# 5. Real-World Example - Calculator
# =====================================================

num1 = 20
num2 = 5
operator = "*"

print("\n===== Simple Calculator =====")

match operator:
    case "+":
        print("Result:", num1 + num2)
    case "-":
        print("Result:", num1 - num2)
    case "*":
        print("Result:", num1 * num2)
    case "/":
        print("Result:", num1 / num2)
    case _:
        print("Invalid Operator")

# =====================================================
# 6. Real-World Example - Student Grade
# =====================================================

grade = "A"

print("\n===== Student Grade =====")

match grade:
    case "A":
        print("Excellent")
    case "B":
        print("Very Good")
    case "C":
        print("Good")
    case "D":
        print("Needs Improvement")
    case _:
        print("Invalid Grade")

# =====================================================
# 7. Best Practices
# =====================================================

# ✔ Use match-case when checking many fixed values.
# ✔ Always include a default case (_).
# ✔ Keep each case simple and readable.
# ✔ Use if-elif-else when conditions involve
#   ranges or complex expressions.

# =====================================================
# 8. Mini Practice
# =====================================================

# Try these on your own:
#
# 1. Print the month name using a month number.
# 2. Create a simple menu-driven calculator.
# 3. Display traffic signal actions (Red, Yellow, Green).
# 4. Display different greetings based on language.
# 5. Print the day type (Weekday/Weekend).

# =====================================================
# End of Program
# =====================================================

print("\nCongratulations! You completed Match-Case in Python. 🎉")