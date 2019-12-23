# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def path_from_leaf_node(self, leaf_node):
        path = []
        curr_node = leaf_node
        while curr_node is not None:
            path.append(curr_node)
            curr_node = curr_node.parent
        path.reverse()
        return path

    def dfs_search_recursive(self, root_node, end_node):
        end_node_found = self._dfs_traversal(
            root_node=root_node, end_node=end_node,
        )
        path = self.path_from_leaf_node(
            leaf_node=end_node_found,
        )
        return path

    def _dfs_traversal(self, root_node, end_node):
        # only one traversal path possible

        assert root_node is not None
        assert end_node is not None

        if not hasattr(root_node, 'parent'):
            root_node.parent = None

        if root_node == end_node:
            return root_node
        else:
            for curr_child in [root_node.left, root_node.right]:
                if curr_child is not None:
                    curr_child.parent = root_node
                    node_searched = self._dfs_traversal(root_node=curr_child, end_node=end_node)
                    if node_searched is not None:
                        return node_searched

        return None

    def lowestCommonAncestor(self, root, p, q):
        p_traversal = self.dfs_search_recursive(root_node=root, end_node=p)
        if p_traversal is None:
            return None

        q_traversal = self.dfs_search_recursive(root_node=root, end_node=q)
        if q_traversal is None:
            return None

        min_traversal_len = min(len(p_traversal), len(q_traversal))

        common_ancestor = root
        for curr_idx in range(min_traversal_len):
            if p_traversal[curr_idx] == q_traversal[curr_idx]:
                common_ancestor = p_traversal[curr_idx]
            else:
                break

        assert common_ancestor is not None

        return common_ancestor
