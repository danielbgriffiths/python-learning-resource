import unittest


# Given a string, find the length of the longest substring without repeating characters.
#
# Time Complexity: O(N^2)
# Space Complexity: O(N)
# Mental Model:
#       for i in string
#            for j in (i, string) until string[j] is repeating
#               check if iterations longest_substring is longest_substring
def longest_substr_without_repeating_chars(string):
    longest_substring = ''

    if not string or len(string) == 0:
        return longest_substring

    for i in range(len(string)):
        longest_substring_from_index = ''

        for j in range(i, len(string)):

            if string[j] in longest_substring_from_index:
                break
            else:
                longest_substring_from_index += string[j]

        if len(longest_substring_from_index) > len(longest_substring):
            longest_substring = longest_substring_from_index

    return longest_substring


class TestLongestSubstrWithoutRepeatingChars(unittest.TestCase):
    def test_valid_case_one(self):
        self.assertEqual(
            longest_substr_without_repeating_chars('thisisastring'),
            'astring',
            'Should handle valid case one'
        )

    def test_valid_case_two(self):
        self.assertEqual(
            longest_substr_without_repeating_chars('somesubstringhasmultipleletters'),
            'tringhasmul',
            'Should handle valid case one'
        )

    def test_empty_case(self):
        self.assertEqual(
            longest_substr_without_repeating_chars(''),
            '',
            'Should handle empty case'
        )

    def handle_weird_case(self):
        self.assertEqual(
            longest_substr_without_repeating_chars('aa'),
            'a',
            'Should handle weird case'
        )

    def handle_null_case(self):
        self.assertEqual(
            longest_substr_without_repeating_chars(None),
            '',
            'Should handle null case'
        )