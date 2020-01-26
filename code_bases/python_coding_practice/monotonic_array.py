class Solution(object):
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        n = len(A)

        is_increase_else_decrease = None

        for i in range(n-1):
            if A[i] == A[i+1]:
                continue
            else:
                if is_increase_else_decrease is None:
                    is_increase_else_decrease = (A[i] < A[i+1])
                else:
                    if (A[i] < A[i+1]) and is_increase_else_decrease:
                        continue
                    elif (A[i] > A[i+1]) and (not is_increase_else_decrease):
                        continue
                    else:
                        return False

        return True
