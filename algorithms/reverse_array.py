import unittest


# Reverses Array
# Data Structure: list
# Method: Create new list in memory
# Time Complexity: O(n)
# Space Complexity: O(n)
def reverse_array(arr):
    if not arr:
        return []

    reversed_array = []

    for (idx, el) in enumerate(arr):
        reversed_array.append(arr[len(arr) - (idx + 1)])

    return reversed_array


# Reverses Array in place
# Data Structure: list
# Method: Mutate array in-place
# Time Complexity: O(n)
# Space Complexity: O(1)
def reverse_array_in_place(arr):
    if not arr:
        return []

    for (idx, el) in enumerate(arr):
        arr = arr[idx + 1:len(arr) - idx] + [el] + arr[len(arr) - idx:]

    return arr


class TestReverseArray(unittest.TestCase):
    def test_valid_case(self):
        self.assertEqual(reverse_array([1, 2, 3]), [3, 2, 1], "Should reverse array")

    def test_null_case(self):
        self.assertEqual(reverse_array(None), [], "Should handle null case")


class TestReverseArrayInPlace(unittest.TestCase):
    def test_valid_case(self):
        self.assertEqual(reverse_array_in_place([1, 2, 3]), [3, 2, 1], "Should reverse array")

    def test_null_case(self):
        self.assertEqual(reverse_array_in_place(None), [], "Should handle null case")