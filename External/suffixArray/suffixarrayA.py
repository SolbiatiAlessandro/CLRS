def suffixArray(string):
    """
    build the suffix array from a given string following
    the n^2logn implementation in S.&F. Halim pg. 253
    """
    substrings = [string[i:] for i in xrange(len(string))]
    res = []
    for substring in sorted(substrings):
        res.append(len(string)-len(substring))
    return res
