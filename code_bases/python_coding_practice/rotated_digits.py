class Solution(object):
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        num_digits = len(str(N))
        digits = [0]*num_digits

        count_good_nums = 0

        count_2_5_6_9 = 0
        count_3_4_7 = 0
        for i in range(1, N+1):
            # adding a number
            carry = 1
            for j in range(num_digits-1, -1, -1):
                org_digit = digits[j]
                if org_digit in [2, 5, 6, 9]:
                    count_2_5_6_9 -= 1
                elif org_digit in [3, 4, 7]:
                    count_3_4_7 -= 1

                curr_digit = org_digit + carry
                if curr_digit > 9:
                    assert curr_digit == 10
                    curr_digit = 0
                    carry = 1
                else:
                    carry = 0

                digits[j] = curr_digit
                if curr_digit in [2, 5, 6, 9]:
                    count_2_5_6_9 += 1
                elif curr_digit in [3, 4, 7]:
                    count_3_4_7 += 1

                if carry == 0:
                    break

            if (count_2_5_6_9 > 0) and (count_3_4_7 == 0):
                count_good_nums += 1

        return count_good_nums


