class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        size = len(nums)
        nums_set = set(nums)

        return [i + 1 for i in range(size) if i + 1 not in nums_set]


sol = Solution()
c = sol.findDisappearedNumbers([1, 1])
print(c)

# there is a solution without using extra space and O(n) runtime?
