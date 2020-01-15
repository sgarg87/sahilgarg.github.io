import copy


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def init_count(self):
        self.count = 0

    def dfs(self, node, ancestors_val, sum):
        assert node is not None

        ancestors_val.append(node.val)

        curr_sum = 0
        for curr_ancestor in reversed(ancestors_val):
            curr_sum += curr_ancestor
            if curr_sum == sum:
                self.count += 1

        if node.left is not None:
            self.dfs(node=node.left, ancestors_val=copy.copy(ancestors_val), sum=sum)

        if node.right is not None:
            self.dfs(node=node.right, ancestors_val=copy.copy(ancestors_val), sum=sum)

    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if root is None:
            return 0

        self.init_count()
        self.dfs(node=root, ancestors_val=[], sum=sum)
        return self.count
