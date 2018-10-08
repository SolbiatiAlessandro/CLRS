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
