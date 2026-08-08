"""
=========================================================
📋 Copy vs Deep Copy in Python
=========================================================

This file covers:

1. Objects and References
2. Assignment
3. Object Identity
4. id()
5. is vs ==
6. Assignment vs Copying
7. Shallow Copy
8. Deep Copy
9. copy.copy()
10. copy.deepcopy()
11. Nested Lists
12. Nested Dictionaries
13. Nested Sets
14. Tuples Containing Mutable Objects
15. Multi-Level Nested Structures
16. Shared References
17. Mutation vs Reassignment
18. Deep Copy and Object Graphs
19. Performance Considerations
20. Common Mistakes
21. Best Practices
22. Debugging Practice
23. Interview Questions
24. Practice Questions
25. Real-World ML/Data Science Example
26. Key Takeaways

=========================================================
"""


# =========================================================
# 1. Objects and References
# =========================================================

print("=" * 60)
print("1. Objects and References")
print("=" * 60)


numbers = [10, 20, 30]

print("Numbers:", numbers)


print("""
Python variables are names that refer to objects.

Conceptually:

numbers
    |
    ↓
[10, 20, 30]
""")


# =========================================================
# 2. Assignment Does Not Create a Copy
# =========================================================

print("\n" + "=" * 60)
print("2. Assignment Does Not Create a Copy")
print("=" * 60)


numbers = [10, 20, 30]

other = numbers

print("numbers:", numbers)
print("other  :", other)

print(
    "Same object:",
    numbers is other
)


# Both names refer to the same list.


# =========================================================
# 3. Object Identity with id()
# =========================================================

print("\n" + "=" * 60)
print("3. Object Identity with id()")
print("=" * 60)


numbers = [10, 20, 30]

other = numbers

print("ID of numbers:", id(numbers))
print("ID of other  :", id(other))

print(
    "Same object:",
    numbers is other
)


# =========================================================
# 4. == vs is
# =========================================================

print("\n" + "=" * 60)
print("4. == vs is")
print("=" * 60)


a = [1, 2, 3]
b = [1, 2, 3]


print("a == b:", a == b)
print("a is b:", a is b)

print("ID of a:", id(a))
print("ID of b:", id(b))


print("""
== → Checks equality of values.

is → Checks object identity.
""")


# =========================================================
# 5. Same Object vs Equal Object
# =========================================================

print("\n" + "=" * 60)
print("5. Same Object vs Equal Object")
print("=" * 60)


# Same object

a = [1, 2, 3]

b = a

print("Same object example:")
print("a == b:", a == b)
print("a is b:", a is b)


# Separate objects

a = [1, 2, 3]

b = [1, 2, 3]

print("\nSeparate objects example:")
print("a == b:", a == b)
print("a is b:", a is b)


# =========================================================
# 6. Reference Sharing
# =========================================================

print("\n" + "=" * 60)
print("6. Reference Sharing")
print("=" * 60)


numbers = [1, 2, 3]

other = numbers

other.append(4)

print("numbers:", numbers)
print("other  :", other)

print(
    "Same object:",
    numbers is other
)


# Modifying through one reference
# affects the same object seen by the other.


# =========================================================
# 7. Assignment vs Copying
# =========================================================

print("\n" + "=" * 60)
print("7. Assignment vs Copying")
print("=" * 60)


original = [1, 2, 3]

assignment = original

copied = original.copy()


print(
    "Assignment shares object:",
    original is assignment
)

print(
    "Copy creates new object:",
    original is copied
)


# =========================================================
# 8. Shallow Copy
# =========================================================

print("\n" + "=" * 60)
print("8. Shallow Copy")
print("=" * 60)


original = [
    [1, 2],
    [3, 4]
]

shallow = original.copy()


print("Original:", original)
print("Shallow :", shallow)

print(
    "Same outer object:",
    original is shallow
)

print(
    "Same first nested object:",
    original[0] is shallow[0]
)


# New outer list
# Shared nested lists


# =========================================================
# 9. Shallow Copy with copy.copy()
# =========================================================

print("\n" + "=" * 60)
print("9. Shallow Copy with copy.copy()")
print("=" * 60)


import copy


original = [
    [1, 2],
    [3, 4]
]

shallow = copy.copy(original)


print(
    "Same outer object:",
    original is shallow
)

print(
    "Same nested object:",
    original[0] is shallow[0]
)


