import unittest


# Sort array with Bubble Sort
# Data Structure: list
# Method: Sort in place
# Time Complexity: O(n^2)
# Space Complexity: O(1)
def bubble_sort(arr, direction='ascending'):
    if not arr:
        return []

    for i in range(len(arr)):
        is_swapped = False
        for j in range(i, len(arr)):
            if arr[i] < arr[j] if direction == 'ascending' else arr[j] < arr[i]:
                continue

            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
            is_swapped = True

        if not is_swapped:
            break

    return arr

class TestBubbleSort(unittest.TestCase):
    def test_ascending(self):
        self.assertEqual(bubble_sort([1, 4, 3, 6, 8, 24, 12], 'ascending'), [1, 3, 4, 6, 8, 12, 24], "Should sort array ascending")

    def test_descending(self):
        self.assertEqual(bubble_sort([1, 4, 3, 6, 8, 24, 12], 'descending'), [24, 12, 8, 6, 4, 3, 1], "Should sort array descending")

    def test_default_direction(self):
        self.assertEqual(bubble_sort([1, 4, 3, 6, 8, 24, 12]), [1, 3, 4, 6, 8, 12, 24], "Should sort array by default ascending")

    def test_null_case(self):
        self.assertEqual(bubble_sort(None), [], "Should handle null case")