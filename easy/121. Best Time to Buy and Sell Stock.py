class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)

        if n == 1:
            return 0

        decreasing = True

        # check of monotoncity seems required?

        maxProfit = 0
        for i in range(n):
            for j in range(n - 1 - i):
                diff = prices[i + j + 1] - prices[i]
                if diff > maxProfit:
                    maxProfit = diff

        return maxProfit


sol = Solution()
c = sol.maxProfit([7, 6, 4, 3, 1])
print(c)
