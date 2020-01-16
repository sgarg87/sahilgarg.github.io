# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def _bst(self, nums, n):
        len_nums = len(nums)
        mid_idx = n/2

        root_node = TreeNode(x=nums[mid_idx])
        if mid_idx > 0:
            root_node.left = self._bst(nums=nums[:mid_idx], n=mid_idx)

        if mid_idx < (len_nums-1):
            root_node.right = self._bst(nums=nums[mid_idx+1:], n=(n-mid_idx-1))

        return root_node

    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None

        n = len(nums)

        return self._bst(nums=nums, n=n)
