class Solution(object):

    def median_of_sorted_list(self, nums, n):
        min_median_idx = int((n - 1) / 2)
        if (n % 2) == 1:
            median = nums[min_median_idx]
            return median, min_median_idx, None
        else:
            max_median_idx = min_median_idx+1
            median = (nums[min_median_idx]+nums[max_median_idx])/2
            return median, min_median_idx, max_median_idx

    def medians_of_two_sorted_arrs(self, nums1, nums2, n1, n2):
        median1, min_median_idx1, max_median_idx1 = self.median_of_sorted_list(nums=nums1, n=n1)
        print(median1, min_median_idx1, max_median_idx1)
        assert min_median_idx1 is not None

        median2, min_median_idx2, max_median_idx2 = self.median_of_sorted_list(nums=nums2, n=n2)
        print(median2, min_median_idx2, max_median_idx2)
        assert min_median_idx2 is not None

        if median1 == median2:
            return median1, None, median2, None
        elif median1 < median2:
            median1_idx = min_median_idx1
            del min_median_idx1, max_median_idx1

            if max_median_idx2 is not None:
                median2_idx = max_median_idx2
            else:
                median2_idx = min_median_idx2
            median2 = nums2[median2_idx]
            del min_median_idx2, max_median_idx2
        else:
            assert median1 > median2
            median2_idx = min_median_idx2
            del min_median_idx2, max_median_idx2

            if max_median_idx1 is not None:
                median1_idx = max_median_idx1
            else:
                median1_idx = min_median_idx1
            median1 = nums1[median1]
            del min_median_idx1, max_median_idx1

        print(median1, median1_idx, median2, median2_idx)

        return median1, median1_idx, median2, median2_idx

    def binary_search(self, arr, val, size):
        start_idx = 0
        end_idx = size-1

        while start_idx != end_idx:
            if arr[start_idx] == val:
                return start_idx
            elif arr[end_idx] == val:
                return end_idx
            else:
                mid_idx = int((start_idx+end_idx)/2)
                mid_val = arr[mid_idx]
                if val > mid_val:
                    start_idx = mid_idx
                elif val < mid_val:
                    end_idx = mid_idx
                else:
                    assert val == mid_val
                    return mid_idx
        assert arr[start_idx] == arr[end_idx]
        if arr[start_idx] != val:
            return None

    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        n1 = len(nums1)
        n2 = len(nums2)
        n = n1+n2
        median1, median1_idx, median2, median2_idx = self.medians_of_two_sorted_arrs(
            nums1=nums1, nums2=nums2, n1=n1, n2=n2,
        )
        if median1 == median2:
            return median1

        req_num_items_around_median = int((n - 1) / 2)

        while True:

            if median1 == median2:
                count_around_median1 = median1_idx+median2_idx
                # count_around_median2 = count_around_median1
                if count_around_median1 == req_num_items_around_median:
                    return median1
            else:
                # if median1 is the median of two arrays
                if median1 < median2:
                    idx_in_num2_for_median1 = self.binary_search(
                        arr=nums2[:median2_idx], val=median1, size=median2_idx,
                    )
                    assert idx_in_num2_for_median1 is not None
                    print(idx_in_num2_for_median1)

                    gap2 = median2_idx - idx_in_num2_for_median1
                else:
                    assert median1 > median2
                    idx_in_num2_for_median1 = self.binary_search(
                        arr=nums2[median2_idx:], val=median1, size=(n2-median2_idx),
                    )
                    assert idx_in_num2_for_median1 is not None
                    idx_in_num2_for_median1 += median2_idx
                    print(idx_in_num2_for_median1)

                    gap2 = idx_in_num2_for_median1 - median2_idx

                count_around_median1 = median1_idx + idx_in_num2_for_median1
                del idx_in_num2_for_median1
                if count_around_median1 == req_num_items_around_median:
                    return median1

                # median2 is the median of two arrays
                if median1 < median2:
                    idx_in_num1_for_median2 = self.binary_search(
                        arr=nums1[median1_idx:], val=median2, size=(n1-median1_idx),
                    )
                    assert idx_in_num1_for_median2 is not None
                    idx_in_num1_for_median2 += median1_idx
                    print(idx_in_num1_for_median2)

                    gap1 = idx_in_num1_for_median2 - median1_idx
                else:
                    idx_in_num1_for_median2 = self.binary_search(
                        arr=nums1[:median1_idx], val=median2, size=median1_idx,
                    )
                    assert idx_in_num1_for_median2 is not None
                    print(idx_in_num1_for_median2)

                    gap1 = median1_idx - idx_in_num1_for_median2
                count_around_median2 = idx_in_num1_for_median2 + median2_idx
                del idx_in_num1_for_median2
                if count_around_median2 == req_num_items_around_median:
                    return median2

                print(gap1, gap2)

                if median1 < median2:
                    assert count_around_median1 < req_num_items_around_median < count_around_median2
                    if gap1 < gap2:
                        median1_idx += 1
                    else:
                        median2_idx -= 1
                elif median1 > median2:
                    assert count_around_median1 > req_num_items_around_median > count_around_median2
                    if gap1 < gap2:
                        median1_idx -= 1
                    else:
                        median2_idx += 1
                else:
                    raise AssertionError

                median1 = nums1[median1_idx]
                median2 = nums2[median2_idx]
