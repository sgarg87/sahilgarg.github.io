# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def zigzagLevelOrder(self, root):
        result = self._zigzagLevelOrder(root=root)
        for curr_idx, curr_list in enumerate(result):
            if (curr_idx % 2) == 1:
                result[curr_idx].reverse()
        return result

    def _zigzagLevelOrder(self, root, depth=0, result=None):
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

        order = ['left', 'right']

        for curr_subtree in order:
            if (curr_subtree == 'left') and (root.left is not None):
                result = self._zigzagLevelOrder(root=root.left, depth=depth+1, result=result)

            if (curr_subtree == 'right') and (root.right is not None):
                result = self._zigzagLevelOrder(root=root.right, depth=depth+1, result=result)

        return result
