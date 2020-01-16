class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums_set = set()
        for curr_num in nums:
            if curr_num in nums_set:
                return True
            else:
                nums_set.add(curr_num)
        return False

