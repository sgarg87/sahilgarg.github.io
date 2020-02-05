import math


class Solution(object):
    def dynamic_program(self, x, square_choices, memory):
        if x == 0:
            return 0

        if x in memory:
            return memory[x]

        min_count = None
        for curr_sqr in reversed(square_choices):
            if curr_sqr > x:
                continue

            curr_count = self.dynamic_program(
                x=(x-curr_sqr),
                square_choices=square_choices,
                memory=memory,
            )
            if curr_count is not None:
                if min_count is None:
                    min_count = curr_count
                else:
                    min_count = min(min_count, curr_count)

        if min_count is None:
            return None
        else:
            min_count += 1
            memory[x] = min_count
            return min_count

    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        sqrt_n = int(math.sqrt(n))
        square_choices = [x**2 for x in xrange(1, sqrt_n+1)]
        memory = {}
        return self.dynamic_program(x=n, square_choices=square_choices, memory=memory)
