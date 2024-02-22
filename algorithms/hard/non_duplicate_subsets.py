import unittest


class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child):
        self.children.append(child)


# Non-duplicate subsets
#
# Time Complexity: ...
# Space Complexity: ...
# Mental Model:
#
#       ...
#       ...
#       ...
def non_duplicate_subsets(set):
    subsets = []

    """
    Cover null and empty cases.
    """
    if not set or len(set) == 0:
        return subsets

    """
    If 'set' is of size 1 there is only one permutation, or subset.
    """
    if len(set) == 1:
        return [set]

    """
    We are finding all non-duplicate permutations of subsets
    
    1. Construct Tree
        a. The root node has chlidren for all other set values
        b. each subsequent child no matter depth has child for any set values that are not direct parents
    2. Traverse tree in a depth-first manner
    3. Collect every combination of nodes
    """
    for i in range(len(set)):
        node = Node(i)

    return subsets


class TestNonDuplicateSubsets(unittest.TestCase):
    def test_valid_case_one(self):
        self.assertEqual(
            non_duplicate_subsets([1, 2, 3]),
            [
                [3],
                [1],
                [2],
                [1, 2, 3],
                [1, 3],
                [2, 3],
                [1, 2],
                []
            ],
            'Should handle valid case one'
        )

    def test_valid_case_two(self):
        self.assertEqual(
            non_duplicate_subsets([1, 1, 1]),
            [[1, 1, 1], [1, 1], [1]],
            'Should handle valid case two'
        )

    def test_single_case(self):
        self.assertEqual(
            non_duplicate_subsets([1]),
            [[1]],
            'Should handle single case'
        )

    def test_empty_case(self):
        self.assertEqual(
            non_duplicate_subsets([]),
            [],
            'Should handle empty case'
        )

    def test_null_case(self):
        self.assertEqual(
            non_duplicate_subsets(None),
            [],
            'Should handle null case'
        )