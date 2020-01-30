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

        max_product_of_pos = max_val*second_max_val*third_max_val
        if max_product_of_pos < 0:
            return max_product_of_pos

        if not nums:
            return max_product_of_pos

        min_val = min(nums)
        if min_val > 0:
            return max_product_of_pos
        else:
            nums.remove(min_val)
            if not nums:
                return max_product_of_pos

            second_min_val = min(nums)
            if second_min_val > 0:
                return max_product_of_pos
            else:
                return max(min_val*second_min_val*max_val, max_product_of_pos)

