import numpy as np


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def split_inorder_into_left_and_right_subtree_elements(self, inorder_elements, root_element):
        # assume unique elements
        root_in_inorder_idx = np.where(inorder_elements == root_element)[0]
        assert root_in_inorder_idx.size == 1
        root_in_inorder_idx = root_in_inorder_idx[0]
        left_subtree_elements = inorder_elements[:root_in_inorder_idx]
        right_subtree_elements = inorder_elements[root_in_inorder_idx+1:]
        return left_subtree_elements, right_subtree_elements

    def select_subset_of_elements_from_array_keeping_order(self, ordered_arr, elements_to_select):
        assert ordered_arr.dtype == elements_to_select.dtype
        ordered_indices_of_elements = np.zeros(elements_to_select.size, ordered_arr.dtype)

        elements_to_select = set(elements_to_select)

        count_idx = 0
        for curr_idx, curr_element in enumerate(ordered_arr):
            if curr_element in elements_to_select:
                ordered_indices_of_elements[count_idx] = curr_element
                count_idx += 1

        return ordered_indices_of_elements

    def construct_binary_tree_from_inorder_and_postorder_traversal(
        self, inorder_elements, postorder_elements):

        # assume unique elements
        num_elements = inorder_elements.size
        # assert num_elements == postorder_elements.size
        # assert np.unique(inorder_elements).size == num_elements
        # assert np.unique(postorder_elements).size == num_elements

        if num_elements == 0:
            return None
        else:
            root_element = postorder_elements[-1]

            inorder_left_subtree_elements,\
            inorder_right_subtree_elements = self.split_inorder_into_left_and_right_subtree_elements(
                    inorder_elements=inorder_elements,
                    root_element=root_element)

            postorder_left_subtree_elements = self.select_subset_of_elements_from_array_keeping_order(
                ordered_arr=postorder_elements,
                elements_to_select=inorder_left_subtree_elements)

            postorder_right_subtree_elements = self.select_subset_of_elements_from_array_keeping_order(
                ordered_arr=postorder_elements,
                elements_to_select=inorder_right_subtree_elements)

            root_node = TreeNode(root_element)
            root_node.left = self.construct_binary_tree_from_inorder_and_postorder_traversal(
                inorder_elements=inorder_left_subtree_elements,
                postorder_elements=postorder_left_subtree_elements)
            root_node.right = self.construct_binary_tree_from_inorder_and_postorder_traversal(
                inorder_elements=inorder_right_subtree_elements,
                postorder_elements=postorder_right_subtree_elements)

            return root_node

    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """

        inorder = np.array(inorder)
        print(inorder.size)

        postorder = np.array(postorder)
        print(postorder.size)

        root = self.construct_binary_tree_from_inorder_and_postorder_traversal(
            inorder_elements=inorder, postorder_elements=postorder)

        return root
