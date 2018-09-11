from optimizedInsertionSort import optimizedInsertionSort as ois

import random
import unittest

class testInPlaceISort( unittest.TestCase ):
    def testNull(self):
        a = []
        ois(a)
        self.assertEqual( a,[] )

    def testSame(self):
        a = [1,1,1]
        ois(a)
        self.assertEqual( a,[1,1,1] )

    def testRandom(self):
        for x in xrange(1000):
            unsorted = [random.random() for _ in xrange(20)] 
            ois(unsorted)
            for i in xrange(19):
                self.assertLessEqual( unsorted[i],unsorted[i+1] )


if __name__ == '__main__':
    unittest.main()
