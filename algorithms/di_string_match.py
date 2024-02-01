import unittest


# A permutation perm of n + 1 integers of all the integers in the range
# [0, n] can be represented as a string s of length n where:
#       s[i] == 'I' if perm[i] < perm[i + 1], and
#       s[i] == 'D' if perm[i] > perm[i + 1].
# Given a string s, reconstruct the permutation perm and return it.
# If there are multiple valid permutations perm, return any of them.
# Time Complexity: O(n)
# Space Complexity: O(n)
def di_string_match(arr):
    perm = []

    if not arr or len(arr) == 0:
        return perm

    s_counter = 0
    d_counter = len(arr)
    for i in range(d_counter):
        if arr[i] == 'D':
            perm.append(d_counter)
            d_counter -= 1
        else:
            perm.append(s_counter)
            s_counter += 1

    return perm


class TestDiStringMatch(unittest.TestCase):
    def test_valid_case(self):
        self.assertEqual(
            di_string_match("IDID"),
            [0, 4, 1, 3],
            'Should return valid permutation'
        )

    def test_complex_case(self):
        self.assertEqual(
            di_string_match("III"),
            [0, 1, 2],
            'Should return valid permutation'
        )

    def test_single_index_case(self):
        self.assertEqual(
            di_string_match("I"),
            [0],
            'Should handle single index case'
        )

    def test_empty_case(self):
        self.assertEqual(
            di_string_match([]),
            [],
            'Should handle empty case'
        )

    def test_none_case(self):
        self.assertEqual(
            di_string_match(None),
            [],
            'Should handle null case'
        )