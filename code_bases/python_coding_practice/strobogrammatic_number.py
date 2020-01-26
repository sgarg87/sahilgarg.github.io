class Solution(object):
    def __init__(self):
        self.reflect_numbers = {
            '1': '1',
            '6': '9',
            '8': '8',
            '9': '6',
            '0': '0',
        }

    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        n = len(num)
        i, j = 0, (n-1)

        while i <= j:
            num_i = num[i]
            num_j = num[j]
            if num_i not in self.reflect_numbers:
                return False
            elif num_j not in self.reflect_numbers:
                return False
            else:
                num_i_reflect = self.reflect_numbers[num_i]
                if num_i_reflect != num_j:
                    return False
            i += 1
            j -= 1

        return True
