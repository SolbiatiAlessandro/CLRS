import unittest
from binary_search_tree import Node
from traverse import in_order_traversal, in_order_traversal_iterative, pre_order_traversal, post_order_traversal
from query import iterative_tree_search, iterative_minimum, iterative_maximum, iterative_successor, iterative_predecessor


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
        """testing functions:
        - in_order_traversal
        - pre_order_traversal
        _ post_order_traversal
        """
        in_order_traversal(self.tree)
        got = in_order_traversal_iterative(self.tree)
        self.assertEqual(got, [2, 3, 5, 5, 7, 8])
        print ""
        pre_order_traversal(self.tree)
        print ""
        post_order_traversal(self.tree)

    def test_search(self):
        """testing functions:
        -iterative_tree_search
        """
        got = iterative_tree_search(self.tree, 7)
        self.assertEqual(got, self.tree.right)

        got = iterative_tree_search(self.tree, 9)
        self.assertEqual(got, None)

    def test_minmax(self):
        """testing functions:
        -iterative_minimum
        -iterative_maximum
        """
        got = iterative_minimum(self.tree)
        self.assertEqual(got, self.tree.left.left)
        self.assertEqual(got.val, 2)

        got = iterative_maximum(self.tree)
        self.assertEqual(got, self.tree.right.right)
        self.assertEqual(got.val, 8)

    def test_successor(self):
        """testing functions:
        -iterative_successor
        """
        self.tree.left.right.val = 4
        got = iterative_successor(self.tree, 7)
        self.assertEqual(got, 8)

        elems = [2, 3, 4, 5, 7, 8]
        for i in xrange(len(elems)-1):
            got = iterative_successor(self.tree, elems[i])
            expected = elems[i+1]
            self.assertEqual(expected, got)
        self.assertEqual(iterative_successor(self.tree, 8), None)

    def test_predecessor(self):
        """testing functions:
        -iterative_predecessor
        """
        self.tree.left.right.val = 4
        got = iterative_predecessor(self.tree, 7)
        self.assertEqual(got, 5)

        elems = [2, 3, 4, 5, 7, 8]
        for i in xrange(1, len(elems)):
            got = iterative_predecessor(self.tree, elems[i])
            expected = elems[i-1]
            self.assertEqual(expected, got)
        self.assertEqual(iterative_predecessor(self.tree, 2), None)


if __name__ == "__main__":
    unittest.main()
