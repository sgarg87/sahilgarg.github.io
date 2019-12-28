# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def inorderTraversal(self, root, p):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        if root is None:
            return [], None

        traversal_list = []

        # left child
        if root.left is not None:
            left_traversal, left_inorder_successor = self.inorderTraversal(root=root.left, p=p)
            # successor found
            if left_traversal is None:
                return left_traversal, left_inorder_successor
            del left_inorder_successor
            traversal_list += left_traversal

        # return inorder successor
        if traversal_list and (traversal_list[-1] == p):
            return None, root

        traversal_list.append(root)

        # right child
        if root.right is not None:
            right_traveral, right_inorder_successor = self.inorderTraversal(root=root.right, p=p)

            # successor found
            if right_traveral is None:
                return right_traveral, right_inorder_successor
            del right_inorder_successor

            # return inorder successor
            if right_traveral and (root == p):
                return None, right_traveral[0]

            traversal_list += right_traveral

        return traversal_list, None

    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """

        inorder_traversal, inorder_successor = self.inorderTraversal(root=root, p=p)

        return inorder_successor
