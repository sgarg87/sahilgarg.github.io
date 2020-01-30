class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        sum_count_map = {}
        count = 0

        s = 0
        sum_count_map[0] = 1
        for i in range(n):
            s += nums[i]

            if (s-k) in sum_count_map:
                count += sum_count_map[s-k]

            if s not in sum_count_map:
                sum_count_map[s] = 0
            sum_count_map[s] += 1

        return count

