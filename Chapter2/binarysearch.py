def _binarysearch( orderedList, element ):
    """
    iterative function that return the index
    of the element serached in a orderedList
    """
    #import pdb;pdb.set_trace() 
    l = len( orderedList ) 
    if ( l>0 and element < orderedList[0] ) or l is 0:
        return 0
    elif element >= orderedList[ l - 1 ]:
        return l
    a, b = 0, l
    while True:
        m = (b-a)/2 + a
        if  orderedList[m] <= element < orderedList[m+1]:
            return m+1
        elif element > orderedList[m]:
            a = m+1
        else:
            b = m