# =========================================================
# 10. Nested Mutation with Shallow Copy
# =========================================================

print("\n" + "=" * 60)
print("10. Nested Mutation with Shallow Copy")
print("=" * 60)


original = [
    [1, 2],
    [3, 4]
]

shallow = original.copy()

shallow[0].append(99)


print("Original:", original)
print("Shallow :", shallow)


# The nested list is shared.
# Therefore both structures reflect the mutation.


# =========================================================
# 11. Deep Copy
# =========================================================

print("\n" + "=" * 60)
print("11. Deep Copy")
print("=" * 60)


original = [
    [1, 2],
    [3, 4]
]

deep = copy.deepcopy(original)


print("Original:", original)
print("Deep    :", deep)

print(
    "Same outer object:",
    original is deep
)

print(
    "Same nested object:",
    original[0] is deep[0]
)


# Both outer and nested objects are independent.


# =========================================================
# 12. Deep Copy and Nested Mutation
# =========================================================

print("\n" + "=" * 60)
print("12. Deep Copy and Nested Mutation")
print("=" * 60)


original = [
    [1, 2],
    [3, 4]
]

deep = copy.deepcopy(original)

deep[0].append(100)


print("Original:", original)
print("Deep    :", deep)


# Original remains unchanged.


# =========================================================
# 13. Comparing Shallow and Deep Copy
# =========================================================

print("\n" + "=" * 60)
print("13. Comparing Shallow and Deep Copy")
print("=" * 60)


original = [
    [1, 2],
    [3, 4]
]

shallow = copy.copy(original)

deep = copy.deepcopy(original)


print(
    "Original is Shallow:",
    original is shallow
)

print(
    "Original is Deep:",
    original is deep
)

print(
    "Nested shared with Shallow:",
    original[0] is shallow[0]
)

print(
    "Nested shared with Deep:",
    original[0] is deep[0]
)


# =========================================================
# 14. Inspecting IDs
# =========================================================

print("\n" + "=" * 60)
print("14. Inspecting IDs")
print("=" * 60)


original = [
    [1, 2],
    [3, 4]
]

shallow = copy.copy(original)

deep = copy.deepcopy(original)


print("Outer IDs:")
print("Original:", id(original))
print("Shallow :", id(shallow))
print("Deep    :", id(deep))


print("\nNested IDs:")
print("Original[0]:", id(original[0]))
print("Shallow[0] :", id(shallow[0]))
print("Deep[0]    :", id(deep[0]))


# =========================================================
# 15. Nested Dictionary
# =========================================================

print("\n" + "=" * 60)
print("15. Nested Dictionary")
print("=" * 60)


original = {
    "student": {
        "name": "Nikita",
        "skills": ["Python", "SQL"]
    }
}

shallow = copy.copy(original)

deep = copy.deepcopy(original)


print(
    "Outer dictionary same:",
    original is shallow
)

print(
    "Nested dictionary shared with Shallow:",
    original["student"]
    is shallow["student"]
)

print(
    "Nested dictionary shared with Deep:",
    original["student"]
    is deep["student"]
)


# =========================================================
# 16. Nested Dictionary Mutation
# =========================================================

print("\n" + "=" * 60)
print("16. Nested Dictionary Mutation")
print("=" * 60)


original = {
    "student": {
        "name": "Nikita",
        "skills": ["Python", "SQL"]
    }
}

shallow = copy.copy(original)

deep = copy.deepcopy(original)


shallow["student"]["skills"].append(
    "Machine Learning"
)

deep["student"]["skills"].append(
    "Statistics"
)


print("Original:", original)
print("Shallow :", shallow)
print("Deep    :", deep)


# =========================================================
# 17. Multi-Level Nested Structure
# =========================================================

print("\n" + "=" * 60)
print("17. Multi-Level Nested Structure")
print("=" * 60)


data = [
    {
        "student": {
            "skills": [
                "Python",
                "Machine Learning"
            ]
        }
    }
]


shallow = copy.copy(data)

deep = copy.deepcopy(data)


print("Level 1:")
print(
    "Original is Shallow:",
    data is shallow
)

print(
    "Original is Deep:",
    data is deep
)


print("\nLevel 2:")

print(
    "Original[0] is Shallow[0]:",
    data[0] is shallow[0]
)

print(
    "Original[0] is Deep[0]:",
    data[0] is deep[0]
)


