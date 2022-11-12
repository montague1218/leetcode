class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        min_cost = [0] * len(cost)
        min_cost[0], min_cost[1] = cost[0], cost[1]

        for i in range(2, len(cost)):
            min_cost[i] = cost[i] + min(min_cost[i - 1], min_cost[i - 2])
        return min(min_cost[-1], min_cost[-2])


sol = Solution()
c = sol.minCostClimbingStairs([10, 15, 20])
print(c)

# this solution admits an inductive structure
