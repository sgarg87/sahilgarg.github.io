# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isValidBST(self, root, min_value=None, max_value=None):
        """
        :type root: TreeNode
        :rtype: bool
        """

        if root is None:
            return True

        root_val = root.val

        # print('{} < {} < {}'.format(min_value, root_val, max_value))

        if min_value is not None:
            if root_val <= min_value:
                return False

        if max_value is not None:
            if root_val >= max_value:
                return False

        if root.left is not None:
            if max_value is None:
                max_value_for_left_subtree = root_val
            else:
                max_value_for_left_subtree = min(max_value, root_val)
            is_left_subtree_valid = self.isValidBST(
                root.left,
                min_value=min_value,
                max_value=max_value_for_left_subtree,
            )
            if not is_left_subtree_valid:
                return False

        if root.right is not None:
            if min_value is None:
                min_value_for_right_subtree = root_val
            else:
                min_value_for_right_subtree = max(min_value, root_val)
            is_right_subtree_valid = self.isValidBST(
                root.right,
                min_value=min_value_for_right_subtree,
                max_value=max_value,
            )
            if not is_right_subtree_valid:
                return False

        return True
