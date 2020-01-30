class Solution(object):
    def digits_square_sum(self, n):
        digits_sqr_sum = 0
        while n != 0:
            x = n % 10
            digits_sqr_sum += (x**2)
            del x
            n = int(n/10)
        return digits_sqr_sum

    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        numbers_set = set()
        numbers_set.add(n)

        while True:
            n = self.digits_square_sum(n)

            if n == 1:
                return True
            elif n in numbers_set:
                return False
            else:
                numbers_set.add(n)
