"""query functions for BST"""


def iterative_tree_search(tree, value):
    """search query as in CLRS pg. 257
    args:
        tree: binary tree
        value: value searched
    returns:
        node: node of the searched tree
    """
    while tree and tree.val != value:
        if tree.val > value:
            tree = tree.left
        else:
            tree = tree.right
    return tree


def iterative_minimum(tree):
    """min query as in CLRS pg. 258
    args:
        tree: binary tree
    returns:
        node: node with min val
    """
    while tree.left:
        tree = tree.left
    return tree


def iterative_maximum(tree):
    """max query as in CLRS pg. 258
    args:
        tree: binary tree
    returns:
        node: node with min val
    """
    while tree.right:
        tree = tree.right
    return tree


def iterative_successor(tree, val):
    """successor query as in CLRS pg. 259
    args:
        tree: binary tree
        val: value
    returns:
        val: successor val
    """
    res = 1e9
    while tree and tree.val != val:
        if tree.val > val:
            res = min(res, tree.val)
            tree = tree.left
        else:
            tree = tree.right
    if tree and tree.right:
        minimum = iterative_minimum(tree.right).val
        res = min(res, minimum)
    return res if res != 1e9 else None


def iterative_predecessor(tree, val):
    """predecessor query as in CLRS pg. 259
    args:
        tree: binary tree
        val: value
    returns:
        val: predecessor val
    """
    res = -1e9
    while tree and tree.val != val:
        if tree.val > val:
            tree = tree.left
        else:
            res = max(res, tree.val)
            tree = tree.right
    if tree and tree.left:
        minimum = iterative_maximum(tree.left).val
        res = max(res, minimum)
    return res if res != -1e9 else None
