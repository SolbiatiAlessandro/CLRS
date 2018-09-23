import rabinKarp
import unittest

prime = 103079
dsize = 256

class testMatcher( unittest.TestCase ):

    def test_horner( self ):
        
        hash1 = rabinKarp.hornerHash( "31415", dsize, prime )
        hash2 = rabinKarp.hornerHash( "31415", dsize, prime )
        hash3 = rabinKarp.hornerHash( "31419", dsize, prime )
        self.assertEqual( hash1, hash2 )
        self.assertNotEqual( hash1, hash3 )

    def test_checkmatch( self ):

        got = rabinKarp.checkForMatch( 10, 10, [1,2,3,4,5], [2,3,4], 1 )
        self.assertEqual( got, [1] )

    #@unittest.skip("wait")
    def test_matcher( self ):
        T = "123141566"
        p = "31415"
        got = rabinKarp.rabinKarpMatcher( T, p, 10, 10000000 )
        self.assertEqual( got, [2] )

        T = "12345678923652321"
        p = "23"
        got = rabinKarp.rabinKarpMatcher( T, p, 10, 10000000 )
        self.assertEqual( got, [1,9,13] )


if __name__ == '__main__':
    unittest.main()