print("\nLevel 3:")

print(
    "Original student is Shallow student:",
    data[0]["student"]
    is shallow[0]["student"]
)

print(
    "Original student is Deep student:",
    data[0]["student"]
    is deep[0]["student"]
)


print("\nLevel 4:")

print(
    "Original skills is Shallow skills:",
    data[0]["student"]["skills"]
    is shallow[0]["student"]["skills"]
)

print(
    "Original skills is Deep skills:",
    data[0]["student"]["skills"]
    is deep[0]["student"]["skills"]
)


# =========================================================
# 18. Mutation vs Reassignment
# =========================================================

print("\n" + "=" * 60)
print("18. Mutation vs Reassignment")
print("=" * 60)


original = [
    [1, 2],
    [3, 4]
]

shallow = copy.copy(original)


# Mutation

shallow[0].append(100)

print("After mutation:")
print("Original:", original)
print("Shallow :", shallow)


# Reset

original = [
    [1, 2],
    [3, 4]
]

shallow = copy.copy(original)


# Reassignment

shallow[0] = [100, 200]


print("\nAfter reassignment:")
print("Original:", original)
print("Shallow :", shallow)


print("""
Mutation:
Changes the existing shared object.

Reassignment:
Replaces the reference in the outer container.
""")


# =========================================================
# 19. Tuple Containing Mutable Objects
# =========================================================

print("\n" + "=" * 60)
print("19. Tuple Containing Mutable Objects")
print("=" * 60)


data = (
    [1, 2],
    [3, 4]
)


data[0].append(100)

print("Tuple:", data)


print("""
The tuple itself is immutable.

But the lists inside the tuple are mutable.
""")


# =========================================================
# 20. Copying Tuple with Mutable Objects
# =========================================================

print("\n" + "=" * 60)
print("20. Copying Tuple with Mutable Objects")
print("=" * 60)


original = (
    [1, 2],
    [3, 4]
)

shallow = copy.copy(original)

deep = copy.deepcopy(original)


print(
    "Original is Shallow:",
    original is shallow
)

print(
    "Original is Deep:",
    original is deep
)

print(
    "Nested list shared with Shallow:",
    original[0] is shallow[0]
)

print(
    "Nested list shared with Deep:",
    original[0] is deep[0]
)


# =========================================================
# 21. Shared References
# =========================================================

print("\n" + "=" * 60)
print("21. Shared References")
print("=" * 60)


shared = [1, 2, 3]

data = [shared, shared]


print("Data:", data)

print(
    "Same nested object:",
    data[0] is data[1]
)


# =========================================================
# 22. Deep Copy and Shared References
# =========================================================

print("\n" + "=" * 60)
print("22. Deep Copy and Shared References")
print("=" * 60)


shared = [1, 2, 3]

data = [shared, shared]

deep = copy.deepcopy(data)


print(
    "Original shared:",
    data[0] is data[1]
)

print(
    "Deep shared:",
    deep[0] is deep[1]
)

print(
    "Original vs Deep:",
    data[0] is deep[0]
)


# Deep Copy preserves internal sharing relationships.


# =========================================================
# 23. Copying Dictionaries
# =========================================================

print("\n" + "=" * 60)
print("23. Copying Dictionaries")
print("=" * 60)


original = {
    "name": "Python",
    "topics": ["OOP", "Functions"]
}

copied = original.copy()


print(
    "Same dictionary:",
    original is copied
)

print(
    "Same topics list:",
    original["topics"] is copied["topics"]
)


# =========================================================
# 24. Copying Sets
# =========================================================

print("\n" + "=" * 60)
print("24. Copying Sets")
print("=" * 60)


original = {1, 2, 3}

copied = original.copy()


print("Original:", original)
print("Copied  :", copied)

print(
    "Same object:",
    original is copied
)

print(
    "Equal values:",
    original == copied
)


# =========================================================
# 25. Complex Nested Structure
# =========================================================

print("\n" + "=" * 60)
print("25. Complex Nested Structure")
print("=" * 60)


data = {
    "student": {
        "name": "Nikita",
        "skills": ["Python", "SQL"],
        "scores": {
            "Python": 90,
            "SQL": 85
        }
    }
}


shallow = copy.copy(data)

deep = copy.deepcopy(data)


print(
    "Student shared with Shallow:",
    data["student"]
    is shallow["student"]
)

