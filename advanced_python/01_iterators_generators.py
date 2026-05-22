# =====================================================================
# Topic: Iterators and Generators (Advanced Python for Data Science)
# =====================================================================

print("--- 1. ITERATOR BASICS ---")
my_list = [10, 20, 30]
iterator_obj = iter(my_list)

print(next(iterator_obj)) # Output: 10
print(next(iterator_obj)) # Output: 20
print(next(iterator_obj)) # Output: 30

print("\n--- 2. GENERATOR (Memory Efficient Data Streaming) ---")
def my_generator(n):
    value = 1
    while value <= n:
        yield value
        value += 1

gen = my_generator(3)
print(next(gen)) # Output: 1
print(next(gen)) # Output: 2
print(next(gen)) # Output: 3

print("\n--- 3. DATA SCIENCE USE-CASE (Large Dataset Streaming) ---")
def log_file_reader():
    dummy_log_lines = [
        "LOG 16:27:45 - User logged in",
        "LOG 16:33:11 - Model training started",
        "LOG 16:35:59 - Epoch 1 Complete"
    ]
    for line in dummy_log_lines:
        yield line

log_stream = log_file_reader()
for log in log_stream:
    if "Model" in log:
        print(f"🎯 Found ML Log: {log}")
