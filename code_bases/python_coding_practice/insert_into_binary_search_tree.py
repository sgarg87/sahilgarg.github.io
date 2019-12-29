# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def insert_element(self, root, element):
        assert element is not None
        if element <= root.val:
            if root.left is not None:
                self.insert_element(root=root.left, element=element)
            else:
                root.left = TreeNode(element)
                return
        else:
            if root.right is not None:
                self.insert_element(root=root.right, element=element)
            else:
                root.right = TreeNode(element)

    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if root is None:
            print('Adding {} as a root node.'.format(val))
            root = TreeNode(val)
        else:
            self.insert_element(root=root, element=val)

        return root
