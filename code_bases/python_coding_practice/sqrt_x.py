import math


class Solution(object):
    def invalid_sol(self, x):
        sqrt_val = math.sqrt(x)
        return int(sqrt_val)

    def binary_search(self, x):
        if x <= 1:
            return x
        elif 2 <= x <= 3:
            return 1
        elif 4 <= x <= 8:
            return 2

        left_val = 2
        right_val = x/2

        # print(left_val, right_val)
        if left_val == right_val:
            return left_val

        while left_val < right_val:
            mid_val = (left_val+right_val)/2
            mid_val_sqr = mid_val**2
            print(left_val, right_val, mid_val)

            if mid_val_sqr > x:
                right_val = mid_val-1
            else:
                if (mid_val+1)**2 <= x:
                    left_val = mid_val+1
                else:
                    return mid_val

        assert left_val == right_val
        return left_val

    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        return self.binary_search(x=x)
