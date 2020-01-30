class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        num_ones = 0
        while n != 0:
            n_xor_one = (n ^ 1)
            if n_xor_one == (n-1):
                num_ones += 1
            else:
                assert n_xor_one == (n+1)

            n = n >> 1

        return num_ones
