class Solution(object):
    def search_dfs_land(
            self,
            grid, m, n, i, j,
            i0, j0,
            visited, land_cells,
    ):
        if (0 <= i < m) and (0 <= j < n) and (grid[i][j] == 1) and ((i, j) not in visited):
            visited.add((i, j))
            land_cells.add((i-i0, j-j0))

            self.search_dfs_land(
                grid=grid, m=m, n=n, i=i-1, j=j,
                i0=i0, j0=j0,
                visited=visited, land_cells=land_cells,
            )

            self.search_dfs_land(
                grid=grid, m=m, n=n, i=i+1, j=j,
                i0=i0, j0=j0,
                visited=visited, land_cells=land_cells,
            )

            self.search_dfs_land(
                grid=grid, m=m, n=n, i=i, j=j-1,
                i0=i0, j0=j0,
                visited=visited, land_cells=land_cells,
            )

            self.search_dfs_land(
                grid=grid, m=m, n=n, i=i, j=j+1,
                i0=i0, j0=j0,
                visited=visited, land_cells=land_cells,
            )

    def numDistinctIslands(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        visited = set()
        islands = set()
        for i in range(m):
            assert len(grid[i]) == n
            for j in range(n):
                curr_land_cells = set()
                self.search_dfs_land(
                    grid=grid,
                    m=m, n=n,
                    i=i, j=j,
                    i0=i, j0=j,
                    visited=visited,
                    land_cells=curr_land_cells
                )

                if curr_land_cells:
                    curr_land_cells = frozenset(curr_land_cells)
                    islands.add(curr_land_cells)
                    del curr_land_cells

        return len(islands)
