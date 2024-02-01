import unittest


# Given an array of integers nums, return the number of good pairs.
# A pair (i, j) is called good if nums[i] == nums[j] and i < j.
# Time Complexity: O(n^(n-1)/2)
# Space Complexity: O(1)
def number_of_good_pairs(arr):
    count = 0

    if not arr or len(arr) <= 1:
        return count

    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j]:
                count += 1

    return count


class TestNumberOfGoodPairs(unittest.TestCase):
    def test_valid_case(self):
        self.assertEqual(
            number_of_good_pairs([1, 2, 3, 1, 1, 3]),
            4,
            "Should return number of good pairs"
        )

    def test_complex_case(self):
        self.assertEqual(
            number_of_good_pairs([1, 1, 1, 1]),
            6,
            "Should return number of good pairs"
        )

    def test_single_index_case(self):
        self.assertEqual(
            number_of_good_pairs([1]),
            0,
            "Should return no pairs"
        )

    def test_empty_case(self):
        self.assertEqual(
            number_of_good_pairs([]),
            0,
            "Should handle empty case"
        )

    def test_null_case(self):
        self.assertEqual(
            number_of_good_pairs(None),
            0,
            "Should handle null case"
        )