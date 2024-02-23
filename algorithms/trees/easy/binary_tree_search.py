import unittest


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# You are given the root of a binary search tree (BST) and an integer val.

# Find the node in the BST that the node's value equals val and return the subtree
# rooted with that node. If such a node does not exist, return null.
# Time complexity: O(1)
# Space complexity: O(n)
# Mental Model:
#       Traverse the tree in a depth first search manner recursively
def binary_tree_search_dfs(node, value):
    if not node:
        return None

    if node.value == value:
        return node

    return binary_tree_search_dfs(node.left, value) or binary_tree_search_dfs(node.right, value)


# Time complexity: O(n)
# Space complexity: O(n)
# Mental Model:
#       Traverse the tree in a breadth first search manner using a queue
def binary_tree_search_bfs(node, value):
    if not node:
        return None

    queue = [node]

    while queue:
        current = queue.pop()

        if current.value == value:
            return current

        if current.left:
            queue.append(current.left)

        if current.right:
            queue.append(current.right)


class TestBinaryTreeSearchDFS(unittest.TestCase):
    def test_valid_case_one(self):
        three_node = Node(3, None, None)
        seven_node = Node(7, None, None)
        five_node = Node(5, three_node, seven_node)
        eighteen_node = Node(18, None, None)
        fifteen_node = Node(15, None, eighteen_node)
        ten_node = Node(10, five_node, fifteen_node)

        self.assertEqual(
            binary_tree_search_dfs(ten_node, 7).value,
            7,
            'Handles valid case'
        )

    def test_valid_case_two(self):
        three_node = Node(3, None, None)
        seven_node = Node(7, None, None)
        five_node = Node(5, three_node, seven_node)
        eighteen_node = Node(18, None, None)
        fifteen_node = Node(15, None, eighteen_node)
        ten_node = Node(10, five_node, fifteen_node)

        self.assertEqual(
            binary_tree_search_dfs(ten_node, 10).value,
            10,
            'Handles valid case'
        )

    def test_empty_case(self):
        one_node = Node(1, None, None)
        self.assertEqual(
            binary_tree_search_dfs(one_node, 1).value,
            1,
            'Handles empty case'
        )

    def test_invalid_case(self):
        one_node = Node(1, None, None)
        self.assertEqual(
            binary_tree_search_dfs(one_node, 2),
            None,
            'Handles invalid case'
        )

    def test_null_case(self):
        self.assertEqual(
            binary_tree_search_dfs(None, 1),
            None,
            'Handles null case'
       )


class TestBinaryTreeSearchBFS(unittest.TestCase):
    def test_valid_case_one(self):
        three_node = Node(3, None, None)
        seven_node = Node(7, None, None)
        five_node = Node(5, three_node, seven_node)
        eighteen_node = Node(18, None, None)
        fifteen_node = Node(15, None, eighteen_node)
        ten_node = Node(10, five_node, fifteen_node)

        self.assertEqual(
            binary_tree_search_bfs(ten_node, 7).value,
            7,
            'Handles valid case'
        )

    def test_valid_case_two(self):
        three_node = Node(3, None, None)
        seven_node = Node(7, None, None)
        five_node = Node(5, three_node, seven_node)
        eighteen_node = Node(18, None, None)
        fifteen_node = Node(15, None, eighteen_node)
        ten_node = Node(10, five_node, fifteen_node)

        self.assertEqual(
            binary_tree_search_bfs(ten_node, 10).value,
            10,
            'Handles valid case'
        )

    def test_empty_case(self):
        one_node = Node(1, None, None)
        self.assertEqual(
            binary_tree_search_bfs(one_node, 1).value,
            1,
            'Handles empty case'
        )

    def test_invalid_case(self):
        one_node = Node(1, None, None)
        self.assertEqual(
            binary_tree_search_bfs(one_node, 2),
            None,
            'Handles invalid case'
        )

    def test_null_case(self):
        self.assertEqual(
            binary_tree_search_bfs(None, 1),
            None,
            'Handles null case'
        )
