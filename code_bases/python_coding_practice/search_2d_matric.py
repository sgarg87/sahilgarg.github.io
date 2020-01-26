class Solution(object):
    def binary_search_row(self, matrix_row, n, target):
        if not matrix_row:
            return False

        left_idx = 0
        right_idx = n-1

        while left_idx < right_idx:
            mid_idx = (left_idx+right_idx)/2

            if matrix_row[left_idx] == target:
                return True
            elif matrix_row[mid_idx] == target:
                return True
            elif matrix_row[right_idx] == target:
                return True
            else:
                if matrix_row[mid_idx] < target:
                    left_idx = mid_idx + 1
                else:
                    assert matrix_row[mid_idx] > target
                    right_idx = mid_idx-1

        return False

    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False

        num_rows = len(matrix)
        num_cols = len(matrix[0])
        # move right to left, and reject columns,
        # if (row, col) greater than the value
        for curr_col_idx in range(num_cols-1, -1, -1):
            if matrix[0][curr_col_idx] == target:
                return True
            elif matrix[0][curr_col_idx] > target:
                # as if we deleted that column
                num_cols -= 1
            else:
                break
        print(num_cols)
        if num_cols == 0:
            return False

        # move up to down along the last column (which could not be rejected),
        # and reject rows if (row, col) less than the value
        # default, 0
        start_row_idx = 0
        for curr_row_idx in range(num_rows):
            # moving along the last column
            if matrix[curr_row_idx][num_cols-1] == target:
                return True
            elif matrix[curr_row_idx][num_cols-1] < target:
                start_row_idx += 1
            else:
                break
        # explicitly truncating rows
        matrix = matrix[start_row_idx:]
        num_rows -= start_row_idx
        print(start_row_idx, num_rows)
        if num_rows == 0:
            return False

        # after deleting rows and columns (implicit)
        for curr_row_idx in range(num_rows):
            curr_search_result = self.binary_search_row(
                matrix_row=matrix[curr_row_idx][:num_cols],
                n=num_cols,
                target=target,
            )
            if curr_search_result:
                return True

        return False
