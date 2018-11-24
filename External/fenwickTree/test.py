import unittest
import fenwick_tree as ft

class testSolution(unittest.TestCase):

    def test_tree(self):
        freq = [2, 1, 1, 3, 2, 3, 4, 5, 6, 7, 8, 9]
        BITTree = ft.construct(freq)
        self.assertEqual(12, ft.getsum(BITTree,5))
        freq[3] += 6
        ft.updatebit(BITTree, 3, 6)
        self.assertEqual(18, ft.getsum(BITTree,5))


if __name__ == "__main__":
    unittest.main()
