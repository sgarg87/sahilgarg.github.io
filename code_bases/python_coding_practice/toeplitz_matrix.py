class Solution(object):
    def walk_along_diagonal(self, matrix, m, n, i, j):
        diag_val = None
        while (i < m) and (j < n):
            curr_val = matrix[i][j]
            if diag_val is None:
                diag_val = curr_val
            else:
                if curr_val != diag_val:
                    return False

            i += 1
            j += 1

        return True

    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        assert matrix
        m = len(matrix)
        n = len(matrix[0])

        # along first column
        i = 0
        for j in range(n):
            if not self.walk_along_diagonal(matrix=matrix, m=m, n=n, i=i, j=j):
                return False

        # along first row
        j = 0
        for i in range(1, m):
            if not self.walk_along_diagonal(matrix=matrix, m=m, n=n, i=i, j=j):
                return False

        return True
