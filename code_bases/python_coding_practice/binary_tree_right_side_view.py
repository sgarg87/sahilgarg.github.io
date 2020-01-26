# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def _right_boundary(self, node, depth_val_map, depth=0):
        if depth not in depth_val_map:
            depth_val_map[depth] = node.val

        child_depth = depth + 1
        if node.right is not None:
            print('right')
            self._right_boundary(node.right, depth_val_map, depth=child_depth)

        if node.left is not None:
            print('left')
            self._right_boundary(node.left, depth_val_map, depth=child_depth)

    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []

        depth_val_map = {}
        self._right_boundary(node=root, depth_val_map=depth_val_map)

        right_view = []
        for curr_depth in sorted(depth_val_map.keys()):
            right_view.append(depth_val_map[curr_depth])

        return right_view

