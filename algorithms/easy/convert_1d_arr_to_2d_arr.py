import unittest


# The elements from indices 0 to n - 1 (inclusive) of original should form the first row of the constructed 2D array,
# the elements from indices n to 2 * n - 1 (inclusive) should form the second row of the constructed 2D array,
# and so on.
#       Return an m x n 2D array constructed according to the above procedure, or an empty 2D array if it is impossible.
# Time Complexity: O(N^2)
# Space Complexity: O(N)
# Example Conceptual Process:
#
#       m[0][0] = arr[0], 0 = (0 + 0 + 0)
#       m[0][1] = arr[1], 1 = (0 + 0 + 1)
#       m[1][0] = arr[2], 2 = (1 + 1 + 0)
#       m[1][1] = arr[3], 3 = (1 + 1 + 1)
#
#       f(r, c, n_cols) = r * n_cols + c
#       f(arr) = arr[f(r, c, n_cols)]       - f(arr) is the value in the array at some function of r, c and n_cols
#       m[r][c] = f(arr)                    - m[r][c] is some function of array
def convert_1d_arr_to_2d_arr(arr, n_rows, n_cols):
    matrix = []

    if not arr or not n_rows or not n_cols or n_cols * n_rows != len(arr):
        return matrix

    for r in range(n_rows):
        matrix.append([])
        for c in range(n_cols):
            matrix[r].append(arr[r * n_cols + c])

    return matrix


class TestConvert1dArrayTo2dArray(unittest.TestCase):
    def test_valid_case_one(self):
        self.assertEqual(
            convert_1d_arr_to_2d_arr([1, 2, 3, 4], 2, 2),
            [[1, 2], [3, 4]],
            "Should handle valid case"
        )

    def test_valid_case_two(self):
        self.assertEqual(
            convert_1d_arr_to_2d_arr([1, 2, 3], 1, 3),
            [[1, 2, 3]],
            "Should handle valid case"
        )

    def test_valid_case_three(self):
        self.assertEqual(
            convert_1d_arr_to_2d_arr([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], 3, 4),
            [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]],
            "Should handle valid case"
        )

    def test_valid_case_four(self):
        self.assertEqual(
            convert_1d_arr_to_2d_arr([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5, 2),
            [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]],
            "Should handle valid case"
        )

    def test_valid_case_five(self):
        self.assertEqual(
            convert_1d_arr_to_2d_arr([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], 5, 3),
            [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]],
            "Should handle valid case"
        )

    def test_invalid_case(self):
        self.assertEqual(
            convert_1d_arr_to_2d_arr([1, 2], 1, 1),
            [],
            "Should handle invalid case"
        )

    def test_empty_case(self):
        self.assertEqual(
            convert_1d_arr_to_2d_arr([], 1, 1),
            [],
            "Should handle empty case"
        )

    def test_null_case(self):
        self.assertEqual(
            convert_1d_arr_to_2d_arr(None, 1, 1),
            [],
            "Should handle empty case"
        )