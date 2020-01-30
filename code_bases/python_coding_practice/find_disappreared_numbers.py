class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        for x in nums:
            abs_x = abs(x)
            if nums[abs_x-1] > 0:
                nums[abs_x-1] *= -1

        print(nums)

        out = []
        for i in range(n):
            if nums[i] > 0:
                out.append(i+1)

        return out