print(
    "Student shared with Deep:",
    data["student"]
    is deep["student"]
)


print(
    "Skills shared with Shallow:",
    data["student"]["skills"]
    is shallow["student"]["skills"]
)

print(
    "Skills shared with Deep:",
    data["student"]["skills"]
    is deep["student"]["skills"]
)


print(
    "Scores shared with Shallow:",
    data["student"]["scores"]
    is shallow["student"]["scores"]
)

print(
    "Scores shared with Deep:",
    data["student"]["scores"]
    is deep["student"]["scores"]
)


# =========================================================
# 26. Selective Reassignment
# =========================================================

print("\n" + "=" * 60)
print("26. Selective Reassignment")
print("=" * 60)


original = {
    "skills": ["Python", "SQL"],
    "scores": [90, 80]
}

shallow = original.copy()


shallow["skills"] = [
    "Python",
    "SQL",
    "Machine Learning"
]


print("Original:", original)
print("Shallow :", shallow)


# Reassignment changes only the shallow dictionary's reference.


# =========================================================
# 27. Deep Copy Performance Consideration
# =========================================================

print("\n" + "=" * 60)
print("27. Deep Copy Performance Consideration")
print("=" * 60)


print("""
Deep Copy may require more:

- Memory
- Processing time
- Recursive copying work

Therefore:

Use the simplest copying strategy
that correctly satisfies the requirement.

Do not use deepcopy() automatically.
""")


# =========================================================
# 28. Choosing the Right Approach
# =========================================================

print("\n" + "=" * 60)
print("28. Choosing the Right Approach")
print("=" * 60)


print("""
Assignment:

Use when another reference to the same
object is intentionally required.


Shallow Copy:

Use when a new outer container is required
and sharing nested objects is acceptable.


Deep Copy:

Use when nested mutable objects also need
to become independent.
""")


# =========================================================
# 29. Debugging Example
# =========================================================

print("\n" + "=" * 60)
print("29. Debugging Example")
print("=" * 60)


data = {
    "scores": [80, 90, 95]
}

backup = copy.copy(data)

backup["scores"].append(100)


print("Original:", data)
print("Backup  :", backup)


print(
    "Same outer dictionary:",
    data is backup
)

print(
    "Same scores list:",
    data["scores"] is backup["scores"]
)


# =========================================================
# 30. Advanced Debugging Challenge
# =========================================================

print("\n" + "=" * 60)
print("30. Advanced Debugging Challenge")
print("=" * 60)


shared = {
    "scores": [90, 80]
}

original = [shared, shared]

shallow = copy.copy(original)

deep = copy.deepcopy(original)


deep[0]["scores"].append(100)


print("Original:", original)
print("Shallow :", shallow)
print("Deep    :", deep)


print(
    "Deep shared reference:",
    deep[0] is deep[1]
)

print(
    "Original vs Deep:",
    original[0] is deep[0]
)


# =========================================================
# 31. ML / Data Science Example
# =========================================================

print("\n" + "=" * 60)
print("31. ML / Data Science Example")
print("=" * 60)


model_config = {
    "model": "Linear Regression",
    "parameters": {
        "alpha": 0.01,
        "features": [
            "age",
            "income",
            "experience"
        ]
    }
}


experiment_config = copy.deepcopy(model_config)


experiment_config["parameters"]["features"].append(
    "education"
)


print("Original Configuration:")
print(model_config)


print("\nExperiment Configuration:")
print(experiment_config)


# Deep Copy prevents the nested feature list
# from being unintentionally shared.


# =========================================================
# 32. Student Dataset Backup System
# =========================================================

print("\n" + "=" * 60)
print("32. Student Dataset Backup System")
print("=" * 60)


students = {
    "student_1": {
        "name": "A",
        "skills": ["Python", "SQL"],
        "scores": [85, 90]
    },
    "student_2": {
        "name": "B",
        "skills": ["Python", "Statistics"],
        "scores": [80, 88]
    }
}


shallow_backup = copy.copy(students)

deep_backup = copy.deepcopy(students)


print(
    "Original is Shallow:",
    students is shallow_backup
)

print(
    "Original is Deep:",
    students is deep_backup
)


print(
    "Nested student shared with Shallow:",
    students["student_1"]
    is shallow_backup["student_1"]
)

print(
    "Nested student shared with Deep:",
    students["student_1"]
    is deep_backup["student_1"]
)


