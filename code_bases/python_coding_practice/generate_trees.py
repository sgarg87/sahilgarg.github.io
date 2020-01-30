# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def generate_recursive(self, nums, i, j):
        root_nodes_list = []

        # split index
        for k in range(i, j+1):

            if k > i:
                left_subtrees = self.generate_recursive(nums=nums, i=i, j=k-1)
            else:
                left_subtrees = [None]

            if k < j:
                right_subtrees = self.generate_recursive(nums=nums, i=k+1, j=j)
            else:
                right_subtrees = [None]

            for left_node in left_subtrees:
                for right_node in right_subtrees:
                    root_node = TreeNode(nums[k])

                    if left_node is not None:
                        root_node.left = left_node

                    if right_node is not None:
                        root_node.right = right_node

                    root_nodes_list.append(root_node)

        return root_nodes_list

    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        nums = range(1, n+1)
        root_nodes = self.generate_recursive(nums=nums, i=0, j=n-1)
        return root_nodes

