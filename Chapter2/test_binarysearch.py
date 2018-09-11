from binarysearch import _binarysearch as bs
import unittest


class testBinarySearch( unittest.TestCase ):
    #def testNull(self):
        #self.assertEqual( bs( [], 0 ), 0 )
    
    def testEven(self):
        self.assertEqual( bs( [1,2,3,4,5,6], 2.5  ), 2 )

    def testOdd(self):
        self.assertEqual( bs( [1,2,3,4,5,6,7], 6  ), 6 )
        self.assertEqual( bs( [1,2,3,4,5,6,7], 4.6  ), 4 )

    def testBoundaries(self):
        self.assertEqual( bs( [1,2,3], 4 ), 3 )
        self.assertEqual( bs( [1,2,3], 0 ), 0 )
        self.assertEqual( bs( [1,2,3], 3 ), 3 )

    #TODO: test searching for the last present element


if __name__ == '__main__':
    unittest.main()
