# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def is_child_node(self, root):
        if (root.left is None) and (root.right is None):
            return True
        else:
            return False

    def left_boundary(self, root, left_boundary):
        assert root is not None

        if self.is_child_node(root):
            return

        left_boundary.append(root.val)
        if root.left is not None:
            if self.is_child_node(root.left):
                return
            else:
                self.left_boundary(root=root.left, left_boundary=left_boundary)
        elif root.right is not None:
            if self.is_child_node(root.right):
                return
            else:
                self.left_boundary(root=root.right, left_boundary=left_boundary)
        else:
            return

    def right_boundary(self, root, right_boundary):
        assert root is not None

        if self.is_child_node(root):
            return

        right_boundary.append(root.val)
        if root.right is not None:
            if self.is_child_node(root.right):
                return
            else:
                self.right_boundary(root=root.right, right_boundary=right_boundary)
        elif root.left is not None:
            if self.is_child_node(root.left):
                return
            else:
                self.right_boundary(root=root.left, right_boundary=right_boundary)
        else:
            return

    def leaf_nodes(self, root, leaf_nodes):
        if root.left is not None:
            if self.is_child_node(root.left):
                leaf_nodes.append(root.left.val)
            else:
                self.leaf_nodes(root=root.left, leaf_nodes=leaf_nodes)

        if root.right is not None:
            if self.is_child_node(root.right):
                leaf_nodes.append(root.right.val)
            else:
                self.leaf_nodes(root=root.right, leaf_nodes=leaf_nodes)

    def boundaryOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []

        left_boundary = []
        if root.left is not None:
            self.left_boundary(
                root=root.left, left_boundary=left_boundary,
            )
        print(left_boundary)

        right_boundary = []
        if root.right is not None:
            self.right_boundary(
                root.right, right_boundary=right_boundary,
            )
            if right_boundary:
                right_boundary = list(reversed(right_boundary))
        print(right_boundary)

        leaf_nodes = []
        self.leaf_nodes(root, leaf_nodes=leaf_nodes)
        print(leaf_nodes)

        boundary = [root.val] + left_boundary + leaf_nodes + right_boundary

        return boundary
