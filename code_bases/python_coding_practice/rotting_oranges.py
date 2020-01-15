

class Solution(object):
    def obtain_neighbors(self, grid, m, n, i, j):
        neighbors = []
        if i > 0:
            neighbors.append((i-1, j))
        if i < (m-1):
            neighbors.append((i+1, j))
        if j > 0:
            neighbors.append((i, j-1))
        if j < (n-1):
            neighbors.append((i, j+1))
        return neighbors

    def bfs(self, grid, m, n):
        queue = list()
        # visited = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    # third value is depth
                    queue.append((i, j, 0))
                    # visited.add((i, j))

        max_depth = 0
        while queue:
            i, j, depth = queue.pop(0)
            neighbors = self.obtain_neighbors(
                grid=grid, m=m, n=n, i=i, j=j,
            )
            del i, j
            max_depth = max(max_depth, depth)

            if neighbors:
                for i, j in neighbors:
                    if grid[i][j] == 1:
                        # make it rotten
                        grid[i][j] = 2
                        queue.append((i, j, depth+1))

        # check if all the oranges are rotten
        is_not_rotten = False
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    is_not_rotten = True
                    break
        if is_not_rotten:
            return -1
        else:
            return max_depth

    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0

        m = len(grid)
        n = len(grid[0])

        depth = self.bfs(grid=grid, m=m, n=n)

        return depth
