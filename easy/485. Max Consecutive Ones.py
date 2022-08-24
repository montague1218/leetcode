class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        count_current = 0
        count_max = 0
        for n in nums:
            if n == 1:
                count_current += 1
            else:
                count_max = max(count_max, count_current)
                count_current = 0
        return max(count_max, count_current)


sol = Solution()
c = sol.findMaxConsecutiveOnes([1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1])
print(c)

# this solution counts consecutive ones by 2 counters
