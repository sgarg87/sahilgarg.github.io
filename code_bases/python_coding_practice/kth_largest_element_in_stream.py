import heapq


class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k = k

        self.nums = nums
        heapq.heapify(self.nums)
        while len(self.nums) > self.k:
            heapq.heappop(self.nums)
        assert len(self.nums) <= self.k, len(self.nums)

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        if len(self.nums) < self.k:
            heapq.heappush(self.nums, val)
            return self.nums[0]
        else:
            if val <= self.nums[0]:
                return self.nums[0]
            else:
                heapq.heappop(self.nums)
                heapq.heappush(self.nums, val)
                return self.nums[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
