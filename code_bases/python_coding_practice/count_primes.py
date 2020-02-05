import math


class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return 0

        primes = [True]*n
        # 0, 1 are not primes
        primes[0] = False
        primes[1] = False

        n_sqrt = int(math.sqrt(n))
        for i in xrange(2, n_sqrt+1):
            if primes[i]:
                sqrt_i = int(math.sqrt(i))

                is_prime = True
                for j in xrange(2, (sqrt_i+1)):
                    if (i % j) == 0:
                        is_prime = False
                        break

                # print(i, is_prime, sqrt_i)

                if is_prime:
                    for k in range(2 * i, n, i):
                        primes[k] = False

        count = sum(primes)
        return count
