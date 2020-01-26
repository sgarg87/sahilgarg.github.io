# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.root = root

    def _smallest(self, node, parent=None):
        if node.left is not None:
            return self._smallest(node=node.left, parent=node)
        else:
            smallest_val = node.val
            if parent is None:
                # root node
                self.root = node.right
            else:
                parent.left = node.right
            return smallest_val

    def next(self):
        """
        @return the next smallest number
        :rtype: int
        """
        return self._smallest(node=self.root)

    def hasNext(self):
        """
        @return whether we have a next smallest number
        :rtype: bool
        """
        return self.root is not None


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()