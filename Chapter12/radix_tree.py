"""
Exercize 12-2 pg. 269: Radix Tree
Let S be a set of distinct binary strings whose length sum up to n.
Show how to use radix tree to sort lexicographically S in O(n) time.

test: ./test_RT.py
"""
from binary_search_tree import Node


def radix_tree_print(tree):
    """util function to debug radix tree
    prints:
    [ node.val ] [ node.end ]
    for everynode in the radix tree
    """
    queue = [tree]
    while queue:
        node = queue.pop()
        print "{} {}".format(node.val,
                             '-' if not hasattr(node, 'end') else node.end)
        if node.right:
            queue.insert(0, node.right)
        if node.left:
            queue.insert(0, node.left)


def radix_tree_insert(tree, string, label):
    """inserts a binary string in a radix tree
    args:
        tree: Node, radix_tree
        string: str, to be inserted ( 01011, 1001, .. )
        label: label the end of the string with
    """
    curr = tree
    for i, char in enumerate(string):

        # traverse the binary tree adding nodes if required
        if char == '1':
            if not curr.right:
                curr.right = Node(1)
            curr = curr.right
        elif char == '0':
            if not curr.left:
                curr.left = Node(0)
            curr = curr.left

        # marks the termination of strings
        if i == len(string) - 1:
            curr.end = label
        elif (hasattr(curr, 'end') and curr.end < 0) \
                or not hasattr(curr, 'end'):
            curr.end = -1


def sort_strings(strings):
    """sorts set of binary strings lexicographically
    args:
        strings: list(strings), binary strings in the form 00101..
    returns:
        list(strings) sorted
    """
    # populating the radix tree
    tree = Node('#')
    for i, string in enumerate(strings):
        radix_tree_insert(tree, string, i)

    # BFS on the radix tree
    res, queue = [], [tree]
    while queue:
        node = queue.pop()
        if hasattr(node, 'end') and not node.end < 0:
            res.append(strings[node.end])
        if node.right:
            queue.insert(0, node.right)
        if node.left:
            queue.insert(0, node.left)
    return res
