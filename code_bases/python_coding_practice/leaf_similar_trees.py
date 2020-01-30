# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def leaves_dfs(self, node, leaves):
        if (node.left is None) and (node.right is None):
            leaves.append(node.val)
        else:
            if node.left is not None:
                self.leaves_dfs(node.left, leaves)
            if node.right is not None:
                self.leaves_dfs(node.right, leaves)

    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """

        leaves1 = []
        self.leaves_dfs(node=root1, leaves=leaves1)
        print(leaves1)

        leaves2 = []
        self.leaves_dfs(node=root2, leaves=leaves2)
        print(leaves2)

        if leaves1 == leaves2:
            return True
        else:
            return False

