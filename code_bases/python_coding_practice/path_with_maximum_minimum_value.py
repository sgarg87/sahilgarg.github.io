import heapq

class Solution(object):
    def maximumMinimumPath(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        if not A:
            return 0

        # rows
        m = len(A)
        # cols
        n = len(A[0])
        print(m, n)

        visited = [[0 for _ in range(n)] for _ in range(m)]
        # print(visited)

        queue = []
        heapq.heappush(queue, (-A[0][0], 0, 0))

        while queue:
            # print(len(queue))
            min_path_value, i, j = heapq.heappop(queue)
            min_path_value *= -1

            # print(min_path_value, i, j)

            if (i == m-1) and (j == n-1):
                return min_path_value

            if i > 0:
                # print('i>.')
                # print(visited[i-1][j])
                if visited[i-1][j] == 0:
                    path_min_val = min(min_path_value, A[i-1][j])
                    # print(-path_min_val, i-1, j)
                    heapq.heappush(queue, (-path_min_val, i-1, j))
                    visited[i-1][j] = 1

            if i < (m-1):
                # print('i<.')
                # print(visited[i+1][j])
                if visited[i+1][j] == 0:
                    path_min_val = min(min_path_value, A[i+1][j])
                    # print(-path_min_val, i+1, j)
                    heapq.heappush(queue, (-path_min_val, i+1, j))
                    visited[i+1][j] = 1

            if j > 0:
                # print('j>.')
                # print(visited[i][j-1])
                if visited[i][j-1] == 0:
                    path_min_val = min(min_path_value, A[i][j-1])
                    # print(-path_min_val, i, j-1)
                    heapq.heappush(queue, (-path_min_val, i, j-1))
                    visited[i][j - 1] = 1

            if j < (n-1):
                # print('j<.')
                # print(visited[i][j+1])
                if visited[i][j+1] == 0:
                    path_min_val = min(min_path_value, A[i][j+1])
                    # print(-path_min_val, i, j+1)
                    heapq.heappush(queue, (-path_min_val, i, j+1))
                    visited[i][j+1] = 1
