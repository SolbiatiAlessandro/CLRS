from insertionsort import insertionSort as isort
from insertionsort import inPlaceInsertionSort as ipisort
from insertionsort import inPlaceDecrInsertionSort as ipidsort

import random
import unittest


class testISort( unittest.TestCase ):
    def testNull(self):
        self.assertEqual( isort([]),[] )

    def testSame(self):
        self.assertEqual( isort([ 1, 1, 1 ]),[1,1,1] ) 

    def testRandom(self):
        for x in xrange(1000):
            unsorted = [random.random() for _ in xrange(20)] 
            got = isort(unsorted)
            for i in xrange(19):
                self.assertLessEqual( got[i],got[i+1] )

class testInPlaceISort( unittest.TestCase ):
    def testNull(self):
        a = []
        ipisort(a)
        self.assertEqual( a,[] )

    def testSame(self):
        a = [1,1,1]
        ipisort(a)
        self.assertEqual( a,[1,1,1] )

    def testRandom(self):
        for x in xrange(1000):
            unsorted = [random.random() for _ in xrange(20)] 
            ipisort(unsorted)
            for i in xrange(19):
                self.assertLessEqual( unsorted[i],unsorted[i+1] )

class testInPlaceDISort( unittest.TestCase ):
    def testNull(self):
        a = []
        ipidsort(a)
        self.assertEqual( a,[] )

    def testSame(self):
        a = [1,1,1]
        ipidsort(a)
        self.assertEqual( a,[1,1,1] )

    def testRandom(self):
        for x in xrange(1000):
            unsorted = [random.random() for _ in xrange(20)] 
            ipidsort(unsorted)
            for i in xrange(19):
                self.assertGreaterEqual( unsorted[i],unsorted[i+1] )


if __name__ == '__main__':
    unittest.main()
