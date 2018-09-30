def countingSort(array):
    """
    this is a O(n+k) implementation
    of counting sort as from CLRS pg. 169
    where n = len(array) 
          k = max(array) - min(array)
    efficient when k=O(n) so that O(k+n)->O(n)
    """
    small, big = int(1e9), int(-1e9)
    for e in array:
        small, big = min(small, e), max(big, e)
    helper, res = [0]*(big-small+1), [0]*len(array) # big-small = k
    for e in array:
        helper[e-small]+=1
    for index in xrange(1,len(helper)):
        helper[index] += helper[index-1]
    for e in reversed(array):
        res[helper[e-small] - 1] = e
        helper[e-small]-=1
    return res
