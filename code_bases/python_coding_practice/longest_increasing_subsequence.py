class Solution(object):
    def dynamic_program(self, nums, i, memory):
        if i in memory:
            # print(i, memory[i])
            return memory[i]

        # including oneself
        max_len = 1
        for j in range(i):
            if nums[i] > nums[j]:
                max_len = max(max_len, self.dynamic_program(nums=nums, i=j, memory=memory)+1)

        print(i, max_len)
        memory[i] = max_len

        return max_len

    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        n = len(nums)
        memory = {}
        for i in range(n):
            self.dynamic_program(nums=nums, i=i, memory=memory)
        return max(memory.values())
