# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0

        min_depth_of_tree = 1

        if root.left is not None:
            left_subtree_depth = self.minDepth(root=root.left)
            min_depth_of_tree += left_subtree_depth

        if root.right is not None:
            right_subtree_depth = self.minDepth(root=root.right)
            if root.left is not None:
                min_depth_of_tree = min(min_depth_of_tree, right_subtree_depth+1)
            else:
                min_depth_of_tree += right_subtree_depth

        return min_depth_of_tree
