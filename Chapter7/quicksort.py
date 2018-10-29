def quicksort(A, p, r):
    """implementation of quicksort following CLRS pg. 146

    Args:
        A: list[int/float] array to be sorted
        p: int, beginning index
        r: int, end index
    """
    if p < r:
        q = partition(A, p, r)
        quicksort(A, p, q - 1)
        quicksort(A, q + 1, r)


def partition(A, p, r):
    """implementation of partition function following CLRS pg. 146

    Args:
        A: list[int/float] array to be sorted
        p: int, beginning index
        r: int, end index
    """
    x = A[r]
    i = p - 1
    for j in xrange(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1
