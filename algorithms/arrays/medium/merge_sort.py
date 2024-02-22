import unittest


# Use Merge Sort algorithm to sort array
# - First check if the array or list contains 1 element or less. If so, return the array.
#   Merge sort is recursive, so the next thing we do is split the array down the middle, inclusive on the first half.
#   After splitting the array we pass the two halves to their recursive merge sort function. Finally,
#   after we have broken down the array to pieces with a length of 1 we combine the sides back up the tree with a sort.
#   The sort maintain
# - Time Complexity: O(N * log N)
# - Space Complexity O(N)
def merge_sort(arr):
    if not arr:
        return []
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    left_pointer = 0
    right_pointer = 0
    arr_pointer = 0

    while left_pointer < len(left) and right_pointer < len(right):
        if left[left_pointer] < right[right_pointer]:
            arr[arr_pointer] = left[left_pointer]
            left_pointer += 1
        else:
            arr[arr_pointer] = right[right_pointer]
            right_pointer += 1
        arr_pointer += 1

    while left_pointer < len(left):
        arr[arr_pointer] = left[left_pointer]
        left_pointer += 1
        arr_pointer += 1

    while right_pointer < len(right):
        arr[arr_pointer] = right[right_pointer]
        right_pointer += 1
        arr_pointer += 1

    return arr


class TestMergeSort(unittest.TestCase):
    def test_valid_case(self):
        self.assertEqual(merge_sort([1, 4, 2, 3]), [1, 2, 3, 4], "Should sort array")

    def test_null_case(self):
        self.assertEqual(merge_sort(None), [], "Should handle null case")