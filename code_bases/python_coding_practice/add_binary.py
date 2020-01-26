class Solution(object):
    def _init_str_to_digit_map(self):
        self.str_digit_map = {
            '0': 0,
            '1': 1,
        }

    def addBinary(self, num1, num2):
        self._init_str_to_digit_map()

        n1 = len(num1)
        n2 = len(num2)
        if n1 < n2:
            temp = num1
            t = n1
            num1 = num2
            n1 = n2
            num2 = temp
            n2 = t
            del temp, t

        assert n1 >= n2
        min_n = min(n1, n2)
        max_n = max(n1, n2)
        diff_n = max_n - min_n

        num_sum = ''
        carry = 0
        for i in range(min_n-1, -1, -1):
            d1 = self.str_digit_map[num1[i+diff_n]]
            d2 = self.str_digit_map[num2[i]]
            curr_digit_sum = d1 + d2 + carry

            carry = int(curr_digit_sum/2)
            curr_digit = (curr_digit_sum % 2)

            num_sum = str(curr_digit) + num_sum

        if n1 > n2:
            for i in range(diff_n-1, -1, -1):
                d1 = self.str_digit_map[num1[i]]
                curr_digit_sum = d1 + carry

                carry = int(curr_digit_sum / 2)
                curr_digit = (curr_digit_sum % 2)

                num_sum = str(curr_digit) + num_sum

        if carry > 0:
            num_sum = str(carry) + num_sum

        return num_sum
