class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        visited = set()
        count = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and (i, j) not in visited:
                    count += 1

                    unvisitedLandQueue = set()
                    unvisitedLandQueue.add((i, j))
                    while len(unvisitedLandQueue) > 0:
                        x, y = unvisitedLandQueue.pop()

                        neighbours = self.getNeighbours(x, y, m, n)
                        for land in neighbours:
                            a, b = land
                            if grid[a][b] == "1" and land not in visited:
                                unvisitedLandQueue.add(land)
                                visited.add(land)
        return count

    def getNeighbours(self, i, j, m, n):
        neighbours = []
        if i + 1 < m:
            neighbours.append((i + 1, j))
        if 0 <= i - 1:
            neighbours.append((i - 1, j))
        if j + 1 < n:
            neighbours.append((i, j + 1))
        if 0 <= j - 1:
            neighbours.append((i, j - 1))
        return neighbours


sol = Solution()
c = sol.numIslands([
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
])
print(c)

# this solution solves by visiting all nodes in the graph, but elminiates revisiting by hashmap
