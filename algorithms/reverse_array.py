import unittest


# Reverses Array
# Data Structure: list
# Method: Create new list in memory
# Time Complexity: O(n)
# Space Complexity: O(n)
def reverse_array(arr):
    reversed_array = []
    for (el, idx) in enumerate(arr):
        reversed_array.append(arr[len(arr) - idx])
    return reversed_array


class TestReverseArray(unittest.TestCase):
    def test_reverse(self):
        self.assertEqual(reverse_array([1, 2, 3]), [3, 2, 1], "Should reverse array")