class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        if len(nums) == k:
            return sum(nums) / k

        self.cumulation = []
        count = 0
        for n in nums:
            count += n
            self.cumulation.append(count)

        max_sum = self.cumulation[k] - nums[k]
        for i in range(len(nums) - k):
            difference = self.cumulation[i + k] - self.cumulation[i]
            max_sum = max(max_sum, difference)

        return max_sum / k


sol = Solution()
c = sol.findMaxAverage([1, 12, -5, -6, 50, 3], 4)
print(c)