deep_backup["student_1"]["skills"].append(
    "Machine Learning"
)


print("\nOriginal:")
print(students)


print("\nDeep Backup:")
print(deep_backup)


# =========================================================
# 33. Common Mistakes
# =========================================================

print("\n" + "=" * 60)
print("33. Common Mistakes")
print("=" * 60)


print("""
❌ Mistake 1:
Thinking assignment creates a copy.

    backup = original


❌ Mistake 2:
Thinking .copy() performs Deep Copy.

    backup = original.copy()


❌ Mistake 3:
Forgetting about nested objects.


❌ Mistake 4:
Using is to compare values.

Use == for equality.


❌ Mistake 5:
Using deepcopy() everywhere.


❌ Mistake 6:
Confusing mutation with reassignment.


❌ Mistake 7:
Forgetting that tuples can contain
mutable objects.
""")


# =========================================================
# 34. Best Practices
# =========================================================

print("\n" + "=" * 60)
print("34. Best Practices")
print("=" * 60)


print("""
✔ Understand object references first.

✔ Use is for identity checks.

✔ Use == for equality checks.

✔ Use .copy() or copy.copy()
  when Shallow Copy is sufficient.

✔ Use copy.deepcopy()
  when nested mutable objects
  need to be independent.

✔ Do not use Deep Copy automatically.

✔ Consider memory and performance.

✔ Understand mutation vs reassignment.

✔ Inspect nested objects when debugging.

✔ Use meaningful names such as:

    original
    shallow_copy
    deep_copy
""")


# =========================================================
# 35. Interview Questions
# =========================================================

print("\n" + "=" * 60)
print("35. Interview Questions")
print("=" * 60)


print("""
Basic:

1. What is the difference between assignment
   and copying?

2. What does id() tell us?

3. What is the difference between == and is?

4. What is Shallow Copy?

5. What is Deep Copy?

6. What does copy.copy() do?

7. What does copy.deepcopy() do?


Intermediate:

8. Why can modifying a nested list affect
   the original after a Shallow Copy?

9. Why does Deep Copy avoid sharing nested
   mutable objects?

10. What is the difference between:

        a = b

    and:

        a = b.copy()


11. What is mutation?

12. What is reassignment?

13. Can a tuple contain mutable objects?

14. Why can Deep Copy be more expensive?


Advanced:

15. Explain Shallow Copy using object references.

16. Explain Deep Copy using a nested object graph.

17. How does Deep Copy handle shared references?

18. Why isn't deepcopy() always the best choice?

19. When should Shallow Copy be used?

20. When should Deep Copy be used?
""")


# =========================================================
# 36. Debugging Questions
# =========================================================

print("\n" + "=" * 60)
print("36. Debugging Questions")
print("=" * 60)


print("""
Question 1:

original = [1, 2, 3]
other = original

other.append(4)

Why does original change?


Question 2:

original = [[1, 2], [3, 4]]
shallow = original.copy()

shallow[0].append(100)

Why does original change?


Question 3:

deep = copy.deepcopy(original)

deep[0].append(100)

Why does original remain unchanged?


Question 4:

data = {
    "scores": [80, 90]
}

backup = data.copy()

Why can:

backup["scores"].append(100)

change data?


Question 5:

Explain the difference between:

backup["scores"].append(100)

and:

backup["scores"] = [80, 90, 100]
""")


# =========================================================
# 37. Practice Questions
# =========================================================

print("\n" + "=" * 60)
print("37. Practice Questions")
print("=" * 60)


print("""
🟢 Easy

1. Create a list and assign it to another variable.
   Check identity using is.


2. Create two separate lists with equal values.
   Compare == and is.


3. Create a Shallow Copy and check outer identity.


🟡 Medium

4. Create a nested list and demonstrate
   Shallow Copy behavior.


5. Create a nested list and demonstrate
   Deep Copy behavior.


6. Create a nested dictionary and compare
   Shallow and Deep Copy.


🔴 Hard

7. Create shared references inside a structure
   and observe Deep Copy behavior.


8. Demonstrate mutation vs reassignment.


9. Create a tuple containing mutable lists
   and compare Shallow and Deep Copy.
""")


# =========================================================
# 38. Final Comparison
# =========================================================

print("\n" + "=" * 60)
print("38. Final Comparison")
print("=" * 60)


