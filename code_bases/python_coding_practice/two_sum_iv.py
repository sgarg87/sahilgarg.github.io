# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def search(self, root, val, non_match_node):
        if (root != non_match_node) and (val == root.val):
            return True

        if val <= root.val:
            if root.left is None:
                return False
            return self.search(root=root.left, val=val, non_match_node=non_match_node)

        if val >= root.val:
            if root.right is None:
                return False
            return self.search(root=root.right, val=val, non_match_node=non_match_node)

    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        # traverse in BFS
        queue = list()
        queue.append(root)

        while queue:
            curr_node = queue.pop(0)
            complement_val = k - curr_node.val
            does_val_exist = self.search(root=root, val=complement_val, non_match_node=curr_node)
            if does_val_exist:
                return True

            if curr_node.left is not None:
                queue.append(curr_node.left)
            if curr_node.right is not None:
                queue.append(curr_node.right)

        return False
