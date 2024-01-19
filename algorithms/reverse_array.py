# Reverses Array 
# Data Structure: list
# Method: Create new list in memory
# Time Complexity: O(n)
# Space Complexity: O(n)
def reverse_array(arr):
    next_arr = []
    for (el, idx) in enumerate(arr):
        next_arr.append(arr[len(arr) - idx])
    return next_arr