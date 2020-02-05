class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []

        m = len(matrix)
        n = len(matrix[0])

        i0, j0 = 0, 0
        ti, bi = 0, m-1
        lj, rj = 0, n-1
        i, j = i0, j0

        out = []
        while True:

            print(matrix[i][j])
            out.append(matrix[i][j])

            # order matters
            if (i == ti) and (j < rj):
                j += 1
            elif (j == rj) and (i == bi) and (bi == ti):
                break
            elif (j == rj) and (i < bi):
                i += 1
            elif (i == bi) and (j == lj) and (lj == rj):
                break
            elif (i == bi) and (j > lj):
                j -= 1
            elif (j == lj) and (i > ti):
                i -= 1
                if i == ti:
                    assert (i == i0) and (j == j0)
                    i0 += 1
                    j0 += 1
                    ti += 1
                    bi -= 1
                    lj += 1
                    rj -= 1
                    i, j = i0, j0
            else:
                raise AssertionError

            if (ti > bi) or (lj > rj):
                break

        return out

