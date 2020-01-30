class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        n = len(nums)
        self.nums = nums
        # self.total_sum = sum(nums)
        left_sums = [0]*n
        curr_sum = 0
        for i in range(n):
            curr_sum += nums[i]
            left_sums[i] = curr_sum
        del curr_sum
        self.left_sums = left_sums

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        sum = self.left_sums[j]
        if i > 0:
            sum -= self.left_sums[i-1]
        return sum

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
