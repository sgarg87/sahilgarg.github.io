class Solution(object):
    def __init__(self):
        self.fibonacci_memory = {}

    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N in [0, 1]:
            return N
        elif N in self.fibonacci_memory:
            return self.fibonacci_memory[N]
        else:
            fib = self.fib(N-1) + self.fib(N-2)
            self.fibonacci_memory[N] = fib
            return fib
