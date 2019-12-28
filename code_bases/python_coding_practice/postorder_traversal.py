# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []

        traversal_list = []

        # left child
        if root.left is not None:
            left_traversal = self.postorderTraversal(root.left)
            traversal_list += left_traversal

        # right child
        if root.right is not None:
            right_traveral = self.postorderTraversal(root.right)
            traversal_list += right_traveral

        traversal_list.append(root.val)

        return traversal_list

