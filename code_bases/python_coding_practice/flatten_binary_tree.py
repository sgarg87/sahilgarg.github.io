# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def _flatten(self, node):
        node_left = node.left
        node_right = node.right
        node.left = None

        if node_left is None:
            prv_node = node
        else:
            node.right = node_left
            prv_node = self._flatten(node=node_left)

        if node_right is not None:
            prv_node.right = node_right
            prv_node = self._flatten(node=node_right)

        return prv_node

    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if root is None:
            return None

        self._flatten(node=root)
