import unittest


# Write a function to find the longest common prefix string amongst an array of strings.
#
# Time Complexity: O(N log N)
# Space Complexity: O(1)
# Mental Model:
#       Step through each string for the length of the minimum string
#       Test for a mismatch at each step
#       If a mismatch exists, return the current longest prefix
def longest_common_prefix(arr):
    longest_prefix = ''

    if not arr or len(arr) == 0:
        return longest_prefix

    if len(arr) == 1:
        return arr[0]

    min_length_of_strings = None
    for arr_idx in range(len(arr)):
        if not min_length_of_strings or len(arr[arr_idx]) < min_length_of_strings:
            min_length_of_strings = len(arr[arr_idx])

    for step in range(min_length_of_strings):
        common_char = arr[0][step]

        for (arr_idx, string) in enumerate(arr):
            if string[step] != common_char:
                return longest_prefix

        longest_prefix += common_char

    return longest_prefix


class TestLongestCommonPrefix(unittest.TestCase):
    def test_valid_case_one(self):
        self.assertEqual(
            longest_common_prefix(['test', 'team']),
            'te',
            'Should handle valid case'
        )

    def test_valid_case_two(self):
        self.assertEqual(
            longest_common_prefix(['cat', 'category', 'caterpillar', 'catapult']),
            'cat',
            'Should handle valid case'
        )

    def test_invalid_case(self):
        self.assertEqual(
            longest_common_prefix(['test', 'team', 'blue']),
            '',
            'Should handle invalid case'
        )

    def test_single_case(self):
        self.assertEqual(
            longest_common_prefix(['test']),
            'test',
            'Should handle single case'
        )

    def test_empty_case(self):
        self.assertEqual(
            longest_common_prefix([]),
            '',
            'Should handle empty case'
        )

    def test_null_case(self):
        self.assertEqual(
            longest_common_prefix(None),
            '',
            'Should handle null case'
        )