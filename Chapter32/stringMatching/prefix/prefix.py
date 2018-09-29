def prefixFunction( string ):
    """
    given a string the function generate the array with 
    prefix function, defined as longest prefix that is 
    also suffix of the given substring.
    Note: on CLRS (pg. 926 ) the prefixFunction is 1 base,
    here is 0 based

    :string (str) input string
    :rtype (list[int]) return the prefix function 
    """
    k,prefixArray=0,[0] 
    for q in xrange(1, len(string)):
        while k>0 and string[k]!=string[q]:
            k=prefixArray[k-1]
        if string[k]==string[q]:
            k=k+1
        prefixArray.append(k)
    return prefixArray
