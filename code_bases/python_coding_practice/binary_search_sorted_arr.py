class Solution(object):

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

