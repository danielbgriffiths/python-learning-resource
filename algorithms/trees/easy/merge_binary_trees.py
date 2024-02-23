import unittest


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# You are given two binary trees subject_node and target_node.
#
# Imagine that when you put one of them to cover the other,
# some nodes of the two trees are overlapped while the others are not.
# You need to merge the two trees into a new binary tree. The merge rule is that if two nodes overlap,
# then sum node values up as the new value of the merged node.
# Otherwise, the NOT null node will be used as the node of the new tree.
#
#       Return the merged tree.
#
#       Note: The merging process must start from the root nodes of both trees.
#
# Time complexity: O(n)
# Space complexity: O(1)
# Mental Model:
#       We depth-first recurse through the subject node and target node.
#       At each level we merge the values, or simulate an empty node if one of the nodes is None.
def merge_binary_trees(subject_node, target_node):
    if not subject_node and target_node:
        subject_node = Node(target_node.value)
    elif not target_node and subject_node:
        target_node = Node(0)
    elif not subject_node and not target_node:
        return subject_node
    else:
        subject_node.value += target_node.value

    subject_node.left = merge_binary_trees(subject_node.left, target_node.left)
    subject_node.right = merge_binary_trees(subject_node.right, target_node.right)

    return subject_node


class TestMergeBinaryTrees(unittest.TestCase):
    def test_valid_case_one(self):
        subject_node = Node(1,
            Node(2,
                Node(3),
                Node(4)
            ),
            Node(5)
        )
        target_node = Node(1,
            Node(2,
                Node(3),
                Node(4)
            ),
            Node(5)
        )
        result = merge_binary_trees(subject_node, target_node)
        self.assertEqual(result.value, 2)
        self.assertEqual(result.left.value, 4)
        self.assertEqual(result.left.left.value, 6)
        self.assertEqual(result.left.right.value, 8)
        self.assertEqual(result.right.value, 10)

    def test_valid_case_two(self):
        subject_node = Node(1,
            Node(2,
                Node(3),
                Node(4)
            ),
        )
        target_node = Node(1,
            Node(2,
                Node(3),
            ),
            Node(5)
        )
        result = merge_binary_trees(subject_node, target_node)
        self.assertEqual(result.value, 2)
        self.assertEqual(result.left.value, 4)
        self.assertEqual(result.left.left.value, 6)
        self.assertEqual(result.left.right.value, 4)
        self.assertEqual(result.right.value, 5)

    def test_invalid_case(self ):
        subject_node = Node(1,
            Node(2,
                Node(3),
                Node(4)
            ),
        )
        target_node = Node(1,
            Node(2,
                Node(3),
            ),
        )
        result = merge_binary_trees(subject_node, target_node)
        self.assertEqual(result.value, 2)
        self.assertEqual(result.left.value, 4)
        self.assertEqual(result.left.left.value, 6)
        self.assertEqual(result.left.right.value, 4)
        self.assertEqual(result.right, None)

    def test_empty_case(self):
        subject_node = Node(1,
            Node(2,
                Node(3),
                Node(4)
            ),
        )
        target_node = None
        result = merge_binary_trees(subject_node, target_node)
        self.assertEqual(result.value, 1)
        self.assertEqual(result.left.value, 2)
        self.assertEqual(result.left.left.value, 3)
        self.assertEqual(result.left.right.value, 4)
        self.assertEqual(result.right, None)

    def test_null_case(self):
        subject_node = None
        target_node = None
        result = merge_binary_trees(subject_node, target_node)
        self.assertEqual(result, None)