# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def _match_trees(self, s, t):
        if s.val != t.val:
            return False

        # left subtree
        if (s.left is None) and (t.left is None):
            is_left_subtree_match = True
        elif (s.left is not None) and (t.left is not None):
            is_left_subtree_match = self._match_trees(s.left, t.left)
            if not is_left_subtree_match:
                return False
        else:
            return False

        #right subtree
        if (s.right is None) and (t.right is None):
            is_right_subtree_match = True
        elif (s.right is not None) and (t.right is not None):
            is_right_subtree_match = self._match_trees(s.right, t.right)
            if not is_right_subtree_match:
                return False
        else:
            return False

        assert is_left_subtree_match and is_right_subtree_match
        return True

    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        queue = list()
        queue.append(s)

        while queue:
            curr_node = queue.pop(0)
            if self._match_trees(s=curr_node, t=t):
                return True

            if curr_node.left is not None:
                queue.append(curr_node.left)

            if curr_node.right is not None:
                queue.append(curr_node.right)

        return False
