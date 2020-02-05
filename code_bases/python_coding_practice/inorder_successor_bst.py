"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""


class Solution(object):
    def _inorder_ancestor(self, node):
        if node.parent is None:
            return None
        else:
            parent_node = node.parent
            if parent_node.left == node:
                return parent_node
            else:
                return self._inorder_ancestor(node=parent_node)

    def _inorder_decendant(self, node):
        while node.left is not None:
            node = node.left
        return node

    def inorderSuccessor(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if node.right is not None:
            return self._inorder_decendant(node.right)
        else:
            return self._inorder_ancestor(node=node)
