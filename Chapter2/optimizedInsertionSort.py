from binarysearch import _binarysearch as bs

def optimizedInsertionSort( unorderedList ):
    """
    given an unorderedList sorts it in place
    using insertion sort, binary search 
    optimization
    """
    for j in xrange(1, len(unorderedList)): 
        key = unorderedList[j]
        i   = bs( unorderedList[0:j], key )
        for k in xrange(i, j):
            unorderedList[i+j-k] = unorderedList[i+j-k-1]
        unorderedList[i] = key


