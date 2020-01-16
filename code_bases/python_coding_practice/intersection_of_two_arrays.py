class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if (not nums1) or (not nums2):
            return []

        len_num1 = len(nums1)
        len_num2 = len(nums2)

        # assuming num1 is smaller in length
        if len_num1 > len_num2:
            temp = nums1
            nums1 = nums2
            nums2 = temp
            del temp

        nums1_set = set(nums1)
        intersection = set()
        for curr_val in nums2:
            if (curr_val in nums1_set) and (curr_val not in intersection):
                intersection.add(curr_val)

        return list(intersection)
