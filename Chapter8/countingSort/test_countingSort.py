from countingsort import countingSort as csort

import random
import unittest


class testISort( unittest.TestCase ):
    def testNull(self):
        self.assertEqual( csort([]),[] )

    def testSame(self):
        self.assertEqual( csort([ 1, 1, 1 ]),[1,1,1] ) 

    def testExample(self):
        self.assertEqual(csort([2, 5, 3, 0, 2, 0, 3]), [0, 0, 2, 2, 3, 3, 5])

    def testRandom(self):
        for x in xrange(1000):
            unsorted = [int(random.random()*100)for _ in xrange(20)] 
            csorted = csort(unsorted)
            for i in xrange(19):
                self.assertLessEqual(csorted[i], csorted[i+1])


if __name__ == '__main__':
    unittest.main()
