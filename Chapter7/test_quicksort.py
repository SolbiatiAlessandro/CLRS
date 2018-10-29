from quicksort import quicksort as qsort

import random
import unittest


class testInPlaceISort( unittest.TestCase ):
    def testNull(self):
        a = []
        qsort(a,0,len(a)-1)
        self.assertEqual( a,[] )

    def testSame(self):
        a = [1,1,1]
        qsort(a,0,len(a)-1)
        self.assertEqual( a,[1,1,1] )

    def testRandom(self):
        import math
        for x in xrange(1000):
            unsorted = [int(math.floor(random.random()*100)) for _ in xrange(20)] 
            qsort(unsorted,0,len(unsorted)-1)
            for i in xrange(19):
                self.assertLessEqual( unsorted[i],unsorted[i+1] )


if __name__ == '__main__':
    unittest.main()
