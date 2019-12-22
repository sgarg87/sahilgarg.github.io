# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def diameterOfBinaryTree(self, root):
        if root is None:
            return 0

        _, max_path_len = self._diameterOfBinaryTree(root=root)
        # number of nodes along the path minus one
        assert max_path_len >= 1
        diameter = max_path_len-1
        del max_path_len

        return diameter

    def _diameterOfBinaryTree(self, root, max_path_len=0):
        """
        :type root: TreeNode
        :rtype: int
        """
        assert root is not None

        if root.left is not None:
            left_subtree_max, max_path_len = self._diameterOfBinaryTree(root.left, max_path_len=max_path_len)
        else:
            left_subtree_max = 0

        if root.right is not None:
            right_subtree_max, max_path_len = self._diameterOfBinaryTree(root.right, max_path_len=max_path_len)
        else:
            right_subtree_max = 0

        max_of_node = 1 + max(left_subtree_max, right_subtree_max)

        path_including_curr_node = 1 + left_subtree_max + right_subtree_max
        if path_including_curr_node > max_path_len:
            max_path_len = path_including_curr_node

        return max_of_node, max_path_len
