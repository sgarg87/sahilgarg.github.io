# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def mirror_image(self, node1, node2):
        if (node1 is not None) and (node2 is not None):
            print(node1.val, node2.val)
            if node1.val != node2.val:
                return False
            else:
                return self.mirror_image(node1.right, node2.left) & self.mirror_image(node1.left, node2.right)
        elif (node1 is None) and (node2 is None):
            return True
        else:
            return False

    def isSymmetric(self, root):
        if root is None:
            return True
        else:
            if (root.left is None) and (root.right is None):
                return True
            else:
                return self.mirror_image(root.left, root.right)
