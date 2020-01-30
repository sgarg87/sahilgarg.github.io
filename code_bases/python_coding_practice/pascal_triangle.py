class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []

        n = 1
        all_rows = [[1]]
        for i in range(numRows-1):
            n += 1
            new_row = [1]*n
            for j in range(1, n-1):
                new_row[j] = all_rows[i][j-1] + all_rows[i][j]
            all_rows.append(new_row)
        return all_rows

