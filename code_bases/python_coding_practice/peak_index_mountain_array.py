class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        n = len(A)
        mountain_idx = None
        for i in range(n-1):
            if mountain_idx is None:
                if A[i] > A[i+1]:
                    mountain_idx = i
                else:
                    assert A[i] < A[i+1]
            else:
                assert A[i] > A[i+1]

        return mountain_idx
