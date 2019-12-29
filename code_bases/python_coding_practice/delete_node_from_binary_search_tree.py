# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def is_left_or_right_child(self, root, parent):
        if parent.left == root:
            is_left_else_right = True
        elif parent.right == root:
            is_left_else_right = False
        else:
            raise AssertionError
        return is_left_else_right

    def find_minimum_value_node(self, root, depth=0):
        if root.left is None:
            return root, depth
        else:
            return self.find_minimum_value_node(root=root.left, depth=depth+1)

    def find_maximum_value_node(self, root, depth=0):
        if root.right is None:
            return root, depth
        else:
            return self.find_maximum_value_node(root=root.right, depth=depth+1)

    def _delete_node(self, root, key, parent=None):
        assert root is not None
        if root.val == key:
            if parent is not None:
                is_left_else_right_child = self.is_left_or_right_child(root=root, parent=parent)
            else:
                is_left_else_right_child = None

            if (root.left is None) and (root.right is None):
                if parent is None:
                    del root
                    return True, None
                else:
                    if is_left_else_right_child:
                        parent.left = None
                        return True, None
                    else:
                        parent.right = None
                        return True, None
            elif (root.left is not None) and (root.right is not None):
                if root.right.left is None:
                    root.right.left = root.left
                    if parent is None:
                        return True, root.right
                    else:
                        if is_left_else_right_child:
                            parent.left = root.right
                        else:
                            parent.right = root.right
                        return True, None
                elif root.left.right is None:
                    root.left.right = root.right
                    if parent is None:
                        return True, root.left
                    else:
                        if is_left_else_right_child:
                            parent.left = root.left
                        else:
                            parent.right = root.left
                        return True, None
                else:
                    min_node_in_right_subtree, right_depth = self.find_minimum_value_node(root=root.right)
                    max_node_in_left_subtree, left_depth = self.find_maximum_value_node(root=root.left)

                    if right_depth < left_depth:
                        min_node_in_right_subtree.left = root.left
                        if parent is None:
                            return True, root.right
                        else:
                            if is_left_else_right_child:
                                parent.left = root.right
                            else:
                                parent.right = root.right
                            return True, None
                    else:
                        max_node_in_left_subtree.right = root.right
                        if parent is None:
                            return True, root.left
                        else:
                            if is_left_else_right_child:
                                parent.left = root.left
                            else:
                                parent.right = root.left
                            return True, None

                    del right_depth, left_depth
            elif root.left is not None:
                assert root.right is None, 'only left child'
                if parent is None:
                    return True, root.left
                else:
                    if is_left_else_right_child:
                        parent.left = root.left
                    else:
                        parent.right = root.left
                    del root
                    return True, None
            elif root.right is not None:
                assert root.left is None, 'only right child'
                if parent is None:
                    return True, root.right
                else:
                    if is_left_else_right_child:
                        parent.left = root.right
                    else:
                        parent.right = root.right
                    del root
                    return True, None
            else:
                raise AssertionError('all conditions explored already')

        if root.left is not None:
            is_deleted, new_root_node = self._delete_node(root=root.left, key=key, parent=root)
            if is_deleted:
                return is_deleted, new_root_node
            del new_root_node

        if root.right is not None:
            is_deleted, new_root_node = self._delete_node(root=root.right, key=key, parent=root)
            if is_deleted:
                return is_deleted, new_root_node
            del new_root_node

        return False, None

    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if root is None:
            return None
        else:
            if (root.left is None) and (root.right is None):
                if root.val == key:
                    return None
                else:
                    return root
            else:
                is_deleted, new_root_node = self._delete_node(root=root, key=key, parent=None)

                if new_root_node is None:
                    return root
                else:
                    return new_root_node

