"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""


class Solution(object):

    def inorder_traveral(self, root):
        if root is None:
            return []

        left_subtree_nodes = self.inorder_traveral(root.left)
        right_subtree_nodes = self.inorder_traveral(root.right)

        return left_subtree_nodes + [root] + right_subtree_nodes

    def treeToDoublyList(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if root is None:
            return None

        list_of_nodes = self.inorder_traveral(root=root)
        n = len(list_of_nodes)

        for curr_idx, curr_node in enumerate(list_of_nodes):
            curr_node.left = list_of_nodes[curr_idx-1]
            curr_node.right = list_of_nodes[(curr_idx+1)%n]

        return list_of_nodes[0]
