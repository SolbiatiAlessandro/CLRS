import unittest
import prefix

class testPrefix( unittest.TestCase ):

    def test_prefix( self ):

        got = prefix.prefixFunction( "abcaby" )
        self.assertEqual( got, [0,0,0,1,2,0] )

        got = prefix.prefixFunction( "aabaaab" )
        self.assertEqual( got, [0,1,0,1,2,2,3] )

        got = prefix.prefixFunction( "aabaabaaa" )
        self.assertEqual( got, [0,1,0,1,2,3,4,5,2] )


if __name__ == "__main__":
    unittest.main()


