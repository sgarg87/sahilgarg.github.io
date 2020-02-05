class Solution(object):
    def backtrack(self, nums, n, i, subset, all_subsets):
        for j in xrange(i, n+1):
            if j == n:
                all_subsets.append(list(subset))
                return
            else:
                x = nums[j]
                subset.add(x)
                self.backtrack(nums=nums, n=n, i=j+1, subset=subset, all_subsets=all_subsets)
                subset.remove(x)

    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        all_subsets = list()
        subset = set()
        self.backtrack(nums=nums, n=n, i=0, subset=subset, all_subsets=all_subsets)
        return all_subsets
