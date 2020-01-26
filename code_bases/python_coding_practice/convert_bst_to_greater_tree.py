# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def inorder_traverse(self, root):
        list = []
        if root.left is not None:
            list += self.inorder_traverse(root.left)
        list.append(root)
        if root.right is not None:
            list += self.inorder_traverse(root.right)
        return list

    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return None

        # sorted
        inorder_list_of_nodes = self.inorder_traverse(root=root)

        num_nodes = len(inorder_list_of_nodes)
        sum_node_values = 0
        for curr_node_idx in range(num_nodes-1, -1, -1):
            curr_node_val = inorder_list_of_nodes[curr_node_idx].val
            inorder_list_of_nodes[curr_node_idx].val += sum_node_values
            sum_node_values += curr_node_val
            del curr_node_val

        return root

