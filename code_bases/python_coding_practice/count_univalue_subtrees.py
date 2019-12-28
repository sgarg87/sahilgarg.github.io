# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def _count_univalue_subtrees(self, root):

        is_tree_univalue = True

        if root.left is not None:
            is_univalue_left, value_left, count_left = self._count_univalue_subtrees(root=root.left)
            if (not is_univalue_left) or (value_left != root.val):
                is_tree_univalue = False
        else:
            count_left = 0

        if root.right is not None:
            is_univalue_right, value_right, count_right = self._count_univalue_subtrees(root=root.right)
            if (not is_univalue_right) or (value_right != root.val):
                is_tree_univalue = False
        else:
            count_right = 0

        if not is_tree_univalue:
            return False, None, (count_left+count_right)
        else:
            return True, root.val, (count_left+count_right+1)

    def countUnivalSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0

        _, _, count = self._count_univalue_subtrees(root=root)
        return count
