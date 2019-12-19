# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def levelOrder(self, root, depth=0, result=None):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if result is None:
            result = []

        if root is None:
            assert depth == 0
            return result

        if len(result) < depth+1:
            result.append([])

        result[depth].append(root.val)

        if root.left is not None:
            result = self.levelOrder(root=root.left, depth=depth+1, result=result)

        if root.right is not None:
            result = self.levelOrder(root=root.right, depth=depth+1, result=result)

        return result
