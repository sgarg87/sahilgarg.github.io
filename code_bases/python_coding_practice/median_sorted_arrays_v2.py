import numpy as np


class Solution(object):

    def median_of_sorted_list(self, nums):
        n = len(nums)
        min_median_idx = int((n - 1) / 2)
        if (n % 2) == 1:
            median = nums[min_median_idx]
            return median
        else:
            max_median_idx = min_median_idx+1
            median = float(nums[min_median_idx]+nums[max_median_idx])/2
            return median

    def find_median_sorted_arrays(self, x, y):
        if (x.size == 1) and (y.size == 1):
            return float(x[0]+y[0])/2

        assert x.size <= y.size
        n = x.size+y.size

        size_left_subsets = int((n+1)/2)
        print('size_left_subsets', size_left_subsets)

        if (n % 2) == 1:
            is_odd_else_even = True
        else:
            is_odd_else_even = False

        # including the index
        x_start_idx = 0
        x_end_idx = x.size-1
        x_split_idx = int((x_start_idx+x_end_idx)/2)
        print(x_start_idx, x_split_idx, x_end_idx)

        while True:

            if x_split_idx is not None:
                y_split_idx = size_left_subsets - (x_split_idx+1) - 1
                if y_split_idx < 0:
                    y_split_idx = None
            else:
                y_split_idx = size_left_subsets-1

            print('..........................')
            print(x_start_idx, x_split_idx, x_end_idx)
            print(x_split_idx, y_split_idx)

            if (x_split_idx is None) and (y_split_idx is None):
                raise AssertionError
            elif (x_split_idx is not None) and (y_split_idx is not None):
                assert 0 <= x_split_idx < x.size
                assert 0 <= y_split_idx < y.size
                if ((y_split_idx+1) < y.size) and (x[x_split_idx] > y[y_split_idx+1]):
                    # move index leftwards of x
                    if x_split_idx == 0:
                        x_split_idx = None
                        x_start_idx = None
                        x_end_idx = None
                    else:
                        x_end_idx = x_split_idx
                        x_split_idx = int((x_start_idx+x_split_idx)/2)
                elif ((x_split_idx+1) < x.size) and (y[y_split_idx] > x[x_split_idx+1]):
                    # move index rightwards of x
                    x_start_idx = x_split_idx
                    x_split_idx = int((x_split_idx+x_end_idx+1)/2)
                else:
                    if is_odd_else_even:
                        return max(x[x_split_idx], y[y_split_idx])
                    else:
                        print(x_split_idx, y_split_idx)
                        if x_split_idx == (x.size-1):
                            return float(max(x[x_split_idx], y[y_split_idx]) + y[y_split_idx+1]) / 2
                        else:
                            return float(max(x[x_split_idx], y[y_split_idx]) + min(x[x_split_idx+1], y[y_split_idx+1]))/2
            elif x_split_idx is None:
                assert 0 <= y_split_idx < y.size
                assert y[y_split_idx] <= x[0]
                if is_odd_else_even:
                    return y[y_split_idx]
                else:
                    if y_split_idx == (y.size-1):
                        return float(y[y_split_idx] + x[0]) / 2
                    else:
                        return float(y[y_split_idx] + min(x[0], y[y_split_idx+1])) / 2
            elif y_split_idx is None:
                # assert 0 <= x_split_idx < x.size
                assert x_split_idx == (x.size-1)
                assert x[x_split_idx] <= y[0]
                print(is_odd_else_even)
                if is_odd_else_even:
                    return x[x_split_idx]
                else:
                    return float(x[x_split_idx] + y[0]) / 2
            else:
                raise AssertionError

    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if (not nums1) and (not nums2):
            raise AssertionError
        elif not nums1:
            return self.median_of_sorted_list(nums=nums2)
        elif not nums2:
            return self.median_of_sorted_list(nums=nums1)
        else:
            nums1 = np.array(nums1)
            nums2 = np.array(nums2)

            if nums1.size <= nums2.size:
                return self.find_median_sorted_arrays(x=nums1, y=nums2)
            else:
                return self.find_median_sorted_arrays(x=nums2, y=nums1)
