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

    def max_depth_recursion(self):
        if self.is_leaf_node():
            return 1
        else:
            # left child
            if self._left is not None:
                left_subtree_depth = self._left.max_depth_recursion()
            else:
                left_subtree_depth = 0

            # right child
            if self._right is not None:
                right_subtree_depth = self._right.max_depth_recursion()
            else:
                right_subtree_depth = 0

            return max(left_subtree_depth, right_subtree_depth)+1

    def path_sums_recursion(self, path_sum, sum=0):
        sum += self.value

        if self.is_leaf_node():
            if sum == path_sum:
                return True
            else:
                return False
        else:
            # left child
            if (self._left is not None) and (not self._left.is_visited):
                is_path_sum_match_left_subtree = self._left.path_sums_recursion(path_sum=path_sum, sum=sum)
            else:
                is_path_sum_match_left_subtree = False

            # right child
            if (self._right is not None) and (not self._right.is_visited):
                is_path_sum_match_right_subtree = self._right.path_sums_recursion(path_sum=path_sum, sum=sum)
            else:
                is_path_sum_match_right_subtree = False

            return is_path_sum_match_left_subtree | is_path_sum_match_right_subtree

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

    @staticmethod
    def split_inorder_into_left_and_right_subtree_elements(inorder_elements, root_element):
        # assume unique elements
        root_in_inorder_idx = np.where(inorder_elements == root_element)[0]
        assert root_in_inorder_idx.size == 1
        root_in_inorder_idx = root_in_inorder_idx[0]
        left_subtree_elements = inorder_elements[:root_in_inorder_idx]
        right_subtree_elements = inorder_elements[root_in_inorder_idx+1:]
        return left_subtree_elements, right_subtree_elements

    @staticmethod
    def select_subset_of_elements_from_array_keeping_order(ordered_arr, elements_to_select):
        assert ordered_arr.dtype == elements_to_select.dtype
        ordered_indices_of_elements = np.zeros(elements_to_select.size, ordered_arr.dtype)
        count_idx = 0
        for curr_idx, curr_element in enumerate(ordered_arr):
            if curr_element in elements_to_select:
                ordered_indices_of_elements[count_idx] = curr_element
                count_idx += 1
        return ordered_indices_of_elements

    @staticmethod
    def construct_binary_tree_from_inorder_and_postorder_traversal(inorder_elements, postorder_elements):
        # assume unique elements
        num_elements = inorder_elements.size
        assert num_elements == postorder_elements.size
        assert np.unique(inorder_elements).size == num_elements
        assert np.unique(postorder_elements).size == num_elements

        if num_elements == 0:
            return None
        else:
            root_element = postorder_elements[-1]
            inorder_left_subtree_elements, inorder_right_subtree_elements = \
                TreeNode.split_inorder_into_left_and_right_subtree_elements(
                    inorder_elements=inorder_elements,
                    root_element=root_element,
            )
            postorder_left_subtree_elements = TreeNode.select_subset_of_elements_from_array_keeping_order(
                ordered_arr=postorder_elements,
                elements_to_select=inorder_left_subtree_elements,
            )
            postorder_right_subtree_elements = TreeNode.select_subset_of_elements_from_array_keeping_order(
                ordered_arr=postorder_elements,
                elements_to_select=inorder_right_subtree_elements,
            )
            root_node = TreeNode(value=root_element)
            root_node._left = TreeNode.construct_binary_tree_from_inorder_and_postorder_traversal(
                inorder_elements=inorder_left_subtree_elements,
                postorder_elements=postorder_left_subtree_elements,
            )
            root_node._right = TreeNode.construct_binary_tree_from_inorder_and_postorder_traversal(
                inorder_elements=inorder_right_subtree_elements,
                postorder_elements=postorder_right_subtree_elements,
            )
            return root_node

    @staticmethod
    def construct_binary_tree_from_inorder_and_preorder_traversal(inorder_elements, preorder_elements):
        # assume unique elements
        num_elements = inorder_elements.size
        assert num_elements == preorder_elements.size
        assert np.unique(inorder_elements).size == num_elements
        assert np.unique(preorder_elements).size == num_elements

        if num_elements == 0:
            return None
        else:
            root_element = preorder_elements[0]
            inorder_left_subtree_elements, inorder_right_subtree_elements = \
                TreeNode.split_inorder_into_left_and_right_subtree_elements(
                    inorder_elements=inorder_elements,
                    root_element=root_element,
            )
            preorder_left_subtree_elements = TreeNode.select_subset_of_elements_from_array_keeping_order(
                ordered_arr=preorder_elements,
                elements_to_select=inorder_left_subtree_elements,
            )
            preorder_right_subtree_elements = TreeNode.select_subset_of_elements_from_array_keeping_order(
                ordered_arr=preorder_elements,
                elements_to_select=inorder_right_subtree_elements,
            )
            root_node = TreeNode(value=root_element)
            root_node._left = TreeNode.construct_binary_tree_from_inorder_and_preorder_traversal(
                inorder_elements=inorder_left_subtree_elements,
                preorder_elements=preorder_left_subtree_elements,
            )
            root_node._right = TreeNode.construct_binary_tree_from_inorder_and_preorder_traversal(
                inorder_elements=inorder_right_subtree_elements,
                preorder_elements=preorder_right_subtree_elements,
            )
            return root_node


