import prefix.prefix

def KMP( text, pattern ):
    """
    KMP algorithm using prefixArray implementation
    :text (string)
    :pattern (string)
    :rtype list[int] with matches
    """

    i,j,res = 0,0,[]
    prefixArray = prefix.prefix.prefixFunction( pattern )
    for j in xrange(0, len(text)):
        while i>0 and text[j]!=pattern[i]:
            i=prefixArray[i-1]
        if text[j] == pattern[i]:
            i+=1
        if i == len(pattern):
            res.append(j + 1 - len(pattern))
    return res

