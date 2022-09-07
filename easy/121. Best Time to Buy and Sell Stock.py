class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        if len(prices) == 1:
            return 0

        max_profit = 0
        min_buy, max_sell = prices[0], prices[0]
        for price in prices:
            if price >= max_sell:
                max_sell = price
                max_profit = max(max_profit, max_sell - max_profit)
            elif price <= min_buy:
                min_buy, max_sell = price, price

        return max_profit


sol = Solution()
c = sol.maxProfit([3, 2, 6, 5, 0, 3])
print(c)

# this solution dynamically traces the profit of the latest longest subsequence
# and memorizes the max profit for comparison
