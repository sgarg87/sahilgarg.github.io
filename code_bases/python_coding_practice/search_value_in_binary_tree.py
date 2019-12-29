# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if root.val == val:
            return root

        if root.left is not None:
            left_subtree_result = self.searchBST(root=root.left, val=val)
            if left_subtree_result is not None:
                return left_subtree_result

        if root.right is not None:
            right_subtree_result = self.searchBST(root=root.right, val=val)
            if right_subtree_result is not None:
                return right_subtree_result

