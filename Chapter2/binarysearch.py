def _binarysearch( orderedList, element ):
    """
    iterative function that return the index
    of the element serached in a orderedList
    """
    #import pdb;pdb.set_trace() 
    l = len( orderedList )
    if l is 0:
        return 0
    a = 0
    b = l 
    while True:
        m = (b-a)/2 + a
        if l % 2:
            if element is orderedList[m]:
                return m
            elif element > orderedList[m]:
                a = m+1
            else:
                b = m-1
        else:
            if orderedList[m] < element < orderedList[m+1]:
                return m
            elif element > orderedList[m]:
                a = m+1
            else:
                b = m
