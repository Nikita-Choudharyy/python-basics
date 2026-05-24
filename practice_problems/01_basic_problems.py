# =====================================================================
# Topic: Basic Python Practice Problems (Foundational Logic)
# Purpose: Implementing loops, conditionals, and math logic in Python.
# =====================================================================

print("--- PROBLEM 1: CHECK IF A NUMBER IS PRIME ---")
# Logic: A number greater than 1 that has no positive divisors other than 1 and itself.

def is_prime(number):
    if number <= 1:
        return False
    # Checking factors from 2 up to the square root of the number for optimization
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False  # Found a factor, so it's not prime
    return True

# Testing our function
test_num = 17
print(f"Is {test_num} a prime number? {is_prime(test_num)}")  # Output: True


print("\n--- PROBLEM 2: FIBONACCI SEQUENCE GENERATION ---")
# Logic: Every number is the sum of the two preceding ones (e.g., 0, 1, 1, 2, 3, 5, 8...)

def generate_fibonacci(n_terms):
    sequence = [0, 1]
    if n_terms <= 0:
        return "Please enter a positive integer."
    elif n_terms == 1:
        return [0]
    elif n_terms == 2:
        return sequence
    
    # Loop to add terms dynamically
    while len(sequence) < n_terms:
        next_term = sequence[-1] + sequence[-2]
        sequence.append(next_term)
    return sequence

print(f"Fibonacci sequence (first 8 terms): {generate_fibonacci(8)}")


print("\n--- PROBLEM 3: PALINDROME CHECKER (STRINGS & NUMBERS) ---")
# Logic: A string or number that reads the same backward as forward (e.g., "radar").

def is_palindrome(data):
    # Converting data to string so it works for both integers and strings safely
    clean_str = str(data).lower().replace(" ", "")
    # Using python's sleek slicing method to reverse the string
    return clean_str == clean_str[::-1]

print(f"Is 'radar' a palindrome? {is_palindrome('radar')}")  # Output: True
print(f"Is 12321 a palindrome? {is_palindrome(12321)}")    # Output: True
print(f"Is 'python' a palindrome? {is_palindrome('python')}") # Output: True


# =====================================================================
# 📝 STUDENT REFLECTION & QUICK REVISION
# - Slicing [[::-1]] is the fastest way to reverse strings in Python.
# - Range optimization (checking factors till sqrt of n) saves computation time.
# =====================================================================
