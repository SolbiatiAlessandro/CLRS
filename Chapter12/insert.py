"""insert functions for BST"""
from binary_search_tree import Node


def tree_insert(tree, val):
    """CLRS pg. 261, insert a new node in the BST
    args:
        tree: Node BST
        val: value to be inserted
    returns:
        Node: the new tree
    """
    prev, res = None, tree
    while tree:
        prev = tree
        if tree.val > val:
            tree = tree.left
        elif tree.val < val:
            tree = tree.right
        else:
            return res
    if prev is None:
        return Node(val)
    elif prev.val > val:
        prev.left = Node(val)
    else:
        prev.right = Node(val)
    return res
