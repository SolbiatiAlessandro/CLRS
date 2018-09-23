def hornerHash( P, d, q ):
    """
    compute the hash of a polynomial with the horner rule
    : input type like rabinKarpMatcher
    : rtype ord, hash
    """
    res = 0
    for c in (P):
       res = d*(ord(c) + res)%q
    return res/d

def checkForMatch( Thash, Phash, T, P, match ):
    """
    helper to check for match
    : rtype [ match ] or [ ]
    """
    if Thash != Phash:
        return []
    for i in xrange(0,len(P)):
        if T[i+match]!=P[i]:
            return []
    return [ match ]
  

def rabinKarpMatcher( T, P, d, q ):
    """
    rabinKarpMatcher procedure as described on CLRS page 914
    :T type list(char), text to be looked in
    :P type list(char), patter to be found
    :d type ord, size of the alphabet
    :q type ord, prime number for the modulo operation
    :rtype list(ord), matches found in the text T with the pattern P
    """
    #import pdb;pdb.set_trace()
    res = []
    m, n = len(P), len(T)
    patternHash, textHash = hornerHash( P, d, q ), hornerHash( T[:m], d, q )
    res += checkForMatch( textHash, patternHash, T, P, 0 )
    for match in xrange(1, n-m):
        textHash = (d*(textHash - ord(T[match-1])*(pow(d,m-1)%q))+ord(T[match+m-1]))%q
        res += checkForMatch( textHash, patternHash, T, P, match )
    return res

    
    return res
