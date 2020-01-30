import copy


class Solution(object):
    def dfs(self, nums, n, i, permutations):
        if i == (n-1):
            permutations.append(copy.copy(nums))

        for j in range(i, n):
            # swap for i and j
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp

            self.dfs(nums=nums, n=n, i=i+1, permutations=permutations)

            # swap for i and j
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        permutations = []
        self.dfs(nums=nums, n=n, i=0, permutations=permutations)
        return permutations
