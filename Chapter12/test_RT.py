import unittest
from binary_search_tree import Node
from radix_tree import radix_tree_insert, sort_strings


class testRT(unittest.TestCase):
    def setUp(self):
        self.tree = Node('#')

    def test_insert(self):
        radix_tree_insert(self.tree, "0100", 2)
        self.assertEqual(self.tree.left.val, 0)
        self.assertEqual(self.tree.left.right.val, 1)
        self.assertEqual(self.tree.left.right.left.val, 0)
        self.assertEqual(self.tree.left.right.left.end, -1)
        self.assertEqual(self.tree.left.right.left.left.val, 0)
        self.assertEqual(self.tree.left.right.left.left.end, 2)
        radix_tree_insert(self.tree, "010", 3)
        self.assertEqual(self.tree.left.right.left.end, 3)
        radix_tree_insert(self.tree, "01001", 5)
        self.assertEqual(self.tree.left.right.left.left.right.end, 5)
        self.assertEqual(self.tree.left.right.left.left.right.val, 1)
        radix_tree_insert(self.tree, "100", 9)
        radix_tree_insert(self.tree, "10", 8)
        self.assertEqual(self.tree.right.left.left.end, 9)
        self.assertEqual(self.tree.right.left.end, 8)

    def test_sort_strings(self):
        strings = ["100", "10", "011", "0", "1011"]
        got = sort_strings(strings)
        self.assertEqual(got, sorted(strings, key=len))


if __name__ == "__main__":
    unittest.main()
