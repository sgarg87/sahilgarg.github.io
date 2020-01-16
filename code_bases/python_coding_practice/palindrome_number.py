class Solution(object):

    def easy_solution(self, x):
        if x < 0:
            return False

        if x == 0:
            return True

        digits = []
        while x != 0:
            curr_digit = x % 10
            digits.append(curr_digit)
            x /= 10

        d = len(digits)

        i = 0
        j = d-1
        while i < j:
            if digits[i] != digits[j]:
                return False
            else:
                i += 1
                j -= 1

        return True

    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # return self.easy_solution(x=x)

        if x < 0:
            return False
        elif x == 0:
            return True

        x_copy = x
        d = 0
        while x != 0:
            x /= 10
            d += 1

        if d == 1:
            return True

        x = x_copy
        del x_copy
        half_d = d/2
        print(d, half_d)
        # from half digits
        y = 0
        count_digits = 0
        while count_digits < half_d:
            curr_digit = x % 10
            y = y*10+curr_digit
            x = x/10
            count_digits += 1

        # odd number of digits
        if (d % 2) == 1:
            x /= 10

        print(x, y)

        if x == y:
            return True
        else:
            return False
