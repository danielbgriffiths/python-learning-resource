import unittest


class Node:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right


# Given two binary trees original and cloned and given a reference to a node
# target in the original tree.
#       The cloned tree is a copy of the original tree.
#       Return a reference to the same node in the cloned tree.
# Note that you are not allowed to change any of the two trees or the target
# node and the answer must be a reference to a node in the cloned tree.
# Time complexity: O(n)
# Space complexity: O(n)
# Mental Model:
#       Traverse the tree in a depth first search manner recursively,
def get_cloned_reference(original, clone, target):
    if not original:
        return None

    if clone.value is target.value:
        return clone

    return get_cloned_reference(original.left, clone.left, target) or get_cloned_reference(original.right, clone.right, target)


class TestCorrespondingNode(unittest.TestCase):
    def test_valid_case_one(self):
        three_node = Node(3, None, None)
        seven_node = Node(7, None, None)
        five_node = Node(5, three_node, seven_node)
        eighteen_node = Node(18, None, None)
        fifteen_node = Node(15, None, eighteen_node)
        ten_node = Node(10, five_node, fifteen_node)

        self.assertEqual(
            get_cloned_reference(ten_node, ten_node, five_node),
            five_node,
            'Handles valid case one'
        )

    def test_valid_case_two(self):
        three_node = Node(3, None, None)
        seven_node = Node(7, None, None)
        five_node = Node(5, three_node, seven_node)
        eighteen_node = Node(18, None, None)
        fifteen_node = Node(15, None, eighteen_node)
        ten_node = Node(10, five_node, fifteen_node)

        self.assertEqual(
            get_cloned_reference(ten_node, ten_node, ten_node),
            ten_node,
            'Handles valid case two'
        )

    def test_valid_case_three(self):
        three_node = Node(3, None, None)
        seven_node = Node(7, None, None)
        five_node = Node(5, three_node, seven_node)
        eighteen_node = Node(18, None, None)
        fifteen_node = Node(15, None, eighteen_node)
        ten_node = Node(10, five_node, fifteen_node)

        self.assertEqual(
            get_cloned_reference(ten_node, ten_node, seven_node),
            seven_node,
            'Handles valid case three'
        )

    def test_empty_case(self):
        one_node = Node(1, None, None)
        self.assertEqual(
            get_cloned_reference(one_node, one_node, one_node),
            one_node,
            'Handles empty case'
        )

    def test_null_case(self):
        self.assertEqual(
            get_cloned_reference(None, None, None),
            None,
            'Handles null case'
        )
