class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        final = 0
        for curr_num in nums:
            # xor
            final ^= curr_num
        return final
