# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.is_visited = False


class Solution(object):

    def path_sums_recursion(self, root, path_sum, sum=0):
        sum += root.val

        if (root.left is None) and (root.right is None):
            if sum == path_sum:
                return True
            else:
                return False
        else:
            # left child
            if root.left is not None:
                is_path_sum_match_left_subtree = self.path_sums_recursion(
                    root=root.left, path_sum=path_sum, sum=sum,
                )
            else:
                is_path_sum_match_left_subtree = False

            # right child
            if root.right is not None:
                is_path_sum_match_right_subtree = self.path_sums_recursion(
                    root=root.right, path_sum=path_sum, sum=sum,
                )
            else:
                is_path_sum_match_right_subtree = False

            return is_path_sum_match_left_subtree | is_path_sum_match_right_subtree

    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root is None:
            return False
        else:
            return self.path_sums_recursion(root=root, path_sum=sum)
