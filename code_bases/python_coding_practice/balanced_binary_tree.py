# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def depth(self, root):
        if root is None:
            return 0

        left_depth = self.depth(root=root.left)
        if left_depth is None:
            return None
        right_depth = self.depth(root=root.right)
        if right_depth is None:
            return None

        if abs(left_depth-right_depth) <= 1:
            return max(left_depth, right_depth)+1
        else:
            return None

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        depth = self.depth(root=root)
        if depth is not None:
            return True
        else:
            return False
