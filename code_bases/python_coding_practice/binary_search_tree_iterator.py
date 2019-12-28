# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.root = root
        self.curr_node = root
        self.parent = None

    def next(self):
        """
        @return the next smallest number
        :rtype: int
        """
        if self.curr_node.left is None:
            self.curr_node = self.curr_node.left
            self.parent = self.curr_node
            return self.curr_node.left.val
        raise AssertionError

    def hasNext(self):
        """
        @return whether we have a next smallest number
        :rtype: bool
        """

