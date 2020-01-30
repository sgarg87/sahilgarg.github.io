class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        d = len(digits)

        carry = 1
        for i in range(d-1, -1, -1):
            curr_digit = digits[i]+carry
            carry = 0

            if curr_digit == 10:
                curr_digit = 0
                carry = 1

            digits[i] = curr_digit
            if carry == 0:
                break
            else:
                if i == 0:
                    return [1] + digits

        return digits
