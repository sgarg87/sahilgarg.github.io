class Solution(object):
    def is_odd(self, x):
        if (x % 2) == 1:
            return True
        else:
            return False

    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        n = len(A)

        i, j = 0, n-1
        while i < j:
            is_i_odd = self.is_odd(A[i])
            is_j_odd = self.is_odd(A[j])

            if (not is_i_odd) and is_j_odd:
                # do nothing
                i += 1
                j -= 1
            elif is_i_odd and (not is_j_odd):
                temp = A[i]
                A[i] = A[j]
                A[j] = temp
                del temp
                i += 1
                j -= 1
            elif is_i_odd and is_j_odd:
                j -= 1
            else:
                assert (not is_i_odd) and (not is_j_odd)
                # both even
                i += 1

        return A
