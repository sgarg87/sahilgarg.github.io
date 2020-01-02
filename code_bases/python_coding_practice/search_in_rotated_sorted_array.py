class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1

        n = len(nums)
        left_idx = 0
        right_idx = n-1

        while True:
            mid_idx = int((left_idx+right_idx)/2)

            print(left_idx, mid_idx, right_idx)

            # boundary scenarios
            if nums[left_idx] == target:
                return left_idx
            elif nums[right_idx] == target:
                return right_idx
            elif nums[mid_idx] == target:
                return mid_idx
            elif left_idx == right_idx:
                return -1
            elif (right_idx-left_idx) == 1:
                assert mid_idx in [left_idx, right_idx]
                return -1
            else:
                if nums[mid_idx] <= nums[right_idx]:
                    is_right_arr_consistent = True
                else:
                    is_right_arr_consistent = False

                if nums[mid_idx] >= nums[left_idx]:
                    is_left_arr_consistent = True
                else:
                    is_left_arr_consistent = False

                if (target > nums[mid_idx]) and (target < nums[right_idx]):
                    assert is_right_arr_consistent
                    left_idx = mid_idx
                elif (target > nums[mid_idx]) and (target > nums[right_idx]):
                    if not is_right_arr_consistent:
                        left_idx = mid_idx
                    elif not is_left_arr_consistent:
                        right_idx = mid_idx
                    else:
                        return -1
                elif (target < nums[mid_idx]) and (target > nums[left_idx]):
                    assert is_left_arr_consistent
                    right_idx = mid_idx
                elif (target < nums[mid_idx]) and (target < nums[left_idx]):
                    if not is_left_arr_consistent:
                        right_idx = mid_idx
                    elif not is_right_arr_consistent:
                        left_idx = mid_idx
                    else:
                        return -1
                else:
                    raise AssertionError

