# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def maxPathSum(self, root):
        if root is None:
            return 0
        else:
            max_path_sum = root.val
            _, max_path_sum = self._maxPathSum(root=root, max_path_sum=max_path_sum)
            return max_path_sum

    def _maxPathSum(self, root, max_path_sum=0):
        """
        :type root: TreeNode
        :rtype: int
        """
        assert root is not None
        root_val = root.val

        if root.left is not None:
            left_subtree_max, max_path_sum = self._maxPathSum(root.left, max_path_sum=max_path_sum)
            left_subtree_max = max(left_subtree_max, 0)
        else:
            left_subtree_max = 0

        if root.right is not None:
            right_subtree_max, max_path_sum = self._maxPathSum(root.right, max_path_sum=max_path_sum)
            right_subtree_max = max(right_subtree_max, 0)
        else:
            right_subtree_max = 0

        max_of_node = root_val + max(left_subtree_max, right_subtree_max)

        path_including_curr_node = root_val + left_subtree_max + right_subtree_max
        path_including_curr_node = max(max_of_node, path_including_curr_node)
        if path_including_curr_node > max_path_sum:
            max_path_sum = path_including_curr_node

        return max_of_node, max_path_sum
