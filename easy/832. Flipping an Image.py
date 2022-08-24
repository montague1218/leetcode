class Solution(object):
    def flipAndInvertImage(self, image):
        """
        :type image: List[List[int]]
        :rtype: List[List[int]]
        """
        n = len(image)
        m = n // 2
        for i in range(n):
            for j in range(n):
                image[i][j] = 1 - image[i][j]
            for j in range(m):
                image[i][j], image[i][n - 1 - j] = image[i][n - 1 - j], image[i][j]
        return image


sol = Solution()
c = sol.flipAndInvertImage([[1,1,0],[1,0,1],[0,0,0]])
print(c)

# this solution do inversion then reflection, though slower but more readable
