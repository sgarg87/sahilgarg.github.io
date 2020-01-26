import heapq


class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        n = len(nums)
        if n < k:
            return [max(nums)]

        window = list()
        for curr_idx in range(k):
            heapq.heappush(window, -nums[curr_idx])

        max_of_windows = []
        curr_idx = k
        while curr_idx < n:
            max_of_windows.append(-window[0])
            old_val = nums[curr_idx-k]
            new_val = nums[curr_idx]
            heapq.he

            heapq.heapreplace(window, -new_val)
            curr_idx += 1

