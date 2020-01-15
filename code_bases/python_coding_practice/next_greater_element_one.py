class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        num2_len = len(nums2)

        nums1_set = set(nums1)
        nums1_idx_in_num2 = {}
        for curr_idx, x in enumerate(nums2):
            if x in nums1_set:
                nums1_idx_in_num2[x] = curr_idx

        output = []
        for x in nums1:
            assert x in nums1_idx_in_num2
            idx_of_x_in_nums2 = nums1_idx_in_num2[x]
            is_found = False
            for curr_idx in range(idx_of_x_in_nums2+1, num2_len):
                curr_val = nums2[curr_idx]
                if curr_val > x:
                    output.append(curr_val)
                    is_found = True
                    break
            if not is_found:
                output.append(-1)

        return output
