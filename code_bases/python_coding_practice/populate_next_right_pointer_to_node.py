"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution(object):

    def _connect(self, root, depth=0, result=None):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if result is None:
            result = {}

        if root is None:
            assert depth == 0
            return result

        root.next = None
        if depth in result:
            result[depth].next = root
        result[depth] = root

        if root.left is not None:
            result = self._connect(root=root.left, depth=depth+1, result=result)

        if root.right is not None:
            result = self._connect(root=root.right, depth=depth+1, result=result)

        return result

    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """

        result = self._connect(root=root)

        return root
