class Solution(object):
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])

        count = 0
        i, j = 0, n - 1
        while i < m and j >= 0:
            if grid[i][j] < 0:
                count += m - i
                j -= 1
            else:
                i += 1

        return count


sol = Solution()
c = sol.countNegatives([[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]])
print(c)

# the questions assumes A[i][j] >= A[p][q] if i < p or j < q
# the solution exploits the fact that a sub-column with a heading negative elements, the proceeding elments
# in the column must also be negative

# Hence, the solution starts with a pointer located at the right-top elements of the array
# and travels leftwards (negative encountered), and occasionally downwards (positive encountered) for efficient counting
