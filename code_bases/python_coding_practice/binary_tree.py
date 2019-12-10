import numpy as np
import queue
import stack


class TreeNode:
    def __init__(self, value, left=None, right=None, is_root=False):
        self.value = value
        self._left = left
        self._right = right
        self.is_root = is_root
        self.is_visited = False

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

    def is_leaf_node(self):
        if (self._left is None) and (self._right is None):
            return True
        else:
            return False

    def depth_first_traverse_recursion(self):
        assert not self.is_visited
        self.is_visited = True

        depth = 0

        # left child
        if (self._left is not None) and (not self._left.is_visited):
            left_subtree_depth = self._left.depth_first_traverse_recursion()
            depth = max(depth, left_subtree_depth)

        # right child
        if (self._right is not None) and (not self._right.is_visited):
            right_subtree_depth = self._right.depth_first_traverse_recursion()
            depth = max(depth, right_subtree_depth)

        # node itself
        print(self.value),
        self.is_visited = False
        depth += 1

        return depth

    def depth_first_traverse(self):
        traversed_nodes = []
        max_depth = 0

        stack_obj = stack.Stack()
        assert not self.is_visited
        self.is_visited = True
        stack_obj.push(self)
        max_depth = max(max_depth, stack_obj.depth)

        while not stack_obj.is_empty():
            curr_node = stack_obj.peek()
            # print('Peeked {}.'.format(curr_node.value))
            assert curr_node is not None

            is_leaf_node_pushed = False
            if not curr_node.is_leaf_node():
                if (curr_node._left is not None) and (not curr_node._left.is_visited):
                    curr_node._left.is_visited = True
                    stack_obj.push(curr_node._left)
                    # print('Pushing left {}.'.format(curr_node._left.value))
                    is_leaf_node_pushed = True
                    max_depth = max(stack_obj.depth, max_depth)
                elif (curr_node._right is not None) and (not curr_node._right.is_visited):
                    curr_node._right.is_visited = True
                    stack_obj.push(curr_node._right)
                    # print('Pushing right {}.'.format(curr_node._right.value))
                    is_leaf_node_pushed = True
                    max_depth = max(stack_obj.depth, max_depth)

            if not is_leaf_node_pushed:
                curr_node = stack_obj.pop()
                traversed_nodes.append(curr_node)
                # print('Popping {}.'.format(curr_node.value))

        for curr_node in traversed_nodes:
            curr_node.is_visited = False
            print(curr_node.value),
        print('')

        print(max_depth)

        return traversed_nodes, max_depth


class BinaryTree:

    def __init__(self):
        self._root = None

    def add_element(self, element):
        if self._root is None:
            print('Adding {} as a root node.'.format(element))
            self._root = TreeNode(element, left=None, right=None, is_root=True)
        else:
            parent_node, position = self._root.find_position_for_element(element=element)
            print('Adding {} as a {} child to {}.'.format(element, position, parent_node.value))
            parent_node.add_child(position=position, element=element)

    def construct_binary_tree(self, inputs):
        print('........Construction of Tree .......')
        for curr_idx, curr_input in enumerate(inputs):
            self.add_element(curr_input)
        print('')

    def breadth_first_traversal(self):
        if self._root is None:
            print('Tree is empty.')
        else:
            queue_obj = queue.Queue()
            queue_obj.add_element(self._root)
            while True:
                curr_node = queue_obj.remove_element()
                if curr_node is None:
                    break
                else:
                    print(curr_node.value),
                    if curr_node._left is not None:
                        queue_obj.add_element(curr_node._left)
                    if curr_node._right is not None:
                        queue_obj.add_element(curr_node._right)

    def depth_first_traveral_recursion(self):
        # using function call stack
        if self._root is None:
            print('Tree is empty.')
        else:
            print('Depth first recursion without stack.')
            max_depth = self._root.depth_first_traverse_recursion()
            print('')
            print(max_depth)

    def match_two_lists_nodes_by_value(self, list1, list2):
        for curr_idx, curr_node_list1 in enumerate(list1):
            curr_node_list2 = list2[curr_idx]
            if curr_node_list1.value != curr_node_list2.value:
                return False
        return True

    def mirror_image(self, node1, node2):
        if (node1 is not None) and (node2 is not None):
            if node2.value != node2.value:
                return False
            else:
                return self.mirror_image(node1._right, node2._left) & self.mirror_image(node1._left, node2._right)
        elif (node1 is None) and (node2 is None):
            return True
        else:
            return False

    def is_symmetric(self):
        print('Is Symmetric?')
        root_node = self._root
        if root_node is None:
            return None
        else:
            if root_node.is_leaf_node():
                return True
            else:
                return self.mirror_image(root_node._left, root_node._right)

    def depth_first_traveral(self):
        if self._root is None:
            print('Tree is empty.')
        else:
            traversed_nodes, max_depth = self._root.depth_first_traverse()

    def construct_binary_tree_for_symmetry_and_test(self):
        self._root = TreeNode(value=1, is_root=True)
        self._root._left = TreeNode(value=2)
        self._root._right = TreeNode(value=2)
        self._root._left._left = TreeNode(value=3)
        self._root._left._right = TreeNode(value=4)
        self._root._right._left = TreeNode(value=4)
        self._root._right._right = TreeNode(value=3)

        is_symmetric = self.is_symmetric()
        print('is_symmetric', is_symmetric)

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
            elif traveral_type == 'breadth_first':
                print('.......Breadth-First traversal........')
                self.breadth_first_traversal()
                print('')
            elif traveral_type == 'depth_first':
                print('.......Depth-First traversal........')
                self.depth_first_traveral()
                print('')
            elif traveral_type == 'depth_first_without_stack':
                print('.......Depth-First traversal........')
                self.depth_first_traveral_recursion()
                print('')
            else:
                raise AssertionError
        else:
            print('Empty Tree.')


if __name__ == '__main__':
    inputs = np.array(['F', 'B', 'G', 'A', 'D', 'I', 'C', 'E', 'H'])
    print('**********************************')
    binary_tree_obj = BinaryTree()
    binary_tree_obj.construct_binary_tree(inputs=inputs)
    binary_tree_obj.traversal(traveral_type='pre_order')
    binary_tree_obj.traversal(traveral_type='in_order')
    binary_tree_obj.traversal(traveral_type='post_order')
    binary_tree_obj.traversal(traveral_type='breadth_first')
    binary_tree_obj.traversal(traveral_type='depth_first')
    binary_tree_obj.traversal(traveral_type='depth_first_without_stack')
    is_symmetric = binary_tree_obj.is_symmetric()
    print('is_symmetric', is_symmetric)
    binary_tree_obj.construct_binary_tree_for_symmetry_and_test()
