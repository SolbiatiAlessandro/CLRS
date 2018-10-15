import unittest
import disjoint_set


class TestImplementation(unittest.TestCase):
    def setUp(self):
        self.ds = disjoint_set.DisjointSets()

    def test_disjoint_set(self):
        self.ds.make_set('c')
        self.ds.make_set('h')
        self.ds.make_set('e')
        self.ds.make_set('b')
        self.ds.make_set('f')
        self.ds.make_set('d')
        self.ds.make_set('g')
        self.ds.link('c', 'h')
        self.ds.link('b', 'h')
        self.ds.link('e', 'c')
        self.ds.link('f', 'd')
        self.ds.link('g', 'd')

        self.assertEqual(self.ds.find_set('h'), self.ds.find_set('c'))
        self.assertEqual(self.ds.find_set('e'), self.ds.find_set('c'))
        self.assertEqual(self.ds.find_set('b'), self.ds.find_set('c'))

        self.assertEqual(self.ds.find_set('d'), self.ds.find_set('f'))
        self.assertEqual(self.ds.find_set('g'), self.ds.find_set('f'))

        self.assertNotEqual(self.ds.find_set('g'), self.ds.find_set('h'))

        self.ds.union('h', 'g')

        self.assertEqual(self.ds.find_set('g'), self.ds.find_set('h'))

        print "okk"


if __name__ == "__main__":
    unittest.main()
