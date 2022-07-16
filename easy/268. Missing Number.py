class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        extendedSum = n * (n + 1) // 2
        numSum = sum(nums)
        return extendedSum - numSum


sol = Solution()
c = sol.missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1])
print(c)
