import math


class Solution(object):

    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        for num_of_one_steps in range(n + 1):
            complement_n = n - num_of_one_steps
            assert complement_n >= 0
            if (complement_n % 2) == 0:
                num_two_steps = complement_n / 2
                curr_count = \
                    math.factorial(num_of_one_steps + num_two_steps) / (
                                math.factorial(num_of_one_steps) * math.factorial(num_two_steps))
                count += curr_count

        return count

