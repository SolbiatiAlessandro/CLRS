import unittest
from binary_search_tree import Node
from traverse import in_order_traversal, in_order_traversal_iterative, pre_order_traversal, post_order_traversal
from query import iterative_tree_search, iterative_minimum, iterative_maximum


class testBST(unittest.TestCase):

    def setUp(self):
        tree = Node(5)
        tree.left = Node(3)
        tree.left.right = Node(5)
        tree.left.left = Node(2)
        tree.right = Node(7)
        tree.right.right = Node(8)
        self.tree = tree

    def test_traversal(self):
        in_order_traversal(self.tree)
        got = in_order_traversal_iterative(self.tree)
        self.assertEqual(got, [2, 3, 5, 5, 7, 8])
        print ""
        pre_order_traversal(self.tree)
        print ""
        post_order_traversal(self.tree)

    def test_query(self):
        got = iterative_tree_search(self.tree, 7)
        self.assertEqual(got, self.tree.right)

        got = iterative_tree_search(self.tree, 9)
        self.assertEqual(got, None)

        got = iterative_minimum(self.tree)
        self.assertEqual(got, self.tree.left.left)
        self.assertEqual(got.val, 2)

        got = iterative_maximum(self.tree)
        self.assertEqual(got, self.tree.right.right)
        self.assertEqual(got.val, 8)
        print "ok"


if __name__ == "__main__":
    unittest.main()
