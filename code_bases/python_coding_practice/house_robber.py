class Solution(object):
    def __init__(self):
        self.dp_len_vals_map = {}

    def dynamic_program(self, nums, n):
        assert nums
        if n not in self.dp_len_vals_map:
            if n == 1:
                self.dp_len_vals_map[n] = nums[0]
            elif n == 2:
                self.dp_len_vals_map[n] = max(nums[0], nums[1])
            else:
                dp_n_min_2 = self.dynamic_program(nums=nums[:-2], n=n-2)
                self.dp_len_vals_map[n-2] = dp_n_min_2

                dp_n_min_1 = self.dynamic_program(nums=nums[:-1], n=n-1)
                self.dp_len_vals_map[n-1] = dp_n_min_1

                self.dp_len_vals_map[n] = max(dp_n_min_1, (dp_n_min_2+nums[-1]))

        return self.dp_len_vals_map[n]

    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        n = len(nums)
        return self.dynamic_program(nums=nums, n=n)
