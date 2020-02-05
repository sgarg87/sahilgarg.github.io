class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)

        i = n-1
        while i > 0:
            is_jump = False
            for j in range(i-1, -1, -1):
                if nums[j] >= (i-j):
                    is_jump = True
                    i = j
                    break
            if not is_jump:
                return False
        return True
