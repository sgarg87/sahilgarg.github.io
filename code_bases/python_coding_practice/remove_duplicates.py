class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        n = len(nums)
        i, j = 1, 1
        while j < n:
            if nums[j] > nums[i-1]:
                nums[i] = nums[j]
                i += 1
            j += 1

        return i
