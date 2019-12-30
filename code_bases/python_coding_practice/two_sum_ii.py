class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not numbers:
            return None, None

        num_numbers = len(numbers)
        left_idx = 0
        right_idx = num_numbers-1

        while left_idx < right_idx:
            assert left_idx != right_idx
            curr_sum = numbers[left_idx] + numbers[right_idx]

            if curr_sum == target:
                return left_idx+1, right_idx+1
            elif curr_sum < target:
                left_idx += 1
            elif curr_sum > target:
                right_idx -= 1
            else:
                raise AssertionError

        return None, None
