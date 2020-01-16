class Solution(object):

    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        total_sum = (n*(n+1))/2
        curr_sum = sum(nums)
        return total_sum-curr_sum
