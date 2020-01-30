class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        n = len(A)
        pos_idx = None
        for i in range(n):
            if (pos_idx is None) and (A[i] >= 0):
                pos_idx = i
            A[i] **= 2

        if pos_idx is None:
            return list(reversed(A))
        elif pos_idx == 0:
            return A
        else:
            i = pos_idx
            j = i-1
            k = 0
            new_list = [0]*n
            while k < n:
                if i > (n-1):
                    new_list[k] = A[j]
                    j -= 1
                elif j < 0:
                    new_list[k] = A[i]
                    i += 1
                else:
                    if A[i] < A[j]:
                        new_list[k] = A[i]
                        i += 1
                    else:
                        new_list[k] = A[j]
                        j -= 1
                k += 1
            return new_list

