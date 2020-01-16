# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def inorder_traveral(self, root, traveral_list):
        if root.left is not None:
            traveral_list = self.inorder_traveral(root=root.left, traveral_list=traveral_list)

        traveral_list.append(root.val)

        if root.right is not None:
            traveral_list = self.inorder_traveral(root=root.right, traveral_list=traveral_list)

        return traveral_list

    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        sorted_values = self.inorder_traveral(root=root, traveral_list=[])
        num_values = len(sorted_values)

        if num_values == 1:
            return sorted_values[0]

        for curr_idx, curr_val in enumerate(sorted_values):
            if target <= curr_val:
                return curr_val
            else:
                assert target > curr_val
                # last index
                if curr_idx == (num_values-1):
                    return curr_val
                elif target < sorted_values[curr_idx+1]:
                    left_diff = target-curr_val
                    right_diff = sorted_values[curr_idx+1]-target
                    if left_diff < right_diff:
                        return curr_val
                    else:
                        return sorted_values[curr_idx+1]
