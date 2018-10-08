"""traversal functions for BST"""


def in_order_traversal(node):
    """
    recrusive function for in order traversal from CLRS pg. 254
    calls the function visit_node() on the visited nods

    Args:
        node: Node instance to traverse from
    """
    if node:
        in_order_traversal(node.left)
        node.visit()
        in_order_traversal(node.right)


def pre_order_traversal(node):
    """
    recrusive function for pre order traversal from CLRS pg. 254
    calls the function visit_node() on the visited nods

    Args:
        node: Node instance to traverse from
    """
    if node:
        node.visit()
        pre_order_traversal(node.left)
        pre_order_traversal(node.right)


def post_order_traversal(node):
    """
    recrusive function for post order traversal from CLRS pg. 254
    calls the function visit_node() on the visited nods

    Args:
        node: Node instance to traverse from
    """
    if node:
        post_order_traversal(node.left)
        post_order_traversal(node.right)
        node.visit()


def in_order_traversal_iterative(node):
    """
    iterative function for in order traversal from CLRS exercize
    calls the function visit_node() on the visited nods

    Args:
        node: Node instance to traverse from

    Returns:
        res: list of values of visited nodes
    """
    stack, res = [], []
    while True:
        if node:
            stack.append(node)
            node = node.left
        elif stack:
            node = stack.pop()
            node.visit()
            res.append(node.val)
            node = node.right
        else:
            return res
