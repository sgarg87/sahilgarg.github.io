class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        len_nums = len(nums)
        assert len_nums >= 3

        max_val = max(nums)
        nums.remove(max_val)
        second_max_val = max(nums)
        nums.remove(second_max_val)
        third_max_val = max(nums)

        return max_val*second_max_val*third_max_val

