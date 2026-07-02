# -----------------------------
# Python Strings
# -----------------------------
# Strings are sequences of characters enclosed in quotes.

# -----------------------------
# Creating strings
# -----------------------------
name = "Python"
message = 'Learning Strings'

print(name)
print(message)

# -----------------------------
# String indexing and slicing
# -----------------------------
text = "Hello World"

print("First character:", text[0])
print("Last character:", text[-1])
print("Slicing (0:5):", text[0:5])
print("Reverse string:", text[::-1])

# -----------------------------
# String concatenation
# -----------------------------
first = "Hello"
second = "Python"

print(first + " " + second)

# -----------------------------
# String methods
# -----------------------------
sample = "  python programming  "

print("Upper:", sample.upper())
print("Lower:", sample.lower())
print("Title:", sample.title())
print("Strip:", sample.strip())
print("Replace:", sample.replace("python", "java"))
print("Find:", sample.find("programming"))
print("Count:", sample.count("p"))

# -----------------------------
# Checking string properties
# -----------------------------
print("Is alpha:", "Python".isalpha())
print("Is digit:", "123".isdigit())
print("Is alphanumeric:", "Python3".isalnum())

# -----------------------------
# String formatting
# -----------------------------
language = "Python"
version = 3

print(f"{language} version is {version}")

# -----------------------------
# Practice examples
# -----------------------------

# Count vowels in a string
word = "education"
vowels = "aeiou"
count = 0

for ch in word:
    if ch in vowels:
        count += 1

print("Vowel count:", count)

# Check if a string is palindrome
text = "madam"
if text == text[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")
