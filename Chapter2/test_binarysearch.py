from binarysearch import _binarysearch as bs
import unittest


class testBinarySearch( unittest.TestCase ):
    def testNull(self):
        self.assertEqual( bs( [], 0 ), 0 )
    
    def testEven(self):
        self.assertEqual( bs( [1,2,3,4,5,6], 2.5  ), 1 )

    def testOdd(self):
        self.assertEqual( bs( [1,2,3,4,5,6,7], 6  ), 5 )


if __name__ == '__main__':
    unittest.main()
