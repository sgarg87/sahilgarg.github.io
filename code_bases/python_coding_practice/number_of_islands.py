import numpy as np


class Solution(object):
    def dfs(self, grid, row_idx, col_idx):
        assert grid[row_idx, col_idx] == '1'
        # visited cell becomes water
        grid[row_idx, col_idx] = '0'

        if ((row_idx-1) >= 0) and (grid[row_idx-1, col_idx] == '1'):
            self.dfs(grid=grid, row_idx=row_idx-1, col_idx=col_idx)

        if ((row_idx+1) < grid.shape[0]) and (grid[row_idx+1, col_idx] == '1'):
            self.dfs(grid=grid, row_idx=row_idx+1, col_idx=col_idx)

        if ((col_idx-1) >= 0) and (grid[row_idx, col_idx-1] == '1'):
            self.dfs(grid=grid, row_idx=row_idx, col_idx=col_idx-1)

        if ((col_idx+1) < grid.shape[1]) and (grid[row_idx, col_idx+1] == '1'):
            self.dfs(grid=grid, row_idx=row_idx, col_idx=col_idx+1)

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0

        grid = np.array(grid)
        print(grid)
        num_rows = grid.shape[0]
        num_columns = grid.shape[1]
        num_islands = 0

        for curr_row_idx in range(num_rows):
            for curr_col_idx in range(num_columns):
                curr_cell = grid[curr_row_idx, curr_col_idx]

                # if water, ignore!
                if curr_cell == '0':
                    continue
                else:
                    self.dfs(grid=grid, row_idx=curr_row_idx, col_idx=curr_col_idx)
                    # print(grid)
                    num_islands += 1

        return num_islands
