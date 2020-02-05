class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        x = 0
        for i in xrange(32):
            x = x + (n & 1)

            if i < 31:
                # move bit up
                x <<= 1
                # remove bit
                n >>= 1

        return x
