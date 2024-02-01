import unittest


# Given an integer array nums of length n,
# you want to create an array of length 2n where
# arr2[i] == arr[i] and arr2[i + n] == arr[i] for 0 <= i < n (0-indexed).
# Time Complexity: O(N)
# Space Complexity O(2N)
def concatenation_of_arrays(arr):
    if not arr or len(arr) < 1:
        return []

    result = [None] * (len(arr) * 2)

    for (idx, el) in enumerate(arr):
        result[idx] = el
        result[idx + len(arr)] = el

    return result


class TestConcatenationOfArrays(unittest.TestCase):
    def test_valid_case(self):
        self.assertEqual(
            concatenation_of_arrays([1, 2, 1]),
            [1, 2, 1, 1, 2, 1],
            'Should return all possible palindromic substrings'
        )

    def test_empty_case(self):
        self.assertEqual(
            concatenation_of_arrays([1, 3, 2, 1]),
            [1, 3, 2, 1, 1, 3, 2, 1],
            'Should return all empty array'
        )

    def test_null_case(self):
        self.assertEqual(
            concatenation_of_arrays(None),
            [],
            'Should return all empty array'
        )