import copy
import random


class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.org_nums = nums
        self.nums = copy.copy(nums)
        self.n = len(nums)
        self.idx = range(self.n)

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        self.nums = copy.copy(self.org_nums)
        return self.nums

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        for i in self.idx:
            j = random.choice(self.idx[i:])
            if i != j:
                temp = self.nums[i]
                self.nums[i] = self.nums[j]
                self.nums[j] = temp
                del temp

        return self.nums


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()