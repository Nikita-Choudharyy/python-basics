# 🐍 Python Internals

A structured and practical guide to understanding the **internal behavior of Python**.

This section focuses on how Python manages **names, namespaces, scope, name resolution, object references, and copying of objects**.

---


## 📂 Folder Structure

    02_Python_Internals/
    │
    ├── README.md
    │
    ├── Notebooks/
    │   ├── 01_Namespaces.ipynb
    │   ├── 02_Scope.ipynb
    │   ├── 03_LEGB_Rule.ipynb
    │   └── 04_Copy_vs_Deep_Copy.ipynb
    │
    └── Source_Code/
        ├── 01_Namespaces.py
        ├── 02_Scope.py
        ├── 03_LEGB_Rule.py
        └── 04_Copy_vs_Deep_Copy.py

---

# 📖 01 — Namespaces

A **Namespace** is a system used by Python to organize and manage names.

It maintains a mapping between names and the objects they refer to.

### Topics Covered

- 🔹 What is a Namespace?
- 🔹 Names and Objects
- 🔹 Local Namespace
- 🔹 Global Namespace
- 🔹 Built-in Namespace
- 🔹 Module Namespace
- 🔹 Function Namespace
- 🔹 `globals()`
- 🔹 `locals()`
- 🔹 Namespace Inspection
- 🔹 Name Conflicts
- 🔹 Variable Resolution
- 🔹 Practical Examples
- 🔹 Debugging
- 🔹 Common Mistakes
- 🔹 Best Practices
- 🔹 Key Takeaways

### Key Concept

    Name
      ↓
    Namespace
      ↓
    Object

---

# 📖 02 — Scope

**Scope** defines where a name can be accessed in a Python program.

Understanding Scope is important when working with variables, functions, nested functions, and closures.

### Topics Covered

- 🔹 What is Scope?
- 🔹 Local Scope
- 🔹 Global Scope
- 🔹 Enclosing Scope
- 🔹 Built-in Scope
- 🔹 Function Scope
- 🔹 Nested Functions
- 🔹 Variable Accessibility
- 🔹 `global`
- 🔹 `nonlocal`
- 🔹 Scope and Functions
- 🔹 Scope-related Errors
- 🔹 Debugging
- 🔹 Common Mistakes
- 🔹 Best Practices
- 🔹 Key Takeaways

### Scope Concept

    Local
      ↓
    Enclosing
      ↓
    Global
      ↓
    Built-in

---

# 📖 03 — LEGB Rule

The **LEGB Rule** explains how Python searches for a name.

### LEGB

- **L → Local**
- **E → Enclosing**
- **G → Global**
- **B → Built-in**

Python searches for names through these scopes in order.

### Lookup Order

    Local
      ↓
    Enclosing
      ↓
    Global
      ↓
    Built-in

If Python cannot find the requested name, a `NameError` can occur.

### Topics Covered

- 🔹 Name Resolution
- 🔹 LEGB Rule
- 🔹 Local Scope
- 🔹 Enclosing Scope
- 🔹 Global Scope
- 🔹 Built-in Scope
- 🔹 Name Shadowing
- 🔹 Built-in Shadowing
- 🔹 `builtins` Module
- 🔹 Functions and LEGB
- 🔹 Lambda Functions and LEGB
- 🔹 Comprehension Scope
- 🔹 Closures and LEGB
- 🔹 Free Variables
- 🔹 Closure Cells
- 🔹 `global`
- 🔹 `nonlocal`
- 🔹 `NameError`
- 🔹 `UnboundLocalError`
- 🔹 Debugging
- 🔹 Interview Questions
- 🔹 Practice Questions
- 🔹 Common Mistakes
- 🔹 Best Practices
- 🔹 Key Takeaways

### LEGB Visualization

    NAME
      │
      ▼
    LOCAL
      │
      │ Not Found
      ▼
    ENCLOSING
      │
      │ Not Found
      ▼
    GLOBAL
      │
      │ Not Found
      ▼
    BUILT-IN
      │
      │ Not Found
      ▼
    NameError

---

# 📖 04 — Copy vs Deep Copy

Python variables are names that refer to objects.

Understanding object references is especially important when working with **mutable and nested data structures**.

### Topics Covered

