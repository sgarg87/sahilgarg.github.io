import collections


class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        AB = []
        for a in A:
            for b in B:
                AB.append(a+b)
        AB = collections.Counter(AB)

        count = 0
        for c in C:
            for d in D:
                x = -c-d
                if x in AB:
                    count += AB[x]

        return count
