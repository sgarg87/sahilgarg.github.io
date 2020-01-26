import copy


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def path_to_str(self, path):
        ancestors = [str(x) for x in path]
        return '->'.join(ancestors)

    def bfs_sol(self, root):
        paths = []

        queue = list()
        queue.append((root, []))
        del root

        while queue:
            x, ancestors = queue.pop(0)
            ancestors.append(x.val)

            if (x.left is None) and (x.right is None):
                paths.append(self.path_to_str(path=ancestors))
            else:
                if x.left is not None:
                    queue.append([x.left, copy.copy(ancestors)])
                if x.right is not None:
                    queue.append([x.right, copy.copy(ancestors)])

        return paths

    def _dfs_sol(self, root, ancestors, paths):
        ancestors.append(root.val)

        if (root.left is None) and (root.right is None):
            paths.append(self.path_to_str(ancestors))
        else:
            if root.left is not None:
                self._dfs_sol(root=root.left, ancestors=ancestors, paths=paths)

            if root.right is not None:
                self._dfs_sol(root=root.right, ancestors=ancestors, paths=paths)

        ancestors.pop()

    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if root is None:
            return []

        # return self.bfs_sol(root=root)

        paths = []
        self._dfs_sol(root=root, ancestors=[], paths=paths)
        return paths
