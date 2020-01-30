class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        n = len(nums)
        i = 0
        max_len = 1
        for j in range(1, n):
            if nums[j] <= nums[j-1]:
                max_len = max(max_len, (j - i))
                i = j
            print(i, j)

        max_len = max(max_len, (n-i))

        return max_len
