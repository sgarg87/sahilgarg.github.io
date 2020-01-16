import math


class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        p = 0

        primes = list()
        for curr_n in range(2, n):
            # is_prime = self.is_prime(n=curr_n, primes=primes)
            # print(curr_n)

            is_prime = True
            sqrt_n = math.sqrt(curr_n)
            for curr_val in primes:
                if curr_val <= sqrt_n:
                    # divisible
                    if (curr_n % curr_val) == 0:
                        is_prime = False
                        break

            if is_prime:
                primes.append(curr_n)
                # print(curr_n),
                p += 1

        return p