print("""
=========================================================
Assignment
=========================================================

Syntax:

    b = a

New outer object:
    No

Nested objects:
    Shared

Purpose:
    Another reference to same object


=========================================================
Shallow Copy
=========================================================

Syntax:

    copy.copy(a)
    a.copy()

New outer object:
    Yes

Nested objects:
    May be shared

Recursive copying:
    No

Purpose:
    Independent outer container


=========================================================
Deep Copy
=========================================================

Syntax:

    copy.deepcopy(a)

New outer object:
    Yes

Nested objects:
    Recursively copied

Recursive copying:
    Yes

Purpose:
    Independent nested structure
=========================================================
""")


# =========================================================
# 39. Final Mental Model
# =========================================================

print("\n" + "=" * 60)
print("39. Final Mental Model")
print("=" * 60)


print("""
                 OBJECT
                   |
          +--------+--------+
          |        |        |
          ↓        ↓        ↓
     Assignment  Shallow   Deep
                  Copy     Copy
          |        |        |
          ↓        ↓        ↓
       Same      New       New
       Object    Outer     Outer
                   |        |
                   ↓        ↓
                Shared    New Nested
                Nested    Objects
""")


# =========================================================
# 40. Key Takeaways
# =========================================================

print("\n" + "=" * 60)
print("40. Key Takeaways")
print("=" * 60)


print("""
✔ Python variables are names that refer to objects.

✔ Assignment creates another reference.

✔ id() helps inspect object identity.

✔ is checks identity.

✔ == checks equality.

✔ Shallow Copy creates a new outer object.

✔ Shallow Copy can share nested mutable objects.

✔ Deep Copy recursively copies nested objects.

✔ Deep Copy can preserve shared-reference
  relationships within the copied structure.

✔ Mutation changes an existing object.

✔ Reassignment changes what a name or
  container entry refers to.

✔ Tuples are immutable but may contain
  mutable objects.

✔ Deep Copy can require more memory
  and processing.

✔ Deep Copy should be used when its
  behavior is actually required.

✔ Understanding object references makes
  copying behavior easier to predict.
""")


# =========================================================
# 41. Summary
# =========================================================

print("\n" + "=" * 60)
print("41. Summary")
print("=" * 60)


print("""
Topics covered:

✔ Objects and References
✔ Assignment
✔ Object Identity
✔ id()
✔ is vs ==
✔ Assignment vs Copying
✔ Shallow Copy
✔ Deep Copy
✔ copy.copy()
✔ copy.deepcopy()
✔ Nested Lists
✔ Nested Dictionaries
✔ Nested Sets
✔ Tuples with Mutable Objects
✔ Multi-Level Nested Structures
✔ Shared References
✔ Mutation vs Reassignment
✔ Object Graphs
✔ Performance Considerations
✔ Debugging
✔ Interview Questions
✔ Practice Questions
✔ Real-World ML/Data Science Example
✔ Common Mistakes
✔ Best Practices
""")


# =========================================================
# 42. Python Internals Completed
# =========================================================

print("\n" + "=" * 60)
print("42. Python Internals Completed")
print("=" * 60)


print("""
🎉 Python Internals Section Completed!

01 — Namespaces
02 — Scope
03 — LEGB Rule
04 — Copy vs Deep Copy

You now have a strong foundation in:

- Names and Objects
- Namespaces
- Scope
- LEGB Name Resolution
- Closures
- global
- nonlocal
- Object Identity
- Object References
- Shallow Copy
- Deep Copy
- Mutable vs Immutable Objects
- Shared References
""")


# =========================================================
# 43. What's Next?
# =========================================================

print("\n" + "=" * 60)
print("43. What's Next?")
print("=" * 60)


print("""
Python Internals is now complete.

Before moving forward, practice explaining:

1. Why b = a does not create a copy.

2. Difference between is and ==.

3. Shallow Copy with nested lists.

4. Deep Copy with nested dictionaries.

5. Mutation vs reassignment.

6. Shared references.

7. Why deepcopy() can be more expensive.

8. When to use Assignment,
   Shallow Copy, or Deep Copy.

Next major topic can be started
after revising Python Internals.
""")


# =========================================================
# 🎉 END
# =========================================================

print("\n" + "=" * 60)
print("🎉 04_Copy_vs_Deep_Copy.py Completed Successfully!")
print("=" * 60)