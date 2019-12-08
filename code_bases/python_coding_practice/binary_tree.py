import numpy as np


class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self._left = left
        self._right = right

    def find_position_for_element(self, element):
        assert element is not None
        if element <= self.value:
            if self._left is not None:
                return self._left.find_position_for_element(element)
            else:
                return self, 0
        else:
            if self._right is not None:
                return self._right.find_position_for_element(element)
            else:
                return self, 1

    def add_child(self, position, element):
        child_node = TreeNode(value=element)

        if position == 0:
            # left position
            self._left = child_node
        elif position == 1:
            # right position
            self._right = child_node
        else:
            raise NotImplementedError

        del position, child_node

    def preorder_traversal(self):
        # node
        print(self.value),
        # left child
        if self._left is not None:
            self._left.preorder_traversal()
        # right child
        if self._right is not None:
            self._right.preorder_traversal()

    def inorder_traversal(self):
        # left child
        if self._left is not None:
            self._left.inorder_traversal()
        # node
        print(self.value),
        # right child
        if self._right is not None:
            self._right.inorder_traversal()

    def postorder_traversal(self):
        # left child
        if self._left is not None:
            self._left.postorder_traversal()
        # right child
        if self._right is not None:
            self._right.postorder_traversal()
        # node
        print(self.value),


class BinaryTree:

    def __init__(self):
        self._root = None

    def add_element(self, element):
        if self._root is None:
            print('Adding {} as a root node.'.format(element))
            self._root = TreeNode(element, left=None, right=None)
        else:
            parent_node, position = self._root.find_position_for_element(element=element)
            print('Adding {} as a {} child to {}.'.format(element, position, parent_node.value))
            parent_node.add_child(position=position, element=element)

    def construct_binary_tree(self, inputs):
        print('........Construction of Tree .......')
        for curr_idx, curr_input in enumerate(inputs):
            self.add_element(curr_input)
        print('')

    def traversal(self, traveral_type):
        if self._root is not None:
            if traveral_type == 'pre_order':
                print('.......Pre-order traversal........')
                self._root.preorder_traversal()
                print('')
            elif traveral_type == 'in_order':
                print('.......In-order traversal........')
                self._root.inorder_traversal()
                print('')
            elif traveral_type == 'post_order':
                print('........Post-order traversal.......')
                self._root.postorder_traversal()
                print('')
            else:
                raise AssertionError
        else:
            print('Empty Tree.')


if __name__ == '__main__':
    inputs = np.array(['F', 'B', 'G', 'A', 'D', 'I', 'C', 'E', 'H'])
    binary_tree_obj = BinaryTree()
    binary_tree_obj.construct_binary_tree(inputs=inputs)
    binary_tree_obj.traversal(traveral_type='pre_order')
    binary_tree_obj.traversal(traveral_type='in_order')
    binary_tree_obj.traversal(traveral_type='post_order')
