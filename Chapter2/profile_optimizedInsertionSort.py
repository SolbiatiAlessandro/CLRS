from optimizedInsertionSort import optimizedInsertionSort as oisort
from implementations.insertionsort import inPlaceInsertionSort as isort
import random
import time

def generateAndSort( size, sortFunction ):
    """util function to profile sorting functions"""
    unsorted = [ random.random() for _ in xrange(size) ]
    t1 = time.time()
    sortFunction( unsorted )
    t2 = time.time()
    return t2-t1

def compare( size ):
    print "InsertionSort size {} : {}".format( str(size), generateAndSort( size, isort ) )
    print "Optimized InsertionSort size {} : {}".format( str(size), generateAndSort( size, oisort ) )

compare(pow(10,2))
compare(pow(10,3))
compare(pow(10,4))

"""
InsertionSort size 100 : 0.00076699256897
Optimized InsertionSort size 100 : 0.00059986114502
InsertionSort size 1000 : 0.0766959190369
Optimized InsertionSort size 1000 : 0.0355279445648
InsertionSort size 10000 : 6.13982009888
Optimized InsertionSort size 10000 : 3.0811150074
"""
