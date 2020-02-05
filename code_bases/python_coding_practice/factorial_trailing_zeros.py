class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        else:
            n_div_5 = int(n/5)
            return n_div_5 + self.trailingZeroes(n_div_5)
