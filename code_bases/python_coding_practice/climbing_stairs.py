import math


class Solution(object):
    # def _init_count(self):
    #     self.count = 0
    #
    # def dfs(self, curr_sum, n):
    #     if curr_sum == n:
    #         self.count += 1
    #         return
    #     else:
    #         if (curr_sum+1) <= n:
    #             self.dfs(curr_sum=curr_sum+1, n=n)
    #         else:
    #             return
    #         if (curr_sum+2) <= n:
    #             self.dfs(curr_sum=curr_sum+2, n=n)

    def bfs(self, n):
        queue = [0]
        count = 0

        while queue:
            curr_sum = queue.pop(0)
            if curr_sum == n:
                count += 1

            if (curr_sum+1) <= n:
                queue.append(curr_sum+1)
            else:
                continue

            if (curr_sum+2) <= n:
                queue.append(curr_sum+2)
            else:
                continue

        return count

    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # self._init_count()
        # self.dfs(curr_sum=0, n=n)
        # return self.count
        count = 0
        for num_of_one_steps in range(n+1):
            complement_n = n-num_of_one_steps
            assert complement_n >= 0
            if (complement_n % 2) == 0:
                num_two_steps = complement_n/2
                curr_count = \
                    math.factorial(num_of_one_steps+num_two_steps)/(math.factorial(num_of_one_steps)*math.factorial(num_two_steps))
                count += curr_count

        return count

