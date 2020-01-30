class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        while b != 0:
            # carry of sum
            a_and_b = ((a & b) << 1)

            # sum without carry
            a = a ^ b

            b = a_and_b
            del a_and_b

        return a
