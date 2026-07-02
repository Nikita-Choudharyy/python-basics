# =====================================================================
# Topic: Intermediate Python Practice Problems (Algorithmic Logic)
# Purpose: Implementing data structures, sorting logic, and frequency maps.
# =====================================================================

print("--- PROBLEM 1: TWO SUM (FIND INDICES OF TARGET SUM) ---")
# Logic: Given an array of integers, return indices of the two numbers 
# such that they add up to a specific target. We use a hash map (dict) for O(n) efficiency.

def two_sum(nums, target):
    seen_elements = {}  # Stores value as key and its index as value
    
    for current_index, current_num in enumerate(nums):
        complement = target - current_num
        
        # If the complement exists in our map, we found the pair!
        if complement in seen_elements:
            return [seen_elements[complement], current_index]
        
        # Otherwise, save the current number and its index to the map
        seen_elements[current_num] = current_index
    return []

# Testing our function
sample_nums = [2, 7, 11, 15]
target_sum = 9
print(f"Indices for target {target_sum}: {two_sum(sample_nums, target_sum)}")  # Output: [0, 1]


print("\n--- PROBLEM 2: WORD FREQUENCY COUNTER ---")
# Logic: Clean a string by removing basic punctuation, lowercasing it, 
# and counting how many times each word appears. Essential for Text Preprocessing in NLP!

def count_word_frequency(text):
    # Basic cleaning: lowering case and splitting by spaces
    words = text.lower().split()
    frequency_map = {}
    
    for word in words:
        # Strip common punctuation from ends of words dynamically
        clean_word = word.strip(".,!?\"'()[]")
        if clean_word:
            frequency_map[clean_word] = frequency_map.get(clean_word, 0) + 1
            
    return frequency_map

sample_text = "Data science is amazing. Python is also amazing for data analysis!"
print("Word Frequencies:")
print(count_word_frequency(sample_text))


print("\n--- PROBLEM 3: MERGE OVERLAPPING INTERVALS ---")
# Logic: Given a collection of intervals, merge all overlapping intervals.
# Highly applicable when handling time-series batches or event scheduling logs.

def merge_intervals(intervals):
    if not intervals:
        return []
    
    # Crucial Step: Sort the intervals based on their starting values
    intervals.sort(key=lambda x: x[0])
    
    merged = [intervals[0]]
    for current in intervals[1:]:
        prev_interval = merged[-1]
        
        # If the current interval overlaps with the previous one, merge them
        if current[0] <= prev_interval[1]:
            prev_interval[1] = max(prev_interval[1], current[1])
        else:
            merged.append(current)
            
    return merged

sample_intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
print(f"Original intervals: {sample_intervals}")
print(f"Merged intervals:   {merge_intervals(sample_intervals)}")  # Output: [[1, 6], [8, 10], [15, 18]]


# =====================================================================
# 📝 STUDENT REFLECTION & QUICK REVISION
# - Dictionary lookups (in) run in O(1) time complexity, making 'Two Sum' ultra-fast.
# - Always sort structures before attempting interval merging algorithms.
# - Using dict.get(key, 0) prevents KeyErrors when counting elements dynamically.
# =====================================================================
