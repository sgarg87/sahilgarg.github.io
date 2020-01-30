class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        J = set(J)

        count = 0
        for x in S:
            if x in J:
                count += 1
        return count
