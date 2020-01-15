class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        even_sum = sum(nums[0:n:2])
        odd_sum = sum(nums[1:n:2])
        return max(even_sum, odd_sum)
