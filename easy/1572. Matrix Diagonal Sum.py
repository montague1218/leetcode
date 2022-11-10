class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        n = len(mat)
        diagonal_sum = 0
        for i in range(n // 2):
            diagonal_sum += mat[i][i] + mat[i][n - 1 - i] + mat[n - 1 - i][i] + mat[n - 1 - i][n - 1 - i]

        if n % 2 != 0:
            diagonal_sum += mat[n // 2][n // 2]

        return diagonal_sum


sol = Solution()
c = sol.diagonalSum([[1, 2, 3],
                     [4, 5, 6],
                     [7, 8, 9]])
print(c)

# this solution counts from the corner of the four diagonals
# the case in odd dimension where there is an extra middle element is handled independently
