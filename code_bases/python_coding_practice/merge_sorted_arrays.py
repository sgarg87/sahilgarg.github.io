class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        num1_right_ptr = m+n-1
        nums1_left_ptr = m-1
        nums2_right_ptr = n-1

        while nums2_right_ptr >= 0:
            curr_val_for_store = nums2[nums2_right_ptr]

            if (nums1_left_ptr < 0) or (curr_val_for_store > nums1[nums1_left_ptr]):
                nums1[num1_right_ptr] = curr_val_for_store
                nums2_right_ptr -= 1
                num1_right_ptr -= 1
            else:
                nums1[num1_right_ptr] = nums1[nums1_left_ptr]
                nums1_left_ptr -= 1
                num1_right_ptr -= 1

