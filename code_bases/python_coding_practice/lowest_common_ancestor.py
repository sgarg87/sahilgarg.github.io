# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def _contains_node(self, root, node_for_search):

        # print(root.val, node_for_search.val)

        if root == node_for_search:
            return True

        if root.left is not None:
            in_left_subtree = self._contains_node(root=root.left, node_for_search=node_for_search)
            if in_left_subtree:
                return True
        else:
            in_left_subtree = False

        if root.right is not None:
            in_right_subtree = self._contains_node(root=root.right, node_for_search=node_for_search)
            if in_right_subtree:
                return True
        else:
            in_right_subtree = False

        return (in_left_subtree | in_right_subtree)

    def lowestCommonAncestor(self, root, p, q):
        p_in_tree = self._contains_node(root=root, node_for_search=p)
        q_in_tree = self._contains_node(root=root, node_for_search=q)
        assert (p_in_tree and q_in_tree)
        return self._lowestCommonAncestor(root=root, p=p, q=q)

    def p_q_in_subtree(self, root, p, q):
        p_in_subtree = self._contains_node(root=root, node_for_search=p)
        q_in_subtree = self._contains_node(root=root, node_for_search=q)
        print(p_in_subtree, q_in_subtree)
        return (p_in_subtree & q_in_subtree)

    def _lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        print(root.val, p.val, q.val)

        if (root != p) and (root != q):
            if (root.left is not None) and self.p_q_in_subtree(root=root.left, p=p, q=q):
                return self._lowestCommonAncestor(root=root.left, p=p, q=q)

            if (root.right is not None) and self.p_q_in_subtree(root=root.right, p=p, q=q):
                return self._lowestCommonAncestor(root=root.right, p=p, q=q)

            return root
        else:
            return root
