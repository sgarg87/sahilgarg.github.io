class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        z = x ^ y
        del x, y

        count_ones = 0
        while z != 0:
            z_xor_one = z ^ 1
            if z_xor_one == (z-1):
                count_ones += 1
            else:
                assert z_xor_one == (z+1)
            z >>= 1

        return count_ones
