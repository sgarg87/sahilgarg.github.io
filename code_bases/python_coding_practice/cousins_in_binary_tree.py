import copy


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def dfs_search(self, root, x, ancestors):
        # keep only last two ancestors
        # if len(ancestors) > 2:
        #     ancestors = ancestors[-2:]
        ancestors.append(root.val)

        if root.val == x:
            return ancestors
        else:
            if root.left is not None:
                left_ancestors = self.dfs_search(root=root.left, x=x, ancestors=copy.copy(ancestors))
                if left_ancestors is not None:
                    return left_ancestors

            if root.right is not None:
                right_ancestors = self.dfs_search(root=root.right, x=x, ancestors=copy.copy(ancestors))
                if right_ancestors is not None:
                    return right_ancestors

    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        x_ancestors = self.dfs_search(root=root, x=x, ancestors=[])
        print(x_ancestors)
        assert x_ancestors is not None

        y_ancestors = self.dfs_search(root=root, x=y, ancestors=[])
        print(y_ancestors)
        assert y_ancestors is not None

        if len(x_ancestors) != len(y_ancestors):
            return False
        else:
            depth = len(x_ancestors)
            if depth < 3:
                return False

            if x_ancestors[-2] == y_ancestors[-2]:
                return False
            else:
                return True
