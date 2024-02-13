import unittest


# You are given an n x n grid where you have placed some 1 x 1 x 1 cubes.
# Each value v = grid[i][j] represents a tower of v cubes placed on top of cell (i, j).
#       - After placing these cubes, you have decided to glue any directly adjacent cubes to each other,
#       forming several irregular 3D shapes.
#       Return the total surface area of the resulting shapes.
# Time Complexity: O(n^2)
# Space Complexity: O(1)
# Example Conceptual Sketch:
#         3 .. len(a2[0])
#         3 .. len(a2[0])
#         2 .. a2[0][0]
#         2 .. a2[0][0]
#         2 .. a2[0][1]
#         1 .. abs(arr[0][1] - arr[1][1])
#         2 .. a2[0][2]
#         2 .. a2[0][2]
#
#         3 .. len(a2[1])
#         3 .. len(a2[1])
#         2 .. a2[1][0]
#         1 .. abs(arr[1][0] - arr[1][1])
#         2 .. a2[1][2]
#         1 .. abs(arr[1][2] - arr[1][1])
#
#         3 .. len(a2[2])
#         3 .. len(a2[2])
#         2 .. a2[2][0]
#         2 .. a2[2][0]
#         2 .. a2[2][1]
#         1 .. abs(arr[2][1] - arr[1][1])
#         2 .. a2[2][2]
#         2 .. a2[2][2]
def surface_area_of_3d_shapes(arr):
    area = 0

    if not arr:
        return area

    n_rows = len(arr)

    if n_rows == 0:
        return area

    for i in range(n_rows):
        n_cols = len(arr[i])
        for j in range(n_cols):

            # Add surface area for base and top faces of element
            if arr[i][j] != 0:
                area += 2

            # Add surface area of simple outer wall of element
            if i == 0 or j == 0 or i == n_rows - 1 or j == n_cols - 1:
                area += arr[i][j]

            # Add surface area to secondary outer wall IF corner element
            if i == 0 and j == 0:
                area += arr[i][j]
            elif i == 0 and j == n_cols - 1:
                area += arr[i][j]
            elif i == n_rows - 1 and j == 0:
                area += arr[i][j]
            elif i == n_rows - 1 and j == n_cols - 1:
                area += arr[i][j]

            # Add surface area of negative topology around element
            if j - 1 >= 0 and arr[i][j] > arr[i][j - 1]:
                area += arr[i][j] - arr[i][j - 1]

            if j + 1 < n_cols and arr[i][j] > arr[i][j + 1]:
                area += arr[i][j] - arr[i][j + 1]

            if i - 1 >= 0 and arr[i][j] > arr[i - 1][j]:
                area += arr[i][j] - arr[i - 1][j]

            if i + 1 < n_rows and arr[i][j] > arr[i + 1][j]:
                area += arr[i][j] - arr[i + 1][j]

    return area


class TestSurfaceAreaOf3dShapes(unittest.TestCase):
    def test_valid_case_one(self):
        self.assertEqual(
            surface_area_of_3d_shapes([
                [1, 2],
                [3, 4]
            ]),
            34,
            'Should test valid case'
        )

    def test_valid_case_two(self):
        self.assertEqual(
            surface_area_of_3d_shapes([
                [1, 1, 1],
                [1, 0, 1],
                [1, 1, 1]
            ]),
            32,
            'Should test valid case'
        )

    def test_valid_case_three(self):
        self.assertEqual(
            surface_area_of_3d_shapes([
                [2, 2, 2],
                [2, 1, 2],
                [2, 2, 2]
            ]),
            46,
            'Should test valid case'
        )

    def test_empty_case(self):
        self.assertEqual(
            surface_area_of_3d_shapes([]),
            0,
            'Should handle empty case'
        )

    def test_empty_columns_case(self):
        self.assertEqual(
            surface_area_of_3d_shapes([[], [], []]),
            0,
            'Should handle empty case'
        )

    def test_null_case(self):
        self.assertEqual(
            surface_area_of_3d_shapes(None),
            0,
            'Should handle null case'
        )