class BinaryTree:

    def __init__(self):
        self._root = None

    def construct_from_inorder_and_postorder(self, inorder_elements, postorder_elements):
        self._root = TreeNode.construct_binary_tree_from_inorder_and_postorder_traversal(
            inorder_elements=inorder_elements,
            postorder_elements=postorder_elements,
        )

    def construct_from_inorder_and_preorder(self, inorder_elements, preorder_elements):
        self._root = TreeNode.construct_binary_tree_from_inorder_and_preorder_traversal(
            inorder_elements=inorder_elements,
            preorder_elements=preorder_elements,
        )

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

    def _mirror_image(self, node1, node2):
        if (node1 is not None) and (node2 is not None):
            if node2.value != node2.value:
                return False
            else:
                return self._mirror_image(node1._right, node2._left) & self._mirror_image(node1._left, node2._right)
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
                return self._mirror_image(root_node._left, root_node._right)

    def max_depth(self):
        if self._root is None:
            return 0
        else:
            return self._root.max_depth_recursion()

    def path_sums_recursion(self, path_sum):
        if self._root is None:
            if path_sum == 0:
                return True
            else:
                return False
        else:
            return self._root.path_sums_recursion(path_sum=path_sum)

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
    # traversal and maximum depth
    inputs = np.array(['F', 'B', 'G', 'A', 'D', 'I', 'C', 'E', 'H'])
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
    max_depth = binary_tree_obj.max_depth()
    print('max_depth', max_depth)

    # max depth
    inputs = np.array([5, 4, 8, 11, 13, 4, 7, 2, 1])
    binary_tree_obj = BinaryTree()
    binary_tree_obj.construct_binary_tree(inputs=inputs)
    max_depth = binary_tree_obj.max_depth()
    print('max_depth', max_depth)

    # path length
    for path_length in [16, 1, 37, 2, 5, 23]:
        is_path_length_match = binary_tree_obj.path_sums_recursion(path_sum=path_length)
        print('is_path_length_match: {}, {}'.format(path_length, is_path_length_match))
    binary_tree_obj.construct_binary_tree_for_symmetry_and_test()

    # construct binary tree from inorder and postorder traversal
    # inorder_elements = np.array([9, 3, 15, 20, 7])
    # postorder_elements = np.array([9, 15, 7, 20, 3])
    inorder_elements = np.array([9, 5, 1, 7, 2, 12, 8, 4, 3, 11])
    postorder_elements = np.array([9, 1, 2, 12, 7, 5, 3, 11, 4, 8])
    binary_tree_obj = BinaryTree()
    binary_tree_obj.construct_from_inorder_and_postorder(
        inorder_elements=inorder_elements,
        postorder_elements=postorder_elements,
    )
    binary_tree_obj.traversal(traveral_type='in_order')
    binary_tree_obj.traversal(traveral_type='post_order')


    # construct binary tree from inorder and postorder traversal
    inorder_elements = np.array([9, 3, 15, 20, 7])
    preorder_elements = np.array([3, 9, 20, 15, 7])
    binary_tree_obj = BinaryTree()
    binary_tree_obj.construct_from_inorder_and_preorder(
        inorder_elements=inorder_elements,
        preorder_elements=preorder_elements,
    )
    binary_tree_obj.traversal(traveral_type='in_order')
    binary_tree_obj.traversal(traveral_type='pre_order')
