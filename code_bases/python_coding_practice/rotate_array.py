class Solution(object):
    def reverse(self, nums, i, j):
        print('..........')
        while i < j:
            print(i, j)
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp
            i += 1
            j -= 1

    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n

        if (k > 0) and (n > 1):
            assert k < n

            self.reverse(nums=nums, i=0, j=n-1)

            self.reverse(nums=nums, i=0, j=k-1)

            self.reverse(nums=nums, i=k, j=n-1)
