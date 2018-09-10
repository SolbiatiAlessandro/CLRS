def merge( a, b ):
    """
    merge two sorted lists a, b in increasing
    orderd and return a sorted merged list
    """
    #import pdb; pdb.set_trace() 
    a = [-1e9] + a
    b = [-1e9] + b
    res = []
    while( a[-1] != -1e9 or b[-1] != -1e9 ):
        if( a[-1] >= b[-1] ):
            res = [ a.pop() ] + res 
        else:
            res = [ b.pop() ] + res 
    return res

def mergesort( a ):
    """
    sort a list a in increasing order
    not in place
    """
    #import pdb;pdb.set_trace()
    l = len(a)
    if l == 1 or l == 0:
        return a
    else:
        a1 = mergesort(a[:(l/2)])
        a2 = mergesort(a[l/2:])
        return merge(a1, a2)
