def insertionSort( unorderedList ):
    """ 
    given an unorderedList return another
    sorted list using insertion sort
    """
    orderedList = []
    for element in unorderedList:
        index = len( unorderedList )
        # import pdb; pdb.set_trace()
        for compareElement in orderedList:
            if element <= compareElement:
                index = orderedList.index(compareElement)
                break
        orderedList.insert(index,element)
    return orderedList

def inPlaceInsertionSort( unorderedList ):
    """
    given an unorderedList sorts it in place
    using insertion sort
    """
    #import pdb; pdb.set_trace()
    for j in xrange(1, len(unorderedList)):
        for i in xrange(0, j):
            key = unorderedList[j]
            if unorderedList[i] >= unorderedList[j]:
                for k in xrange(i, j):
                    unorderedList[i+j-k] = unorderedList[i+j-k-1]
                unorderedList[i] = key

def inPlaceDecrInsertionSort( unorderedList ):
    """
    given an unorderedList sorts it in place
    using insertion sort in decreasing order
    """
    #import pdb; pdb.set_trace()
    for j in xrange(1, len(unorderedList)):
        for i in xrange(0, j):
            key = unorderedList[j]
            if unorderedList[i] <= unorderedList[j]:
                for k in xrange(i, j):
                    unorderedList[i+j-k] = unorderedList[i+j-k-1]
                unorderedList[i] = key

