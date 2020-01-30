import math


class Solution(object):

    def log_sol(self, n):
        # not working
        if n == 0:
            return False

        x = math.log(n, 3)
        print(x)

        mod_x = (x % 1.0)
        print(mod_x)

        # print(x, mod_x)
        if mod_x > 1e-10:
            return False
        else:
            return True

    def base_conversion_sol(self, n, base):
        if n == 0:
            return [0]

        base_digits = []
        while n != 0:
            curr_digit = (n % base)
            base_digits.append(curr_digit)
            n = int(n/3)

        return list(reversed(base_digits))

    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # return self.log_sol(n)
        if n <= 0:
            return False

        digits_3base = self.base_conversion_sol(n, 3)
        print(digits_3base)
        if (digits_3base[0] == 1) and sum(digits_3base[1:]) == 0:
            return True
        else:
            return False

