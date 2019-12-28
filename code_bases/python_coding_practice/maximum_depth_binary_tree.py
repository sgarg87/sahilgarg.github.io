# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0

        if root.left is not None:
            left_max_depth = self.maxDepth(root=root.left)
        else:
            left_max_depth = 0

        if root.right is not None:
            right_max_depth = self.maxDepth(root=root.right)
        else:
            right_max_depth = 0

        max_subtree_depth = max(left_max_depth, right_max_depth)

        return 1 + max_subtree_depth
