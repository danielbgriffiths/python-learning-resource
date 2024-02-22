import unittest


class Node:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right


# Given the root node of a binary search tree and two integers low and high,
# return the sum of values of all nodes with a value in the inclusive range [low, high].
# Time complexity: O(n)
# Space complexity: O(n)
# Mental Model:
#       Traverse the tree in a depth first search manner recursively
#       Pass an accumulator to keep track of the sum of the nodes that are within the range
def range_sum_bst(node, low, high, acc=0):
    if not node:
        return acc

    if low <= node.value <= high:
        acc += node.value

    acc = range_sum_bst(node.left, low, high, acc)
    acc = range_sum_bst(node.right, low, high, acc)

    return acc


class TestRangeSumBST(unittest.TestCase):
    def test_valid_case_one(self):
        three_node = Node(3, None, None)
        seven_node = Node(7, None, None)
        five_node = Node(5, three_node, seven_node)
        eighteen_node = Node(18, None, None)
        fifteen_node = Node(15, None, eighteen_node)
        ten_node = Node(10, five_node, fifteen_node)

        self.assertEqual(
            range_sum_bst(ten_node, 7, 15),
            32,
            'Handles valid case one'
        )

    def test_valid_case_four(self):
        six_node = Node(6, None, None)
        one_node = Node(1, None, None)
        three_node = Node(3, one_node, None)
        seven_node = Node(7, None, six_node)
        five_node = Node(5, three_node, seven_node)
        thirteen_node = Node(13, None, None)
        eighteen_node = Node(18, None, None)
        fifteen_node = Node(15, thirteen_node, eighteen_node)
        ten_node = Node(10, five_node, fifteen_node)

        self.assertEqual(
            range_sum_bst(ten_node, 6, 10),
            23,
            'Handles valid case four'
        )

    def test_empty_case(self):
        self.assertEqual(
            range_sum_bst(Node(1, None, None), 7, 15),
            0,
            'Handles empty case'
        )

    def test_null_case(self):
        self.assertEqual(
            range_sum_bst(None, 7, 15),
            0,
            'Handles null case'
        )