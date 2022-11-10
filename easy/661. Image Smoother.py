class Solution(object):
    def imageSmoother(self, img):
        """
        :type img: List[List[int]]
        :rtype: List[List[int]]
        """
        row_cumulator = []

        for row in img:
            counter = 0
            cumulator = []
            for n in row:
                counter += n
                cumulator.append(counter)
            row_cumulator.append(cumulator)

        new_img = []
        m, n = len(img), len(img[0])
        for i in range(m):
            new_img.append([])
            for j in range(n):
                region_sum = 0
                left, right = max(0, j - 1), min(n - 1, j + 1)
                up, down = max(0, i - 1), min(m - 1, i + 1)

                for k in range(up, down + 1):
                    region_sum += row_cumulator[k][right] - row_cumulator[k][left] + img[k][left]

                count = (down - up + 1) * (right - left + 1)
                new_img[i].append(region_sum // count)
        return new_img


sol = Solution()
c = sol.imageSmoother([[100, 200, 100], [200, 50, 200], [100, 200, 100]])
print(c)

# this solution prepares a 2d-cumulator with respect to rows (which trades off space for time),
# the smoother is applied by getting the sum of cumulator within the valid range of row
