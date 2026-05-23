# =====================================================================
# Topic: Decorators in Python (Advanced Concepts for Data Science)
# Purpose: Learning how to modify the behavior of functions dynamically.
# =====================================================================

print("--- 1. UNDERSTANDING FUNCTIONS AS FIRST-CLASS CITIZENS ---")
# Before learning decorators, we must know that functions can be passed as arguments,
# returned from other functions, and assigned to variables.

def greet(name):
    return f"Hello, {name}!"

# Assigning function to a variable
say_hello = greet
print(say_hello("Nikita"))  # Output: Hello, Nikita!


print("\n--- 2. CREATING OUR FIRST SIMPLE DECORATOR ---")
# A decorator is a function that takes another function as an argument,
# adds some extra functionality, and returns it without changing the original code.

def my_decorator(original_function):
    def wrapper_function():
        print("🔔 [Before] Something is happening before the function is called.")
        original_function() # Executing the actual function
        print("🔔 [After] Something is happening after the function is called.")
    return wrapper_function

# Using the decorator with the '@' symbol (The standard Pythonic way)
@my_decorator
def display_message():
    print("🚀 The core function 'display_message' is executing.")

# Calling the decorated function
display_message()


print("\n--- 3. DECORATORS THAT ACCEPT ARGUMENTS ---")
# If our original function takes arguments (like parameters), 
# we use *args and **kwargs in the wrapper function so it can accept any input.

def Smart_divider(original_divide):
    def wrapper(a, b):
        print(f"🤖 Checking arguments: a={a}, b={b}")
        if b == 0:
            return "❌ Error: Cannot divide by zero! Returning safe value (0)."
        return original_divide(a, b)
    return wrapper

@Smart_divider
def divide_numbers(a, b):
    return a / b

print(divide_numbers(10, 2))  # Output: 5.0
print(divide_numbers(10, 0))  # Output: Safe error message handled by decorator


print("\n--- 4. REAL-WORLD DATA SCIENCE USE-CASE (Timing ML Model Training) ---")
# In Machine Learning, we often need to check how much time an epoch or 
# a data processing pipeline takes. We can use a decorator for this!

import time

def calculate_execution_time(original_fn):
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Start the timer
        print(f"⏳ [Timer Started] Executing data science pipeline...")
        
        result = original_fn(*args, **kwargs)  # Run the actual function
        
        end_time = time.time()    # Stop the timer
        execution_time = end_time - start_time
        print(f"⏱️ [Timer Stopped] Total Time Taken: {execution_time:.4f} seconds")
        return result
    return wrapper

@calculate_execution_time
def train_dummy_ml_model(epochs):
    print(f"⚙️ Training a model with {epochs} epochs...")
    time.sleep(1.5)  # Simulating a heavy ML training process delay
    return "✅ Model Training Successfully Completed!"

# Running our timed ML pipeline
status = train_dummy_ml_model(epochs=50)
print(status)


# =====================================================================
# 📝 STUDENT REFLECTION & QUICK REVISION
# - Decorators help keep our code DRY (Don't Repeat Yourself).
# - Instead of writing timing logic in 10 different ML training functions,
#   we just write it once in a decorator and use '@calculate_execution_time'.
# =====================================================================
