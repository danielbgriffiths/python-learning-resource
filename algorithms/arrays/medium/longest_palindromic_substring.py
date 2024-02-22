import unittest


# Longest Palindromic Substring
# Given a string s, find the longest palindromic substring in s.
# You may assume that the maximum length of s is 1000.
#
# Time Complexity: O(n log n)
# Space Complexity: O(2N)
# Mental Model:
#
# ['d', 'a', 'd', 'd', 'y']
# ['y', 'd', 'd', 'a', 'd']
#
#      ['d', 'a', 'd', 'd', 'y']
# ['y', 'd', 'd', 'a', 'd']
#
#            ['d', 'a', 'd', 'd', 'y']
# ['y', 'd', 'd', 'a', 'd']
def longest_palindromic_substring(string):
    longest_palindrome = ''

    if  not string or len(string) == 0:
        return longest_palindrome

    reversed_string = ''
    for char in reversed(string):
        reversed_string += char

    for str_pointer in  range(len(string)):

        current_step_palindrome = ''
        is_palindrome = True
        i = 0

        while is_palindrome and i + str_pointer < len(string):
            if string[i] == reversed_string[i + str_pointer]:
                current_step_palindrome += string[i]
            else:
                is_palindrome = False

            if len(current_step_palindrome) > 1 and len(current_step_palindrome) > len(longest_palindrome):
                longest_palindrome = current_step_palindrome

            if i + str_pointer == len(string) - 1 and is_palindrome:
                return longest_palindrome

            i += 1

    return longest_palindrome


class TestLongestPalindromicSubstring(unittest.TestCase):
    def test_invalid_case_one(self):
        self.assertEqual(
            longest_palindromic_substring('test'),
            '',
            'Should handle invalid case'
        )

    def test_invalid_case_two(self):
        self.assertEqual(
            longest_palindromic_substring('people'),
            '',
            'Should handle invalid case'
        )

    def test_valid_case_one(self):
        self.assertEqual(
            longest_palindromic_substring('dad'),
            'dad',
            'Should handle valid case'
        )

    def test_valid_case_two(self):
        self.assertEqual(
            longest_palindromic_substring('daddy'),
            'dad',
            'Should handle valid case'
        )

    def test_valid_case_three(self):
        self.assertEqual(
            longest_palindromic_substring('racecar'),
            'racecar',
            'Should handle valid case'
        )

    def test_empty_case(self):
        self.assertEqual(
            longest_palindromic_substring(''),
            '',
            'Should handle empty case'
        )

    def test_null_case(self):
        self.assertEqual(
            longest_palindromic_substring(None),
            '',
            'Should handle null case'
        )