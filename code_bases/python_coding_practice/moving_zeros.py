class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        nums_len = len(nums)
        left_most_zero_idx = -1
        curr_idx = 0
        while curr_idx < nums_len:
            print('....................')
            print(left_most_zero_idx, curr_idx)
            curr_val = nums[curr_idx]
            if (left_most_zero_idx == -1) and (curr_val == 0):
                left_most_zero_idx = curr_idx
                curr_idx += 1
                continue
            elif left_most_zero_idx == -1:
                curr_idx += 1
            else:
                if curr_val != 0:
                    nums[left_most_zero_idx] = curr_val
                    nums[curr_idx] = 0
                    left_most_zero_idx += 1
                    curr_idx += 1
                else:
                    curr_idx += 1
            # print(nums[:curr_idx])

