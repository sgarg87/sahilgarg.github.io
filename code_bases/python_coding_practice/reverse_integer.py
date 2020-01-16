class Solution(object):
    def __init__(self):
        self.max = 2**31-1
        self.min = -(2**31)

    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        if x < 0:
            is_negative_val = True
            x *= -1
        else:
            is_negative_val = False

        reversed_int = 0
        while x != 0:
            curr_digit = x % 10
            x = int(x/10)

            if is_negative_val:
                reversed_int = reversed_int*10-curr_digit
                if reversed_int < self.min:
                    return 0
            else:
                reversed_int = reversed_int*10+curr_digit
                if reversed_int > self.max:
                    return 0

        return reversed_int
