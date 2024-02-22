import unittest


def get_constant(step):
    half_step = step / 2
    if step % 2 == 0:
        return half_step * half_step
    else:
        return (half_step - .5) * (half_step + .5)


# Complete the spiral matrix of the square
#
# Time Complexity where N == len(matrix): O(log N)
# Space Complexity where N == len(matrix): O(N)
def spiral_matrix(square):
    """""
    Step through O(2n) and find all corner values
    
    Expressions:
    CONSTANT(n) = n % 2 == 0 ? (n * n) : (n/2-.5) * (n/2-.5)
    TURNS(0...2(sq) as n, sq) = n == 0 ? 1 : ((n)sq - CONSTANT(n))
    """""
    corner_values = []
    matrix = [[None] * square] * square
    for step in range(square * 2):
        if step == 0:
            corner_values.append(1)
            continue
        corner_value = step * square - get_constant(step)
        corner_values.append(int(corner_value))

    """""
    Step through corner_values and fill in spiral matrix
    
    Expressions:
    starting_cells_per_face = sq - 2
    number_of_faces = sq - 1
    
    ...
    """""
    for (corner_value_idx, corner_value) in enumerate(corner_values):
        print(corner_value)


    return matrix


class TestSpiralMatrix(unittest.TestCase):
    def test_valid_case(self):
        self.assertEqual(
            spiral_matrix(6),
            [
                [1, 2, 3],
                [8, 9, 4],
                [7, 6, 5],
            ],
            'Should handle valid case one'
        )