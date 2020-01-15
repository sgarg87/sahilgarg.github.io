# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if (p is None) and (q is None):
            return True
        elif (p is not None) and (q is not None):
            if p.val != q.val:
                return False
        else:
            return False

        if (p.left is None) and (q.left is None):
            is_left_match = True
        elif (p.left is not None) and (q.left is not None):
            is_left_match = self.isSameTree(p.left, q.left)
            if not is_left_match:
                return False
        else:
            return False

        if (p.right is None) and (q.right is None):
            is_right_match = True
        elif (p.right is not None) and (q.right is not None):
            is_right_match = self.isSameTree(p.right, q.right)
            if not is_right_match:
                return False
        else:
            return False

        assert is_left_match and is_right_match
        return True

