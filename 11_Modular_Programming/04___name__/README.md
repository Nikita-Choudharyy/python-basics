# 🏷️ `__name__` in Python

Welcome to the **`__name__` in Python** section of this repository.

Every Python file contains a special built-in variable called **`__name__`**. This variable helps Python determine whether a file is being executed directly or imported as a module.

Understanding `__name__` is essential for writing reusable modules, separating testing code from production code, and building professional Python applications.

One of the most commonly used Python statements,

```python
if __name__ == "__main__":
```

is based on this concept.

In this notebook, you will learn how Python assigns the value of `__name__`, what `__main__` means, and why this pattern is widely used in real-world Python projects.

---

# 🎯 Learning Outcomes

After completing this notebook, you will be able to:

- ✅ Understand what `__name__` is.
- ✅ Explain the purpose of `__main__`.
- ✅ Differentiate between executing and importing a Python file.
- ✅ Understand how Python executes modules.
- ✅ Use `if __name__ == "__main__":` correctly.
- ✅ Write reusable Python modules.
- ✅ Follow professional Python coding practices.

---

# 📂 Folder Structure

```text
04___name__/

│
├── README.md
├── 04___name__.ipynb
├── calculator.py
└── main.py
```

---

# 📚 Topics Covered

This notebook covers the following topics:

- 📖 Introduction
- 🎯 Learning Objectives
- 🤔 Why Do We Need `__name__`?
- 🌍 Real-World Analogy
- 📌 What is `__name__`?
- 🧠 Understanding `__main__`
- 🔄 How Python Executes a File
- 📝 Running a Python File Directly
- 📦 Importing a Python File
- 🎯 `if __name__ == "__main__":`
- 🌍 Real-World Use Cases
- ⚠️ Common Mistakes
- ✅ Best Practices
- 💼 Interview Questions
- 🐞 Debugging Practice
- 🎯 Mini Practice

---

# 📋 Prerequisites

Before starting this notebook, you should be familiar with:

- Python Modules
- Import Statements
- Functions
- Basic Python Syntax

---

# 💡 Why Learn `__name__`?

The `__name__` variable is used in almost every professional Python project.

It helps developers:

- ♻️ Build reusable modules
- 🧪 Separate testing code from reusable code
- 📦 Prevent unwanted code execution during imports
- 🧹 Keep projects organized
- 🚀 Build scalable Python applications

Without this concept, importing Python modules would often execute unnecessary code.

---

# 🌍 Real-World Applications

The `__name__` concept is commonly used in:

- 🤖 Machine Learning Projects
- 📊 Data Science Scripts
- 🌐 Web Development
- ⚙️ Automation Scripts
- 📦 Python Libraries
- 🧪 Testing Modules
- 🖥️ Command-Line Applications

---

# 📓 Files Included

| File | Description |
|------|-------------|
| `04___name__.ipynb` | Complete tutorial explaining `__name__`, `__main__`, execution flow, examples, interview questions, debugging exercises, and best practices. |
| `calculator.py` | Demonstrates how `__name__` behaves when a file is executed directly or imported. |
| `main.py` | Imports `calculator.py` to demonstrate module execution behavior. |
| `README.md` | Documentation for this section. |

---

# ▶️ How to Run

1. Open `04___name__.ipynb`.
2. Read each concept carefully.
3. Create the example files (`calculator.py` and `main.py`).
4. Execute `calculator.py` directly.
5. Execute `main.py`.
6. Compare the outputs.
7. Complete the debugging exercises and mini practice.

> **Tip:** Observe the value of `__name__` in both situations to clearly understand how Python distinguishes between running and importing a module.

---

# ✅ Best Practices

- Keep reusable functions and classes outside the `if` block.
- Use `if __name__ == "__main__":` for testing or demonstration code.
- Avoid placing important logic only inside the `if` block.
- Write modules that can be safely imported without unwanted execution.
- Follow this pattern consistently in professional Python projects.

---

# 👨‍🎓 Who Should Use This?

This notebook is designed for:

- 🟢 Python Beginners
- 🎓 Students learning Python
- 💼 Interview Preparation
- 🤖 Future Data Science & Machine Learning learners
- 👨‍💻 Anyone interested in writing reusable Python modules

---

# 🚀 What's Next?

Once you understand `__name__`, continue with:

➡️ **05_Virtual_Environment**

In the next notebook, you will learn:

- What is a Virtual Environment?
- Why Virtual Environments are important.
- Creating a Virtual Environment.
- Activating and Deactivating it.
- Installing packages inside a Virtual Environment.
- Managing project dependencies.

Happy Learning! 🚀