- 🔹 Objects and References
- 🔹 Assignment
- 🔹 Object Identity
- 🔹 `id()`
- 🔹 `is`
- 🔹 `==`
- 🔹 Assignment vs Copying
- 🔹 Shallow Copy
- 🔹 Deep Copy
- 🔹 `copy.copy()`
- 🔹 `copy.deepcopy()`
- 🔹 Nested Lists
- 🔹 Nested Dictionaries
- 🔹 Nested Sets
- 🔹 Tuples Containing Mutable Objects
- 🔹 Multi-Level Nested Structures
- 🔹 Shared References
- 🔹 Mutation vs Reassignment
- 🔹 Object Graphs
- 🔹 Performance Considerations
- 🔹 Debugging
- 🔹 Interview Questions
- 🔹 Practice Questions
- 🔹 Real-World ML/Data Science Examples
- 🔹 Common Mistakes
- 🔹 Best Practices
- 🔹 Key Takeaways

---

# 🎯 Learning Objectives

After completing this section, you should be able to:

- ✅ Understand Python Namespaces.
- ✅ Explain Local, Enclosing, Global, and Built-in Scope.
- ✅ Understand the LEGB name-resolution process.
- ✅ Explain how Python searches for names.
- ✅ Understand `global` and `nonlocal`.
- ✅ Understand object references.
- ✅ Explain object identity using `id()` and `is`.
- ✅ Distinguish `is` from `==`.
- ✅ Understand Assignment.
- ✅ Understand Shallow Copy.
- ✅ Understand Deep Copy.
- ✅ Identify shared nested references.
- ✅ Understand mutation vs reassignment.
- ✅ Understand mutable and immutable objects.
- ✅ Choose an appropriate copying strategy.
- ✅ Debug common Python Internals problems.


---

# 🤖 Why Python Internals Matter for AI/ML

Understanding Python Internals becomes valuable when working with:

- 🤖 Machine Learning pipelines
- 📊 Data preprocessing
- 🧮 Numerical computation
- ⚙️ Model configurations
- 🧪 ML experiments
- 📦 Nested datasets
- 🔧 Custom Python utilities
- 🏗️ Large Python projects

For example, understanding object references and copying can help prevent accidental modification of:

    Model Configuration
            ↓
    Hyperparameters
            ↓
    Feature Lists
            ↓
    Training Settings

Understanding Scope and LEGB is also useful when working with:

    Functions
       ↓
    Nested Functions
       ↓
    Closures
       ↓
    Callbacks
       ↓
    ML/Data Science Code


---



# 💻 Learning Approach

Each topic is available in two formats.

## 📓 Jupyter Notebooks

The notebooks provide an interactive learning environment containing:

- 📖 Concept explanations
- 💻 Code examples
- 🔍 Practical demonstrations
- 🧠 Visual representations
- 🐞 Debugging exercises
- 🎯 Practice questions
- 💼 Interview questions
- 🔥 Advanced coding challenges
- 🤖 Real-world ML/Data Science examples
- ⚠️ Common mistakes
- ✅ Best practices
- 📌 Key takeaways
- 📝 Summaries

## 🐍 Source Code

Each notebook has a corresponding `.py` source-code file.

This provides a consistent learning workflow:

    Jupyter Notebook
           ↓
    Concept Understanding
           ↓
    Code Examples
           ↓
    Source Code
           ↓
    Practice
           ↓
    Debugging

---


# 🔗 Connection Between Topics

The four topics in Python Internals are connected:

    Namespaces
        ↓
    Where names are stored
        ↓
    Scope
        ↓
    Where names can be accessed
        ↓
    LEGB
        ↓
    How Python searches for names
        ↓
    Object References
        ↓
    What names refer to
        ↓
    Shallow / Deep Copy
        ↓
    How references behave when copying

Together, these concepts provide a deeper understanding of how Python programs work.

---


# 🚀 What's Next?

After completing **Python Internals**, the next section in the Python learning journey is:

## 📂 03_Advanced_Functions

The next section focuses on strengthening and extending Python function concepts through advanced argument handling, unpacking, Lambda revision, and Higher-Order Functions.

---

# 🤝 Contributing

Contributions, suggestions, and improvements are always welcome.

If you find an issue or have ideas for enhancement, feel free to open an issue or submit a pull request.

