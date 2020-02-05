class StringKeyNumber(str):
    def __lt__(x, y):
        # strings
        xplsy = int(x+y)
        yplsx = int(y+x)
        if xplsy < yplsx:
            return True
        else:
            return False


class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        nums_str = map(str, nums)
        print nums_str
        nums_str = sorted(nums_str, key=StringKeyNumber, reverse=True)
        print nums_str

        out = ''.join(nums_str)
        if out[0] == '0':
            return '0'
        else:
            return out
