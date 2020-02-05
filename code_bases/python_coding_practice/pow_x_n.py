import math


class Solution(object):
    def log_exp_sol(self, x, n):
        y = math.exp(n*math.log(abs(x)))
        if (x > 0) or ((n % 2) == 0):
            return y
        else:
            return -y

    def pow_recursion(self, x, n, memory):
        if n in memory:
            return memory[n]
        else:
            if n == 1:
                out = x
            else:
                n_half = int(n/2)
                n_half_complement = n-n_half
                out = self.pow_recursion(
                        x=x, n=n_half, memory=memory)*\
                      self.pow_recursion(
                        x=x, n=n_half_complement, memory=memory
                        )
            memory[n] = out
            return out

    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1.0

        memory = {}
        out = self.pow_recursion(x=abs(x), n=abs(n), memory=memory)
        if n < 0:
            out = 1/float(out)
        if (x > 0) or ((n % 2) == 0):
            return out
        else:
            return -out
