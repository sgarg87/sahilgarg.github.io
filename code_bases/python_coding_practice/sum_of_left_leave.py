# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def is_leaf_node(self, node):
        if (node.left is None) and (node.right is None):
            return True
        else:
            return False

    def sum_dfs(self, node, is_left_child):
        if node is None:
            return 0

        if self.is_leaf_node(node):
            assert is_left_child is not None
            if is_left_child:
                return node.val
            else:
                return 0
        else:
            total_sum = 0
            total_sum += self.sum_dfs(node.left, is_left_child=True)
            total_sum += self.sum_dfs(node.right, is_left_child=False)
            return total_sum

    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if (root is None) or self.is_leaf_node(root):
            return 0

        return self.sum_dfs(root, None)
