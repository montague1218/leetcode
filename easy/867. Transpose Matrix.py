class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """

        m, n = len(matrix), len(matrix[0])
        transpose = []
        for j in range(n):
            transpose.append([])
            for i in range(m):
                transpose[j].append(matrix[i][j])
        return transpose


sol = Solution()
c = sol.transpose([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(c)
