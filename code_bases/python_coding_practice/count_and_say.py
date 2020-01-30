class Solution(object):
    def map_char_to_digit(self, c):
        return int(c)

    def read_next_number(self, num):
        curr_digit = None
        curr_digit_count = None
        next_num = ''
        for x in num:
            x = self.map_char_to_digit(x)
            # print(x)
            if curr_digit is None:
                assert curr_digit_count is None
                curr_digit = x
                curr_digit_count = 1
            else:
                assert curr_digit_count is not None
                if x == curr_digit:
                    curr_digit_count += 1
                else:
                    next_num += str(curr_digit_count)+str(curr_digit)
                    curr_digit = x
                    curr_digit_count = 1

        next_num += str(curr_digit_count) + str(curr_digit)

        return next_num

    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        x = '1'
        for i in range(n-1):
            # print(x)
            x = self.read_next_number(x)
        return x
