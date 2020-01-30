# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def inorder(self, root, k, k_elements):
        if len(k_elements) == k:
            return

        if root.left is not None:
            self.inorder(root=root.left, k=k, k_elements=k_elements)
            if len(k_elements) == k:
                return
        k_elements.append(root.val)
        if len(k_elements) == k:
            return
        if root.right is not None:
            self.inorder(root=root.right, k=k, k_elements=k_elements)

    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        k_elements = []
        self.inorder(root=root, k=k, k_elements=k_elements)
        return k_elements[-1]
