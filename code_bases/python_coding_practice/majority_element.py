class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_len = len(nums)

        start_idx = 0

        for curr_idx in range(nums_len):
            if start_idx == curr_idx:
                majority_element = nums[curr_idx]
                count_majority = 1
            else:
                if nums[curr_idx] == majority_element:
                    count_majority += 1
                else:
                    count_majority -= 1

                    if count_majority == 0:
                        start_idx = curr_idx+1

        return majority_element
