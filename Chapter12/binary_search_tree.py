"""contains a basic implementation of a BST"""


class Node(object):
    """
    This is the base class for a BST node

    Args:
        val: integer indicating the value of the node
        right: the right child Node
        left: the left child Node
    """
    def __init__(self, value):
        self.right = None
        self.left = None
        self.val = value

    def visit(self):
        """
        Visits the current node printing the value
        """
        print self.val

    def modify_value(self, value):
        """
        Modifies the value of the current node

        Args:
            value: integer, value to be modified
        """
        self.val = value
