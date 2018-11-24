""""implementation of Fenwick Tree
following S. Halim, Competitive Programming 3, pg. 59"""


def construct(frequency_array):
    """construct the fenwick tree
    Args:
        frequency_array: list(int), list of frequencies
    Returns:
        tree: list(int), fenwick tree
    """
    tree = [0] * (len(frequency_array) + 1)
    for index, frequency in enumerate(frequency_array):
        updatebit(tree, index, frequency)
    print tree
    return tree


def getsum(fenwick_tree, index):
    """query the fenwick_tree
    Args:
        fenwick_tree: list(int)
        index: int, this is the query
    Returns:
        int: query results
    """
    res = 0
    index += 1
    while index > 0:
        res += fenwick_tree[index]
        index -= (index & -index)
    return res


def updatebit(fenwick_tree, index, value):
    """update the fenwick_tree
    Args:
        fenwick_tree: list(int)
        index: int
        value: int
    """
    index += 1
    while index <= len(fenwick_tree):
        fenwick_tree[index] += value
        index += (index & -index)
