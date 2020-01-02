class Solution(object):

    def _init_max_sum_map(self):
        self.max_sum_map = {}

    def max_subarray(self, nums, n, left_idx, right_idx, sum):
        max_sum = sum

        # move right
        if right_idx < n:
            curr_right_tuple = (left_idx, right_idx+1)
            if curr_right_tuple not in self.max_sum_map:
                curr_right_sum = sum+nums[right_idx]
                self.max_sum_map[curr_right_tuple] = curr_right_sum
            else:
                curr_right_sum = self.max_sum_map[curr_right_tuple]
            del curr_right_tuple
            right_sum = self.max_subarray(
                nums=nums, n=n,
                left_idx=left_idx,
                right_idx=right_idx+1,
                sum=curr_right_sum,
            )
            del curr_right_sum
            max_sum = max(max_sum, right_sum)
            del right_sum

        if left_idx < (right_idx-1):
            curr_left_tuple = (left_idx+1, right_idx)
            if curr_left_tuple not in self.max_sum_map:
                curr_left_sum = sum-nums[left_idx]
                self.max_sum_map[curr_left_tuple] = curr_left_sum
            else:
                curr_left_sum = self.max_sum_map[curr_left_tuple]
            del curr_left_tuple
            left_sum = self.max_subarray(
                nums=nums, n=n,
                left_idx=left_idx+1,
                right_idx=right_idx,
                sum=curr_left_sum,
            )
            del curr_left_sum
            max_sum = max(max_sum, left_sum)
            del left_sum

        return max_sum

    def greedy_algo(self, nums):
        n = len(nums)
        curr_sum = max_sum = nums[0]

        for i in range(1, n):
            curr_sum = max(nums[i], curr_sum + nums[i])
            max_sum = max(max_sum, curr_sum)

        return max_sum

    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        left_idx = 0
        right_idx = 1
        sum = nums[0]

        if not nums:
            return 0

        return self.greedy_algo(nums=nums)

        # self._init_max_sum_map()
        # max_sum = self.max_subarray(
        #     nums=nums, n=n,
        #     left_idx=left_idx,
        #     right_idx=right_idx,
        #     sum=sum,
        # )
        # return max_sum



