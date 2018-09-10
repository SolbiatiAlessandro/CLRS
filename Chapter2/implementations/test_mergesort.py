from mergesort import merge as mg
from mergesort import mergesort as mgs
from insertionsort import inPlaceInsertionSort as ipmgs

import random
import unittest


class testMerge( unittest.TestCase ):
    def testNull(self):
        self.assertEqual( mg([],[]),[] )

    def testSame(self):
        #import pdb; pdb.set_trace()
        self.assertEqual( mg([1,1,1],[1,1,1]),[1,1,1,1,1,1] )

    def testRandom(self):
        for x in xrange(1000):
            a = [random.random() for _ in xrange(20)] 
            ipmgs(a)
            b = [random.random() for _ in xrange(20)] 
            ipmgs(b)
            c = mg(a,b)
            for x in a:
                self.assertTrue( x in c  )
            for x in b:
                self.assertTrue( x in c  )
            for x in c:
                self.assertTrue( x in b or x in a  )
            for i in xrange(39):
                self.assertLessEqual( c[i],c[i+1] )


class testMergeSort( unittest.TestCase ):
    def testNull(self):
        self.assertEqual( mgs([]),[] )

    def testSame(self):
        import pdb;pdb.set_trace()
        self.assertEqual( mgs([ 1, 1, 1 ]),[1,1,1] ) 

    def testRandom(self):
        for x in xrange(1000):
            unsorted = [random.random() for _ in xrange(20)] 
            got = mgs(unsorted)
            for i in xrange(19):
                self.assertLessEqual( got[i],got[i+1] )


if __name__ == '__main__':
    unittest.main()
