import unittest
from knuthMorrisPratt import KMP 

def naiveMatching( text, pattern ):
    """
    naive matching to benchmark KMP
    :text (string)
    :pattern (string)
    :rtype list[int] with matches
    """
    res = []
    for i in xrange(0, len(text)):
        match = 1
        for j in xrange(0, len(pattern)):
            if text[i+j]!=pattern[j]:
                match=0
                break
        if match:
            res.append(i)
    return res

class testKMP( unittest.TestCase ):

    def testKMP( self ):

        got = KMP( "abxabcabcaby", "abcaby" )
        self.assertEqual( got, [6] )

        got = naiveMatching( "abxabcabcaby", "abcaby" )
        self.assertEqual( got, [6] )

    def test_benchmarkKMP( self ):

        import time 
        t1 = time.time()
        got = KMP( "abxabcabcaby", "abcaby" )
        t2 = time.time()
        got = naiveMatching( "abxabcabcaby", "abcaby" )
        t3 = time.time()

        print "KMP: "+str(t2-t1)
        print "NAIVE: "+str(t3-t2)


if __name__ == "__main__":
    unittest.main()



