class Solution(object):
    def binary_search_peak(self, nums, i, j):
        # todo: corner case of j-i = 1
        if i == j:
            return i
        elif (j-i) == 1:
            if nums[i] < nums[j]:
                return j
            else:
                return i

        mid = int((i+j)/2)
        if nums[mid] < nums[mid+1]:
            return self.binary_search_peak(nums=nums, i=mid, j=j)
        else:
            return self.binary_search_peak(nums=nums, i=i, j=mid)

    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        return self.binary_search_peak(nums=nums, i=0, j=(n-1))
