class Solution(object):
    def count_land_neighbor_cells(self, grid, m, n, i, j):
        # print(m, n, i, j)
        count_land_neighbor_cells = 0

        if (i > 0) and (grid[i-1][j] == 1):
            count_land_neighbor_cells += 1

        if (i < (m-1)) and (grid[i+1][j] == 1):
            count_land_neighbor_cells += 1

        if (j > 0) and (grid[i][j-1] == 1):
            count_land_neighbor_cells += 1

        if (j < (n-1)) and (grid[i][j+1] == 1):
            count_land_neighbor_cells += 1

        return count_land_neighbor_cells

    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0

        num_rows = len(grid)
        num_cols = len(grid[0])
        print(num_rows, num_cols)

        parameter = 0
        for i in range(num_rows):
            assert len(grid[i]) == num_cols
            for j in range(num_cols):
                # water grid, ignore!
                if grid[i][j] == 0:
                    continue
                else:
                    # land grid
                    assert grid[i][j] == 1
                    num_neighboring_land_cells = self.count_land_neighbor_cells(
                        grid=grid,
                        m=num_rows, n=num_cols,
                        i=i, j=j,
                    )
                    # print(i, j, num_neighboring_land_cells)
                    parameter_of_curr_cell = 4-num_neighboring_land_cells
                    parameter += parameter_of_curr_cell

        return parameter

